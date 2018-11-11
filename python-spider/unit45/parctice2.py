from lxml import etree

parser=etree.HTMLParser(encoding='utf-8')
htmlelement=etree.parse('hongniang.html',parser=parser)
xx=htmlelement.xpath('//li[@class="pin"]/div[@class="xx"]/span')
print(len(xx))
messe=[]
for i in range(0,len(xx),4):
    me={"age":xx[i].text,"addr":xx[i+1].text,"marry":xx[i+2].text,"height":xx[i+3].text}
    messe.append(me)

print(messe)
