import re

str1='<li>001</li><li>002</li><li>003</li>'
reg=r'<li>(.*?)</li>'
regex=re.compile(reg)
res01=regex.findall(str1)
print(res01)

res=re.findall(reg,str1)
print(res)

str03='abcabc is a abc word,and defdef is a word too'
res03=re.findall(r'((?P<tt>abc){2})',str03)
print(res03)

str03='aabb is a abc word,and defdef is a word too'
res03=re.findall(r'(a)\1(b)\2',str03)
print(res03)