# -*- coding: utf-8 -*-
import scrapy


class TodayseriesSpider(scrapy.Spider):
    name = 'todayseries'
    allowed_domains = ['todaytvseries2.com']

    def start_requests(self):
        yield scrapy.Request('http://todaytvseries2.com/tv-series', callback=self.parse)

    def parse(self, response):
        series_name = []
        series_href = []
        for title in response.css('h1.uk-article-title1 > a::attr(title)').extract():
            series_name.append(title)
        for href in response.css('h1.uk-article-title1 > a::attr(href)').extract():
            series_href.append(href)

        info = dict(zip(series_name, series_href))

        return info

