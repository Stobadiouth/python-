# -*- coding: utf-8 -*-
import scrapy
from myspiders.items import Activity


class HongnangspiderSpider(scrapy.Spider):
    name = 'hongnangSpider'
    allowed_domains = ['hongniang.com']
    start_urls = ['http://www.hongniang.com/huodong']

    def parse(self, response):
        div = response.xpath('//*[@id="evecontent"]/div[@class="ac_list_sub"]')
        for d in div:
            # 创建一个item
            item = Activity()
            item['title'] = d.xpath('./a/div/text()')[0].extract()
            item['date'] = d.xpath('./div[2]/ul/li[1]/text()')[0].extract().strip()
            item['addr'] = d.xpath('./div[2]/ul/li[2]/text()')[0].extract().strip()
            item['number']=d.xpath('./div[2]/div[2]/span/text()')[0].extract().strip()
            item['img_src']=d.xpath('./div[1]/a/img/@src')[0].extract()
            yield item
        # 获取下一页的链接
        next_page = response.xpath('/html/body/div[5]/div/a[11]/@href')[0].extract()
        # 链接是否存在
        if next_page:
            # 把链接改为完整路径
            next_page = response.urljoin(next_page)
            # 回调
            yield scrapy.Request(next_page, callback=self.parse)
