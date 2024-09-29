#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

@pytest.fixture()
def abc():
    print("前置")
    yield
    print("后置")

@pytest.mark.parametrize('a,b',[(1,2)])
def test_01(a,b,abc):
    print("01")
    print(a+b)

def test_02(abc):
    print("02")

if __name__ == '__main__':
    pytest.main(["-sv"])