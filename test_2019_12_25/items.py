# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

## 存储数据
class Test20191225Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    # company_code=scrapy.Field()
    # company_name=scrapy.Field()
    # date=scrapy.Field()
    # mail_type=scrapy.Field()
    # mail_title=scrapy.Field()

    ##巨潮资讯网
    secCode=scrapy.Field()
    secName=scrapy.Field()
    announcementTitle=scrapy.Field()
    announcementTime=scrapy.Field()
    adjunctUrl=scrapy.Field()


class JuchaoZiXunItem(scrapy.Item):
     ##巨潮资讯网
    secCode=scrapy.Field()
    secName=scrapy.Field()
    announcementTitle=scrapy.Field()
    announcementTime=scrapy.Field()
    file_urls=scrapy.Field()
    files=scrapy.Field()
##减持的文档
class Zixun_shItem(scrapy.Item):
    secCode=scrapy.Field()
    secName=scrapy.Field()
    announcementTitle=scrapy.Field()
    announcementTime=scrapy.Field()
    file_urls=scrapy.Field()
    files=scrapy.Field()
    zixun_type=scrapy.Field()
class Zixun_szItem(scrapy.Item):
    secCode=scrapy.Field()
    secName=scrapy.Field()
    announcementTitle=scrapy.Field()
    announcementTime=scrapy.Field()
    file_urls=scrapy.Field()
    files=scrapy.Field()
    zixun_type=scrapy.Field()
class Zixun_decreaseItem(scrapy.Item):
    secCode=scrapy.Field()
    secName=scrapy.Field()
    announcementTitle=scrapy.Field()
    announcementTime=scrapy.Field()
    file_urls=scrapy.Field()
    files=scrapy.Field()
    zixun_type=scrapy.Field()
class Zixun_hotItem(scrapy.Item):
    secCode=scrapy.Field()
    secName=scrapy.Field()
    announcementTitle=scrapy.Field()
    announcementTime=scrapy.Field()
    file_urls=scrapy.Field()
    files=scrapy.Field()
    zixun_type=scrapy.Field()
