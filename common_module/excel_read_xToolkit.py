#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xToolkit import xfile

def read_excel():
    datas=xfile.read("../data/电话号码查询.xls").excel_to_dict()
    return datas

if __name__ == '__main__':
    s=read_excel()
    print(s)