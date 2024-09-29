#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import pytest
import allure
from allure_commons.types import LinkType
from selenium import webdriver
from time import sleep
from common_module.excel_read_web import read_case
from common_module.web_keyword import Keyword

folder='../data_web/登录'

@pytest.fixture()
def abc():
    global case, element, keyword, driver, folder,case
    # case_file='../data_web/登录/登录百度.xlsx'
    # case=read_case(case_file)
    case=read_case(folder)
    keyword=Keyword()

    # 设置浏览器选项
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver=webdriver.Chrome(options=option)
    # driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield
    sleep(3)
    print("真是操蛋")
    driver.quit()



@pytest.mark.parametrize("data",read_case(folder))
def test_login(abc,data,my_option_value):
    allure.dynamic.mro()
    allure.dynamic.feature(data['模块'])
    allure.dynamic.story("查询功能story")
    allure.dynamic.title(f"{data['编号']}: {data['用例名称']}")
    allure.dynamic.link('https://www.baidu.com/', LinkType.LINK, '我是修改后的link')
    allure.dynamic.label('我是修改后的label')
    allure.dynamic.issue('https://www.baidu.com/', '我是修改后的issue')
    allure.dynamic.description('我是修改后的description')
    allure.dynamic.severity(f"{data['模块']}")
    allure.dynamic.tag(f"{data['用例等级']}")
    allure.dynamic.testcase('https://www.baidu.com/', '我是修改后的testcase')
    if my_option_value["module"] is None or data["模块"] in my_option_value["module"]:
        if my_option_value["case"] is None or data["用例名称"]==my_option_value["case"]:
            if my_option_value["level"] is None or data["用例等级"]==my_option_value["level"]:
                for key, value in data.items():
                    if key not in ('模块','编号','用例名称','用例等级'):
                        with allure.step(key):
                            if value[0]=="open":
                                value.pop(0)
                                keyword.open(driver,*value)
                            elif value[0]=="move_to_element":
                                value.pop(0)
                                keyword.move_to_element(driver, *value)
                            elif value[0] == "click":
                                value.pop(0)
                                keyword.click(driver, *value)
                            elif value[0] == "switch_to_window":
                                value.pop(0)
                                keyword.switch_to_window(driver, *value)
                            elif value[0] == "input":
                                value.pop(0)
                                keyword.input(driver, *value)
                            elif value[0] == "assert":
                                value.pop(0)
                                keyword.input(driver, *value)
            else:
                pytest.skip("非所选等级用例")
        else:
            pytest.skip("非所选用例")
    else:
        pytest.skip("非所选模块用例")


if __name__ == '__main__':
    pytest.main(["-sv","--alluredir",'../result','--clean-alluredir'])
    os.system('allure generate ../reslut -o ../report_allure --clean')