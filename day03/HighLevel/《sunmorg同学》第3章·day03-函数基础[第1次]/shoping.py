# -*- coding:utf-8 -*-
# Author：sunmorg

import os

user_list = []

goods =[
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
    {"name": "手机", "price": 2998},
    {"name": "键盘", "price": 598}
]


def prompt_func():
    """
    开始输出菜单方法
    :return: None
    """
    return ('''
欢迎来到购物系统！
操作选项：
    1、登录购物
    2、注册账号
    3、exit退出程序''')


def user_signin():
    """
    用户登入方法
    :return:
    """
    count = 0

    login_flag = False
    login_name = ''
    while count < 3:
        signin_name = input('请输入用户名：')
        signin_pwd= input('请输入密码：')
        if check_pwd(signin_name, signin_pwd):
            print('登入成功')
            login_flag = True
            login_name = signin_name
            break
        else:
            count += 1
            print('用户名或密码错误请重新输入！')
        if count == 3:
            exit('错误次数已达三次，程序自动退出！')
    if login_flag:
        print_shop(login_name)


def print_shop(login_name):
    """
    打印购物信息
    :return:
    """
    while True:
        print("----  商品列表  ----")
        for i, v in enumerate(goods):
            print(i, v['name'], v['price'])
        var = (input("\033[94m请输入你要买的商品序列号(充值：t; 余额：b;  金额记录：h; 退出：q)：\033[0m")).strip()
        if var.isdigit():
            var = int(var)
            if var >=0 and len(goods) > var:
                u = open('user.txt', mode='r', encoding='utf-8')
                for line in u:
                    line = line.strip()
                    userinfo = line.split(',')
                    if userinfo[0] == login_name:
                        user_num = int(userinfo[2])
                u.close()
                shop_func(login_name, user_num, var)
            else:
                print("\033[91m没有找到您想要的商品,请重新输入商品编号。\033[0m")
        elif var == 't':
            num = input("请输入用充值的金额：").strip()
            if num.isdigit():
                num = int(num)
                recharge(login_name, num, 't')
            else:
                print('输入金额无效！')
        elif var == "b":
            show_num(login_name)
        elif var == 'h':
            f_name = login_name + '.txt'
            f = open(f_name, "r", encoding='utf-8')
            print("历史消费记录：")
            for i, line in enumerate(f.readlines()):
                print(i, line.strip())
            f.close()
        elif var == "q":
            exit('欢迎下次再来！')
        else:
            print("\033[91m请输入正确的商品编号。\033[0m")
            continue



def shop_func(login_name, user_num, num):
    """
    购物方法
    :param login_name: 已登入用户名
    :param user_num: 已登入用户总金额
    :param num: 商品下标
    :return:
    """
    f_name = login_name + '.txt'
    choiceGood = goods[num]
    total_num= 0
    # 判断用户的余额是否足够买想要的商品
    if choiceGood['price'] <= user_num:
        user_num = user_num - choiceGood['price']
        total_num += choiceGood['price']
        print("\033[94m您选的物品\033[0m\033[95m%s\033[0m\033[94m已购买，您的余额还有\033[0m\033[95m%s\033[0m" % (
        choiceGood['name'], user_num))
        f = open(f_name, mode='a', encoding='utf-8')
        li = ['购买 %s ，价格%s 元，余额 %s 元\n' % (choiceGood['name'], choiceGood['price'], user_num)]
        f.writelines(li)
        f.close()
        recharge(login_name, 0-total_num, 'b')
    else:
        print("\033[91m您的余额不足(余额：%s)，请充值后购买(充值：t)。\033[0m" % user_num)


def recharge(login_name, num, type):
    """
    充值与结算方法
    :param login_name: 已登入用户名
    :param num: 金额
    :param type: 类型 b:购物 t:充值
    :return:
    """
    os.rename('user.txt', 'userbak.txt')
    f = open('userbak.txt', mode='r', encoding='utf-8')
    n = open('user.txt', mode='w', encoding='utf-8')
    num_str = ''
    for line in f:
        line = line.strip()
        userinfo = line.split(',')
        if userinfo[0] == login_name:
            if type == 't':
                num_str = '充值前金额为 %s 元,充值 %s 元,目前总金额为: %s 元\n'%(userinfo[2], num, str(int(userinfo[2]) + int(num)))
            userinfo[2] = str(int(userinfo[2]) + int(num))
        userstr = ','.join(userinfo)
        userstr += '\n'
        n.write(userstr)
    f.close()
    n.close()
    os.remove('userbak.txt')
    f_name = login_name + '.txt'
    f = open(f_name, mode='a', encoding='utf-8')
    f.writelines(num_str)
    f.close()


def show_num(login_name):
    """
    查询余额
    :param login_name: 已登入用户名
    :return:
    """
    f = open('user.txt', mode='r', encoding='utf-8')
    for line in f:
        line = line.strip()
        userinfo = line.split(',')
        if userinfo[0] == login_name:
            print('您还剩 %s 元！'%userinfo[2])
    f.close()


def check_pwd(name, pwd):
    """
    校验密码
    :param name: 用户名
    :param pwd: 密码
    :return: True or False
    """
    for user in user_list:
        if name == user['username'] and pwd == user['pwd']:
            return True
    return False


def user_signup():
    """
    用户注册方法
    """
    user_name = input('请输入需要注册的用户名：')
    if check_username(user_name):
        pwd = input('请输入新用户名的密码：')
        f = open('user.txt', mode='a', encoding='utf-8')
        f.write(user_name + ',' + pwd + ','+ '0' + '\n')
        user_list.append({'username': user_name, 'pwd': pwd, 'total': 0})
        print('新用户注册成功，用户名：%s，密码%s'%(user_name, pwd))
        f.close()
    else:
        print('用户名已存在！')


def read_user():
    """
    将用户读入内存
    :return:
    """
    f = open('user.txt', mode='r', encoding='utf-8')
    for line in f:
        user = line.strip().split(',')
        user_list.append({'username': user[0], 'pwd': user[1], 'total': user[2]})
    f.close()


def check_username(username):
    """
    检查用户名是否重复
    :param username: 用户名
    :return: True or False
    """
    for i in user_list:
        if i['username'] == username:
            return False
    return True


if __name__ == '__main__':
    while True:
        print(prompt_func())
        read_user()
        user_opt = input('选项:')
        if user_opt == '1':
            user_signin()
        elif user_opt == '2':
            user_signup()
        elif user_opt == '3':
            exit('感谢使用购物系统，欢迎下次再来!'.center(30,'*'))
        else:
            print('选项不存在，请重新选择！')

