#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choices

import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--lv",
        action="store",
        default=None,
        help="按用例等级执行"
    )
    parser.addoption(
        "--module",
        action="append",
        default=None,
        choices=['登录1','登录2','登录3'],
        help="按模块执行"
    )
    parser.addoption(
        "--case",
        action="store",
        default=None,
        help="按用例执行"
    )


@pytest.fixture(scope="session")
def my_option_value(request):
    option={}
    option["level"]=request.config.getoption('--lv')
    option['module']=request.config.getoption('--module')
    option['case'] = request.config.getoption('--case')
    return option



