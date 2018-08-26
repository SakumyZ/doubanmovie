# -*- coding:UTF-8 -*-

"""
    @name 
    @author SakumyZ
    @date 2018-7-
    @description
"""
import os
import time

import xlwt
import xlrd

from xlutils.copy import copy

class DoubanmoviePipeline(object):

    def __init__(self):
        self.folder_name = 'output'
        if not os.path.exists(self.folder_name):
            os.mkdir(self.folder_name)
            pass
        pass

        # 设置文件名
        current_time = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
        self.file_name ="doubanMoviesTop250"+ current_time+ ".xls"
        # 创建文件的绝对路径
        self.excelPath = self.folder_name+ os.sep+ self.file_name

        #创建工作部
        wb = xlwt.Workbook(encoding='utf-8')
        #单页
        sheet = wb.add_sheet("豆瓣")
        # 标题列表
        header = ['rank', 'title', 'poster']

        for colIndex in range(0, len(header)):
            sheet.write(0, colIndex, header[colIndex])
            pass
        self.rowIndex = 1
        #保存
        wb.save(self.excelPath)


    def process_item(self, item, spider):
        #打开已创建excel表
        wb = xlrd.open_workbook(self.excelPath, formatting_info=True)
        # 拷贝wb
        newwb = copy(wb)
        # 选页
        sheet = newwb.get_sheet(0)

        line = [item['rank'], item['title'], item['poster']]
        for colIndex in range(0, len(item)):
            sheet.write(self.rowIndex, colIndex, line[colIndex])

            pass

        newwb.save(self.excelPath)
        self.rowIndex = self.rowIndex + 1
        return item
