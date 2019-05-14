from urllib.request import urlopen
import re
import sys
import urllib


def get_website_content(page, *args):
    lst = []
    website = 'http://www.lntb.gov.cn/Article_Class2.asp?ClassID=1&SpecialID=0&page=' + str(page)
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
                lst.append(
                    {'arg': arg, 'page': page, 'title': title, 'code': code, 'author': author, 'uptime': uptime})
                break
    return lst


def main_operate():
    flag = False
    argv = sys.argv
    lst = []
    if len(argv) == 2:  # 处理传入的参数
        if ',' in argv[1]:
            lst = argv[1].split(',')
            if lst[0].isdigit():
                lst[0] = int(lst[0])
                flag = True
            else:
                print('page参数错误!')
            for i, item in enumerate(lst):
                print(f'第{i + 1}个参数是{item},参数类型为{type(item)}')
        else:
            print('''
            请传入正确的参数,程序会在页面中获取参数相关信息,其中页面数量和第一个查找内容为必填项!
            getwebsite pagenum,arg1,[arg2]
            示例:
                getwebsite 1,中国,乡村
            ''')
        if flag:
            print('''
                        此网站访问速度较慢,请等待执行结果!
                        ''')
            for page in range(lst[0]):
                res = get_website_content(page+1, *lst[1:])  # 传入参数,获取结果
                for i in res:
                    print(f"第{i['page']}页--> 标题:{i['title']}--包含内容:'{i['arg']}'")
    else:
        print('''
        请传入正确的参数,程序会在页面中获取参数相关信息,其中页面数量和第一个查找内容为必填项!
        getwebsite pagenum,arg1,[arg2]
        示例:
            getwebsite 1,中国,乡村
        ''')


if __name__ == '__main__':
    while 1:
        try:

            main_operate()
            break
        except urllib.error.HTTPError as e:
            print(e)
            continue
