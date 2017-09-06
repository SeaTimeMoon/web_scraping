from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url1 = "http://pythonscraping.com/pages/warandpeace.html"
html = urlopen(url1)
# html_data = html.read().decode('utf-8')
# print(html_data)
bsobj = BeautifulSoup(html, "html.parser")

# nameList = bsobj.find_all("span", {"class":"green"})
# for name in nameList:
#     print(name.get_text())

url2 = "http://pythonscraping.com/pages/page3.html"
html2 = urlopen(url2)
bsobj2 = BeautifulSoup(html2, "html.parser")

#处理子标签
# for child in bsobj2.find("table",{"id":"giftList"}).children:
#     print(child)

#处理兄弟标签
# for sibling in bsobj2.find("table", {"id":"giftList"}).tr.next_sibling:
#     print(sibling)

#使用正则表达式获取图片
images = bsobj2.find_all("img", {"src":re.compile(r"../img/gifts/img.*.jpg")})
for image in images:
    print(image["src"])
