# -*- coding:UTF-8 -*-

"""
    @name 
    @author SakumyZ
    @date 2018-7-
    @description
"""

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class DoubanmoviePipeline(object):

    def process_item(self, item, spider):
        database = pymysql.connect('localhost', 'root', 'NO107yhyskl', 'douban', charset = 'utf8')

        cur = database.cursor()

        # # 设置编码方式
        # cur.execute("set title utf8")
        #获取爬取的数据
        rank = item['rank'][0]
        title = item['title'][0]
        sql = "insert into douban values(%s, %s)"
        # 执行sql语句
        cur.execute(sql, ((int)(rank),title))
        # 提交
        database.commit()
        # 关闭游标
        if cur:
            cur.close()
            pass
        return item
