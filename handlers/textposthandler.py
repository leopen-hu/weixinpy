#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
import urllib2
import json
from commonfunc import showmenu
import plugins.responses

# global variable
_KEYWORDS = {
    '天气': 'getweather',
    '温度': 'gettemperature',
    '0000': 'showmenu'
}
_PREFIX = {'1001': 'repeatwords', '1002': 'translate'}
_MYSPLIT = '+'


class TextReqHandler:
    def __init__(self, req):
        self.req = req
        self.resp = plugins.responses.Response(req)

    # main function
    def getresponse(self):
        content = self.req.content
        global _KEYWORDS
        global _PREFIX
        global _MYSPLIT
        funcresp = dict()
        try:
            # if a keyword-command(staticmethod)
            funcresp = getattr(self, _KEYWORDS[content])()
        except Exception as e:
            logging.exception(e)
            try:
                # if a keyword-command(commonmethod)
                funcresp = eval(_KEYWORDS[content])()
            except Exception as e:
                logging.exception(e)
                try:
                    # if a prefix-command
                    prefix, realcontent = content.split(_MYSPLIT, 1)
                except Exception as e:
                    logging.exception(e)
                    # no match command
                    errcode = '0'
                    funcresp = showmenu(errcode)
                else:
                    try:
                        # if a right prefix
                        funcresp = getattr(self, _PREFIX[prefix])(realcontent)
                    except Exception as e:
                        logging.exception(e)
                        # no match prefix
                        errcode = '1'
                        funcresp = showmenu(errcode)
        finally:
            for key, value in funcresp.iteritems():
                self.resp.__dict__[key] = value
        return self.resp

    # ----------------------------------------staticmethod-----------------------------------------------
    # define all common functions in this section
    # common function means function which can run without the class
    # for example you can make a 'switch' function here
    @staticmethod
    def getweather():
        resp = dict()
        resp['type'] = ''
        pass
        return resp

    @staticmethod
    def gettemperature():
        resp = dict()
        resp['type'] = ''
        pass
        return resp

    @staticmethod
    def repeatwords(words):
        resp = dict()
        resp['type'] = 'text'
        resp['content'] = words
        return resp

    @staticmethod
    def translate(words):
        words = words.encode('utf-8')
        resp = dict()
        resp['type'] = 'text'
        resp['content'] = ''
        qwords = urllib2.quote(words)
        transurl = u'http://fanyi.youdao.com/openapi.do' \
                   u'?keyfrom=leopenweixin&key=1317704549&type=data&doctype=json&version=1.1&q=' + qwords
        respjson = urllib2.urlopen(transurl)
        result = json.loads(respjson.read())
        if result['errorCode'] == 0:
            if 'basic' in result.keys():
                resp['content'] = u'%s:\n%s\n%s\n网络释义：\n%s' % (
                    result['query'], ','.join(result['translation']),
                    ','.join(result['basic']['explains']), ','.join(result['web'][0]['value']))
            else:
                resp['content'] = u'%s: \n基本翻译: %s\n' % (result[u'query'], ','.join(result[u'translation']))
        elif result['errorCode'] == 20:
            resp['content'] = u'对不起，要翻译的文本过长'
        elif result['errorCode'] == 30:
            resp['content'] = u'对不起，无法进行有效的翻译'
        elif result['errorCode'] == 40:
            resp['content'] = u'对不起，不支持的语言类型'
        else:
            resp['content'] = u'对不起，您输入的单词无法翻译,请检查拼写'
        return resp
