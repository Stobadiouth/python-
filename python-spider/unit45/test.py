import requests
from lxml import etree
import json
import time
with open('test','r') as fp:
    data=json.load(fp)
    fp.close()
    print(data)

# url='http://www.hongniang.com/index/search?sort=0&wh=0&sex=2&starage=0&province=%E6%B1%9F%E8%8B%8F&city=%E8%8B%8F%E5%B7%9E&marriage=0&edu=0&income=0&height=0&pro=0&house=0&child=0&xz=0&sx=0&mz=0&hometownprovince=0&page=1'
# data=requests.get(url).text
# s=etree.HTML(data)
# page_mess=s.xpath('/html/body/div[4]/div[3]/div[1]/ul/li[1]/div[4]/text()')[1].strip()
# print(page_mess)

