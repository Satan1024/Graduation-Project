import scrapy
from Hupu.items import News
from scrapy.selector import Selector
import re
class Newspider(scrapy.Spider):
    name = "newspider"
    allowed_domains = ["voice.hupu.com"]
    start_urls = ['https://voice.hupu.com/nba']
    custom_settings = {
    'ITEM_PIPELINES' : {'Hupu.pipelines.MongoPipeline':300}}
    def __init__(self):
        self.URLS24=[]
        self.cau = 0
    def parse(self, response):
        item = News()
        print('**************************SPIDER**********START*************************************************')
        hxs = Selector(response)
        if(self.cau==0):
            self.URLS24 = hxs.xpath('/html/body/div[3]/div[2]/div[1]/div[2]/ul/li/a/@href').extract()
            for i in range(len(self.URLS24)):
                self.URLS24[i]='https://voice.hupu.com'+self.URLS24[i]
            print(self.URLS24)
            print('**************************SPIDER**********END*************************************************')
        else:
            item['N24Title']=hxs.xpath('/html/body/div[4]/div[1]/div[1]/h1/text()').extract_first()
            item['N24Source']=hxs.xpath('//*[@id="source_baidu"]/a/text()').extract_first()
            item['N24Time']=hxs.xpath('//*[@id="pubtime_baidu"]/text()').extract_first()
            item['N24Text'] = ','.join(hxs.xpath('/html/body/div[4]/div[1]/div[2]/div/div[@class="artical-main-content"]/p/text()').extract())
            yield item        
        if self.cau<len(self.URLS24):
            yield scrapy.Request(url=self.URLS24[self.cau],callback=self.parse)
            self.cau+=1
        else:
            pass
        print('**************************SPIDER**********END*************************************************')
 
