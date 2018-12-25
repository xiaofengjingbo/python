# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShanbayscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    en = scrapy.Field()
    row_ind = scrapy.Field()
    voice_url = scrapy.Field()
    id = scrapy.Field()
    symbol = scrapy.Field()
    audio_name = scrapy.Field()
    result_voice = scrapy.Field()
