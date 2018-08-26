# -*- coding: utf-8 -*-
import scrapy

from doubanmovie.items import DoubanmovieItem
# from pipeLinesToFile import DonbanmoviePipeLine

# addToFile = DoubanmovieItem()

class DoubanSpider(scrapy.Spider):
    name = 'movieSpider'         #爬虫程序的名字
    allowed_domains = ['douban.com']    #爬虫的域名
    start_urls = ['http://movie.douban.com/top250'] #网络爬虫的地址

    #paese 解析函数
    def parse(self, response):
        #解析所有<div class = "item"> <div>
        itemList = response.xpath('//div[@class = "item"]')
        movie = DoubanmovieItem()
        # 循环读取每一个item
        for item in itemList:
        # 爬取top250排名
            movie['rank'] = item.xpath('div[@class = "pic"]/em/text()').extract()

        # 爬取电影名称
            movie['title'] = item.xpath('div[@class = "info"]/div[@class = "hd"]/a/span[@class = "title"][1]/text()').extract()

        #爬取电影海报
            movie['poster'] = item.xpath('div[@class = "pic"]/a/img/@src').extract()

        # 添加对象到列表中
            yield movie
            pass

            # 下一页请求
        next_page = response.xpath('//span[@class = "next"]/a/@href')

        #判断
        if next_page:
            # 拼接网址
            url = response.urljoin(next_page[0].extract())
            # 重新请求parse函数
            yield scrapy.Request(url, self.parse)
            pass
        pass



