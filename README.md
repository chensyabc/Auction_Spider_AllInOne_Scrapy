#--How To Use--
1, config Python Interpreter

2, install these packages: Scrapy + selenium + pymysql

###a, ALi Auction Spider
1, change "setting.py=>ITEM_PIPELINES" to be AuctionSpiderScrapyALiMySQLPipeline

2, change "setting.py=>DEFAULT_REQUEST_HEADERS.cookie" to be the one from Browser TaoBao login

3, execute spiders/run.py

###b, JD Auction Spider
1, change "setting.py=>ITEM_PIPELINES" to be AuctionSpiderScrapyxxxMySQLPipeline

###c, GPai Auction Spider
1, change "setting.py=>ITEM_PIPELINES" to be AuctionSpiderScrapyxxxMySQLPipeline



#--Update History--
Finish by 2020/11/12:
1, gpai spider
2, implement scrapy with 3 level parse function
3, save into file and DB

Set aim on 2020/11/12:
1, ali spider
2, implement useragent
3, implement middleware
4, save into file and DB

Finish by 2020/11/19:
1, ali spider
2, save into file and DB
