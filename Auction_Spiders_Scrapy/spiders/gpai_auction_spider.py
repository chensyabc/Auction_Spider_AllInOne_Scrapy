import scrapy
from scrapy.selector import Selector
import re
import sys
sys.path.append(r'../')
from Auction_Spiders_Scrapy.items import AuctionSpiderScrapyItem
import json
from selenium import webdriver
# import DateTimeUtil
import time
from datetime import datetime
# import DateTimeUtil


class GPaiAuctionSpider(scrapy.Spider):
    name = 'gpai_auction_spider'
    allowed_domains = ['gpai.net']
    # start_urls = ['http://www.gpai.net/sf/search.do?action=court']
    start_urls = ['http://www.gpai.net/sf/search.do?action=court&cityNum=35&restate=1','http://www.gpai.net/sf/search.do?action=court&cityNum=35&restate=2','http://www.gpai.net/sf/search.do?action=court&cityNum=35&restate=3','http://www.gpai.net/sf/search.do?action=court&cityNum=35&restate=4']
    total_page_count = 0
    parse_count = 0
    retry_count = 0
    failure_count = 0
    start_time = time.time()
    end_time = time.time()
    # scrapy crawl gpai_auction_spider --nolog

    def parse(self, response):
        self.start_time = datetime.now()
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + " " + self.name + " start parsing...................................")
        selector = Selector(response)
        # print(selector.extract())
        # court_node_list = selector.xpath('.//span/span/a')
        total_page = selector.xpath(".//span[@class='page-infos']/label/text()")
        if total_page:
            self.total_page_count = int(total_page.extract_first()[1:-1])
        else:
            self.total_page_count = 1
        print('total page count: ' + str(self.total_page_count))
        for page_count in range(self.total_page_count):
            page_url = response.url + '&Page=' + str(page_count)
            # print("process page " + str(page_count) + " url: " + page_url)
            yield scrapy.Request(url=page_url, callback=self.parse_auction_list)

    def parse_auction_list(self, response):
        selector = Selector(response)
        # print('parse_auction_list ' + response.url)
        auction_urls = selector.xpath(".//div[@class='list-item']/a/@href")
        auction_urls_extract = auction_urls.extract()
        # auction_urls_extract = ['http://www.gpai.net/sf/item2.do?Web_Item_ID=29999']
        restate_char_index = response.url.find("restate=")
        restate = -1
        if restate_char_index > -1:
            restate = response.url[restate_char_index + 8:restate_char_index + 9]
        for i in range(len(auction_urls_extract)):
            # item['court_name'] = court_node.xpath('./text()').extract_first().strip()
            # print("process page " + str(i) + " url: " + auction_urls_extract[i])
            yield scrapy.Request(url=auction_urls_extract[i], callback=self.parse_auction_detail, meta={'try_time': 1, 'restate':restate})

    def parse_auction_detail(self, response):
        try:
            self.parse_count += 1
            if int(response.meta['try_time']) > 1:
                self.retry_count += 1
            print('1, start parse_auction_detail ' + response.url)
            selector = Selector(response)
            # print(selector.extract())
            details_tbody = selector.xpath(".//div[@class='d-m-tb']/table")
            access_price = float(details_tbody.xpath("tr")[3].xpath("td/text()")[0].extract().strip().replace('\r', '').replace('\n', '').replace('\t', '').replace(',', '')[4:-1])
            # print(access_price)
            deposit = float(details_tbody.xpath("tr")[2].xpath("td/text()")[2].extract().strip().replace('\r', '').replace('\n', '').replace('\t', '').replace(',', '')[4:-1])
            # print(deposit)
            increment = float(selector.xpath(".//span[@id='Price_Step']/text()").extract_first().replace('元',''))
            # print(increment)
            price_xpath = selector.xpath(".//div[@class='d-m-price']/p/b/text()")
            if price_xpath:
                item = AuctionSpiderScrapyItem()
                item['CourtName'] = selector.xpath(".//td[@class='pr7']/text()").extract_first().strip()[5:]#response.meta['title']
                item['Title'] = selector.xpath(".//div[@class='d-m-title']/b/text()").extract_first().strip()#response.meta['title']
                item['URL'] = response.url
                item['StartPrice'] = float(selector.xpath(".//span[@id='Price_Start']/text()").extract_first().strip())
                item['CurrentPrice'] = float(price_xpath.extract_first().strip())
                item['AccessPrice'] = access_price
                item['CashDeposit'] = deposit
                item['Increment'] = increment
                item['CreatedOn'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                item['UpdatedOn'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                item['UpdatedOn'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                item['StatusId'] = response.meta['restate']
                print('2, yield ' + response.url)
                yield item
            else:
                print('null price value field' + selector.xpath(".//div[@class='d-m-price']").extract())
        except Exception as ex:
            # print(selector.extract())
            redirect_url = selector.xpath('.//script/text()').extract_first()[22:-2]
            # print('parse_auction_detail failure: url ' + response.url)
            # print("parse_auction_detail failure detail -- code: %d detail: %s" % (ex.args[0], ex.args[1]))
            print("2, parse_auction_detail failure detail -- code: %s detail: " % (ex.args[0]))
            if int(response.meta['try_time']) == 3:
                self.failure_count += 1
                print("3, try 3 times still error with redirect_url: " + redirect_url)
            else:
                print("3, try again with redirect_url: " + redirect_url)
                yield scrapy.Request(url=redirect_url, callback=self.parse_auction_detail, meta={'try_time': int(response.meta['try_time']) + 1, 'restate': response.meta['restate']})

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