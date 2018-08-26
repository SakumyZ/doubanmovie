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

import sys
import os
import urllib.request
# reload(sys)
# sys.setdefaultencoding('utf8')



class DoubanmoviePipeline(object):

    #构造方法
    def __init__(self):
        self.folder_name = 'output/images'

        if not os.path.exists(self.folder_name):
            os.mkdir(self.folder_name)
            pass

        pass

    # 数据处理方法
    def process_item(self, item, spider):
        poster_url = item['poster'][0]
        file_name = poster_url.split('/')[-1]

        # 图片下载 url.request.url(地址， 路径， 文件名， 后缀名)
        urllib.request.urlretrieve(poster_url, self.folder_name+ os.sep+ file_name)

        return item