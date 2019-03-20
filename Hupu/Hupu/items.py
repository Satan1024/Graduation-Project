# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HupuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    PName = scrapy.Field()
    PNumber = scrapy.Field()
    PLocation = scrapy.Field()
    PHeight = scrapy.Field()
    PWeight = scrapy.Field()
    PBirth = scrapy.Field()
    PContract = scrapy.Field()
    PCurrent_salary = scrapy.Field()
    PTeam = scrapy.Field()
    pass
