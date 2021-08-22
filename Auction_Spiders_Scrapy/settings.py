# Scrapy settings for Auction_Spiders_Scrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Auction_Spiders_Scrapy'

SPIDER_MODULES = ['Auction_Spiders_Scrapy.spiders']
NEWSPIDER_MODULE = 'Auction_Spiders_Scrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Auction_Spiders_Scrapy (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
   'cookie': 'thw=cn; cna=8rDQF1c6fS4CAXnh9oGUkqaa; tracknick=%5Cu5929%5Cu8DEF%5Cu98CE%5Cu884C%5Cu4E4B%5Cu7231; miid=454699911920153047; hng=CN%7Czh-CN%7CCNY%7C156; _cc_=Vq8l%2BKCLiw%3D%3D; xlly_s=1; _samesite_flag_=true; cookie2=152490dbf1ecce2a9532a5165474d331; t=ab05fd698b1e4c211cef87832545f3d3; _tb_token_=719d771ebe5e3; sgcookie=E1000pjZ7J7AquOVbO0E%2BCK9FlbcwZz7DO%2BUmeM6EQ%2BN7uHj11y6yTG5SJ%2BjCFtHBpdKxuqueB%2Fz8OocqHJjRkB0cj78hdO5jeOWENlCDl6NuYY%3D; unb=49280070; uc3=id2=VyUOWs7Troo%3D&nk2=r7kk0YGOXhkbGayK&lg2=V32FPkk%2Fw0dUvg%3D%3D&vt3=F8dCujHuJdHHR%2B5CgTU%3D; csg=4de22d79; lgc=%5Cu5929%5Cu8DEF%5Cu98CE%5Cu884C%5Cu4E4B%5Cu7231; cancelledSubSites=empty; cookie17=VyUOWs7Troo%3D; dnk=%5Cu5929%5Cu8DEF%5Cu98CE%5Cu884C%5Cu4E4B%5Cu7231; skt=c551080e7be389e7; existShop=MTYyOTYyMjQ3NA%3D%3D; uc4=nk4=0%40rVte3KfQVNOnUZFuVGegHLhsSDAEUqM%3D&id4=0%40VXJ%2FFKzAmnj3LZx%2FTiBXNOQw8Q%3D%3D; publishItemObj=Ng%3D%3D; _l_g_=Ug%3D%3D; sg=%E7%88%B108; _nk_=%5Cu5929%5Cu8DEF%5Cu98CE%5Cu884C%5Cu4E4B%5Cu7231; cookie1=AC%2BTgIP8JLxJ4uTfo978VmFgk3YPLcyUsyWP2tCGjdw%3D; mt=ci=96_1; uc1=pas=0&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&existShop=false&cookie21=UIHiLt3xSift4ZS1LW77rg%3D%3D&cookie14=Uoe2xMVGXgygcw%3D%3D&cookie15=W5iHLLyFOGW7aA%3D%3D; isg=BBoasQOlLzdRaZ3hozsPrQ7qa8A8S54lyLj1RySTxq14l7rRDNvuNeDlZ2sLXBa9; l=eBIcm9-POhPNFEvzBOfanurza77OSIRYYuPzaNbMiOCPOWCB5Cr5W6nqodY6C3GNh6UMR3SW3fIXBeYBqQAonxv9m4xN0ikmn; tfstk=crb1Bpfn6AD1biqq71NEQ1Ja2IYAwNlWGl9G1gyQTbY6DL10x4J5DZImH2KJO'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Auction_Spiders_Scrapy.middlewares.AliAuctionSpiderScrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Auction_Spiders_Scrapy.middlewares.AliAuctionSpiderScrapyDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Auction_Spiders_Scrapy.pipelines.AuctionSpiderScrapyALiMySQLPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# DOWNLOADER_MIDDLEWARES = {
#    'Auction_Spiders_Scrapy.useragent.UserAgent': 1,
#    'Auction_Spiders_Scrapy.middlewares.ProxyMiddleware': 2,
# }
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
