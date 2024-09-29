#!/usr/bin/env python
# -*- coding: utf-8 -*-

import openpyxl

def read_excel(level=None):
    workbook=openpyxl.load_workbook("../data/电话号码查询.xlsx")
    sheet=workbook["Sheet1"]
    row_list=list(sheet.values)[1:sheet.max_row]
    level_list=[]
    if level is None:
        return row_list
    else:
        for level_data in row_list:
            if level==level_data[2]:
                level_list.append(level_data)
        return level_list

if __name__ == '__main__':
    s=read_excel()
    print(s)