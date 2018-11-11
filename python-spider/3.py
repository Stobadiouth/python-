import requests
from lxml import etree
import time
for a in range(2):

    url='https://cd.xiaozhu.com/limitaccess.php?p={}'.format(a)
    data=requests.get(url).text
    s=etree.HTML(data)
    r=requests.get(url)
    print(r.status_code)
    file=s.xpath('//*[@id="page_list"]/ul/li')#整个信息


    for div in file:
        title = div.xpath('./div[2]/div/a/span/text()')[0]
        price=div.xpath('./div[2]/span[1]/text()')[0]

        image=div.xpath('./a/img/@lazy_src')[0]
        print('{0 {1} {2}'.format(title,price,image))