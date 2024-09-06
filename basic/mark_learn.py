#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 标记测试类（单个标签）

import pytest

class TestOrder:
    # 给类中的所有测试方法打上order标签

    pytestmark = pytest.mark.order

    def test_order(self):
        print("下单")

    def test_pay(self):
        print("支付")

if __name__ == '__main__':
    pytest.main(["-sv"])