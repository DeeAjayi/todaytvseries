# -*- coding: utf-8 -*-
import scrapy
from todaytvseries.items import TodaytvseriesItem

class TodayseriesSpider(scrapy.Spider):
    name = 'todayseries'
    allowed_domains = ['todaytvseries2.com']

    def start_requests(self):
        yield scrapy.Request('http://todaytvseries2.com/tv-series', callback=self.parse)

    def parse(self, response):
        series_info = TodaytvseriesItem()
        series_name = []
        series_href = []
        for title in response.css('h1.uk-article-title1 > a::attr(title)').extract():
            series_name.append(title)
        for href in response.css('h1.uk-article-title1 > a::attr(href)').extract():
            url = response.urljoin(href)
            series_href.append(url)

        series_info['series_info'] = dict(zip(series_name, series_href))

        return series_info



