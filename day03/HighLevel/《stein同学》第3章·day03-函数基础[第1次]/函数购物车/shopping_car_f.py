# 1，启动程序，用户可选择四个选项：登录，注册，购物，退出。
# 2，用户注册，用户名不能重复，注册成功之后，用户名密码记录到文件中。
# 3，用户登录，用户名密码从文件中读取，进行三次验证，验证不成功则退出整个程序。
# 4，用户登录成功之后才能选择购物功能进行购物，购物功能（就是将购物车封装到购物的函数中）。
# 5，退出则是退出整个程序。
#用函数完成登录注册以及购物车的功能
# -*- coding:utf-8 -*-
def login():
    count = 0
    while True:
        r_name = input('请输入已注册账号>>>>>>')
        r_pwd = input('请输入已注册密码>>>>>>')
        use_pwd = r_name + ',' + r_pwd + '\n'
        with open('use_pwd',mode='r',encoding='utf-8') as f:
            for i in f:
                if use_pwd == i:
                    print('登录成功')
                    return True
        print('账号或密码不正确')
        if count == 2:
            return  False
        count += 1

def regiest():
    flag = True
    while flag:
        l = []
        r_name = input('注册账号>>>>>>')
        with open('use_pwd',mode='r',encoding='utf-8') as f,open('use_pwd',mode='a',encoding='utf-8') as f1:
            for i in f:
                s = i.strip().split(',')
                l.append(s[0])
            if r_name not in l:
                r_pwd = input('注册密码>>>>>>')
                use_pwd = r_name + ',' + r_pwd + '\n'
                f1.write(use_pwd)
                print('注册成功')
                flag = False
            else:
                print('账号已存在，请重新输入')

def shopping():
    shopping_list = [
        {'电脑': 3000},
        {'鼠标': 70},
        {'手机': 1440},
        {'充电宝': 100},
        {'音响': 1000},
        {'耳机': 120},
        {'去购物车结算': ''},
    ]
    shopping_car = []
    lis = []
    flag = True
    while flag:
        money = input('请充值金额：')
        if money.isdigit():
            money = int(money)
            print('您的余额为：%s' % money)
            while flag:
                for i in shopping_list:
                    for k in i:
                        print('%s.%s %s' % (shopping_list.index(i) + 1, k, i.get(k)))
                chooise = input('请输入商品序号：').strip()
                if chooise.isdigit():
                    chooise = int(chooise)
                    if chooise > 0 and chooise < len(shopping_list):
                        print('%s已加入购物车' % shopping_list[chooise - 1])
                        shopping_car.append(shopping_list[chooise - 1])
                    elif chooise == len(shopping_list):
                        while flag:
                            sum = 0
                            count = 0
                            for w in shopping_car:
                                if w not in lis:  # 购物车商品去重
                                    lis.append(w)
                            for w1 in lis:  # 计算重复商品购买次数，总价sum
                                count = shopping_car.count(w1)
                                for k1 in w1:
                                    print('%s.%s %s *%s' % (lis.index(w1) + 1, k1, w1.get(k1), count))  # 打印购买的商品详情
                                    sum += int(w1.get(k1)) * count  # 总价

                            if money >= sum:  # 可以完成购买
                                overplus = money - sum
                                chooise1 = input('余额充足，请输入q确认购买，并退出').upper().strip()
                                if chooise1 == 'Q':
                                    for w in lis:
                                        count = shopping_car.count(w)
                                        for k1 in w:
                                            print('%s.%s %s *%s' % (lis.index(w) + 1, k1, w.get(k1), count))
                                    print('此次共消费%s账户余额%s' % (sum, overplus))
                                    flag = False

                                else:
                                    print('请输入正确字符')

                            elif money < sum:  # 钱不够，需要删除商品
                                flag = True
                                sum1 = sum
                                while flag:
                                    if money < sum1:
                                        overplus1 = sum1 - money
                                        print('余额不足，还差%s，请删除购物车中的部分商品' % overplus1)
                                        chooise2 = input('请输入要删除的商品编号：')
                                        if chooise2.isdigit():
                                            chooise2 = int(chooise2)
                                            if chooise2 > 0 and len(lis) >= chooise2:
                                                shopping_car.remove(lis[chooise2 - 1])  # 删除shopping_car中的元素，来更新count
                                            else:
                                                print('请输入正确商品序号')
                                        else:
                                            print('请输入正确编号')
                                        sum1 = 0
                                        for x in lis:  # 判断shopping_car中商品是否被删除
                                            count = shopping_car.count(x)
                                            if count == 0:  # 同步更新lis
                                                lis.remove(x)
                                        for x in lis:
                                            count = shopping_car.count(x)
                                            for k2 in x:
                                                print('%s.%s %s *%s' % (lis.index(x) + 1, k2, x.get(k2), count))
                                                sum1 += int(x.get(k2)) * count

                                    elif money >= sum1:
                                        overplus2 = money - sum1
                                        chooise2 = input('余额充足，请输入q确认购买，并退出').upper().strip()
                                        if chooise2 == 'Q':
                                            for w in lis:
                                                count = shopping_car.count(w)
                                                for k1 in w:
                                                    print('%s.%s %s *%s' % (lis.index(w) + 1, k1, w.get(k1), count))
                                            print('此次共消费%s账户余额%s' % (sum1, overplus2))
                                            flag = False

                                        else:
                                            print('请输入正确字符')
                    else:
                        print('请输入列表展示的商品序号')

                else:
                    print('请输入正确的商品序号')
        else:
            print('输入有误，请输入数字')


def main():
    flag = True
    q = 0
    while flag:
        lis = ['登录','注册','购物','退出']
        for i in lis:
            print('%s,%s'%(lis.index(i)+1,i))
        chooise = input('请选择相应的功能序号（使用购物功能请先登录）>>>')
        if chooise == '1':
            flag = login()
            if flag == True:
                q = 1
        elif chooise == '2':
            regiest()
        elif chooise == '3':
            if q == 1:
                shopping()
            else:
                print('请先进行登录')
        elif chooise == '4':
            flag = False
        else:print('请选择正确的序号')
main()