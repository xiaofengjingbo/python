# -*- coding: utf-8 -*-
import os
import MySQLdb
from scrapy.exceptions import DropItem
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

INDEX = 1
DATE = "2015-02-26"

class UrlPipeline(object):

    def __init__(self):
        try:
            self.db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="1234", port=3306, db="html_url",  charset="utf8")
            self.cursor = self.db.cursor()
            print "Connect to db successfully!"

        except:
            print "Fail to connect to db!"

    def process_item(self, item, spider):
        global INDEX
        global DATE
        if item['summary']:
            u = 0
            for summary in item['summary']:
                url = 'http://baike.baidu.com'+item['url'][u]
                param = (INDEX, summary, url, DATE, '1')
                sql = "insert into documents (id,summary,url,date_info,group_id) values(%s,%s,%s,%s,%s)"
                self.cursor.execute(sql, param)
                u = u + 1
                INDEX = INDEX + 1

        else:
            raise DropItem(item)

        return item


    def close_spider(self, spider):
        self.db.commit()
        self.db.close
        print("Done")