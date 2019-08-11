from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html5lib")

# findall函数  按照标签找到所有相同标签下的值
title = bsObj.find("h1")
namelist = bsObj.find_all("span", {"class": "green"})
print(len(namelist))
print("title: {0}, namelist:{1}".format(title, namelist))

# 导航树
naviTree = bsObj.children
for child in naviTree:
    print(child)
