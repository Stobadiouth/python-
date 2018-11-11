# -*- coding: utf-8 -*-
import scrapy
from myspiders.items import RunoobItem


class RunoobspiderSpider(scrapy.Spider):
    name = 'runoobSpider'
    allowed_domains = ['runoob.com']
    start_urls = ['http://www.runoob.com/']

    def parse(self, response):
        links=response.xpath('//div[@class="col nav"]/ul/li/a')
        items=[]
        for link in links:
            item=RunoobItem()
            item['href']=link.xpath('./@href').extract()
            item['title']=link.xpath('./text()').extract()

            yield item
        #     items.append(item)
        # return items