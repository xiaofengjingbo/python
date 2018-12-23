import scrapy
from ..items import TestmysqlItem


class YinyeyuanSpider(scrapy.Spider):
    name = 'yingyeyuan'
    # allowed_domains = ['http://cs.58.com/yingyeyuan/']
    start_urls = ['http://cs.58.com/yingyeyuan/']

    def parse(self, response):
        # 获取标题
        title = response.xpath(".//*[@id='list_con']/li/div[1]/div[1]/a/span[2]/text()").extract()
        # 获取公司名称
        comname = response.xpath(".//*[@id='list_con']/li/div[2]/div/a/text()").extract()
        # 获取工资
        money = response.xpath(".//*[@id='list_con']/li/div[1]/p/text()").extract()
        # 获取福利
        getfree = response.xpath(".//*[@id='list_con']/li/div[1]/div[2]/span[1]/text()").extract()

        # 实例化TongchengItem类
        tongcheng = TestmysqlItem()
        # 存入items
        tongcheng["title"] = title
        tongcheng["comname"] = comname
        tongcheng["money"] = money
        tongcheng["getfree"] = getfree
        yield tongcheng
