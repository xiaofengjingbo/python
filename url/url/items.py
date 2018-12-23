# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


#设置要抓取的字段
#summary和url
class UrlItem(scrapy.Item):

    summary = scrapy.Field()
    url = scrapy.Field()
