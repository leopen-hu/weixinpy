#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import site
from main import WeixinRequest

urls = (
    '/(.*)/', 'redirect',
    '/site', site,
    '/', 'WeixinRequest'
)
app = web.application(urls, globals())

class redirect:
    def GET(self, path):
        web.seeother('/' + path)

if __name__ == '__main__':
    app.run()