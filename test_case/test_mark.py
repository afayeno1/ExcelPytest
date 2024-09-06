#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

class TestClass:
    # 加一个 pytestmark的类属性
    data=["lv1","lv2"]
    dictData={"a":pytest.mark.data[0],
        "b":pytest.mark.data[1]}

    # pytestmark = [pytest.mark.data, pytest.mark.data1]