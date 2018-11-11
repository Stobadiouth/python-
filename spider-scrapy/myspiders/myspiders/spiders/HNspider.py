# -*- coding: utf-8 -*-
import scrapy
import requests
from lxml import etree
from urllib import parse
import string
from myspiders.items import HNbase
from scrapy.conf import settings

class HnspiderSpider(scrapy.Spider):
    name = 'HNspider'
    allowed_domains = ['hongniang.com']
    start_urls = []
    cookie = settings['COOKIE']  # 带着Cookie向网页发请求

    # 发送给服务器的http头信息，有的网站需要伪装出浏览器头进行爬取，有的则不需要
    headers = {
        'Connection': 'keep - alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }
    def start_requests(self):
        for i in range(1,10):
                url='http://www.hongniang.com/index/search?sort=0&wh=0&starage=0&sex=2&province=%E6%B1%9F%E8%8B%8F&city=0&marriage=0&edu=4,5,6,7&income=0&height=0&pro=0&house=0&child=0&xz=0&sx=0&mz=0&hometownprovince=0&page={0}'.format(i)
                data=requests.get(url).text
                s=etree.HTML(data)
                #获取所有的链接
                links=s.xpath('//li[@class="pin"]/div[@class="pin_img"]/a/@href')
                for link in links:
                    link='http://www.hongniang.com'+link
                    yield scrapy.FormRequest(url=link,callback=self.parse,cookies=self.cookie,headers=self.headers)

    def parse(self, response):
        item=HNbase()
        item["title"]=response.xpath("/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/text()")[0].extract().strip()
        item["id"]=response.xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[2]/text()')[0].extract()
        item["sex"]=response.xpath("/html/body/div[3]/div[3]/div[1]/div[2]/ul[1]/li[1]/text()")[0].extract()
        item["birth"]=response.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/ul[1]/li[1]/text()')[0].extract()
        item["height"]=response.xpath("/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/ul[2]/li[1]/text()")[0].extract()
        item["income"]=response.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/ul[3]/li[1]/text()')[0].extract()
        item["marry"]=response.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/ul[1]/li[2]/text()')[0].extract()
        item["edu"]=response.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/ul[2]/li[2]/text()')[0].extract()
        item["city"]=response.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/ul[3]/li[2]/text()')[0].extract()
        item["signature"]=response.xpath('/html/body/div[3]/div[1]/div[2]/div[5]/div[3]/text()')[0].extract().strip()
        item["img_src"]=response.xpath('//*[@id="pic_"]/@src')[0].extract()
        yield item
