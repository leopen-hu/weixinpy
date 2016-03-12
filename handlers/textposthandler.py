#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import time
from common import showmenu

# global variable
_KEYWORDS = {'天气': 'getweather', '温度': 'gettemperature'}
_PREFIX = {'1001': 'repeatwords', '1002': 'translate'}
_MYSPLIT = '+'


class TextReqHandler:
    def __init__(self, req):
        self.req = req
        self.fromuser = req.touser
        self.touser = req.fromuser
        self.createtime = int(time.time())

    # main function
    def getresponse(self):
        content = self.req.content
        global _KEYWORDS
        global _PREFIX
        global _MYSPLIT
        funcresp = dict()
        try:
            # if a keyword-command
            funcresp = _KEYWORDS[content]()
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
                    funcresp = _PREFIX[prefix](realcontent)
                except Exception as e:
                    logging.exception(e)
                    # no match prefix
                    errcode = '1'
                    funcresp = showmenu(errcode)
            finally:
                for item in funcresp:
                    setattr(self.resp, item.key, item.value)
        return self.resp

    # ----------------------------------------classmethod-----------------------------------------------
    # define all common functions in this section
    # common function means function which can run without the class
    # for example you can make a 'switch' function here
    @classmethod
    def getweather(cls):
        resp = dict()
        resp['type'] = ''
        pass
        return resp

    @classmethod
    def gettemperature(cls):
        resp = dict()
        resp['type'] = 'text'
        pass
        return resp

    @classmethod
    def repeatwords(cls, words):
        resp = dict()
        resp['type'] = ''
        resp['content'] = words
        pass
        return resp

    @classmethod
    def translate(cls, words):
        resp = dict()
        resp['type'] = ''
        pass
        return resp
