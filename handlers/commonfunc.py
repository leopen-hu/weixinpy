#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import urllib2
import json
import time
_ERRORDICT = {
    0: u'无效的命令',
    1: u'无效的前缀',
    2: u'未定义事件'
}
_MENU = (
    u'0000: 查看菜单',
    u'0001+内容: 学舌',
    u'0002+内容: 翻译'
)
APPIDTEST = u'wx0876208de79615e9'
APPSECRETTEST = u'5a318d6f54054fe21ce691161ad93d3a'
ACCESSTOKEN = ''
TOKENSTARTTIME = 0
EXPIRESIN = 6000


# ----------------------------------------BusinessMethods-------------------------------------------
# in this section, you can define your function which is used to solve business requirement.
class BusinessMethod(object):

    @staticmethod
    def showmenu(err=''):
        resp = dict()
        resp['type'] = 'text'
        global _ERRORDICT
        global _MENU
        if err:
            menustr = _ERRORDICT[err] + '\n' + '菜单' + '\n'
        else:
            menustr = '菜单' + '\n'
        for item in _MENU:
            menustr = menustr + item + '\n'
        resp['content'] = menustr
        return resp

    @staticmethod
    def getaccesstoken():
        global ACCESSTOKEN
        global TOKENSTARTTIME
        global EXPIRESIN
        nowtime = int(time.time())
        lasttime = nowtime - TOKENSTARTTIME
        if lasttime < 0 or lasttime > EXPIRESIN:
            url = u'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid='\
                  + APPIDTEST + u'&secret=' + APPSECRETTEST
            respjson = urllib2.urlopen(url)
            result = json.loads(respjson.read())
            ACCESSTOKEN = result['access_token']
            EXPIRESIN = result['expires_in'] - 1200
            TOKENSTARTTIME = int(time.time())


# ----------------------------------------ToolMethods-------------------------------------------
# in this section, you can define your own tool functions these who are used as tools,
# such as a switch function
class TOOLMETHOD(object):

    @staticmethod
    def isfunc(funcname):
        try:
            eval(funcname)
        except Exception as e:
            logging.exception(e)
            return 0
        else:
            return 1
