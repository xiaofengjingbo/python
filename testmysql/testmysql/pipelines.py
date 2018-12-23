import pymysql


class TestmysqlPipeline(object):
    def __init__(self):
        # connection database
        self.connect = pymysql.connect('localhost', 'root', 'root', 'tongcheng', use_unicode=True, charset='utf8')
        # get cursor
        self.cursor = self.connect.cursor()
        print("connecting mysql success!")

    def process_item(self, item, spider):
        print("start writing datas...")
        try:
            for i in range(0, len(item['title'])):
                # insert data
                sqlstr = "insert into zhaoping(title,companyname,getfree,money) VALUES('%s','%s','%s','%s')" % (
                item['title'][i], item['comname'][i], item['getfree'][i], item['money'][i])
                self.cursor.execute(sqlstr)
                self.connect.commit()
            self.connect.close()
        except Exception as error:
            # print error
            print(error)
        return item
