# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import pymongo

class HupuPipeline(object):
    def __init__(self):
        pass
    def process_item(self, item, spider):
        pass
            
#暂时不需要处理
#现在定义另外一个存入mongodb的pipeline
class MongoPipeline(object):
    def __init__(self,mongo_url,mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db
    
    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_url = crawler.settings.get('MONGO_URL'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]
    
    def process_item(self,item,spider):
        name = item.__class__.__name__
        self.db[name].insert(dict(item))
        return item
    
    def class_spider(self,spider):
        self.client.close()

