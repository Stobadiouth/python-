# -*- coding: utf-8 -*-

# Scrapy settings for myspiders project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'myspiders'

SPIDER_MODULES = ['myspiders.spiders']
NEWSPIDER_MODULE = 'myspiders.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'myspiders (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'myspiders.middlewares.MyspidersSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'myspiders.middlewares.MyspidersDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'myspiders.pipelines.MyspidersPipeline': 300,
   # 'myspiders.pipelines.MiPipeline': 300,
   # 'myspiders.imagepipelines.saveImage': 400,
   # 'myspiders.Messagepipelines.MessagePipeline': 400,
   # 'myspiders.Lifepipelines.LifePipeline': 400,
   # 'myspiders.Hobbypipelines.HobbyPipeline': 400,
   # 'myspiders.Mongopipelines.MongoPipeline': 400,
   'myspiders.activepipelines.MiPipeline': 400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

IMAGES_STORE = 'HNimages/full'
# IMAGES_EXPIRES = 30

##过滤图片
# IMAGES_MIN_HEIGHT = 110
# IMAGES_MIN_WIDTH = 110

# IMAGES_THUMBS = {
#     'big': (270, 270),
#     'small': (80, 80)
# }
COOKIE={'CwCzwf_sex_ta': '2', 'CwCzwf_userid': '11004091', '11004255': '11004255', 'CwCzwf_dialog_greet_index': '1', '10917494': '10917494', '10637213': '10637213', '10842417': '10842417', '10820078': '10820078', '10443693': '10443693', '10997501': '10997501', '10583600': '10583600', '10729173': '10729173', '10961561': '10961561', '10666092': '10666092', '10673026': '10673026', '10554236': '10554236', '10970329': '10970329', '10433893': '10433893', '10591754': '10591754', '10587353': '10587353', '10710495': '10710495', '10598658': '10598658', '10838862': '10838862', '10963975': '10963975', '10430633': '10430633', '10981739': '10981739', '10581579': '10581579', '10786990': '10786990', '10901490': '10901490', '10763821': '10763821', '329432': '329432', '10500023': '10500023', '10976045': '10976045', '10427311': '10427311', '10969246': '10969246', '10713231': '10713231', '10764176': '10764176', '10825465': '10825465', '10590704': '10590704', 'Hm_lvt_13345a0835e13dfae20053e4d44560b9': '1539570372,1539671853,1539764087,1539909782', 'PHPSESSID': 'cb7cd565fkgsgnq55l6e046fi2', 'CwCzwf_prompt_tomorry': '1', '10981110': '10981110', 'Hm_lpvt_13345a0835e13dfae20053e4d44560b9': '1539910587'}
