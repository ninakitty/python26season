# -*- coding: utf-8 -*-
#注意点：此程序中的login文件是存在的。
import  os

#初始化函数
def init():
    #标志位判断用户是否已经登陆，0代表不登陆，1代表登陆
    flag = 0
    while True:
        print('''您这边有四个购物选择，
        1 代表的是登陆 ，
        2 代表的是注册，
        3 代表的是购物，
        4 代表的是退出
        ''')
        user_answer= input("请输入你的选择:")
        #判断输入的选择是否是为数字选择
        if user_answer.isdigit():
            user_answer = int(user_answer)
        else:
            print('您输入的内容有误！！！')
            continue
        # 判断用户的选择，分别进入对应的函数
        if user_answer == 1 :
            #取回登陆的返回值，用来购物时进行判断
            flag = login()
        elif user_answer == 2:
            register()
        elif user_answer == 3:
            #判断是否已经登陆成功，登陆成功则直接进入shopping(),没有登陆成功则进入登陆再进入shopping
            if flag == 1:
                shopping()
            else:
                login()
                shopping()
        elif user_answer == 4:
            exit(0)
        else:
            print("您输入的内容不是我们的选择范围，请重新输入。")
            continue
#登陆模块
def login():
    print("--------------登陆----------------")
    count = 1
    while True:
        if  count <4:
            name = input("请输入用户名:")
            password = input("请输入密码:")
            #以默认的r模式(可读模式打开文件)
            f_r = open('login')
            for i in f_r:
                info = i.split(' ')
                if name == info[0] and password == info[1].strip():
                    print("--------登陆成功----------")
                    f_r.close()
                    #返回1用于购物时判断是否成功登陆。
                    return 1
            else:
                print('-----用户名或者密码错误------')
                count +=1
                f_r.close()
        else:
            print("你输入密码次数超过限制")
            exit(0)

#注册模块
def register():
    print("--------------注册----------------")
    while True:
        name = input("请输入用户名:")
        f_r = open('login')
        for i in f_r:
            info = i.split(' ')
            if name == info[0]:
                print("用户名已经存在,请重新输入用户名:")
                break
        else:
            password = input("请输入密码:")
            f_r.close()
            break
    user_info=name + ' ' +password
    #将用户信息以追加形式写入文本文件
    f_w =open('login',mode='a')
    f_w.write('\n%s' % (user_info) )
    print("您已经注册成功，谢谢")
    f_w.close()
#购物模块
def shopping():
    print('---------欢迎购物----------')
    goods = [
        {'name': '电脑', 'price': 1999},
        {'name': '鼠标', 'price': 10},
        {'name': '游艇', 'price': 20},
        {'name': '美女', 'price': 998}]
    sum_price = 0
    money = input("请输入你的初始资产：")
    if not money.isdigit():
        print("资产不合法")
    money = int(money)
    pay_dic = {}
    while (money - sum_price) >= 10:
        print("价格如下")
        for i, g in enumerate(goods):
            print("%d: %s %d$" % (i + 1, g["name"], g["price"]))
        buy = input("请输入产品序列号购买：")
        if not buy.isdigit() or int(buy) < len(goods):
            print("序列号无效")
        buy = int(buy)
        if money < sum_price + goods[buy - 1]["price"]:
            print("余额不足啊兄弟")
            continue
        if buy - 1 in pay_dic:
            pay_dic[buy - 1] += 1
        else:
            pay_dic[buy - 1] = 1
        sum_price += goods[buy - 1]["price"]
        print("购买成功！")
        print("您已经购买以下物品：")
        for k, v in pay_dic.items():
            print("名称：%s, 价格:%d$, 数量:%d" % (goods[k]["name"], goods[k]["price"], v))
        print("您的账户剩余资产", money - sum_price)
    else:
        print("最便宜的你都买不起了滚吧 穷逼！")
# 运行程序
init()





