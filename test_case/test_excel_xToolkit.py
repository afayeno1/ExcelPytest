#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from common_module.excel_read_xToolkit import read_excel
from common_module.api_keyword import Keyword

ak=Keyword()
@pytest.mark.parametrize("data",read_excel())
def test01(data,my_option_value):
    if my_option_value is None or my_option_value==data["用例等级"]:
        dict_data={
            'method':data['method'],
            'url':data['url'],
            'headers':eval(data['headers']),
            'data':eval(data['data']),
            'cookies':data['cookies'],
            'json':data['json']
        }
        res = getattr(ak, "interface")(**dict_data)
        # print(res.text)
    else:
        pytest.skip("非所选等级用例")
    try:
        result=ak.get_value(res.text,data["检查字段"])
    except:
        print("接口错误，检查出入参")
    finally:
        assert result==data["预期结果"]

if __name__ == '__main__':
    pytest.main(['-sv','--lv=LV1'])