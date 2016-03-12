#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import site
from weixin import WeixinHandler

urls = (
    '/(.*)/', 'Redirect',
    '/site', site,
    '/', 'WeixinHandler'
)
app = web.application(urls, globals())


class Redirect:
    def __init__(self):
        pass

    def GET(self, path):
        web.seeother('/' + path)

if __name__ == '__main__':
    app.run()
