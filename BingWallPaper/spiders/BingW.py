# -*- coding: utf-8 -*-
import scrapy
import json
from BingWallPaper.items import BingwallpaperItem


class BingwSpider(scrapy.Spider):
    name = 'BingW'
    allowed_domains = ['cn.bing.com']

    custom_settings = {
        'ITEM_PIPELINES': {'BingWallPaper.pipelines.BingwallpaperPipeline': 1, },
        'IMAGES_STORE': '/home/lumia/BingImages',
        'ROBOTSTXT_OBEY': False,
        'DOWNLOAD_DELAY': 3,
        # 'HTTPCACHE_ENABLED': False
    }

    def start_requests(self):
        url_format = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=%d&n=1&mkt=zh-CN'
        headers = {
            'authority': 'cn.bing.com',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        for i in range(8):
            yield scrapy.Request(url=url_format % i, headers=headers)

    def parse(self, response):
        jsonstr = json.loads(response.text)
        image_str = jsonstr['images'][0]
        image_url = image_str['url']
        image_startDate = image_str['startdate']
        image_name = image_str['copyright']
        item = BingwallpaperItem()
        item['image_url_relatively'] = image_url
        item['image_url'] = response.urljoin(image_url)
        item['image_startDate'] = image_startDate
        item['image_name'] = image_name
        yield item
