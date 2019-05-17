#作业要求
#1，启动程序，用户可选择四个选项：登录，注册，购物，退出。
#2，用户注册，用户名不能重复，注册成功之后，用户名密码记录到文件中。
#3，用户登录，用户名密码从文件中读取，进行三次验证，验证不成功则退出整个程序。
#4，用户登录成功之后才能选择购物功能进行购物，购物功能（就是将购物车封装到购物的函数中，这部分没思路写出来）。
#5，退出则是退出整个程序。



while True:
    print('-----新建用户：N/n------')
    print('-----登陆用户：E/e------')
    print('-----开心购物：S/s------')
    print('-----退出程序：Q/q------')
    choice = input('请输入您的选择：').strip()
    if choice.upper() == 'N':
        #注册
        with  open('login.txt',mode='a+',encoding='utf-8') as f:
            f.seek(0)
            user = {}  # 把用户名和密码存放字典中
            for line in f:
                v=line.strip().split(':')
                user[v[0]] = v[1]
            for i in range(3):
                username = input('请输入用户名：').strip()
                password = input('请输入密码：').strip()
                re_pw = input('确认密码：').strip()
                if username in user:
                    print('该用户名已存在')
                elif re_pw != password:
                    print('密码不一致，请重新输入密码')
                else:
                    print('%s注册成功,请登陆'%(username))
                    f.write(username + ':' + password + '\n')
                    break
            else:
                print('注册失败')

    if choice.upper() == 'E':
        # 登陆
        with open('login.txt',mode='a+',encoding='utf-8') as f1:
            f1.seek(0)
            users = {}
            for l in f1:
                k = l.strip().split(':')
                users[k[0]] = k[1]
            for x in range(3):
                v_user = input('请输入用户名：').strip()
                v_password = input('请输入密码：').strip()
                if v_user in users and v_password == users[v_user]:
                    print(v_user,'welcome to shop_city')
                    break
                else:
                    print('用户/密码错误')
            else:
                print('登陆失败')

    if choice.upper() == 'S':
        #开心购物
        goods = [
            {'name': '电脑', 'price': 1999},
            {'name': '鼠标', 'price': 10},
            {'name': '美女', 'price': 50},
            {'name': '游艇', 'price': 20},
            {'name': '火箭', 'price': 250},
        ]

        shop_car = {}
        money = input('请输入您的金额:')
        if money.isdigit():
            while 1:
                for i in range(len(goods)):
                    print(i + 1, goods[i]['name'], goods[i]['price'])
                choose = input('请输入您要购买的商品序号(N/结算 -- Q/退出):') #先选商品后结算
                if choose.isdigit() and 0 < int(choose) <= len(goods):
                    int_index = int(choose) - 1
                    if shop_car.get(int_index) == None:
                        shop_car[int_index] = 1
                    else:
                        shop_car[int_index] = shop_car[int_index] + 1
                elif choose.upper() == 'N':
                    fei_yong = 0
                    for f in shop_car:
                        fei_yong = fei_yong + shop_car[f] * goods[f]['price']
                    if int(money) - fei_yong >= 0:
                        for k in shop_car:
                            print(f'您购买的商品是{goods[k]["name"]},单价{goods[k]["price"]},数量{shop_car[k]}')
                    else:
                        print('余额不足')
                        for i in shop_car:
                            print(i, goods[i]['name'], shop_car[i])
                        str_del = input('请选择要删除的商品序号:')
                        if shop_car[int(str_del)] == 1:
                            shop_car.pop(int(str_del))
                        else:
                            shop_car[int(str_del)] = shop_car[int(str_del)] - 1
                elif choose.upper() == 'Q':
                    print(f'您此次购物消费了{fei_yong},剩余余额{int(money) - fei_yong}')
                    break
                else:
                    print('输入有误,请重新输入!')
        else:
            print('请正确输入!')
    if choice.upper() == 'Q':
        #退出
        print('退出成功')
        break

