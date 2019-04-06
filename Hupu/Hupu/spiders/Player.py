import scrapy
from Hupu.items import PlayerInfo
from scrapy.selector import Selector
import re
class PlayerSpider(scrapy.Spider):
    def __init__(self):
        self.cau = 0
    name = "playerspider"
    # ???????
    allowed_domains = ["nba.hupu.com"]
    # ???????url??
    start_urls = ['https://nba.hupu.com/players/rockets']
    custom_settings = {
    'ITEM_PIPELINES' : {'Hupu.pipelines.MongoPipeline':300}
}
    cau = 0
    # ?????Item??
    def parse(self, response):
        print('**************************SPIDER**********START*************************************************')
        hxs = Selector(response)
        players = hxs.xpath('/html/body/div[3]/div[4]/table/tbody/tr').extract()
        for player in players[1:]:
            # print(player)
            item = PlayerInfo()
            item['PName'] = ','.join(re.findall(".*.html\">(.*)</a></b>",player))#球员姓名
            INFO = re.findall(".*<td>(.*)</td>",player)
            # print(INFO)
            item['PNumber'] = INFO[0]#球员球衣编号 
            item['PLocation'] = INFO[1]#球员在场位置
            item['PHeight'] = INFO[2]#球员高度  
            item['PWeight'] = INFO[3]#球员体重
            item['PBirth'] = INFO[4] #球员生日  
            item['PContract'] = ','.join(re.findall(".*<td class=\"left\">(.*)<br><b>",player))#球员在职合同
            item['PCurrent_salary'] = ','.join(re.findall(".*<br><b>本年薪金：(.*)万美元</b></td>",player))#球员本年薪资
            item['PTeam'] = hxs.xpath('//span[@class="team_name"]//a/text()').extract()[self.cau]
            yield item
        self.cau += 1   
        allurl =  hxs.xpath('//span[@class="team_name"]//a/@href').extract()
        # print(allurl[0])
        if(len(allurl)>self.cau):
            url = allurl[self.cau]
            yield scrapy.Request(url=url,callback=self.parse)
        else:
            pass
        print('**************************SPIDER**********END*************************************************')