# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field

class MyspidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class RunoobItem(scrapy.Item):
    href=Field()  #域
    title=Field()

class mingyanItem(scrapy.Item):
    text=Field()  #域
    author=Field()
    href=Field()

class JobItem(scrapy.Item):
    title=Field()  #域
    company=Field()
    addr=Field()

class MiItem(scrapy.Item):
    title=Field()  #域
    img_src=Field()

class HNbase(scrapy.Item):
    title=Field()  #域
    id=Field()
    sex=Field()
    birth=Field()
    height=Field()
    income=Field()
    marry=Field()
    edu=Field()
    city=Field()
    signature=Field()
    img_src=Field()

class HNMessage(scrapy.Item):
    id=Field()
    addr=Field()
    weight=Field()
    constellation=Field()
    blood=Field()
    nation=Field()
    profession=Field()
    house=Field()
    school=Field()
    children=Field()
    img_src = Field()

class HNLife(scrapy.Item):
    id=Field()
    drink=Field()
    smoke=Field()
    car=Field()
    cook=Field()
    housework=Field()
    parent=Field()
    img_src = Field()

class HNHobby(scrapy.Item):
    id=Field()
    food=Field()
    music=Field()
    film=Field()
    book=Field()
    pet=Field()
    img_src = Field()

class Activity(scrapy.Item):
    title=Field()
    date=Field()
    addr=Field()
    number=Field()
    img_src=Field()

