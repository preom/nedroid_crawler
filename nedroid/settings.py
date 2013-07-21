# Scrapy settings for nedroid project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'nedroid'

SPIDER_MODULES = ['nedroid.spiders']
NEWSPIDER_MODULE = 'nedroid.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'nedroid (+http://www.yourdomain.com)'

ITEM_PIPELINES = ['scrapy.contrib.pipeline.images.ImagesPipeline']
IMAGES_STORE = '/home/preom/Workarea/python/scrapy/nedroid/nedroid/img/'

DOWNLOAD_DELAY = 0.250

