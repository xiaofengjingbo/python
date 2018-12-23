#-*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from url.items import UrlItem

#爬取相关页面的summary和url
#存进页面的item列表里
class URLSpider(CrawlSpider):

    name = "url"

    allowed_domains = ["baidu.com"]

    start_urls=["http://baike.baidu.com/fenlei/%E7%BE%8E%E9%A3%9F?limit=30&index=1&offset=0#gotoList"]

    rules = [
        Rule(SgmlLinkExtractor(allow=('.*#gotoList')),  callback = 'parse_url', follow=True),
        ]

    def parse_url(self, response):
        item = UrlItem()

        item['url'] = response.selector.xpath('//div[@class="list"]/a/@href').extract()
        item['summary'] = response.selector.xpath('//div[@class="list"]/a/text()').extract()

        yield item