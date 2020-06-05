# -*- coding: utf-8 -*-
import scrapy
from ..items import WozhulyItem
import json


class WzlySpider(scrapy.Spider):
    name = 'wzly'
    allowed_domains = ['7799520.com']
    start_urls = []
    for i in range(1, 11):
        url = f'http://www.7799520.com/api/recommend/pc/luck/list?token=&page={i}'
        start_urls.append(url)

    def parse(self, response):
        result = response.text
        dts = json.loads(result)
        data = dts['data']['list']
        for dt in data:
            item = WozhulyItem()
            item['avatar'] = dt['avatar']
            # print(item['avatar'])
            item['birthdayyear'] = dt['birthdayyear']
            item['city'] = dt['city']
            item['education'] = dt['education']
            item['gender'] = dt['gender']
            item['height'] = dt['height']
            item['marry'] = dt['marry']
            item['monolog'] = dt['monolog']
            item['monologflag'] = dt['monologflag']
            item['province'] = dt['province']
            item['salary'] = dt['salary']
            item['userid'] = dt['userid']
            item['username'] = dt['username']
            yield item