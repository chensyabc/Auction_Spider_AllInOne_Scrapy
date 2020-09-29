# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class AliAuctionSpiderScrapyPipeline(object):
    def __init__(self):
        self.f = open('TestALiSpider.json', 'wb')

    def process_item(self, item, spider):
        print("process_item...process_item...process_item...process_item...")
        data = json.dumps(dict(item), ensure_ascii=False, indent=4) + ','
        self.f.write(data.encode('utf-8'))

    def close_spider(self, spider):
        print("close_spider...close_spider...close_spider...close_spider...")
        self.f.close()