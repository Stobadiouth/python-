# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import re
from datetime import datetime


class MyspidersPipeline(object):
    def process_item(self, item, spider):
        # print('**************---**************')
        # print(item)
        return item

class MiPipeline(object):
    def __init__(self):

        self.fp=open('hnBase2.json','a+')
        self.user=[]

    def process_item(self, item, spider):
        print(111111111111111111)
        line=dict(item)
        line["id"]=re.findall(r'\d+',line["id"])[0]
        # 根据年龄计算出出生日期
        age=int(re.findall(r'\d+',line["birth"])[0])
        now=datetime.now()
        years=now.year-age
        day=now.day if now.day>9 else '0'+str(now.day)
        month = now.month if now.month > 9 else '0' + str(now.month)
        line["birth"]="{0}-{1}-{2}".format(years,month,day)
        # 把升高转为int型
        height=re.findall(r'\d+',line["height"])
        if height:
            line["height"]=height[0]
        self.user.append(line)
        return line

    def close_spider(self,spider):
        json.dump(self.user,self.fp,ensure_ascii=True)
        print(len(self.user))
        self.fp.close()