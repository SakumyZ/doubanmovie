# -*- coding:UTF-8 -*-

"""
    @name main.py
    @author SakumyZ
    @date 2018-7-
    @description excel文件操作
"""

import os
import time
import xlwt

#主函数
if __name__ == "__main__":
    # 创建文件
    excelPath = os.path.join(os.getcwd(),'excelOutput')
    if not os.path.exists(excelPath):
        os.mkdir(excelPath)
        pass

    #设置文件名
    currentTime = time.strftime("%Y-%m-%d-%H-%M",time.localtime())
    fileName = excelPath+ os.sep+ 'doubantop250'+currentTime+'.xls'

    #设置文件编码格式
    wokebook = xlwt.Workbook(encoding='utf-8')
    #创建一个单页并重命名
    sheet = wokebook.add_sheet('测试')
    #定义行数据
    headers = ['rank','name']
    for i in range(0, len(headers)):
        sheet.write(0, i, headers[i])
    pass
    print("数据写入完成")

    # 添加数据
    for rowIndex in range(1, 5):
        for colIndex in range(len(headers)):
            sheet.write(rowIndex, colIndex, 10)
            pass
        pass
    #保存
    wokebook.save(fileName)
pass