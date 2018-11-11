import requests
from lxml import etree
import time

# file=s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div[1]/a/@title')
# file1=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[1]/a/@title')
# file2=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[2]/span[2]/text()')
#
# for i in file1:
#     print(i)

for a in range(2):
    url = 'https://book.douban.com/top250?start{0}'.format(a*25)
    data = requests.get(url).text

    s = etree.HTML(data)
    book=s.xpath('//*[@id="content"]/div/div[1]/div/table')#整本书的内容
    for div in book:
        title=div.xpath("./tr/td[2]/div[1]/a/@title")[0]#书名，xpath相同的部分省略
        socre=div.xpath("./tr/td[2]/div[2]/span[2]/text()")[0]#评分
        price= div.xpath("./tr/td[2]/p[1]/text()")[0].strip("(").strip().strip(")")#价格
        num= div.xpath("./tr/td[2]/div[2]/span[3]/text()")[0].strip("(").strip().strip(")")#评价
        time.sleep(2)

        print("{0}{1}{2}{3}".format(title,socre,price,num))