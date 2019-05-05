from bs4 import BeautifulSoup
from lxml import html
import xml
import requests, re

start_page = 1
pages = 1  # 要搜索的页数
filter_char = ['沈阳铁路局', '铁路工程']  # 要搜索的关键字段
prepear_link = 'http://www.lntb.gov.cn/Article_Show.asp?ArticleID='
url = f"http://www.lntb.gov.cn/Article_Class2.asp?ClassID=1&SpecialID=0&page="
for page in range(1, pages + 1):
    f = requests.get(url + str(page))
    soup = BeautifulSoup(f.content, "lxml")
    for td in soup.find_all('td', height='200'):
        for a in td.find_all('a', target='_blank'):
            print(a)
