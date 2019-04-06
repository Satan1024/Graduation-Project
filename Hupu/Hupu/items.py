# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PlayerInfo(scrapy.Item):
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

class TeamInfo(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    TName = scrapy.Field()
    TStartTime= scrapy.Field()
    THome = scrapy.Field()
    TURL = scrapy.Field()
    TCoach = scrapy.Field()
    TIntroduction = scrapy.Field()
    TAvgScore = scrapy.Field()
    TAvgPer = scrapy.Field()
    TAvgRebound= scrapy.Field()
    TAvgLosepoint = scrapy.Field()
    TAvgTurnover = scrapy.Field()
    pass

class News(scrapy.Item):
    N24Title = scrapy.Field()
    N24Source = scrapy.Field()
    N24Time = scrapy.Field()
    N24Text = scrapy.Field()
