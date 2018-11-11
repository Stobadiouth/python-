# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import re
from datetime import datetime


class HobbyPipeline(object):
    def __init__(self):
        self.fp=open('hnHobby2.json','a+')
        self.user=[]

    def process_item(self, item, spider):
        print(111111111111111111)
        line=dict(item)
        line["id"]=re.findall(r'\d+',line["id"])[0]
        del line["img_src"]
        self.user.append(line)
        return line

    def close_spider(self,spider):
        json.dump(self.user,self.fp,ensure_ascii=True)
        print(len(self.user))
        self.fp.close()