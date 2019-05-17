#!/usr/bin/nev python


# 1，启动程序，用户可选择四个选项：登录，注册，购物，退出。
# 2，用户注册，用户名不能重复，注册成功之后，用户名密码记录到文件中。
# 3，用户登录，用户名密码从文件中读取，进行三次验证，验证不成功则退出整个程序。
# 4，用户登录成功之后才能选择购物功能进行购物，购物功能（就是将购物车封装到购物的函数中）。
# 5，退出则是退出整个程序。

count = 0

def login():
    user = input("用户:")
    passwd = input("密码:")
    with open("passwd.txt","r",encoding="utf-8") as f:
        for i in f:
            if i == user+","+passwd+"\n":
                print("登入成功")
                break
        else:
            print("用户名或密码错误！")

def register():
    print("欢迎注册！")
    count = 0
    while count < 3:
        user = input("用户:")
        passwd = input("密码:")
        with open("passwd.txt","r+",encoding="utf-8") as f:
            for i in f:
                if i.startswith(user):
                    print("用户已经被注册！")
                    break
            else:
                f.write(user+","+passwd+"\n")
                print("注册成功!")
                break

        count += 1

def shopping():
    shopping_list = [
        {"name": "电脑", "price": 1999},
        {"name": "手机", "price": 3000},
        {"name": "汽车", "price": 300000}
    ]

    shopping_cart = []

    user_money = input("请充值:")
    if user_money.isdigit():
        user_money = int(user_money)
        while True:
            for itme in shopping_list:
                print(shopping_list.index(itme), itme["name"], itme["price"])
            user_inupt = input("请输入的想要选择的商品序号:")
            if user_inupt.isdigit():
                user_inupt = int(user_inupt)
                if user_inupt < len(shopping_list) and user_inupt >= 0:
                    p_itme = shopping_list[user_inupt]
                    if p_itme["price"] <= user_money:
                        shopping_cart.append(p_itme)
                        user_money -= p_itme["price"]
                        print("余额%s" % user_money)
                    else:
                        print("余额不足%s" % user_money)
                else:
                    print("商品不存在")

            elif user_inupt.upper() == "Q":
                print("------- 购买的商品 ------")
                for p in shopping_cart:
                    print(p["name"], p["price"])
                exit()
            elif user_inupt.upper() == "N":
                print("------- 购买的商品 ------")
                for p in shopping_cart:
                    print(p["name"], p["price"])
                print("-------------------------")
            else:
                print("您输入的有误，请重新输入")
    else:
        print("你的输入有误")


def sign_out():
    exit()

for i in range(3):
    menu = input("1[登入],2[注册],3[购物],4[退出]:")
    if menu.isdigit():
       menu = int(menu)
       if menu == 1:
           login()
           count = 1
       elif menu == 2:
           register()
       elif menu == 4:
           sign_out()
       elif menu == 3:
           if count == 1:
               shopping()
           else:
               print("您需要登入！")
    else:
       print("输入有误请重新输入!")
