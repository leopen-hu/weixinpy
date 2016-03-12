#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import lxml
import os
import sys
import time
import urllib2
import hashlib
import json
import imp
import handlers.textposthandler
import plugins.requests
from lxml import etree

# global variable
_TOKEN = 'leopenweixin'


# custom classes
class BusResponse:
    def __init__(self, req):
        self.touser = ''
        self.fromuser = ''


class TmplResponse:
    def __init__(self):
        pass


class ReqHandlerSelector:
    def __init__(self, req):
        msgtype = req.find('MsgType').text
        if msgtype == 'text':
            self.req = plugins.requests.TextPostRequest(req)
            self.handler = handlers.textposthandler.TextReqHandler(self.req)
        else:
            pass


class FormattedResponse:
    def __init__(self, resp):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
        self.resp = resp

    def getresponser(self):
        resp = self.resp
        resptype = resp.type
        if resptype == 'text':
            self.render = self.render.reply_text(resp.touser, resp.fromuser, resp.createtime, resp.content)
        else:
            pass
        return self.render


class TemplateChoice:
    def __init__(self, resp):
        resptype = resp.type
        if resptype == 'text':
            pass
        else:
            pass

    def getresp(self):
        resp = TmplResponse()
        pass
        return resp


# main class
class WeixinHandler:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        req = web.input()
        global _TOKEN
        hashcode = gethashcode(req.timestamp, req.nonce, _TOKEN)
        if hashcode == req.signature:
            return req.echostr

    def POST(self):
        req = web.data()
        req = etree.fromstring(req)
        selector = ReqHandlerSelector(req)
        resp = selector.handler.getresponse()
        response = FormattedResponse(resp)
        return response


# commonly used functions
def gethashcode(*arg):
        timestamp = arg[0]
        nonce = arg[1]
        token = arg[2]
        newlist = [token, timestamp, nonce]
        newlist.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, newlist)
        return sha1.hexdigest()
