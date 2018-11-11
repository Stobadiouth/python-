import requests
from lxml import etree
import time
url="https://www.csdn.net/"
data=requests.get(url).text
s=etree.HTML(data)
# film=s.xpath('//*[@id="Pl_Official_WeiboDetail__60"]/div/div/div/div[4]/div/div[2]/div[2]/div/div/div[1]')
film=s.xpath('//*[@id="feedlist_id"]/li[1]/div/div[1]/h2/a/text()')
# film=s.xpath('/html/body/div[3]/div/div[4]/div[2]/ul[1]/li[1]/a[1]/i/img')

print(film)

# for div in film:
#     print(1111)
#
#     title=div.xpath('./div[2]/div[1]/text()')[0]
#     # sign=div.xpath('./div[2]/div[3]/div[1]/ul/li[4]/span/a/span/em[2]/text()')[0]
#     # time.sleep(2)
#     print(1111,'{0}{1}'.format(title,sign))