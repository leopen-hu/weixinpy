#!/usr/bin/env python
# -*- coding: utf-8 -*-


import plugins


class ClickReqHandler:
    def __init__(self, req):
        self.req = req
        self.resp = plugins.responses.Response(req)

    def getresponse(self):
        pass
