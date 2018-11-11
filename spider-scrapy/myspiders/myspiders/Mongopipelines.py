# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import re
from datetime import datetime
from pymongo import MongoClient


class MongoPipeline(object):
    def __init__(self):
        client=MongoClient()
        self.db = client.mingyan

    def process_item(self, item, spider):
        print(111111111111111111)
        line=dict(item)
        self.db.data.insert(line)
        return line

    def close_spider(self,spider):
        print('*****************')