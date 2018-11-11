# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
import string
from myspiders.items import MiItem

class TbspiderSpider(scrapy.Spider):
    name = 'tbSpider'
    allowed_domains = ['mi.com']
    start_urls = []
    for i in range(2):
        query={
            "q":"手机",
            "s":1
        }
        query["s"]=i
        url="https://search.mi.com/search_{0}-0-0-0-0-0-0-0-0-{1}".format(query["q"],query["s"])
        url=parse.quote(url,safe=string.printable)
        start_urls.append(url)

    # def start_requests(self):
    #     query = {
    #             "q":"手机",
    #             "s":0
    #         }
    #     for i in range(2):
    #         url = "https://s.taobao.com/search?"
    #         query["s"]=i*48
    #         url=url+parse.urlencode(query)
    #         url=parse.quote(url,safe=string.printable)
    #         yield scrapy.FormRequest(url=url,callback=self.parse)

    def parse(self, response):
        phones=response.xpath('//div[@class="goods-item"]')
        for phone in phones:
            item=MiItem()
            item["title"]=phone.xpath('./h2[@class="title"]/a/text()')[0].extract()
            item["img_src"]=phone.xpath('./div[@class="figure figure-img"]/a/img/@src')[0].extract()
            yield item
