import scrapy
from scrapy.selector import Selector
import re
import sys
sys.path.append(r'../')
from Ali_Auction_Spider_Scrapy.items import AliAuctionSpiderScrapyItem


class AliSpiderSpider(scrapy.Spider):
    name = 'ali_spider'
    allowed_domains = ['taobao.com']
    start_urls = ['https://sf.taobao.com/court_list.htm']

    def parse(self, response):
        print("ali_spider_simple start parsing...................................")
        # item['court_name'] = self.get_court_data(response, r'<a href="\S*?\/(\d+)\/(\d+)\S*?" \S+>\s*(\S+)\s*</a>\s*</span>\s*<span class="iconfont-sf">\((\d+)')
        # print("response: " + Selector(response))
        # response.body.decode(response.encoding)
        selector = Selector(response)
        court_node_list = selector.xpath('.//span/span/a')
        for court_node in court_node_list:
            item = AliAuctionSpiderScrapyItem()
            item['court_name'] = court_node.xpath('./text()').extract_first().strip()
            item['court_url'] = 'https://' + court_node.xpath('./@href').extract_first()
            # yield item
            yield item
            yield scrapy.Request(url=item['court_url'], callback=self.parse_auction_list, meta={'item': item})
        # print(court.xpath('.//a/@href').extract().strip())


    def parse_auction_detail(self, response):
        if self.page < int(2):
            self.page += 1
            yield scrapy.Request(self.base_url+str(self.page), callback=self.parse)

            def parse_auction_list(self, response):
                if self.page < int(2):
                    self.page += 1
                    yield scrapy.Request(self.base_url + str(self.page), callback=self.parse)

    def get_court_data(self, response, court_item_regex):
        # html = UrlUtil.get_html(response)
        court_data_list = re.findall(re.compile(court_item_regex, re.S), response.decode('gbk'))
        return court_data_list