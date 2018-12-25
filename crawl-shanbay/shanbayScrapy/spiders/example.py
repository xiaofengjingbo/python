# -*- coding: utf-8 -*-
import scrapy
import xlrd
import time
import json
from ..items import ShanbayscrapyItem


class ExampleSpider(scrapy.Spider):
    name = 'shanbay'
    # allowed_domains = ['shanbay.com']
    search_template = 'https://www.shanbay.com/api/v1/bdc/search/?version=2&word={0}&_={1}'
    # start_urls = ['https://www.shanbay.com/api/v1/bdc/search/?version=2&word=still&_=1529148124687']

    def start_requests(self):
        path = self.crawler.settings.get('TARGET_EXCEL_PATH')
        workbook = xlrd.open_workbook(path)
        sheet_names = workbook.sheet_names()
        if len(sheet_names) > 0:
            first_sheet = workbook.sheet_by_name(sheet_names[0])
            # sheet的名称，行数，列数
            print('sheet的名称',first_sheet.name, first_sheet.nrows, first_sheet.ncols)
            for i in range(first_sheet.nrows+1):
                en = first_sheet.row(i)[0]
                if en.ctype == 1:
                    millisecond = (int(round(time.time() * 1000)))
                    value = en.value
                    print('111111111111111111111',value)
                    url = self.search_template.format(value, millisecond)
                    item = ShanbayscrapyItem()
                    item['en'] = value
                    item['row_ind'] = i
                    yield scrapy.Request(url=url, callback=self.parse, meta={'item': item})




    def parse(self, response):
        item = response.meta['item']
        json_dict = json.loads(response.body)
        print(json_dict)
        if 'msg' in json_dict and json_dict['msg'] == 'SUCCESS' and 'data' in json_dict \
                and 'audio_addresses' in json_dict['data'] \
                and 'us' in json_dict['data']['audio_addresses']:
            us_arr = json_dict['data']['audio_addresses']['us']
            if len(us_arr) > 0:
                for i in range(len(us_arr)):
                    if us_arr[i].startswith('http://'):
                        item['voice_url'] = [us_arr[i]]
                        if 'audio_name' in json_dict['data']:
                            item['audio_name'] = json_dict['data']['audio_name']
                        if 'id' in json_dict['data']:
                            item['id'] = json_dict['data']['id']
                        if 'pronunciations' in json_dict['data']:
                            item['symbol'] = json_dict['data']['pronunciations']['us']
                        yield item