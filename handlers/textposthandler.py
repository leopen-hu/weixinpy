#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
import time
from commonfunc import showmenu
import plugins.responses

# global variable
_KEYWORDS = {'天气': 'getweather', '温度': 'gettemperature'}
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
            # if a keyword-command
            funcresp = self.getattr(self, _KEYWORDS[content])()
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

    # ----------------------------------------classmethod-----------------------------------------------
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
        resp['type'] = 'text'
        pass
        return resp

    @staticmethod
    def repeatwords(words):
        resp = dict()
        resp['type'] = ''
        resp['content'] = words
        return resp

    @staticmethod
    def translate(words):
        resp = dict()
        resp['type'] = ''
        pass
        return resp