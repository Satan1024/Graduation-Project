from django.db import models 
from mongoengine import * 

class PlayerINFO(Document): 
    PName = StringField() 
    PNumber = StringField() 
    PLocation = StringField() 
    PHeight = StringField() 
    PWeight = StringField() 
    PBirth = StringField() 
    PContract = StringField() 
    PCurrent_salary = StringField() 
    PTeam = StringField() 
    meta = { 'collection': 'PlayerInfo'} # 指明连接数据库的哪张表 

# for i in ArtiInfo.objects[:10]: # 测试是否连接成功 
#     print(i.PName)
class ContactINFO(Document):
    name = StringField() 
    email = StringField() 
    message = StringField() 
    meta = { 'collection': 'ContactINFO'}

class TeamINFO(Document):
    TName = StringField() 
    TStartTime= StringField() 
    THome = StringField() 
    TURL = StringField() 
    TCoach = StringField() 
    TIntroduction = StringField() 
    TAvgScore = StringField() 
    TAvgPer = StringField() 
    TAvgRebound= StringField() 
    TAvgLosepoint = StringField() 
    TAvgTurnover = StringField() 
    meta = { 'collection': 'TeamInfo'}


class NewsINFO(Document):
    N24Title = StringField() 
    N24Source = StringField() 
    N24Time = StringField() 
    N24Text = StringField() 
    meta = { 'collection': 'News'}

class Account(Document):
    UserNM = StringField()
    UserPwd = StringField()
    UserStrartTime = StringField()
    UserLV = StringField()
    meta = { 'collection': 'Account'}