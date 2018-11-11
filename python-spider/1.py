import requests
from lxml import etree
url='https://movie.douban.com/subject/1292052/'
data=requests.get(url).text
s=etree.HTML(data)
film=s.xpath('//*[@id="content"]/h1/span[1]/text()')#片名
director=s.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')#导演
actor1=s.xpath('//*[@id="info"]/span[3]/span[2]/span[1]/a/text()')#主演1
actor2=s.xpath('//*[@id="info"]/span[3]/span[2]/span[2]/a/text()')#主演2
r=requests.get(url)
print(r.status_code)
print(film)
print(director)
print(actor1)
print(actor2)