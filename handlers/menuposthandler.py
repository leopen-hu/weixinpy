#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import plugins
from commonfunc import BusinessMethod
from handlers.commonfunc import TOOLMETHOD

# 键值：(函数名, (参数1, 参数2， ......))
_CLICKKEYS = {
    'me': ('BusinessMethod.showmenu', ),
    'url1': ('BusinessMethod.urlopen', (1, 2, 3))
}


class MenuReqHandler:
    def __init__(self, req):
        self.req = req
        self.resp = plugins.responses.Response(req)

    def getresponse(self):
        global _CLICKKEYS
        funcresp = dict()
        errcode = None
        eventkey = self.req.eventkey
        if eventkey in _CLICKKEYS.iterkyes():
            valuelen = len(_CLICKKEYS[eventkey])
            if valuelen == 1:
                try:
                    funcresp = eval(_CLICKKEYS[eventkey][0])()
                except Exception as e:
                    logging.exception(e)
                    errcode = 2
            elif valuelen == 2:
                try:
                    funcresp = eval(_CLICKKEYS[eventkey][0])(*_CLICKKEYS[eventkey][1])
                except Exception as e:
                    logging.exception(e)
                    errcode = 2
            else:
                errcode = 2
        else:
            errcode = 2
        if errcode:
            funcresp = BusinessMethod.showmenu(errcode)
        for key, value in funcresp.iteritems():
            self.resp.__dict__[key] = value
        return self.resp
