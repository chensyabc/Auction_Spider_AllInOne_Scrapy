import scrapy
from scrapy.selector import Selector
import re
import sys
sys.path.append(r'../')
from Auction_Spiders_Scrapy.items import AliAuctionSpiderScrapyItem
import json


class JDAuctionSpider(scrapy.Spider):
    name = 'jd_auction_spider'
    allowed_domains = ['jd.com']
    start_urls = ['https://paimai.jd.com/services/currentList.action?paimaiIds=116786339-117135333-117134916-117135372-117586115-117585932-116181957-117597427-117587873-117600181-117588477-117595650-117595476-117592620-117259028-117246797-117601068-117253553-117256215-117585607-117588021-117587730-117584972-117595751-117529916-117585616-117565886-117588498-117752868-117586093-117230958-117257892-117595507-117548491-117565806-117208528-116257520-117256370-117565970-117562889&callback=jQuery1348314&=1601625401404']

    def parse(self, response):
        print(self.name + " start parsing...................................")
        # item['court_name'] = self.get_court_data(response, r'<a href="\S*?\/(\d+)\/(\d+)\S*?" \S+>\s*(\S+)\s*</a>\s*</span>\s*<span class="iconfont-sf">\((\d+)')
        # print("response: " + Selector(response))
        # response.body.decode(response.encoding)
        selector = Selector(response)
        # print(selector.extract())
        # json_urls = json.dump(selector.extract())
        # print(selector.xpath('.//p/text()').extract_first())
        json_urls_str = selector.xpath('.//p/text()').extract_first()
        json_urls_str = json_urls_str[14:-1]
        print('json_urls_str')
        print(json_urls_str)
        # json_urls_str = json_urls_str[13:]
        # print(json_urls_str[13:])
        json_urls = json.loads(json_urls_str)
        print("json_urls")
        print(json_urls)
        # court_node_list = selector.xpath('.//span/span/a')
        # auction_list = selector.xpath('.//li[@class=pm-item]/a')
        # print(auction_list)
        for json_url in json_urls:
            if json_url is None:
                break
            print('json_url')
            print(json_url)
            item = AliAuctionSpiderScrapyItem()
            item['court_name'] = json_url['productId']
            # item['court_name'] = court_node.xpath('./a/@href').extract_first().strip()
            item['court_url'] = 'https://api.m.jd.com/api?appid=paimai&functionId=getProductBasicInfo&body={%22paimaiId%22:' + str(json_url['paimaiId'])+'}&loginType=3&jsonp=jsonp_1601644011323_6068'
            # yield item
            # yield item
            yield scrapy.Request(url=item['court_url'], callback=self.parse_auction_list, meta={'item': item})
        # print(court.xpath('.//a/@href').extract().strip())


    def parse_auction_list(self, response):
        total_page = response.xpath("//span[@class=page-skip]/em/text()").extract_first()
        auction_list = response.xpath("//a[@class=link-wrap]/@href").extract_first()
        for auction_url in auction_list:
            item = AliAuctionSpiderScrapyItem()
            # item['court_name'] = court_node.xpath('./text()').extract_first().strip()
            item['court_url'] = 'https://' + auction_url.extract()
            yield item

        # if self.page < int(2):
        #     self.page += 1
        #     yield scrapy.Request(self.base_url+str(self.page), callback=self.parse)
        #
        #     def parse_auction_list(self, response):
        #         if self.page < int(2):
        #             self.page += 1
        #             yield scrapy.Request(self.base_url + str(self.page), callback=self.parse)

    def parse_auction_detail(self, response):
        selector = Selector(response)
        print('parse_auction_detail selector')
        auction_detail_str = selector.xpath('.//p/text()').extract_first()
        auction_detail_str = auction_detail_str[25:-2]
        print('auction_detail_str')
        print(auction_detail_str)
        # json_urls_str = json_urls_str[13:]
        # print(json_urls_str[13:])
        auction_detail_json = json.loads(auction_detail_str)
        # print(json_urls[0]['productAddressResult']['address'])
        print('auction_detail_json')
        item = AliAuctionSpiderScrapyItem()
        item['court_name'] = auction_detail_json['data']['title']
        item['court_url'] = auction_detail_json['data']['startPrice']
        yield item

    # def get_court_data(self, response, court_item_regex):
    #     # html = UrlUtil.get_html(response)
    #     court_data_list = re.findall(re.compile(court_item_regex, re.S), response.decode('gbk'))
    #     return court_data_list