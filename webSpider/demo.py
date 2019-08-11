from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError


def getTitle(url):
        try:
            html = urlopen(url)
        except (HTTPError, URLError) as e:
            print("HTTPError")
            return None
        try:
            bsObj = BeautifulSoup(html.read(), "html5lib")  # "html5lib"防止报错
            title = bsObj.body.h1
        except AttributeError as e:
            return None
        return title

# 要考虑好抛异常的情况
title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
    print("title could not found")
else:
    print(title)



