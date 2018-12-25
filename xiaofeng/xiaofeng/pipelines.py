# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook

class XiaofengPipeline(object):
        def __init__(self):
            self.wb = Workbook()  # class实例化
            self.ws = self.wb.active  # 激活工作表

        def process_item(self, item, spider):
            print(item['num'].replace("\n", "").strip()[4:])

            line = [item['name'],item['value'],item['num'].replace("\n", "").strip()[4:]]  # 把数据中每一项整理出来
            self.ws.append(line)  # 将数据以行的形式添加到xlsx中
            self.wb.save('/Users/xiaofeng/Desktop/chuzhongpagelist.xlsx')  # 保存xlsx文件
            return item
