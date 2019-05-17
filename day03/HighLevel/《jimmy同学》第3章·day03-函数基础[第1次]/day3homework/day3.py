goods = {'电脑': 5000,
         '键盘': 300,
         '鼠标': 150,
         '风扇': 50,
         '耳机': 30,
         '水杯': 15,
         }
import os

user_info_list = []  # 用户信息
shopping_car = []  # 购物车
commodity_count = {}  # 商品数量
# print("编号:{}商品:{}价格:{}".format(format(i,'<2'),format(k,'<10'),format(goods[k],'>5')))
# 新建一个空文本文件
with open('用户信息.txt', 'r+', encoding='utf-8') as f:
    if len(f.read()) == 0:
        f.write('%s \t%s \t%s\n' % ('用户名', '密码', '金额'))

def modify_money(loginer, balance):
    '''
    修改用户金额信息
    '''
    with open('用户信息.txt', 'r', encoding='utf-8') as read_f, \
            open('临时文件.txt', 'w', encoding='utf-8') as write_f:
        for line in read_f:
            data = line.strip().split(' \t')
            if loginer == data[0]:
                line = line.replace(data[2], balance)
            write_f.write(line)
    os.remove('用户信息.txt')
    os.rename('临时文件.txt', '用户信息.txt')

def user_name_info():
    '''验证用户名是否已被注册'''
    while True:  # 验证用户名是否已被注册
        user_info = input('请输入用户名：').strip().lower()
        with open('用户信息.txt', 'r', encoding='utf-8') as f:
            for lines in f:
                name = lines.strip().split(' ')
                if user_info == name[0]:
                    print('用户已存在')
                    break
            else:
                print('用户名可使用')
                return user_info

def user_pwd_info():
    '''验证密码是否一致'''
    while True:  # 验证密码是否一致
        user_pwd = input('请输入密码：').strip()
        user_pwd_again = input('请确认密码：').strip()
        if user_pwd == user_pwd_again:
            print('注册成功')
            return user_pwd
        print('密码不一致')

def write_user_info(newuser_name, newuser_pwd):
    '''将新用户的用户名,密码,初始购物卡金额写入文件'''
    with open('用户信息.txt', 'a', encoding='utf-8') as f:
        f.write('%s \t%s \t%d\n' % (newuser_name, newuser_pwd, 10000))  # 将刚注册的用户的名字和初始的购物卡余额（0）写入文件
        return

def read_user_info(login_user, login_pwd):
    '''验证用户输入的账户及密码'''
    while True:
        if len(user_info_list) > 2:
            print('非法操作')
            return
        with open('用户信息.txt', 'r', encoding='utf-8') as f:
            for line in f:
                data = line.strip().split(' \t')
                if login_user == data[0] and login_pwd == data[1]:
                    print('登陆成功!')
                    return login_user, login_pwd
            print('用户名或密码错误')
            return '错误信息'

def user_money_info(user_balance):
    '''获取用于余额添加到列表'''
    with open('用户信息.txt', 'r', encoding='utf-8') as f:
        for line in f:
            data = line.strip().split(' \t')
            if user_balance == data[0]:
                return data[2]

def log_in():
    '''注册'''
    new_name = user_name_info()  # 检查新用户注册的名字是否可以使用
    new_pwd = user_pwd_info()  # 检查用户注册的密码是否一致
    write_user_info(new_name, new_pwd)  # 将新用户的用户名,密码,初始购物卡金额写入文件
    return

def auth():
    '''登陆'''
    count = 0
    while True:
        if count == 3:
            print('错误次数过多...')
            exit()
        user = input('请输入账户名:').strip().lower()
        pwd = input('请输入登陆密码:').strip()
        res1 = read_user_info(user, pwd)
        if res1 == '错误信息':
            count += 1
        else:
            user_info_list.append(user)  # 将用户名加入列表
            user_info_list.append(pwd)  # 将用户密码加入列表
            res2 = user_money_info(user)  # 获取用户的余额
            user_info_list.append(res2)  # 将用户余额添加到列表
            return res1

def buy():
    while True:
        if len(user_info_list) == 0:
            print('请先登陆...')
            return
        else:
            print('用户名:%s 余额:%s ' % (user_info_list[0], user_info_list[2]))
            print('如果结束购买请输入"q"...')
            oof = int(user_info_list[2])  # 将字符串转成整型
        while True:
            for k in goods:
                print('商品名称:%s 价格:%s' % (k, goods[k]))
            commodity_list = list(goods.keys())  # 将商品添加到列表
            choice2 = input('请输入商品名称:').strip()
            if oof == 0:
                print('你的余额为0,请先充值再进行购买')
                return
            if choice2 in commodity_list:
                # shopping_car.append(choice2)
                if choice2 in commodity_count:
                    commodity_count[choice2] += 1
                else:
                    commodity_count[choice2] = 1
                print('商品已成功添加到购物车')
            elif choice2 == 'q':
                while True:
                    if len(commodity_count) == 0:
                        return
                    choice3 = input('请确认是否购买Y/N:').strip().upper()
                    if choice3 == 'Y':
                        price = 0
                        # for i in shopping_car:
                        for i in commodity_count:
                            price += goods[i]
                        if price > oof:  # 如果商品的价格大于用户余额
                            print('余额不足,请先充值或购买其他商品')
                            return
                        else:
                            oof = oof - price
                            print(''.center(50, '-'))
                            print('%-30s %s' % ('商品', '价格(元)'))
                            for i in commodity_count:
                                print('%-30s %s' % (i, goods[i]))
                            print(''.center(50, '-'))

                            print('购买成功')

                            str_oof = str(oof)
                            modify_money(user_info_list[0], str_oof)
                            return str_oof
            else:
                print('没有此商品')

def quit():
    print('欢迎下次再来!')
    exit()

dic = {
    '1': log_in,
    '2': auth,
    '3': buy,
    '4': quit
}

def register():
    while True:
        print('''
        1.注册
        2.登陆
        3.购买
        4.退出   
        ''')
        choice1 = input('请输入对应序号：').strip()
        if choice1 in dic:
            dic[choice1]()    #调用对应的函数，dic[]()意思是dic[key]对应的value的函数调用，即log_in()、auth()、buy()、quit()
        else:
            print('输入有误')

register()
