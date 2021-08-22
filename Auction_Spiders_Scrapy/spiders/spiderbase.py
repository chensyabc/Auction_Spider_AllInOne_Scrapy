import scrapy
from scrapy.selector import Selector
import re
import sys
sys.path.append(r'../')
from Auction_Spiders_Scrapy.items import AliAuctionSpiderScrapyItem
import json
import time
from datetime import datetime


class SpiderBase(scrapy.Spider):
    def parse(self, response, **kwargs):
        pass

    total_page_count = 0
    parse_count = 0
    retry_count = 0
    failure_count = 0
    start_time = time.time()
    end_time = time.time()

    def closed(self, reason):
        self.end_time = datetime.now()
        duration = (self.end_time - self.start_time).seconds
        print('duration: ' + str(duration) + 's')
        print('each page duration: ' + str(duration/self.total_page_count) + 's')
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ': total parse: ' + str(self.parse_count) +' retry parse: ' + str(self.retry_count) + ' success parse: ' + str(self.parse_count - self.retry_count - self.failure_count) + ' failure count: ' + str(self.failure_count))


    # def get_court_data(self, response, court_item_regex):
    #     # html = UrlUtil.get_html(response)
    #     court_data_list = re.findall(re.compile(court_item_regex, re.S), response.decode('gbk'))
    #     return court_data_list
    # if self.page < int(2):
    #     self.page += 1
    #     yield scrapy.Request(self.base_url+str(self.page), callback=self.parse)
    #
    #     def parse_auction_list(self, response):
    #         if self.page < int(2):
    #             self.page += 1
    #             yield scrapy.Request(self.base_url + str(self.page), callback=self.parse)