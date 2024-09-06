#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import jsonpath
import requests

class Keyword:

    def interface(self,method,url,**kwargs):
        res=requests.request(method=method,url=url,**kwargs)
        return res

    def get_value(self,data,exp):
        res=json.loads(data)
        value_list=jsonpath.jsonpath(res,exp)
        return value_list[0]