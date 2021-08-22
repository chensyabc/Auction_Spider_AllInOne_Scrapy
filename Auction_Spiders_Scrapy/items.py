# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AliAuctionSpiderScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    Title = scrapy.Field()
    URL = scrapy.Field()
    StartPrice = scrapy.Field()
    CurrentPrice = scrapy.Field()
    AssessPrice = scrapy.Field()
    CashDeposit = scrapy.Field()
    Increment = scrapy.Field()
    DelayCycle = scrapy.Field()
    auction_online_cycle = scrapy.Field()
    # auction_time = scrapy.Field()
    # contact_name = scrapy.Field()
    ContactPhone = scrapy.Field()
    # priority_buyer_name = scrapy.Field()
    CreatedOn = scrapy.Field()
    UpdatedOn = scrapy.Field()
    StatusId = scrapy.Field()
    pass


class AuctionSpiderScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    CourtName = scrapy.Field()
    Title = scrapy.Field()
    URL = scrapy.Field()
    StartPrice = scrapy.Field()
    CurrentPrice = scrapy.Field()
    AssessPrice = scrapy.Field()
    CashDeposit = scrapy.Field()
    Increment = scrapy.Field()
    DelayCycle = scrapy.Field()
    auction_online_cycle = scrapy.Field()
    # auction_time = scrapy.Field()
    # contact_name = scrapy.Field()
    ContactPhone = scrapy.Field()
    # priority_buyer_name = scrapy.Field()
    CreatedOn = scrapy.Field()
    UpdatedOn = scrapy.Field()
    StatusId = scrapy.Field()
    pass
