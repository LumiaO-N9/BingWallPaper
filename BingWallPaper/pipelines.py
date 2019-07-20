# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class BingwallpaperPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_url_relatively = item['image_url_relatively']
        image_url = item['image_url']
        headers = {
            'authority': 'cn.bing.com',
            'method': 'GET',
            'path': image_url_relatively,
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

        request = scrapy.Request(url=image_url, headers=headers)
        request.meta['item'] = item
        yield request

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]

        if not image_path:
            raise DropItem("Item contains no images")

        item['image_path'] = image_path
        return item

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        image_name = item['image_name']
        image_startDate = item['image_startDate']
        image_download_name = u'%s-%s.jpg' % (image_name.replace('/', '\\'), image_startDate)
        return image_download_name
