# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/']

    def parse(self, response):
        pass
