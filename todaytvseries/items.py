# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TodaytvseriesItem(scrapy.Item):
    series_info = scrapy.Field()


class SeriesEpisodeLinksItem(scrapy.Item):
    no_of_season = scrapy.Field()
    episode_per_season = scrapy.Field()
    episode_url =scrapy.Field()