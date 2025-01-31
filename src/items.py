# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Article(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()

class Body(scrapy.Item):
    title = scrapy.Field()
    paragraph = scrapy.Field()

class Page(scrapy.Item):
    link = scrapy.Field()
    body = scrapy.Field()

