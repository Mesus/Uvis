from bs4 import BeautifulSoup
import requests
url = 'https://en.wikipedia.org/wiki/Autonomous_underwater_vehicle'
r = requests.get(url)
r.encoding = 'utf-8'
doc = r.text
# print doc
pagesoup = BeautifulSoup(doc)
content = pagesoup.find(id='content')
for x in content.findAll("span", { "class" : "mw-editsection" }):
    # print x
    # pagesoup.__delitem__(x)
    x.extract()
content.find(id='siteSub').extract()
content.find(id='jump-to-nav').extract()
p = content.prettify()
print p
# print [x.extract() for x in pagesoup.findAll("span", { "class" : "mw-editsection" })]