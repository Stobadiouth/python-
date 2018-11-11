from lxml import etree
import requests

xml=etree.parse('data.xml')
books=[]
titles=xml.xpath('//book/title')
authors=xml.xpath('//book/author')
prices=xml.xpath('//book/price')

for i in range(len(titles)):
    book={"title":titles[i].text,"author":authors[i].text,"price":prices[i].text}
    books.append(book)

print(books)
