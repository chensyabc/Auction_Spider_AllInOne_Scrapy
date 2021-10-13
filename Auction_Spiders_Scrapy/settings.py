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
   'cookie': '_uab_collina=160233935637893845930814; thw=cn; cna=8rDQF1c6fS4CAXnh9oGUkqaa; tracknick=%5Cu5929%5Cu8DEF%5Cu98CE%5Cu884C%5Cu4E4B%5Cu7231; miid=454699911920153047; hng=CN%7Czh-CN%7CCNY%7C156; enc=c%2FSebd4TrDXLblCTMu2SxTUkT%2B5eOgvJNOVsxCQ2cPLc5Ni6PLNLM7eIIri9k%2FQd7mpNlFLDvHqV17fh%2Ba27Dw%3D%3D; t=fa4e0065ea4f4cacf7adfd3f1a600f31; _m_h5_tk=f6e4271afd6604d2dfd8e5a7db5e6eb8_1634129557553; _m_h5_tk_enc=05ab862c6f1b7ad79f106abd98eaf970; xlly_s=1; cookie2=1c05530d052716164f9e678ad1d1dac7; _tb_token_=35e9ab1b13335; _samesite_flag_=true; unb=49280070; lgc=%5Cu5929%5Cu8DEF%5Cu98CE%5Cu884C%5Cu4E4B%5Cu7231; cancelledSubSites=empty; cookie17=VyUOWs7Troo%3D; dnk=%5Cu5929%5Cu8DEF%5Cu98CE%5Cu884C%5Cu4E4B%5Cu7231; publishItemObj=Ng%3D%3D; _l_g_=Ug%3D%3D; sg=%E7%88%B108; _nk_=%5Cu5929%5Cu8DEF%5Cu98CE%5Cu884C%5Cu4E4B%5Cu7231; cookie1=AC%2BTgIP8JLxJ4uTfo978VmFgk3YPLcyUsyWP2tCGjdw%3D; sgcookie=E100sMxSguKLmWFso39q8V%2BSD%2Fuysy1XZehrQGVsDoET0HT5jGGqtgRPWQWdgNRAVtYoMwpSoVBtmUx1T4KQEKgyRlaQC6d4NTX9WXW1XSPHJDQ%3D; uc3=id2=VyUOWs7Troo%3D&nk2=r7kk0YGOXhkbGayK&lg2=UIHiLt3xD8xYTw%3D%3D&vt3=F8dCujXDNt7LKCWHlCA%3D; csg=d68795e8; skt=39c9316b27694ff1; existShop=MTYzNDEyMTMwNQ%3D%3D; uc4=id4=0%40VXJ%2FFKzAmnj3LZx%2BTSd%2BUhze3Q%3D%3D&nk4=0%40rVte3KfQVNOnUZFuVGegHR6PgE%2F%2FS7Q%3D; _cc_=UIHiLt3xSw%3D%3D; mt=ci=74_1; UM_distinctid=17c7938eca2748-0bf35054993f5-b7a1438-1fa400-17c7938eca31207; uc1=cookie21=UIHiLt3xSift4ZS1LW77rg%3D%3D&cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=false&cookie14=Uoe3c93fvk5b8g%3D%3D&cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&pas=0; x5sec=7b22676f7661756374696f6e3b32223a223238353163333532316465333266303336343337313536383232356430646439434b2f786d6f734745502f2b3559664c6d4b334e34674561436a51354d6a67774d4463774f7a4577744b2b727851633d227d; isg=BLm5VGFu_M6_3J5kvKZcIGn_yCWTxq14mbzZgdvuNeBfYtn0Ixa9SCew4G6UQUWw; l=eBIcm9-POhPNFZukBOfanurza77OSIRYYuPzaNbMiOCPOWfB54APW6EyLVY6C3GNh6RpR3z0PcjeBeYBq3xonxv9m8RWcnMmn; tfstk=c_lhBbAX_vyQo7wihBNI52YEoedAw85zmbls_jmrmaKFT6fmEOW41uLgxntFF'
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
