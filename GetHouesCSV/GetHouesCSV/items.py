# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GethouescsvItem(scrapy.Item):
    # define the fields for your item here like:
    # 小区名称
    name = scrapy.Field()
    # 租金
    rant = scrapy.Field()
    # 房型
    root_type = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 装修
    decoration = scrapy.Field()
    # 电梯
    elevator = scrapy.Field()
    # 朝向
    toward = scrapy.Field()
    # 详情链接
    url = scrapy.Field()
