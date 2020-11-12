# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import pymysql


class AuctionSpiderScrapyPipeline(object):
    def __init__(self):
        self.f = open('TestSpider.json', 'wb')

    def process_item(self, item, spider):
        print("process_item...process_item...process_item...process_item...")
        data = json.dumps(dict(item), ensure_ascii=False, indent=4) + ','
        self.f.write(data.encode('utf-8'))

    def close_spider(self, spider):
        print("close_spider...close_spider...close_spider...close_spider...")
        self.f.close()


class AuctionSpiderScrapyMySQLPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(host='localhost', user='root', password='chensy123', db='auction_spider_gpai', port=3306)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            # print("MySQLPipeline...process_item..................")
            # self.cursor.execute('insert into Auctions(Title,Url,StartPrice) VALUES ("{}","{}","{}")'.format(item['auction_title'], item['auction_url'], item['start_price']))

            # TODO, do update when previous one exists
            # sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
            # update = ','.join([" {key} = %s".format(key=key) for key in item.keys])
            # sql += update

            sql = self.generate_sql('Auctions2', item)
            self.cursor.execute(sql, tuple(item.values()))
            self.connect.commit()
            return item
        except pymysql.Error as e:
            print("Connect DB Failure e: code: %d detail: %s" % (e.args[0], e.args[1]))
        except Exception as ex:
            print("Connect DB Failure ex: code: %d detail: %s" % (ex.args[0], ex.args[1]))

    def close_spider(self, spider):
        print(".........................................pipelines execution has been done, close_MySQLPipeline.........................................")
        self.cursor.close()
        self.connect.close()

    def generate_sql(self, table, item):
        keys = ', '.join(item.keys())
        values = ', '.join(['%s'] * len(item))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
        return sql
