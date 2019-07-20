# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BingwallpaperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_url_relatively = scrapy.Field()
    image_url = scrapy.Field()
    image_startDate = scrapy.Field()
    image_name = scrapy.Field()
    images = scrapy.Field()
    image_path = scrapy.Field()
