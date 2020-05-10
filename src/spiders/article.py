# -*- coding: utf-8 -*-
import scrapy
from src.items import Article, Body, Page

class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Featured_articles']

    custom_settings = {
        'FEED_FORMAT' : 'json',
        'FEED_URI' : 'data/featured_article-%(time)s.json'
    }

    def parse(self, response):
        host = self.allowed_domains[0]

        # yield Page(
        #     url = response.url,
        #     title = response.css('firstHeading'),
        #     paragraph = response.css('.bodyContent > p:first-child')
        # )

        for link in response.css(".featured_article_metadata > a"):
            page = Page(
                link = f"https://{host}{link.attrib.get('href')}/"
            )
            yield response.follow(link.attrib.get('href'), callback=self.parse_body, meta={'page': page})


    def parse_body(self, response):
        page = response.meta['page']

        body = Body(
            title = response.css('.firstHeading::text').get(),
            paragraph = ''.join(response.css('#bodyContent table.infobox + p:not(.mw-empty-elt)::text').extract())
        )

        page['body'] = body
        
        return page