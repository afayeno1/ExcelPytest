#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

def test001(doctest_namespace):
    print(type(doctest_namespace))
    doctest_namespace["abc"]="testabc"

def test002(doctest_namespace):
    name=doctest_namespace["abc"]
    print(name)

if __name__ == '__main__':
    pytest.main(["-sv"])