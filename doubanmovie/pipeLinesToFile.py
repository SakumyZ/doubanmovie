# -*- coding:UTF-8 -*-

"""
    @name 
    @author SakumyZ
    @date 2018-7-
    @description
"""

import sys
import os
import time

class DoubanmoviePipeline(object):

    # 构造方法
    def __init__(self):
        self.floderName = 'output'
        if not os.path.exists(self.floderName):
            os.mkdir(self.floderName)
            pass

        # 创建文件
        currentTime = time.strftime("%Y-%m-%d-%H-%M",time.localtime())
        self.fileName = self.floderName+os.sep+'doubantop250'+currentTime+'.txt'
        pass

    # 推入方法
    def process_item(self,item,spider):
        with open(self.fileName, 'a', encoding='utf-8') as fp:
            fp.write("rank:%s\t"%item['rank'][0])
            fp.write("title:%s\t"%item['title'][0])
            fp.write("poster:%s"%item['poster'][0])
            fp.write("\n")
        pass
        return item
    pass
pass