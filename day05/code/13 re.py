import re


# lst = re.findall(r"\d+", "今天吃了2次鸡, alex吃了0次鸡, 他是砸在")
# print(lst)


# it = re.finditer(r"\d+", "今天吃了2次鸡, alex吃了0次鸡, 他是砸在")
# for item in it:
#     print(item.group())

# # 查找, 查找导第一个匹配项就返回了
# obj = re.search(r"\w+", "@@@www.baidu.com")
# print(obj.group())
#
# # # 匹配, 查找导第一个匹配项就返回了
# # 从头匹配
# obj = re.match(r"\w+", "@@@www.baidu.com")
# print(obj)

# # 把正则加载到内存
# obj = re.compile(r"\w+")
# obj.match("www.baidu.com")


# # 重点
# # <div>(?P<name>.*?)</div>
# # <div>倚天屠龙</div>
# s = "<span><div>倚天屠龙</div><div>少林武当</div></span>fasdfasdfsda</div>"
#
# it = re.finditer(r"<div>(?P<hahaha>.*?)</div>", s)
# for item in it:
#     print(item.group("hahaha"))


# 爬虫应用

# 获取到网络源代码需要的包
from urllib.request import urlopen

content = urlopen("https://www.dytt8.net/html/gndy/dyzz/20190419/58500.html").read().decode("gbk")
# print(content)

obj = re.compile(r'<div id="Zoom">.*?◎片　　名(?P<name>.*?)<br />.*?◎主　　演(?P<arts>.*?)<br /><br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<url>.*?)">',re.S)

it = obj.finditer(content)
for item in it:
    print(item.group("name"))
    print(item.group("arts"))
    print(item.group("url"))

'''
# 作业
# 爬去dytt 2019新片精品  -> 把所有电影的名字, 主演, 下载链接. 放在一个json文件里

[
    {"main_people": ["井柏然", "张一山"], "name": xxxx, "url":},
    {},
    {}
    
]

要求: 代码合理性
'''
