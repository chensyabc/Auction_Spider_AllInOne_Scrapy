from scrapy import cmdline


cmd = 'scrapy crawl ali_auction_spider --nolog'
cmdline.execute(cmd.split())