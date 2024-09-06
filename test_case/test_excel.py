#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from common_module.api_keyword import Keyword
import openpyxl
from common_module.excel_read import read_excel


def setup_module():
    global ak,excel,sheet,excel_path
    ak=Keyword()
    excel_path='../data/电话号码查询.xlsx'
    excel=openpyxl.load_workbook(excel_path)
    sheet=excel["Sheet1"]

@pytest.mark.parametrize("data",read_excel())
def test01(data):
    dict_data={
        "url":data[3],
        "method":data[4],
        "headers":eval(data[5]),
        "data":eval(data[6])
        # "json":eval(data[7]),
        # "params":eval(data[8])
    }
    # res=ak.interface(url=dict_data["url"],method=dict_data["method"],headers=dict_data["headers"],data=dict_data["data"],json=dict_data["json"],params=dict_data["params"])
    # res = ak.interface(url=dict_data["url"], method=dict_data["method"], headers=dict_data["headers"],
    #                    data=dict_data["data"])
    res=getattr(ak,"interface")(**dict_data) #ak=Keyword()实例化类，interface为类中的函数

    try:
        # print(res.text)
        s=ak.get_value(res.text,data[10])

        # print("通过")
    finally:
        assert s==data[11]


if __name__ == '__main__':
    pytest.main(["-sv"])