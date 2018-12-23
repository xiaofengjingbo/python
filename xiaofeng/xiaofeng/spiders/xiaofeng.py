#-*- coding: utf-8 -*-
import scrapy
from xiaofeng.items import XiaofengItem


class XIAOFENGSpider(scrapy.Spider):
    # 爬虫名称，唯一
    name = "xiaofeng"
    # 允许访问的域
    #allowed_domains = ["xiaohuar.com"]
    # 初始URL
    #start_urls = ['http://www.xiaohuar.com/list-1-1.html']

    allowed_domains = ["shanbay.com"]

    start_urls=["https://www.shanbay.com/wordbook/16/"]

    def parse(self, response):
        # 获取所有图片的a标签
        #allPics = response.xpath('//td[@class="wordbook-wordlist-name"]/a')
        allPics = response.xpath('//div[@class="wordbook-create-wordlist-title"]/table/tr')
        for pic in allPics:
            # 分别处理每个图片，取出名称及地址
            item = XiaofengItem()
            addr = pic.xpath('./td[@class="wordbook-wordlist-name"]/a/@href').extract()[0]
            addr = 'https://www.shanbay.com' + addr
            name = pic.xpath('./td[@class="wordbook-wordlist-name"]/a/text()').extract()[0]
            nums = pic.xpath('./td[@class="wordbook-wordlist-count"]')
            num = nums.xpath('string(.)').extract()[0]
            #item['name'] = name
            item['value'] = addr
            item['name'] = name
            item['num'] = num
            print(item)
            # 返回爬取到的数据
            yield item