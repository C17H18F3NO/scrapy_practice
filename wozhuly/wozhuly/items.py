# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WozhulyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    avatar = scrapy.Field()
    birthdayyear = scrapy.Field()
    city = scrapy.Field()
    education = scrapy.Field()
    gender = scrapy.Field()
    height = scrapy.Field()
    marry = scrapy.Field()
    monolog = scrapy.Field()
    monologflag = scrapy.Field()
    province = scrapy.Field()
    salary = scrapy.Field()
    userid = scrapy.Field()
    username = scrapy.Field()
