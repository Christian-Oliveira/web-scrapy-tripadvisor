# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TripadvisorItem(scrapy.Item):
    # define the fields for your item here like:
    author = scrapy.Field()
    address = scrapy.Field()
    title = scrapy.Field()
    comment = scrapy.Field()
    date_published = scrapy.Field()
