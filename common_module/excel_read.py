#!/usr/bin/env python
# -*- coding: utf-8 -*-

import openpyxl

def read_excel(level=None):
    workbook=openpyxl.load_workbook("../data/电话号码查询.xlsx")
    sheet=workbook["Sheet1"]
    list_tuple=list(sheet.values)[1:sheet.max_row]
    level_list=[]
    for level_data in list_tuple:
        if level==level_data[]
    return list_tuple

if __name__ == '__main__':
    s=read_excel()
    print(s)