#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from common_module.excel_read_xToolkit import read_excel
from common_module.api_keyword import Keyword

ak=Keyword()
@pytest.mark.parametrize("data",read_excel())
def test01(data):
    dict_data={
        'method':data['method'],
        'url':data['url'],
        'headers':eval(data['headers']),
        'data':eval(data['data']),
        'cookies':data['cookies'],
        'json':data['json']
    }
    print(dict_data)
    res = getattr(ak, "interface")(**dict_data)
    print(res)