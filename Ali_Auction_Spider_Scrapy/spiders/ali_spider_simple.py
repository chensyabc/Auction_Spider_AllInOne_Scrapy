import scrapy


class AliSpiderSimpleSpider(scrapy.Spider):
    name = 'ali_spider_simple'
    allowed_domains = ['taobao.com']
    start_urls = ['https://sf.taobao.com/court_list.htm']

    def parse(self, response):
        print("ali_spider_simple start parsing...................................")
        pass
