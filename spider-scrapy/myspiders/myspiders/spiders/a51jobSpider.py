# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
import string
from myspiders.items import JobItem

class A51jobspiderSpider(scrapy.Spider):
    name = '51jobSpider'
    allowed_domains = ['51job.com']
    start_urls = []

    # url='https://search.51job.com/list/070300,000000,0000,00,9,99,python,2,1.html'
    # url='https://search.51job.com/list/070300,000000,0000,00,9,99,'
    # for i in range(1,3):
    #     url = 'https://search.51job.com/list/070300,000000,0000,00,9,99,'
    #     query["page"]='2.{0}.html'.format(i)
    #     url=url+parse.urlencode(query)
    #     url=parse.quote(url,safe=string.printable)
    #     start_urls.append(url)
    def start_requests(self):
        query = {
            "position": "python",
            "page": '2,1.html'
        }
        for i in range(1,3):
            query['page']='2,{0}.html'.format(i)
            url='https://search.51job.com/list/070300,000000,0000,00,9,99,{0},{1}'.format(query["position"],query["page"])
            yield scrapy.FormRequest(url=url,callback=self.parse)

    def parse(self, response):
        positions=response.xpath('//div[@id="resultList"]/div[@class="el"]')
        items=[]
        for po in positions:
            item=JobItem()
            item["title"]=po.xpath('./p/span/a/@title')[0].extract()
            item["company"]=po.xpath('./span[@class="t2"]/a/text()')[0].extract()
            item["addr"]=po.xpath('./span[@class="t3"]/text()')[0].extract()
            items.append(item)
        return items
