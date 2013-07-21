# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class NedroidItem(Item):
    date = Field()
    title = Field()
    description = Field()
    image_urls = Field()
    images = Field()
