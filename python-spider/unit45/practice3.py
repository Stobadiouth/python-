import requests
from lxml import etree
import json
import time

for page in range(1,2):
    url='http://www.hongniang.com/index/search?sort=0&wh=0&sex=2&starage=0&province=%E6%B1%9F%E8%8B%8F&city=%E8%8B%8F%E5%B7%9E&marriage=0&edu=0&income=0&height=0&pro=0&house=0&child=0&xz=0&sx=0&mz=0&hometownprovince=0&page={0}'.format(page)
    user_list=[]
    data=requests.get(url).text
    s=etree.HTML(data)
    #一页的信息
    page_mess=s.xpath('/html/body/div[4]/div[3]/div[1]/ul/li')
    for i in page_mess:
        name=i.xpath('./div[2]/a/text()')[0]
        age=i.xpath('./div[3]/span[1]/text()')[0]
        addr=i.xpath('./div[3]/span[2]/text()')[0]
        addr=str(addr).split(' ')
        marry=i.xpath('./div[3]/span[3]/text()')[0]
        height=i.xpath('./div[3]/span[4]/text()')[0]
        signature=i.xpath('./div[4]/text()')[1].strip()
        user={"name":name,"age":age,"province":addr[0],"city":addr[1],"marry":marry,"height":height,"signature":signature}
        user_list.append(user)
        time.sleep(1)
    try:
        fp=None
        with open('test','a') as fp:
            json.dump(user_list,fp)
    except Exception as ex:
        print(ex)
    finally:
        if fp:
            fp.close()

