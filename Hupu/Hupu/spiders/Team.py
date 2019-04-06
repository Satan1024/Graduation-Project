import scrapy
from Hupu.items import TeamInfo
from scrapy.selector import Selector
import re
class HupuSpider(scrapy.Spider):
    def __init__(self):
        self.cau = -1
        self.allurl=[]
    name = "teamspider"
    # ???????
    allowed_domains = ["nba.hupu.com"]
    # ???????url??
    start_urls = ['https://nba.hupu.com/teams']  
    custom_settings = {'ITEM_PIPELINES' : {'Hupu.pipelines.MongoPipeline':400}}
   # ?????Item??
    def parse(self, response):
        print('**************************SPIDER**********START*************************************************')
        hxs = Selector(response)
        item = TeamInfo()
        if(self.cau==-1):
            self.allurl =  hxs.xpath('//a[@class="a_teamlink"]/@href').extract()
        if(len(self.allurl)>self.cau and self.cau!=-1):
            Team = ','.join(hxs.xpath('/html/body/div[3]/div[3]/div[1]/div[1]').extract())
            item['TName'] = re.search(".*<span class=\"title-text\">(.*)</span>.*",Team).group(1)
            item['TStartTime']=  re.search(".*<p>进入NBA：(.*)年</p>.*",Team).group(1)
            item['THome'] =  re.search(".*<p>主场：(.*)赛区</p>.*",Team).group(1)
            item['TURL'] =  re.search(".*<p>官网：<a target=\"_blank\" href=\"(.*)\">http.*",Team).group(1)
            item['TCoach'] =  re.search(".*<p>主教练：(.*)</p>*",Team).group(1)
            item['TIntroduction'] =  re.search(".*<div class=\"txt\">\\n(.*)\\n</div>.*",Team).group(1)
            DATAINFO=hxs.xpath("/html/body/div[3]/div[3]/div[1]/div[1]/div/div[1]/div[3]/div/div/span[2]/b/text()").extract()
            item['TAvgScore'] =  DATAINFO[0]
            item['TAvgPer'] =  DATAINFO[1]
            item['TAvgRebound'] = DATAINFO[2]
            item['TAvgLosepoint'] = DATAINFO[3]
            item['TAvgTurnover'] =  DATAINFO[4]
            yield item
            # print(item['TName'])
            # print(item['TStartTime'])
            # print(item['THome'])
            # print(item['TURL'])
            # print(item['TCoach'])
            # print(item['TIntroduction'])
            # print(item['TAvgScore'],item['TAvgPer'],item['TAvgRebound'],item['TAvgLosepoint'],item['TAvgTurnover'])
            if(self.cau<29):
                self.cau += 1
                yield scrapy.Request(url=self.allurl[self.cau],callback=self.parse)   
            else:
                pass
        elif(self.cau==-1):
            self.cau+=1
            yield scrapy.Request(url=self.allurl[self.cau],callback=self.parse)
        print('**************************SPIDER**********END*************************************************')
        # print(item['Team)
        # print(item['TName)
        # for player in players[1:]:
        #     # print(player)
        #     
        #     item[item['TName'] = hxs.xpath('/html/body/div[3]/div[3]/div[1]/div[1]/h2/span[1]').extract()#球队姓名
        #     INFO = re.findall(".*<td>(.*)</td>",player)
        #     # print(INFO)
        #     item['PNumber'] = INFO[0]#球员球衣编号 
        #     item['PLocation'] = INFO[1]#球员在场位置
        #     item['PHeight'] = INFO[2]#球员高度  
        #     item['PWeight'] = INFO[3]#球员体重
        #     item['PBirth'] = INFO[4] #球员生日  
        #     item['PContract'] = ','.join(re.findall(".*<td class=\"left\">(.*)<br><b>",player))#球员在职合同
        #     item['PCurrent_salary'] = ','.join(re.findall(".*<br><b>本年薪金：(.*)万美元</b></td>",player))#球员本年薪资
        #     item['PTeam'] = hxs.xpath('//span[@class="team_name"]//a/text()').extract()[self.cau]
            # yield item         


