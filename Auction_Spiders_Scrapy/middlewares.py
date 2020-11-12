# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from pip._vendor import requests
from scrapy import signals
import random

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class AliAuctionSpiderScrapySpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class AliAuctionSpiderScrapyDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ProxyMiddleware:
    def process_request(self, request, spider):
        try:
            request.meta['proxy'] = 'https://' + proxies[random.randint(0, 999)]
        except requests.exceptions.RequestException:
            print('获取讯代理ip失败！')
            spider.logger.error('获取讯代理ip失败！')


proxies = ["115.46.117.189:8123", "61.135.217.7:80", "118.114.77.47:8080", "114.67.149.209:808",
           "171.37.171.111:8123",
           "110.73.1.24:8123", "60.169.78.218:808", "110.73.41.201:8123", "119.62.105.44:8118",
           "125.37.107.23:8118",
           "222.141.15.122:8118", "27.159.124.78:8118", "175.31.188.253:8118", "220.166.243.12:8118",
           "171.39.42.137:8123", "111.155.116.219:8123", "121.31.103.169:8123", "110.73.9.147:8123",
           "114.230.99.36:46773", "115.219.130.196:80", "183.189.213.50:80", "110.73.5.63:8123",
           "117.78.37.198:8000",
           "182.88.14.59:8123", "180.167.46.22:53281", "59.41.202.239:53281", "124.72.216.83:808",
           "153.34.199.194:80",
           "27.40.139.239:61234", "171.39.42.206:8123", "221.10.159.234:1337", "110.172.220.194:8080",
           "121.12.42.223:61234", "183.133.50.38:80", "42.243.138.84:4336", "39.81.158.112:8118",
           "171.212.140.219:8118", "14.111.8.46:8118", "180.126.168.43:8118", "42.55.170.182:80",
           "60.24.165.120:8118",
           "111.155.116.195:8123", "123.185.129.186:8080", "110.73.1.9:8123", "110.216.60.162:80",
           "59.40.69.108:8010",
           "110.73.31.1:8123", "113.195.163.212:48888", "110.73.1.102:8123", "101.22.113.198:8118",
           "114.101.208.180:4326", "171.39.42.227:8123", "121.31.84.162:8123", "110.73.41.188:8123",
           "123.169.34.240:4366", "114.234.162.180:4364", "115.200.70.75:80", "115.203.199.106:28897",
           "116.52.196.69:8118", "114.98.8.113:4326", "58.243.204.50:4358", "120.27.131.204:3128",
           "110.73.5.196:8123",
           "110.73.4.254:8123", "171.83.227.239:808", "110.72.44.198:8123", "115.46.70.143:8123",
           "115.46.71.57:8123",
           "115.210.176.74:47849", "60.187.241.79:808", "115.46.85.200:8123", "121.31.192.120:8123",
           "182.90.105.26:8123", "171.39.31.93:8123", "182.90.51.202:8123", "115.46.85.142:8123",
           "222.185.53.190:8118",
           "115.221.127.117:33280", "27.37.177.44:9999", "119.5.107.213:9999", "114.216.219.114:8118",
           "113.128.28.242:45438", "110.73.32.169:8123", "110.73.15.21:8123", "117.93.23.208:8118",
           "110.73.43.70:8123",
           "118.254.149.61:3128", "180.110.151.31:8118", "218.6.160.93:63000", "59.40.50.10:8010",
           "39.71.148.34:8118",
           "110.73.3.129:8123", "110.73.14.114:8123", "106.58.123.43:80", "121.31.174.175:8123",
           "220.161.39.43:8118",
           "218.108.215.162:80", "59.40.68.111:8010", "42.59.216.137:80", "171.122.217.159:9999",
           "110.73.15.167:8123",
           "110.73.0.116:8123", "121.12.42.207:61234", "119.144.124.108:8118", "110.73.2.5:8123", "106.58.152.8:80",
           "180.118.242.92:808", "114.232.93.137:25963", "59.63.178.203:53281", "113.195.163.231:48888",
           "121.31.102.192:8123", "59.40.51.73:8010", "27.8.158.12:808", "124.72.216.78:808", "121.31.103.101:8123",
           "121.31.138.228:8123", "110.73.49.52:8123", "139.210.49.68:8118", "183.151.43.145:3128",
           "60.168.80.135:808",
           "59.32.37.32:3128", "114.226.38.171:808", "121.12.42.142:61234", "121.31.143.171:8123",
           "110.73.33.48:9999",
           "171.38.26.16:8123", "61.178.238.122:63000", "175.154.131.8:9999", "121.31.100.219:8123",
           "117.92.153.213:21896", "223.241.78.40:8010", "112.233.59.149:9999", "112.233.14.244:9999",
           "123.8.228.186:9999", "120.82.239.228:9999", "27.209.248.155:9999", "221.215.68.216:9999",
           "180.121.133.41:8118", "183.184.144.157:80", "110.73.35.59:8123", "111.155.116.215:8123",
           "115.200.28.220:80", "180.122.147.17:48557", "182.88.129.40:8123", "180.122.150.164:39472",
           "115.203.194.185:43444", "125.47.150.220:9999", "113.123.50.79:808", "115.61.77.120:9999",
           "110.73.40.204:8123", "111.155.116.217:8123", "110.73.7.178:8123", "122.245.156.212:808",
           "110.73.52.67:8123", "115.46.86.251:8123", "123.145.128.139:8118", "111.155.116.211:8123",
           "59.40.51.190:8010", "123.169.4.84:36711", "182.90.83.85:8123", "60.218.153.177:80",
           "27.159.126.93:8118",
           "110.73.51.92:8123", "111.155.116.220:8123", "122.4.28.117:40684", "101.26.122.114:8118",
           "111.155.116.196:8123", "110.72.35.18:8123", "118.187.58.34:53281", "117.65.38.28:52335",
           "114.216.93.175:8118", "101.224.70.98:30149", "115.203.210.129:43513", "59.40.51.228:8010",
           "171.38.26.83:8123", "110.73.40.224:8123", "218.81.232.107:31480", "115.213.244.163:27141",
           "112.94.190.231:9999", "171.38.85.216:8123", "183.186.23.128:9999", "110.72.31.80:8123",
           "175.163.66.22:80",
           "125.45.131.40:8118", "218.73.140.236:48603", "222.210.170.55:8118", "180.122.147.185:21642",
           "59.40.51.85:8010", "119.5.107.218:9999", "113.85.170.0:9999", "175.11.214.111:808",
           "110.73.55.231:8123",
           "124.161.146.142:9999", "180.121.160.85:27913", "59.40.68.210:8010", "60.221.48.47:80",
           "111.155.116.232:8123", "112.114.86.164:9999", "59.40.51.52:8010", "27.11.241.78:8118",
           "125.112.207.153:29459", "49.76.10.215:808", "59.40.68.97:8010", "140.250.123.1:808",
           "121.31.103.230:8123",
           "123.185.128.210:8080", "27.197.117.229:808", "112.81.143.245:8118", "222.141.10.176:8118",
           "110.73.55.14:8123", "120.39.117.253:34587", "183.128.66.107:45438", "110.73.53.139:8123",
           "110.73.51.124:8123", "171.39.0.149:8123", "110.73.12.133:8123", "110.73.35.25:8123",
           "119.109.101.120:80",
           "110.73.9.169:8123", "182.90.21.137:8118", "110.73.32.116:8123", "175.165.51.145:9999",
           "27.184.125.229:8118", "110.73.5.170:8123", "113.242.144.171:808", "60.184.201.171:44849",
           "115.46.69.146:8123", "115.46.88.164:8123", "110.72.16.194:8123", "58.23.207.155:9999",
           "222.242.171.5:63000", "116.19.97.102:8118", "59.40.51.37:8010", "110.73.43.110:8123",
           "182.90.71.45:8123",
           "1.26.50.103:9999", "115.203.199.121:32164", "113.121.240.48:808", "110.73.12.21:8123",
           "171.124.56.253:9999", "60.168.2.182:8118", "27.154.181.26:47936", "114.232.171.150:31278",
           "110.73.28.39:8123", "110.73.48.184:8123", "222.54.76.235:80", "119.5.0.23:808", "171.36.154.21:8123",
           "125.126.165.130:40933", "110.73.6.149:8123", "119.176.86.214:9999", "171.121.25.99:9999",
           "182.43.231.27:9999", "182.245.93.94:8118", "121.31.100.120:8123", "58.209.47.32:42557",
           "60.175.213.40:44435", "117.69.99.116:37377", "110.73.34.143:8123", "115.46.71.206:8123",
           "182.90.100.145:8123", "115.46.96.48:8123", "113.64.92.22:8080", "183.184.148.221:80",
           "223.241.117.86:8010",
           "115.46.221.184:8123", "110.73.35.233:8123", "106.9.168.45:808", "110.73.42.127:8123",
           "110.73.9.109:8123",
           "110.73.42.110:8123", "121.31.101.159:8123", "60.167.22.156:20548", "121.31.100.38:8123",
           "27.159.127.3:8118", "121.31.101.212:8123", "115.215.48.240:45933", "123.163.19.30:30702",
           "140.224.76.139:808", "110.73.11.100:8123", "110.73.3.246:8123", "222.134.168.60:808",
           "61.135.155.82:443",
           "123.146.100.158:53005", "223.241.116.214:8010", "223.241.79.171:8010", "182.90.123.89:8123",
           "110.73.5.19:8123", "110.87.0.247:25847", "60.22.179.8:80", "42.84.244.71:80", "42.57.107.211:80",
           "182.127.206.141:9999", "120.39.118.130:31783", "42.49.119.146:8118", "222.221.161.161:9999",
           "110.73.42.98:8123", "59.40.50.184:8010", "110.73.41.175:8123", "111.137.6.95:80", "110.73.8.233:8123",
           "110.73.1.156:8123", "110.73.40.2:8123", "106.46.200.177:49962", "171.39.40.121:8123",
           "121.232.16.232:8118",
           "110.73.14.39:8123", "27.42.157.223:8080", "121.205.254.134:47254", "180.120.214.181:8888",
           "49.87.180.155:40807", "221.206.251.143:9999", "110.73.1.245:8123", "171.39.40.176:8123",
           "182.90.56.98:80",
           "59.40.51.225:8010", "121.31.100.110:8123", "180.120.208.104:8888", "27.159.126.33:8118",
           "110.73.48.152:8123", "110.73.53.188:8123", "110.73.10.241:8123", "171.38.37.174:8123",
           "115.221.120.38:808",
           "27.206.232.130:8118", "123.163.19.181:39967", "171.39.40.112:8123", "218.15.25.153:808",
           "111.155.116.207:8123", "101.65.205.40:808", "125.122.142.242:80", "110.73.51.39:8123",
           "112.117.73.81:9999",
           "223.241.119.131:8010", "113.110.102.46:9999", "114.217.117.96:23675", "60.208.44.228:80",
           "111.155.116.210:8123", "171.39.28.205:8123", "121.31.197.201:8123", "112.95.27.62:9999",
           "59.40.50.97:8010",
           "59.40.68.160:8010", "171.38.26.25:8123", "115.61.109.221:8118", "171.37.16.46:8123", "110.73.8.58:8123",
           "110.73.7.71:8123", "123.185.131.48:8080", "123.155.21.12:80", "110.73.0.11:8123", "59.40.69.187:8010",
           "113.116.235.48:8118", "49.66.201.177:8118", "59.40.50.255:8010", "112.252.255.86:8118",
           "121.31.103.124:8123", "120.40.135.252:27709", "223.241.79.7:8010", "121.12.42.233:61234",
           "36.26.113.2:8118", "222.76.147.29:29668", "59.32.37.170:808", "110.73.35.77:8123",
           "182.88.123.254:8118",
           "59.40.51.8:8010", "110.73.54.112:8123", "111.155.116.236:8123", "111.155.116.205:8123",
           "121.31.177.211:8123", "110.73.4.217:8123", "123.161.152.196:43293", "120.39.119.112:23521",
           "115.217.254.49:36480", "171.38.90.53:8123", "115.46.250.0:8123", "110.73.29.24:8123",
           "121.12.42.234:61234",
           "110.73.206.237:8123", "110.73.7.21:8123", "111.155.120.226:8123", "111.155.116.225:8123",
           "110.73.35.64:8123", "125.126.172.91:22388", "223.241.117.173:8010", "111.155.116.239:8123",
           "110.185.42.43:8118", "180.111.9.1:8118", "113.123.3.19:808", "221.4.133.67:53281", "171.37.86.228:8123",
           "111.155.120.229:8123", "180.125.20.131:808", "114.239.249.244:808", "111.155.120.141:8123",
           "171.108.205.85:53281", "111.155.120.202:8123", "111.155.120.173:8123", "110.72.26.172:8123",
           "121.30.57.244:80", "121.30.57.244:80", "110.73.3.198:8123", "111.155.116.206:8123", "113.232.2.252:80",
           "110.73.11.39:8123", "180.111.5.192:808", "119.5.0.37:808", "117.24.21.7:46115", "183.184.145.173:80",
           "218.81.71.3:37314", "110.73.172.158:8123", "183.130.63.251:80", "114.231.29.29:41269",
           "183.133.50.17:80",
           "111.155.120.220:8123", "123.163.21.70:42393", "111.155.120.223:8123", "121.31.193.230:8123",
           "59.40.51.46:8010", "110.73.34.181:8123", "112.229.100.1:8118", "182.90.71.215:8123",
           "119.109.101.108:8118",
           "183.189.164.200:80", "115.46.87.39:8123", "27.22.61.26:3128", "59.40.51.193:8010", "110.73.49.176:8123",
           "171.38.39.169:8123", "59.40.69.81:8010", "183.185.150.113:80", "182.88.90.64:8123", "110.73.10.48:8123",
           "59.40.51.4:8010", "110.73.54.120:8123", "112.113.209.182:4336", "110.73.6.193:8123",
           "110.73.9.146:8123",
           "121.31.176.10:8123", "121.31.192.196:8123", "110.72.21.188:8123", "110.200.241.253:80",
           "111.155.120.170:8123", "113.121.227.71:808", "182.90.6.94:8118", "110.73.3.53:8123",
           "121.31.103.227:8123",
           "116.208.13.253:3128", "60.172.118.105:8888", "123.161.238.241:49260", "110.73.11.249:8123",
           "121.31.172.123:8123", "110.87.248.101:808", "123.55.147.239:808", "110.73.53.29:8123",
           "125.122.117.155:808", "110.73.10.251:8123", "113.122.51.179:808", "123.55.189.161:808",
           "183.128.66.125:35826", "121.12.42.250:61234", "115.239.42.3:8118", "110.72.16.64:8123",
           "110.73.1.19:8123",
           "119.167.51.101:8118", "114.230.217.251:808", "110.73.41.100:8123", "110.73.2.187:8123",
           "110.73.40.24:8123",
           "182.90.101.77:8123", "110.73.52.155:8123", "110.73.41.21:8123", "119.55.120.145:9999",
           "180.173.82.97:8118",
           "110.73.43.71:8123", "171.127.174.82:9999", "171.37.193.84:8123", "110.73.12.179:8123",
           "110.73.50.84:8123",
           "171.38.37.226:8123", "171.38.84.177:8123", "121.31.198.135:8123", "110.73.8.32:8123",
           "171.37.171.145:8123",
           "110.73.50.128:8123", "121.31.103.95:8123", "121.31.141.112:8123", "121.31.71.36:8123",
           "171.37.160.185:8123", "115.46.78.25:8123", "121.31.87.246:8123", "121.31.177.106:8123",
           "110.73.2.83:8123",
           "171.38.42.20:8123", "171.38.34.211:8123", "110.73.29.180:8123", "121.31.100.53:8123",
           "110.73.41.76:8123",
           "110.165.59.189:808", "117.68.167.215:8118", "110.73.8.108:8123", "110.73.55.189:8123",
           "27.19.78.70:808",
           "119.108.156.5:8080", "27.22.7.222:3128", "121.12.42.7:61234", "121.207.33.164:808",
           "123.162.197.189:37802",
           "110.73.54.122:8123", "180.124.5.56:808", "222.85.5.244:808", "121.31.101.118:8123", "27.40.140.174:808",
           "49.85.6.67:20675", "110.73.42.68:8123", "171.39.238.198:8123", "113.121.245.46:48475",
           "60.167.135.145:40986", "117.63.27.208:808", "110.73.11.54:8123", "115.200.21.206:80",
           "49.85.4.65:48748",
           "59.40.69.158:8010", "112.86.197.163:808", "183.166.197.61:808", "59.40.68.142:8010",
           "218.18.232.29:8080",
           "106.46.95.132:47615", "121.31.102.141:8123", "115.200.2.20:80", "110.72.45.8:8123", "171.39.31.36:8123",
           "121.31.147.33:8123", "180.122.151.143:48803", "113.87.89.129:53281", "112.229.239.77:8118",
           "171.39.236.84:8123", "180.118.243.181:61234", "101.27.189.92:8118", "113.234.169.19:8118",
           "115.46.68.36:8123", "180.118.243.229:61234", "121.31.100.148:8123", "121.31.198.242:8123",
           "117.60.208.12:38258", "171.38.74.212:8123", "182.88.253.149:8123", "180.118.241.249:808",
           "110.72.21.74:8123", "117.25.189.125:43944", "180.118.243.228:808", "121.31.86.20:80",
           "180.113.81.132:43756", "117.71.156.96:28333", "218.5.161.211:42859", "223.215.142.118:4326",
           "222.240.233.154:80", "1.197.153.133:25831", "183.133.51.165:80", "218.5.161.211:42859",
           "183.19.250.220:808", "110.73.42.24:8123", "59.40.69.58:8010", "110.73.43.201:8123", "171.39.42.62:8123",
           "27.159.124.191:8118", "110.87.5.148:25882", "60.179.42.212:20688", "180.172.221.37:29242",
           "122.4.29.132:30900", "110.73.15.115:8123", "171.36.225.236:80", "123.55.177.140:48523",
           "59.58.240.95:31576", "117.64.225.194:808", "123.169.37.189:44644", "110.73.2.143:8123",
           "59.40.50.213:8010",
           "60.187.15.232:80", "110.73.41.219:8123", "140.250.169.240:29557", "113.93.103.92:42580",
           "110.87.5.27:23015", "110.72.29.50:8123", "115.58.84.48:4331", "116.28.171.38:808", "122.4.40.56:31558",
           "113.121.173.185:43527", "220.162.165.164:45145", "110.73.10.225:8123", "111.155.116.208:8123",
           "110.72.45.148:8123", "115.203.192.233:41908", "115.203.194.20:28560", "180.155.142.38:42732",
           "122.4.28.209:45192", "114.230.121.171:39767", "183.128.71.112:44827", "220.178.197.101:41595",
           "121.12.42.71:61234", "121.12.42.89:61234", "171.38.65.173:8123", "222.85.5.126:49080",
           "115.203.194.58:34527", "115.203.213.21:808", "115.203.193.151:29074", "121.12.13.83:61234",
           "115.222.1.168:80", "110.73.52.71:8123", "110.73.33.235:8123", "114.99.85.78:45808",
           "125.112.173.244:26370",
           "110.72.254.183:8123", "180.121.133.239:8888", "110.73.11.111:8123", "110.73.6.48:8123",
           "180.122.148.103:20551", "121.205.254.129:28588", "114.226.164.89:29077", "125.126.173.120:41580",
           "171.38.98.161:8123", "110.73.15.172:8123", "106.58.120.137:80", "180.106.34.147:8118",
           "110.73.5.120:8123",
           "115.217.252.201:48863", "125.112.207.164:38380", "110.73.30.135:8123", "221.205.207.242:80",
           "60.186.155.61:46267", "115.215.51.29:30987", "180.115.3.151:41838", "49.83.118.88:8118",
           "121.31.103.41:8123", "111.155.116.224:8123", "183.15.34.24:8010", "121.228.10.96:25306",
           "180.122.146.217:48336", "210.26.59.192:8080", "118.254.153.227:3128", "121.31.101.241:8123",
           "117.69.98.36:49884", "183.150.239.18:3128", "110.73.43.205:8123", "58.244.196.29:808",
           "110.73.28.140:8123",
           "123.163.20.109:39493", "42.235.254.13:8118", "110.73.11.248:8123", "110.73.48.106:8123",
           "115.200.8.96:80",
           "110.73.8.120:8123", "113.226.207.134:80", "59.62.233.230:8118", "110.73.9.235:8123", "59.40.50.2:8010",
           "182.246.214.29:9999", "121.31.143.184:8123", "182.246.206.245:9999", "121.31.101.0:8123",
           "111.155.116.249:8123", "115.200.35.2:80", "110.73.12.206:8123", "183.151.145.69:8118",
           "111.155.116.229:8123", "101.81.218.33:53281", "223.241.78.213:8010", "175.155.232.111:9999",
           "110.73.8.142:8123", "171.38.41.45:8123", "110.72.39.251:8123", "59.40.68.215:8010",
           "121.31.87.238:8123",
           "121.31.102.118:8123", "121.12.42.219:61234", "59.40.50.57:8010", "27.46.30.61:9999", "59.40.50.43:8010",
           "110.73.28.27:8123", "183.163.46.145:52335", "110.73.28.216:8123", "110.73.7.146:8123",
           "110.216.64.135:80",
           "59.40.51.242:8010", "182.90.80.49:8123", "59.40.50.160:8010", "139.196.168.172:8888",
           "111.155.116.240:8123", "182.88.134.101:8123", "125.41.109.177:8118", "111.155.120.186:8123",
           "106.43.52.239:9999", "59.40.51.218:8010", "171.38.26.87:8123", "59.40.68.222:8010",
           "111.155.120.188:8123",
           "59.40.51.212:8010", "116.196.90.236:808", "118.122.110.62:8118", "115.200.1.75:80", "114.235.83.2:8118",
           "115.200.170.183:80", "115.239.53.206:8118", "114.99.7.122:808", "110.73.48.55:8123",
           "121.31.100.152:8123",
           "110.73.6.95:8123", "110.73.14.93:8123", "14.118.84.107:9999", "121.31.86.143:8123", "59.40.50.115:8010",
           "183.151.40.252:3128", "59.40.51.18:8010", "171.39.0.191:8123", "110.73.7.213:8123", "110.73.30.15:8123",
           "121.12.42.49:61234", "121.31.156.92:8123", "110.73.2.197:8123", "123.56.137.89:808",
           "112.255.225.238:8118",
           "110.73.13.70:8123", "121.31.173.246:8123", "121.31.73.238:8123", "111.155.116.201:8123",
           "110.73.53.11:8123", "110.73.4.53:8123", "110.73.49.57:8123", "111.155.116.228:8123",
           "111.155.120.208:8123",
           "110.73.15.228:8123", "110.73.33.103:8123", "111.222.0.221:80", "110.73.48.168:8123",
           "110.73.14.118:8123",
           "182.90.109.27:8123", "112.114.118.115:9999", "110.73.8.162:8123", "182.88.179.42:8123",
           "180.124.6.74:808",
           "59.40.69.5:8010", "112.193.131.24:8118", "121.31.145.213:8123", "110.73.15.158:8123",
           "110.72.45.137:8123",
           "115.220.229.65:8118", "180.173.141.242:52335", "59.40.50.21:8010", "110.73.43.188:8123",
           "171.37.193.48:8123", "110.73.9.28:8123", "110.73.32.239:8123", "180.175.120.249:62225",
           "110.72.32.31:8123",
           "114.95.186.244:62225", "118.77.242.30:9999", "110.73.34.248:8123", "110.73.51.176:8123",
           "110.73.9.34:8123",
           "124.89.33.59:53281", "121.31.102.51:8123", "182.90.79.181:8123", "110.72.16.2:8123",
           "121.31.71.133:8123",
           "60.189.123.156:8118", "110.73.3.195:8123", "110.73.42.125:8123", "123.52.84.161:8118",
           "110.73.55.145:8123",
           "121.31.168.150:8123", "182.90.101.177:8123", "112.114.113.101:9999", "110.73.12.146:8123",
           "120.27.101.68:808", "27.40.146.17:61234", "183.63.101.62:53281", "183.133.73.105:8118",
           "180.121.129.70:8118", "110.73.11.122:8123", "121.31.169.129:8123", "27.159.126.178:8118",
           "110.73.3.95:8123", "144.0.81.120:808", "139.210.49.229:8118", "101.68.73.54:53281",
           "183.144.197.195:808",
           "27.19.87.134:808", "42.58.221.23:9999", "119.41.202.158:53281", "110.73.41.199:8123",
           "49.64.222.236:8118",
           "59.40.50.90:8010", "114.115.216.99:80", "121.31.103.192:8123", "113.121.244.64:808",
           "171.39.39.197:8123",
           "42.49.119.145:8118", "110.73.43.238:8123", "110.73.5.97:8123", "122.237.106.16:80", "115.200.6.82:80",
           "115.200.11.6:80", "59.40.51.253:8010", "110.73.11.8:8123", "110.72.22.38:8123", "220.163.241.148:8118",
           "110.73.15.93:8123", "59.40.50.94:8010", "121.31.101.18:8123", "110.73.7.200:8123",
           "223.241.116.251:8010",
           "182.112.132.128:8118", "113.250.61.163:9999", "121.12.42.91:61234", "110.73.31.155:8123",
           "113.242.141.27:808", "121.31.101.99:8123", "27.197.85.218:9999", "121.31.101.134:8123",
           "49.83.63.18:8118",
           "117.64.225.229:808", "115.148.169.191:9999", "223.241.79.6:8010", "59.40.69.64:8010",
           "113.138.189.134:9999", "110.73.11.224:8123", "27.188.147.202:8118", "59.40.51.130:8010",
           "110.73.35.30:8123", "121.12.42.60:61234", "123.128.121.6:8118", "110.73.9.112:8123",
           "110.73.30.33:8123",
           "180.118.240.141:61234", "110.73.49.234:8123", "117.13.199.113:8118", "110.73.11.239:8123",
           "182.88.89.81:8123", "175.166.174.133:80", "113.69.149.109:808", "113.67.164.59:8118",
           "171.124.219.7:9999",
           "116.249.222.237:8118", "121.31.193.99:8123", "60.24.168.182:8118", "110.73.54.210:8123",
           "222.93.255.235:8118", "110.73.30.204:8123", "115.46.97.81:8123", "114.230.30.195:808",
           "180.118.243.23:61234", "115.200.46.74:80", "59.40.51.156:8010", "110.73.50.72:8123",
           "59.40.50.253:8010",
           "113.123.44.98:808", "114.226.166.217:35656", "171.37.161.138:8123", "27.219.24.71:9999",
           "171.37.160.63:8123", "180.122.149.21:48447", "60.184.185.179:23521", "113.237.48.172:9999",
           "182.107.98.194:8118", "221.205.180.178:80", "116.115.169.160:9999", "110.85.89.138:48140",
           "180.155.138.16:35808", "113.128.30.186:23318", "222.76.147.202:32057", "114.230.233.127:22424",
           "121.12.42.32:61234", "115.63.110.113:9999", "115.202.161.57:808", "111.155.120.137:8123",
           "59.40.68.175:8010", "111.183.80.179:8118", "110.73.41.254:8123", "182.88.187.44:8123",
           "112.81.71.205:8118",
           "114.230.41.206:808", "115.200.25.38:80", "124.161.116.66:9999", "1.59.17.213:9999",
           "222.163.155.175:9999",
           "111.155.120.217:8123", "110.73.48.194:8123", "182.32.169.11:32886", "121.31.103.110:8123",
           "121.205.72.159:49591", "106.46.88.41:36223", "121.12.42.247:61234", "49.76.234.225:8118",
           "139.226.109.150:8118", "119.119.27.5:8080", "39.64.0.88:8118", "180.118.121.58:41885",
           "113.121.240.40:40179", "59.40.50.63:8010", "125.109.197.230:24405", "125.78.104.116:20470",
           "121.207.76.211:25913", "125.122.137.164:80", "110.73.4.112:8123", "110.73.1.212:8123",
           "115.203.221.152:34601", "218.14.141.53:26007", "171.36.62.40:8123", "111.155.120.147:8123",
           "59.40.68.170:8010", "140.250.120.46:9999", "27.40.132.250:808", "110.73.7.224:8123",
           "117.69.97.214:43783",
           "122.242.94.9:48770", "59.58.243.34:40297", "222.89.86.175:24657", "27.159.125.193:8118",
           "49.88.158.218:22680", "49.88.158.218:22680", "125.126.171.111:44507", "110.73.11.45:8123",
           "112.229.239.211:8118", "110.73.11.208:8123", "171.39.45.216:8123", "115.217.252.6:24061",
           "110.73.14.159:8123", "1.199.193.36:37156", "124.165.175.161:9999", "182.34.19.214:44452",
           "171.39.28.104:8123", "171.38.41.247:8123", "110.73.1.73:8123", "171.38.25.26:8123",
           "180.118.241.54:61234",
           "222.81.137.35:9999", "110.73.40.16:8123", "60.162.19.188:20612", "115.203.198.35:23371",
           "119.183.154.208:8118", "182.88.167.131:8123", "171.36.60.69:8123", "182.246.2.214:9999",
           "180.118.241.240:808", "49.85.0.40:30239", "180.118.243.49:808", "110.72.39.151:8123",
           "27.11.241.247:8118",
           "113.4.216.109:8118", "101.64.140.53:8118", "180.155.143.114:45806", "115.203.207.124:32449",
           "111.155.120.165:8123", "110.85.132.65:8118", "222.141.12.188:8118", "113.91.65.133:8118",
           "163.125.73.235:9999", "1.197.59.154:43024", "120.32.139.174:45687", "49.87.147.176:38281",
           "60.175.198.155:22274", "122.241.30.205:34841", "180.122.149.1:42863", "119.178.141.248:8118",
           "123.163.131.84:20806", "114.238.216.134:45348", "60.214.190.248:9999", "110.73.53.77:8123",
           "115.203.193.71:26273", "123.163.21.183:48300", "222.191.169.159:25509", "117.93.8.129:20830",
           "180.122.145.93:37091", "118.254.142.42:53281", "114.232.116.190:8888", "180.212.72.95:8118",
           "180.115.14.140:22315", "60.209.179.212:8118", "115.203.210.69:42982", "125.126.172.237:37102",
           "115.203.200.122:40878", "115.203.200.139:33015", "110.72.23.123:8123", "115.203.209.91:23214",
           "222.161.123.3:9999", "222.71.90.95:26265", "49.77.185.97:44494", "121.226.186.243:27468",
           "120.42.120.230:48507", "110.73.29.253:8123", "59.40.68.201:8010", "223.241.119.85:8010",
           "111.155.120.139:8123", "111.155.116.212:8123", "114.225.251.174:8118", "27.197.83.210:9999",
           "110.73.15.69:8123", "110.73.33.115:8123", "110.73.0.78:8123", "110.73.9.58:8123"]