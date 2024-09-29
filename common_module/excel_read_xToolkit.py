#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xToolkit import xfile

def read_excel(level=None):
    datas=xfile.read("../data/电话号码查询.xls").excel_to_dict()
    if level is None:
        return datas
    else:
        row_list=[]
        for data in datas:
            if level==data["用例等级"]:
                row_list.append(data)
        return row_list


# if __name__ == '__main__':
#     s=read_excel("LV1")
#     print(s)
#     s = read_excel("LV4")
#     print(s)