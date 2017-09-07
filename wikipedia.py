from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
import datetime
import random


ssl._create_default_https_context = ssl._create_unverified_context

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("https://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    regex = re.compile("^(/wiki/)"  # starts with /wiki/
                       "((?!:).)"  # not include :
                       "*$")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=regex)

links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)

