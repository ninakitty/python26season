from urllib.request import urlopen
import re
import sys


def get_website_content(page, *args):
    lst = []
    for i in range(page):
        website = 'http://www.lntb.gov.cn/Article_Class2.asp?ClassID=1&SpecialID=0&page=' + str(i + 1)
        content = urlopen(website).read().decode('gbk')
        obj = re.compile(r"title='文章标题：(?P<title>.*?)招标代码：(?P<code>.*?)作    者：(?P<author>.*?)更新时间：(?P<uptime>.*?)点击次数",
                         re.S)
        items = obj.finditer(content)
        for item in items:
            title = item.group('title').strip()
            code = item.group('code').strip()
            author = item.group('author').strip()
            uptime = item.group('uptime').strip()
            for arg in args:
                if arg in title:
                    lst.append({'page': i + 1, 'title': title, 'code': code, 'author': author, 'uptime': uptime})
                    break
    return lst


argv = sys.argv
argv.pop(0)
for arg in argv:  # 参数为str,需要修改为int,str,str样式
    print(type(arg), arg)
res = get_website_content(1, '中国')
for i in res:
    print(i['page'], '-->', i['title'])
