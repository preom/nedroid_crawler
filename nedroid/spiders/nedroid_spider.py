from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from nedroid.items import NedroidItem

class NedroidSpider(CrawlSpider):
    name = 'nedroid'
    start_urls = ['http://www.nedroid.com']

    rules = [
        Rule(SgmlLinkExtractor(restrict_xpaths="//div[@class='nav-previous']"), follow=True, callback='parse_item')
    ]

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        image_link = hxs.select("//div[@id='comic']/img")
        item = NedroidItem()
        item['image_urls'] = image_link.select("@src").extract()
        item['description'] = image_link.select("@title").extract()
        item['title'] = image_link.select("@alt").extract()
        item['date'] = hxs.select("//div[@class='comicdate']/text()").re(r'([\w, ]+)')
        return item

    parse_start_url = parse_item
