# weixinpy
基于web.py开发的微信后台开发框架

*由于是部署在sae上，所以路由规则是写在index.wsgi文件中的，config.yaml是为服务器（应用）添加需要引用的模块。
（测试环境可以将wsgi文件转为py文件，config.yaml需要自己安装对应的模块）*

## 总体逻辑

1. 访问应用会首先访问index.wsgi文件，根据路由规则，访问根目录的请求会被weixin.py的WeixinHandler类处理。
2. 当访问是一个GET请求，GET()方法提供默认的微信服务器配置返回功能。
3. 当访问是一个POST请求，POST会对请求进行处理并给出回应，具体逻辑如下：
    1. 获取post数据（web.data()）并解析生成格式化的请求req，解析使用的是lxml模块的etree.fromstring()方法；
    2. 根据解析后的请求生成一个请求处理器的选择器（ReqHandlerSelector），该选择器的作用是：
        1. 依据req的类型将req转化为对应class的一个实例（如‘text’请求会被转化为一个TextPostRequest实例）并作为选择器的self.req属性；
        2. 根据req的类型确定请求处理器的类型（如‘text’请求需要使用TextReqHandler类型的处理器处理），
        3. 根据生成的属性self.req实例化一个请求处理器handler并作为处理器的另一个属性。
        4. 综上，即根据请求类型确定处理器类型，根据请求内容实例化一个处理器。
    3. 执行处理器的getresponse()方法获取返回值resp：
    4. 根据返回值，生成一个格式化返回值类型的实例
    5. 执行该实例的getresponse()方法获取最终需要返回到请求者的结果并对POST请求进行响应。

*以上步骤中的第2,3步根据请求类型不同会有不同类型的处理器。一下是各个类型处理器的逻辑。*

## 处理器逻辑

1. 相同的逻辑部分：

    1. 实例化时执行__init__(self)函数，获取该实例的两个属性req和resp（req即参数传递过来的请求，resp是一个实例化的Response）
        *Response是处理器的返回值的公共类，包含了所有返回值的共有属性，这些属性在实例化时根据req赋值。
    2. 定义了getresponse()函数用于处理请求，根据请求类型及内容决定执行哪种@staticmethod方法，调用该方法并获取结果，使用该结果为self.resp属性添加Response类之外的属性，最后将self.resp作为返回值返回。
    3. 定义了一些@staticmethod方法，getresponse()需要调用。

2. 不同的逻辑部分：
*不同的逻辑部分主要在getresponse()内部和一些@staticmethod方法。*
    1. TextReqHandler:

            _KEYWORDS = {'天气': 'getweather', '温度': 'gettemperature'}
            _PREFIX = {'1001': 'repeatwords', '1002': 'translate'}
            _MYSPLIT = '+'

        1. getresponse()--根据请求内容决定执行哪种@staticmethod方法，多种情况:
            1. 如果是关键字命令，则执行关键字命令对应的@staticmethod方法，关键字命令与@staticmethod方法的对应关系通过全局字典变量_KEYWORDS定义；
            2. 如果不是关键字命令，则视为是前缀命令，分解前缀与真实的请求内容，分割符在全局变量_MYSPLIT定义：
                1. 如果分解成功，查看前缀与@staticmethod方法的对应关系--全局字典变量_PREFIX定义：
                    1. 如果找不到对应关系，直接调用显示菜单方法；
                    2. 如果找到对应关系，调用对应@staticmethod方法；
                2. 如果分解失败，则直接调用显示菜单方法；

        2. 复杂的@staticmethod方法解释:
        暂无



