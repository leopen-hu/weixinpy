#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time


class Response:
    def __init__(self, req):
        self.fromuser = req.touser
        self.touser = req.fromuser
        self.createtime = int(time.time())


class TextResponse(Response):
    def __init__(self, a):
        Response.__init__(a)
        self.msgtype = 'text'
        self.content = a.content
