# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import xlrd
from scrapy.http.request import Request
from scrapy.pipelines.files import FilesPipeline
from xlutils.copy import copy


class DownloadVoicePipeline(FilesPipeline):
    # def get_media_requests(self, item, info):
    #     voice_url = item["voice_url"]
    #     return [Request(voice_url)]

    def file_path(self, request, response=None, info=None):
        super(DownloadVoicePipeline, self).file_path(request, response, info)
        path = request.url
        path = path[path.rindex("/") + 1:]
        return path

    # def item_completed(self, results, item, info):
    #     file_path = [x['path'] for ok, x in results if ok]
    #     if file_path:
    #         print("file path :" + file_path)
    #     return item


class ChangeExcelPipeline(object):
    def __init__(self, excel_uri, new_excel):
        self.new_excel = new_excel
        self.workbook = copy(xlrd.open_workbook(excel_uri))
        self.sheet = self.workbook.get_sheet(0)

    def process_item(self, item, spider):
        row_ind = item['row_ind']
        voice_url = item['voice_url']
        has_collins_defn = item['has_collins_defn']
        self.sheet.write(row_ind, 6, voice_url)
        self.sheet.write(row_ind, 8, has_collins_defn)
        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.workbook.save(self.new_excel)

    @classmethod
    def from_settings(cls, settings):
        excel_uri = settings['TARGET_EXCEL_PATH']
        new_excel = settings['NEW_EXCEL_PATH']
        return cls(excel_uri=excel_uri, new_excel=new_excel)
