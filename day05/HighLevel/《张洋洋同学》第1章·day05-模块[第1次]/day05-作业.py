# auth_Yang
# date_2019-02-15

import re ,json
from urllib.request import urlopen
Big_dic = {} #用于json存储用

def Move_FTP_S(*args): #
    Move_link = list(args)[0]  # 函数调用传来的为元组  转成列表  其中[0] 表示取第一个元素,也就是影片主页连接
    content_2 = urlopen(Move_link).read().decode("gbk")

    Move_And_FTP = re.compile(r'''<div class="title_all"><h1><font color=#07519a>201.*?《(?P<Move_Name>.*?)》.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<FTP_Link>.*?)"''',re.S)  # 正则匹配影片名称 和 下载连接
    it = Move_And_FTP.finditer(content_2)
    for ele in it:
        M_name = ele.group("Move_Name") #电影名称
        M_link = ele.group("FTP_Link")  #电影下载连接
        dic = {M_name:M_link}  # 每个电影看完一个字典
        Big_dic.update(dic)  #添加到全局的大字典中

def Save_Moves():  #JSON 存储
    json.dump(Big_dic, open("Down_Link.json", mode="w", encoding="utf-8"), ensure_ascii=False)

def Select_All(): #查询所有影片
    Move_list = json.load(open("Down_Link.json", mode="r", encoding="utf-8")) #打开json文件, 也可以简化成用Big_dic = {} 不打开json文件
    for item in Move_list:
        print("电影名称：", item, '\n下载连接:', Move_list[item])

def Select_Move(): #查询单个影片
    Show_Move = {} #用于显示查询得到的所有影片
    Search = input("输入要搜索的影片名称:>>")
    Move_list = json.load(open("Down_Link.json", mode="r", encoding="utf-8"))
    for item in Move_list:
        if Search in item:
            Select_Single_Move = {item:Move_list[item]} #查到的影片和下载连接放到查一个字典中
            Show_Move.update(Select_Single_Move)  #查到的影片放到将要显示的字典中
        else:
            pass
    if len(Show_Move) == 0: #判断是否查询到影片
        print("对不起,没有查询到该影片!!")
    else:
        print('共查询到 %s 部影片\n' %len(Show_Move)) #输出查询到的影片
        for item in Show_Move:
            print("电影名称：", item, '\n下载连接:', Move_list[item])

def Menu(): #查询函数
    while 1:
        choise = input('\n请输入选项  1[查看所有影片] 2[搜索影片]  3[退出] >>')
        if choise == "1":
            Select_All()
        elif choise == "2":
            Select_Move()
        elif choise == "3":
            exit()
        else:
            print("输入有误重新输入!!")

def man():
    url = "https://www.dytt8.net"  # 电影主页连接
    content = urlopen(url).read().decode("gbk")
    lst = re.findall(r'''.*?最新电影下载</a>]<a href='(?P<down_link>.*?)'>''',content)  #获取所有最新电影连接
    print("开始爬取2019新片精品电影地址...\n")

    for el in lst:
        link = url + el   # 每部影片的主页连接
        Move_FTP_S(link)  # 调用 爬取每一部影片 电影名称及下载连接

    print("爬取2019新片精品电影共 %s 部影片" %len(Big_dic))
    Save_Moves() #调用存储函数
    Menu() #调用查询函数


man()


