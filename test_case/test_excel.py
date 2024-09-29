#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
from allure_commons.types import LinkType, Severity

from common_module.api_keyword import Keyword
import openpyxl
from common_module.excel_read import read_excel


def setup_module():
    global ak,excel,sheet,excel_path
    ak=Keyword()
    excel_path='../data/电话号码查询.xlsx'
    excel=openpyxl.load_workbook(excel_path)
    sheet=excel["Sheet1"]

@allure.id('我是id')
@allure.title('我是title')
@allure.link('https://www.baidu.com/', LinkType.ISSUE, '我是link_ISSUE')
@allure.label('我是label')
@allure.issue('https://www.baidu.com/', '我是issue')
@allure.description('我是description')
@allure.severity(Severity.BLOCKER)
@allure.tag('我是tag')
@allure.testcase('https://www.baidu.com/', 'testcase')
@pytest.mark.parametrize("data",read_excel())
def test01(data,my_option_value):
    allure.dynamic.mro()
    allure.dynamic.story("查询功能story")
    allure.dynamic.feature("查询功能feature")
    allure.dynamic.title(f'{data[0]}: {data[1]}')
    allure.dynamic.link('https://www.baidu.com/', LinkType.LINK, '我是修改后的link')
    allure.dynamic.label('我是修改后的label')
    allure.dynamic.issue('https://www.baidu.com/', '我是修改后的issue')
    allure.dynamic.description('我是修改后的description')
    allure.dynamic.severity(f'{data[2]}')
    allure.dynamic.tag(f'{data[3]}')
    allure.dynamic.testcase('https://www.baidu.com/', '我是修改后的testcase')
    print(my_option_value)
    if my_option_value['level'] is None or my_option_value['level']==data[2]:
        with allure.step('请求'):
            allure.attach(data[3], name=f'{data[4]}请求')
            # with allure.step('响应'):
            #     allure.attach('{}'.format(h.status_code), name='状态码')
            # with allure.step('断言'):
            #     assert h.status_code == 200
            #     allure.attach('OK', name='断言')

            dict_data={
                "url":data[3],
                "method":data[4],
                "headers":eval(data[5]),
                "data":eval(data[6])
                # "json":eval(data[7]),s
                # "params":eval(data[8])
            }
            # res=ak.interface(url=dict_data["url"],method=dict_data["method"],headers=dict_data["headers"],data=dict_data["data"],json=dict_data["json"],params=dict_data["params"])
            # res = ak.interface(url=dict_data["url"], method=dict_data["method"], headers=dict_data["headers"],
            #                    data=dict_data["data"])
            res=getattr(ak,"interface")(**dict_data) #ak=Keyword()实例化类，interface为类中的函数
    else:
        pytest.skip("非所选等级用例")

    try:
        with allure.step('响应'):
            allure.attach('{}'.format(res.status_code), name='状态码')
            s=ak.get_value(res.text,data[10])
            allure.attach("{}".format(res.json()), name="response body")
    except:
        print("错误")
    finally:
        with allure.step('断言'):
            assert res.status_code == 200
            assert s == data[11]
            allure.attach('OK', name='断言')



if __name__ == '__main__':
    pytest.main(["-sv","--lv=lv1"])