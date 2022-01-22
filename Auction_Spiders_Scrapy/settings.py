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
   'cookie': '_m_h5_tk=7ea1406c52dda6db4c871dccd0c63e26_1642867026779; _m_h5_tk_enc=52bab177677a6016ebf3394ba0e48dd6; cna=kifOF0pLb0ECAXnh9oH0zIwe; cookie2=14e85c60cf76471c85eb48f838f7a168; t=f8eec379672a41df12ada890514930f8; _tb_token_=56959bef60533; _samesite_flag_=true; xlly_s=1; sgcookie=E100CCUE%2F%2Bsr05jWeVDP3gHDnnmpjOsz7%2FvjWon3nz3K12BmFDRUcQirOKeLf9pRRqHwTsjE6bhbyiFp%2F4GCWyIpbSrl1JjlOgbN0qGix2FcWp6i5TjjACPZEEURVUP%2BDOhC; unb=49280070; uc3=lg2=V32FPkk%2Fw0dUvg%3D%3D&nk2=r7kk0YGOXhkbGayK&id2=VyUOWs7Troo%3D&vt3=F8dCvU15WsZwFOvNWKM%3D; csg=8529f9d4; lgc=%5Cu5929%5Cu8DEF%5Cu98CE%5Cu884C%5Cu4E4B%5Cu7231; cancelledSubSites=empty; cookie17=VyUOWs7Troo%3D; dnk=%5Cu5929%5Cu8DEF%5Cu98CE%5Cu884C%5Cu4E4B%5Cu7231; skt=a26238d3eb47a9b6; existShop=MTY0Mjg1NjYwNA%3D%3D; uc4=id4=0%40VXJ%2FFKzAmnj3LZx5qB5S4cshew%3D%3D&nk4=0%40rVte3KfQVNOnUZFuVGegGlIduLs8VPM%3D; publishItemObj=Ng%3D%3D; tracknick=%5Cu5929%5Cu8DEF%5Cu98CE%5Cu884C%5Cu4E4B%5Cu7231; _cc_=Vq8l%2BKCLiw%3D%3D; _l_g_=Ug%3D%3D; sg=%E7%88%B108; _nk_=%5Cu5929%5Cu8DEF%5Cu98CE%5Cu884C%5Cu4E4B%5Cu7231; cookie1=AC%2BTgIP8JLxJ4uTfo978VmFgk3YPLcyUsyWP2tCGjdw%3D; mt=ci=114_1; thw=cn; uc1=cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie15=URm48syIIVrSKA%3D%3D&cookie14=UoewAjYa5oXC1A%3D%3D&cookie21=Vq8l%2BKCLivbdjeuVIQ2NTQ%3D%3D&pas=0&existShop=false; tfstk=c98VB0afgq32DKbsvZ_Zfjipzw7AZYODsz5CmnN4yeeIA6scit2OZt1Aa1NzIif..; l=eBLekutPg7E2CXh9BO5Zourza77tCIRb4sPzaNbMiInca6sc9F_rwNCpvHnwWdtjgtCbeetrkuu1tRLHR3fiO8SsbAqfjCon3xvO.; isg=BNXVB2I8GPjDkTyEx6EFL8VX5NGP0onkHtB7VFd6bMybrvWgHiaAtrwkeLIYrqGc'
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
