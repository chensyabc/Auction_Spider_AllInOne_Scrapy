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
   'cookie': 't=4546a0c6b354254696be2d7b44819f52; thw=cn; xlly_s=1; cookie2=73401570ddfecc142e0bdd2631e55d6b; _tb_token_=3ea37935b937e; _samesite_flag_=true; cna=8rDQF1c6fS4CAXnh9oGUkqaa; sgcookie=E100CTyFs7CDal8FxHw0B8sQSuZ745OoPgkSQXYSA9Oz8jdKsUTlSPRFHJYW7TaPLXDTf%2FzieHI6SPKZpIUOOxOANQ%3D%3D; unb=49280070; uc3=vt3=F8dCufHBy92RtVTkqOQ%3D&id2=VyUOWs7Troo%3D&nk2=r7kk0YGOXhkbGayK&lg2=UIHiLt3xD8xYTw%3D%3D; csg=c07203f6; lgc=%5Cu5929%5Cu8DEF%5Cu98CE%5Cu884C%5Cu4E4B%5Cu7231; cookie17=VyUOWs7Troo%3D; dnk=%5Cu5929%5Cu8DEF%5Cu98CE%5Cu884C%5Cu4E4B%5Cu7231; skt=63d0adbd4d9c4119; existShop=MTYwMjQyMzQ4MQ%3D%3D; uc4=nk4=0%40rVte3KfQVNOnUZFuVGegHtq5Dv1A3Pg%3D&id4=0%40VXJ%2FFKzAmnj3LZx9Z4WrHw%2F6ZA%3D%3D; publishItemObj=Ng%3D%3D; tracknick=%5Cu5929%5Cu8DEF%5Cu98CE%5Cu884C%5Cu4E4B%5Cu7231; _cc_=VT5L2FSpdA%3D%3D; _l_g_=Ug%3D%3D; sg=%E7%88%B108; _nk_=%5Cu5929%5Cu8DEF%5Cu98CE%5Cu884C%5Cu4E4B%5Cu7231; cookie1=AC%2BTgIP8JLxJ4uTfo978VmFgk3YPLcyUsyWP2tCGjdw%3D; mt=ci=38_1; uc1=cookie15=V32FPkk%2Fw0dUvg%3D%3D&pas=0&cookie21=U%2BGCWk%2F7ow0zmglPa33heg%3D%3D&existShop=false&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie14=Uoe0b0F4vp71rw%3D%3D; isg=BB0dKHdfHj_B_frIuKowlLWrLPkXOlGMH0THod_jBnSvljzIpY8_XakUwoKQTWlE; l=eBIcm9-POhPNFcNbBOfanurza77OSIRYYuPzaNbMiOCPOB1B5x0CWZ5c1k86C3GNh6YJR3usn_92BeYBqQAonxv9w8VMULkmn; tfstk=cBmGB_2JoVz1IQ4nPhZsez9SE3xRwCs4ZmoIYDrd2tKhra5c-w7zgZv3sfmAl'
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
   'Auction_Spiders_Scrapy.pipelines.AuctionSpiderScrapyMySQLPipeline': 300,
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
