#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

@pytest.mark.parametrize("a",["aaa"])
def test_01(a):
    print(f'\n{a}')

@pytest.mark.parametrize("b",["123","456"])
def test_02(b):
    print(f'\n{b}')

@pytest.mark.parametrize("a,b",[(123,456),(567,789)])
def test_03(a,b):
    print(f'\na:{a},b:{b}')

def return_data():
    return [("abc","def"),("ghi","jkl")]

@pytest.mark.parametrize("a,b",return_data())
def test_04(a,b):
    print(f'\na:{a},b:{b}')

@pytest.mark.parametrize("data",return_data())
def test_05(data):
    print(f'\na:{data[0]},b:{data[1]}')

if __name__=='__main__':
    pytest.main(['-sv','./'])