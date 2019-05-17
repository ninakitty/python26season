#!/usr/bin/python
# -*- coding:utf-8 -*-
# 用函数完成登录注册以及购物车的功能
# 1，启动程序，用户可选择四个选项：登录，注册，购物，退出。
# 2，用户注册，用户名不能重复，注册成功之后，用户名密码记录到文件中。
# 3，用户登录，用户名密码从文件中读取，进行三次验证，验证不成功则退出整个程序。
# 4，用户登录成功之后才能选择购物功能进行购物，购物功能（就是将购物车封装到购物的函数中）。
# 5，退出则是退出整个程序。
#
goods=[{"name":"电脑","price":1999},{"name":"鼠标","price":10},{"name":"键盘","price":100}]
islogin='false'

def registered():
    #注册函数
    while True:
        username=input('请输入用户名: ').strip()
        password = input('请输入密码：').strip()
        if username=='' or password=='':
            print("用户名或密码为空，请重新输入")
            continue
        with open(r'用户管理',encoding='utf-8') as f:
            for line in f:
                newline=line.strip().split()
                if username==newline[0]:
                    print("用户名已存在，请重新输入")
                    break
            else:
                with open(r'用户管理',mode='a', encoding='utf-8') as f:
                    f.write('\n'+username+'  '+password)
                    print("注册成功")
                    break

def login():
    #登录函数
    count=3
    global islogin
    while count>0:
        username=input('请输入用户名: ').strip()
        password=input('请输入密码：').strip()
        with open(r'用户管理',encoding='utf-8') as f:
            for line in f:
                newline=line.strip().split()
                if username==newline[0] and  password==newline[1]:
                    print("登录成功")
                    islogin='True'
                    break
            else:
                print("登录失败，您还有%d次机会，请重新输入" % (count-1))
                count-=1
                continue
            break

# 4，用户登录成功之后才能选择购物功能进行购物，购物功能（就是将购物车封装到购物的函数中）。
def shopping():
    #购物函数
    #判断是否登录
    flag=True
    while flag:
        if islogin == 'True':
            while True:
                recharge = input('请输入您的金额：').strip()
                if recharge.isdigit():
                    print('您当前的金额为%s元' % recharge)
                    break
                else:
                    print('您输入了非法字符，请重新输入')
            print('*************商品列表展示******************')
            for i in goods:
                print((goods.index(i)) + 1, i.get('name'), i.get('price'))
            print('*******************************************')
            print('(输入n为购物车结算,\n输入Q或者q退出程序)')
            # 定义购物车goods_car
            goods_car = {}
            # 定义总消费金额car_price
            car_price = 0
            while True:
                select_number = input('请输入选择的商品序号：').strip()
                if select_number.isdigit():
                    if 0 < int(select_number) <= len(goods):
                        print("当前商品名称%s,商品价格%d" % (
                        goods[int(select_number) - 1].get('name'), goods[int(select_number) - 1].get('price')))
                        if (int(select_number) - 1) not in goods_car:
                            goods_car[int(select_number) - 1] = {"name": goods[int(select_number) - 1].get('name'),
                                                                 "price": goods[int(select_number) - 1].get('price'),
                                                                 "amount": 1}
                        else:
                            goods_car[int(select_number) - 1]['amount'] += 1
                    else:
                        print('您当前输入有误，请重新输入')
                elif select_number == 'n':
                    while True:
                        if goods_car == {}:
                            print('当前购物车为空，无法结算，请进行购物')
                            break
                        else:
                            for i in goods_car:
                                print(goods_car[i].get('name'), goods_car[i].get('amount'), goods_car[i].get('price'))
                                car_price += goods_car[i].get('amount') * goods_car[i].get('price')
                            if int(recharge) < car_price:
                                print('购物车中结算金额为%d,当前余额为%d,余额不足，请选择删除某商品' % (car_price, int(recharge)))
                                car_price = 0
                                delete_number = input('请输入需要删除的商品的商品序号：').strip()
                                if delete_number.isdigit():
                                    if 0 < int(delete_number) <= len(goods_car):
                                        goods_car[int(delete_number) - 1]['amount'] -= 1
                                        if goods_car[int(delete_number) - 1]['amount'] == 0:
                                            del goods_car[int(delete_number) - 1]
                                    else:
                                        print('您当前输入有误，请重新输入')
                                else:
                                    print('您当前输入有误，请重新输入')
                            else:
                                break
                    print('当前用户成功消费%d元,余额为%d元' % (car_price, int(recharge) - car_price))
                elif select_number.upper() == 'Q':
                    print('成功退出')
                    flag = False
                    break
                else:
                    print('您当前输入有误，请重新输入')
            for j in goods_car:
                print('购买的商品%s,数量%d,单价%d，\n此次共消费%d，\n账户余额%d' % (
                goods_car[j].get('name'), goods_car[j].get('amount'), goods_car[j].get('price'),
                car_price, int(recharge) - car_price))
        else:
            print("未登录，请登录后进行购买")
            login()

def main():
    li = ["注册", "登陆", "购物", "退出"]
    print("欢迎进入新世界购物系统:")
    for i in range(len(li)):
        print(i+1, ".", li[i])
    while True:
        choice = input('请输入选项:').strip()
        if choice == '1':
            registered()
        elif choice == '2':
            login()
            continue
        elif choice == '3':
            shopping()
            continue
        elif choice == '4':
            break
        else:
            print('输入有误,请重新输入')
        break
main()