#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import lxml
import os
import hashlib
import handlers
import plugins.requests
from lxml import etree

# global variable
_TOKEN = 'leopenweixin'


class ReqHandlerSelector:
    def __init__(self, req):
        self.req = req
        msgtype = req.find('MsgType').text
        if msgtype == 'text':
            self.req = plugins.requests.TextPostRequest(req)
            self.handler = handlers.textposthandler.TextReqHandler(self.req)
        elif msgtype == 'event':
            event = req.find('Event').text
            if event == 'subscribe':
                # if a scan before subscribe
                if req.find('EventKey').text:
                    pass
                else:
                    pass

            elif event == 'unsubscribe':
                pass
            elif event == 'CLICK' or event == 'VIEW':
                self.req = plugins.requests.MenuEventPostRequest(req)
                self.handler = handlers.menuposthandler.MenuReqHandler(self.req)
            elif event == 'LOCATION':
                pass
        else:
            pass


class FormattedResponse:
    def __init__(self, resp):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
        self.resp = resp

    def getresponse(self):
        resp = self.resp
        resptype = resp.type
        if resptype == 'text':
            self.render = self.render.reply_text(resp.touser, resp.fromuser, resp.createtime, resp.content)
        else:
            pass
        return self.render


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
        req_xml = web.data()
        req = etree.fromstring(req_xml)
        selector = ReqHandlerSelector(req)
        resp = selector.handler.getresponse()
        response = FormattedResponse(resp)
        return response.getresponse()


# commonly used functions
def gethashcode(*args):
        newlist = []
        for arg in args:
            newlist.append(arg)
        newlist.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, newlist)
        return sha1.hexdigest()
