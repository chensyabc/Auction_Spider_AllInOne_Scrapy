import scrapy
from scrapy.selector import Selector
import re
import sys
sys.path.append(r'../')
from Auction_Spiders_Scrapy.items import AliAuctionSpiderScrapyItem
import json
import time
from datetime import datetime


class AliAuctionSpider(scrapy.Spider):
    name = 'ali_auction_spider'
    allowed_domains = ['taobao.com']
    start_urls = ['https://sf.taobao.com/court_list.htm']
    total_page_count = 0
    parse_count = 0
    retry_count = 0
    failure_count = 0
    start_time = time.time()
    end_time = time.time()
    # scrapy crawl ali_auction_spider --nolog
    # change settings.py cookie

    def parse(self, response):
        self.start_time = datetime.now()
        print(self.name + " start parsing...................................")
        # item['court_name'] = self.get_court_data(response, r'<a href="\S*?\/(\d+)\/(\d+)\S*?" \S+>\s*(\S+)\s*</a>\s*</span>\s*<span class="iconfont-sf">\((\d+)')
        selector = Selector(response)
        # print(selector.extract())
        court_wrapper_list = selector.xpath(".//span[@class='county i-b w-b ']")
        court_long_county_wrapper_list = selector.xpath(".//span[@class='county i-b w-b long-county']")
        # print(court_wrapper_list)
        # for court_wrapper_node in court_wrapper_list[0:2]:
        for court_wrapper_node in court_wrapper_list[0:2]:
            if court_wrapper_node is None:
                continue
            # print(court_wrapper_node.extract())
            court_link = court_wrapper_node.xpath('span/a/@href').extract_first()
            court_url = 'https:' + court_link
            count_part = court_wrapper_node.xpath(".//span[@class='iconfont-sf']/text()").extract_first()
            if count_part == '(0)':
                print('parse court: ' + court_url + ' count is 0, skip, wrapper: ' + court_wrapper_node.extract().replace('\n', '').replace('\r', '').replace('\t', ''))
                continue
            # print(court_url)
            # yield item
            for i in range(0, 5):
                yield scrapy.Request(url=court_url+"?sorder="+str(i), callback=self.parse_auction_list, meta={'parse': 0, 'statusid': i, 'trycount':1})

    def parse_auction_list(self, response):
        selector = Selector(response)
        # restate_char_index = response.url.find("sorder=")
        # restate = -1
        # if restate_char_index > -1:
        #     restate = response.url[restate_char_index + 7:restate_char_index + 8]
        # print(selector.extract())
        if response.meta['parse'] == 1:
            auction_list_python = selector.xpath(".//script[@id='sf-item-list-data']/text()").extract_first()
            auction_list=json.loads(auction_list_python)
            print('process auction list url: ' + response.url)
            for auction_item in auction_list['data'][0:2]:
                auction_item_url = 'https:' + auction_item['itemUrl']
                yield scrapy.Request(url=auction_item_url, callback=self.parse_auction_detail, meta={'title': auction_item['title'], 'statusid': response.meta['statusid']})
        else:
            total_page = selector.xpath(".//em[@class='page-total']/text()").extract_first()
            if total_page is not None:
                print('parse court: ' + response.url + ' total_page: ' + total_page)
                self.total_page_count += int(total_page)
                print(selector.xpath(".//li[@class='current']").extract())
                base_path = 'https:' + selector.xpath(".//li[@class='current']/a/@href").extract_first()
                for i in range(int(total_page)):
                    auction_list_url = base_path + '&page=' + str(i)
                    yield scrapy.Request(url=auction_list_url, callback=self.parse_auction_list, meta={'parse': 1, 'statusid': response.meta['statusid']})
            else:
                if selector.extract().find('亲，小二正忙，滑动一下马上回来')>0:
                    reason = 'due to need drag in view: 亲，小二正忙，滑动一下马上回来'
                elif selector.extract().find('将用户正常页面写入到 x5referer ，以备后续跳转返回')>0:
                    reason = "due to expired cookie: 将用户正常页面写入到 x5referer ，以备后续跳转返回"
                    # TODO: try with call request with setting to another cookie. 3/29/2021
                    yield scrapy.Request(url=response.url, callback=self.parse_auction_list, meta=response.meta)
                if selector.extract().find('很抱歉，没有您要找的标的物，') > 0:
                    reason = 'due to need drag in view: 很抱歉，没有您要找的标的物，'
                # elif selector.extract().find('霸下通用') > 0:
                #     reason = "due to blabla verification code: 霸下通用 web 页面 - 验证码"
                #     # TODO: try with call request with setting to another cookie. 8/22/2021
                #     yield scrapy.Request(url=response.url, callback=self.parse_auction_list, meta=response.meta)
                else:
                    reason = 'unknown reason -- ' + selector.extract()
                print('parse court: ' + response.url + ' page not found because: ' + reason)

    def parse_auction_detail(self, response):
        print('1, parse auction item url:' + response.url)
        self.parse_count += 1
        selector = Selector(response)
        # print(selector.extract().replace('\n', '').replace('\r', '').replace('\t', ''))
        try:
            detail_trs_xpath = selector.xpath(".//tbody[@id='J_HoverShow']/tr")
            # print(detail_trs_xpath.extract())
            # print(detail_trs_xpath.extract_first().replace('\n', '').replace('\r', '').replace('\t', ''))
            current_price = selector.xpath(".//span[@class='pm-current-price J_Price']/em/text()").extract_first().strip().replace(',', '')
            content = detail_trs_xpath[0].xpath("td/span/text()").extract_first()
            if content == "保证金":
                print("   condition a: " + content)
                start_price = detail_trs_xpath[1].xpath("td/span[@class='pay-price']/span/text()").extract_first().strip().replace(',', '')
                cash_deposit = detail_trs_xpath[0].xpath("td/span/span[@class='J_Price']/text()").extract_first().strip().replace(',', '')
                access_price = detail_trs_xpath[1].xpath("td/span/span[@class='J_Price']/text()").extract_first().strip().replace(',', '')
                fare_increase = detail_trs_xpath[2].xpath("td/span/span[@class='J_Price']/text()").extract_first().strip().replace(',', '')
                # print(cash_deposit)
            else:
                print("   condition b: " + content)
                start_price = detail_trs_xpath[2].xpath("td/span[@class='pay-price']/span/text()").extract_first().strip().replace(',', '')
                cash_deposit = detail_trs_xpath[0].xpath("td[@class='J_PaySellOff pay-selloff']/span/span[@class='J_Price']/text()").extract_first().strip().replace(',', '')
                access_price = detail_trs_xpath[1].xpath("td/span/span[@class='J_Price']/text()").extract_first().strip().replace(',', '')
                fare_increase = detail_trs_xpath[2].xpath("td/span/span[@class='J_Price']/text()").extract_first().strip().replace(',', '')
                # print(cash_deposit)
            # print('pm-current-price: '+str(selector.xpath(".//span[@class='pm-current-price J_Price']")))
            item = AliAuctionSpiderScrapyItem()
            item['Title'] = response.meta['title']
            item['URL'] = response.url
            item['StartPrice'] = float(start_price)
            item['CurrentPrice'] = float(current_price)
            item['CashDeposit'] = float(cash_deposit)
            item['AssessPrice'] = float(access_price)
            item['Increment'] = float(fare_increase)
            item['CreatedOn'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            item['UpdatedOn'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            item['StatusId'] = response.meta['statusid']
            print('2, yield auction item')
            yield item
        except Exception as ex:
            reason = ''
            if selector.extract().find('亲，小二正忙，滑动一下马上回来') > 0:
                reason = 'due to need drag in view: 亲，小二正忙，滑动一下马上回来'
            if selector.extract().find('霸下通用 web 页面') > 0:
                reason = 'due to need drag in view: 霸下通用 web 页面'
            print("2, parse_auction_detail failure detail -- code: %s detail: " % (ex.args[0]) + ' reason: ' + reason)
            self.failure_count += 1

    def closed(self, reason):
        self.end_time = datetime.now()
        duration = (self.end_time - self.start_time).seconds
        print('total duration: ' + str(duration) + 's')
        print('total page: ' + str(self.total_page_count))
        if self.total_page_count == 0:
            each_page_duration = 0
        else:
            each_page_duration = duration / self.total_page_count
        print('each page duration: ' + str(each_page_duration) + 's')
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