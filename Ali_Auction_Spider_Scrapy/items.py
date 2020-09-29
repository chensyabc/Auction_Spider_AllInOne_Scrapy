# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AliAuctionSpiderScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    court_name = scrapy.Field()
    court_url = scrapy.Field()
    pass
