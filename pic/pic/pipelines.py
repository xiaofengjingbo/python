# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib.request
import os


class PicPipeline(object):
    def process_item(self, item, spider):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        res = urllib.request.urlopen(item['addr'])
        file_name = os.path.join(r'/Users/xiaofeng/Desktop/aaa', item['name'] + '.jpg')
        with open(file_name, 'wb') as fp:
            fp.write(res.read())
