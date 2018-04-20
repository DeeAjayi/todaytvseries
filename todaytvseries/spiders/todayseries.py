# -*- coding: utf-8 -*-
import scrapy
from todaytvseries.items import TodaytvseriesItem
from scrapy.linkextractors import LinkExtractor

class TodayseriesSpider(scrapy.Spider):
    name = 'todayseries'
    allowed_domains = ['todaytvseries2.com']

    def start_requests(self):
        yield scrapy.Request('http://todaytvseries2.com/tv-series', callback=self.parse)

    def parse(self, response):
        latest_series_info = TodaytvseriesItem()
        latest_series_info['series_info'] = {}

        for series in response.css('h1.uk-article-title1'):
            latest_series_info['series_info'][series.css('a::text').extract_first()] = series.css('a::attr(href)').extract_first()

        return latest_series_info





