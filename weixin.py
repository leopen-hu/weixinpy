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
#global variable
TOKEN = 'leopenweixin'

#custom classes
class BusResponse:
    def __init__(self):
        self.type = ''
        self.touser = ''
        self.fromuser = ''

class TmplResponse:
    pass

class HandlerLoader:
    def __init__(self):
        self.handlers = []

class HandlerChoice:
    def __init__(self, xml):
        msgtype = xml.find('MsgType').text
        if msgtype == 'text':
            self.handler = texthandler.TextHandler(xml)
        else:
            pass

    def getresp(self):
        resp = BusResponse()
        self.handler.prefix_handler()
        return resp

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

#main class
class WeixinHandler:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)


    def GET(self):
        req = web.input()
        global TOKEN
        hashcode = gethashcode(req.timestamp, req.nonce, TOKEN)
        if hashcode == req.signature:
            return req.echostr

    def POST(self):
        req = web.data()
        req_xml = etree.fromstring(req)
        req_handler = HandlerChoice(req_xml)
        #bus_resp = req_handler.getresp()
        #tmpl_handler = TemplateChoice(bus_resp)
        #tmpl_resp = tmpl_handler.getresp()
        return req_handler.handler.msgid

#commonly used functions
def gethashcode(*arg):
        timestamp = arg[0]
        nonce = arg[1]
        token = arg[2]
        list = [token,timestamp,nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update,list)
        return sha1.hexdigest()