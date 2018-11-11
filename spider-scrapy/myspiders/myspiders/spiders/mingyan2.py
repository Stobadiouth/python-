# -*- coding: utf-8 -*-
import scrapy
from myspiders.items import mingyanItem


class Mingyan2Spider(scrapy.Spider):
    name = 'mingyan2'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/page/1/']

    def parse(self, response):
        div=response.xpath('//div[@class="quote post"]')
        for d in div:
            item=mingyanItem()
            item['text']=d.xpath('./span[@class="text"]/text()')[0].extract()
            item['author']=d.xpath('./span/small/text()')[0].extract()
            item['href']=d.xpath('./span/a/@href')[0].extract()
            yield item

        next_page=response.xpath('//li[@class="next"]/a/@href')[0].extract()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)
