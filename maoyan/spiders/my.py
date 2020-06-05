# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem


class MySpider(scrapy.Spider):
    name = 'my'
    allowed_domains = ['maoyan.com']
    start_urls = []
    for i in range(0, 100, 10):
        url = f'https://maoyan.com/board/4?offset={i}'
        start_urls.append(url)

    def parse(self, response):
        datas = response.xpath('//dl[@class="board-wrapper"]')
        for data in datas:
            item = MaoyanItem()
            item["name"] = data.xpath('.//div//a/text()').extract()
            item["star"] = data.xpath('.//p[@class="star"]/text()').extract()
            item["releasetime"] = data.xpath('//p[@class="releasetime"]/text()').extract()
            # item["score"] = data.xpath('//dl[@class="board-wrapper"]').extract()
            print(item["name"])
            yield item
