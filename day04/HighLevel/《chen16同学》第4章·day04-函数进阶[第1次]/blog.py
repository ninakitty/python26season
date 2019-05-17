# -*- coding:utf-8 -*-
# !/usr/bin/python3

# 1)，启动程序，首页面应该显示成如下格式：
#     欢迎来到博客园首页
#     1:请登录
#     2:请注册
#     3:文章页面
#     4:日记页面
#     5:评论页面
#     6:收藏页面
#     7:注销
#     8:退出程序
# 2)，用户输入选项，3~6选项必须在用户登录成功之后，才能访问成功。
# 3)，用户选择登录，用户名密码从register文件中读取验证，三次机会，
#         没成功则结束整个程序运行，成功之后，可以选择访问3~6项，访问页面之前，
#         必须要在log文件中打印日志，日志格式为-->用户:xx 在xx年xx月xx日 执行了 %s函数，
#         访问页面时，页面内容为：欢迎xx用户访问评论（文章，日记，收藏）页面
# 4)，如果用户没有注册，则可以选择注册，注册成功之后，可以自动完成登录，然后进入首页选择。
# 5)，注销用户是指注销用户的登录状态，使其在访问任何页面时，必须重新登录。

import time

user = {
    'username': None,
    'login': False
}

def login(*args, **kwargs):           #定义登录用函数
    count = 2
    while count > -1:
        username = input("请输入用户名：").strip()
        password = input("请输入登录密码：").strip()
        with open('register.txt', encoding='utf-8') as f:
            for line in f:
                line_lst = line.strip().split()
                if username == line_lst[0] and password == line_lst[1]:
                    print("登录成功")
                    user['username'] = username
                    user['login'] = True
                    return  True
            else:
                if count == 0:
                    print('输入有误，程序退出')
                    quit()
                else:
                    print('输入的信息有误，请重新输入，剩余 %s次' % count)
            count -= 1

def register(*args, **kwargs):       #定义注册用函数
    while True:
        username = input("请输入注册的用户名：").strip()
        check = open('register.txt', encoding='utf-8')
        for line in check:           #遍历判断用户名是否重复
            if username in check:
                print("用户名已存在，请重新输入")
                check.close()
                break
            else:        #如不重复，关闭文件重新打开并追加注册信息
                check.close()
                password = input("请输入密码").strip()
                insert = open('register.txt', mode='a', encoding='utf-8')
                insert.write('\n{}\t{}'.format(username, password))
                insert.close()
                print("注册成功，登录中...")
                user['username'] = username
                user['login'] = True
                return True

def wrapper(func):      #定义一个装饰器
    def inner(*args, **kwargs):
        if user['login']:
            ret = func(*args, **kwargs)
            return ret
        else:
            print('欢迎登录'.center(20, '-'))
            if login():
                ret = func(*args, **kwargs)
                return ret
    return inner

def log(func):         #定义日志用函数
    def inner(*args, **kwargs):
        with open('log.log', mode='a', encoding='utf-8') as f:
            f.write('用户:%s 在%s 执行了 %s函数\n' % (user['username'], time.strftime("%Y-%m-%d %H:%M:%S"), func.__name__))
        ret = func(*args, **kwargs)
        return ret
    return inner

def logout():        #定义注销用函数
    if user['username'] is not None:
        user['username'] = None,
        user['login'] = False
        print('注销成功')
    else:
        print('未登录，注销失败')

def quit():        #定义退出程序用函数
    global flag
    flag = False
    return flag

def index():     #定义首页显示用函数
    print(
'''
欢迎来到博客园首页

 1: 请登录
 2: 请注册
 3: 文章页面
 4: 日记页面
 5: 评论页面
 6: 收藏页面
 7: 注销
 8: 退出程序
'''
    )

@wrapper
@log
def article():
    print('欢迎 %s 访问文章页面' % user['username'])

@wrapper
@log
def diary():
    print('欢迎 %s 访问日记页面' % user['username'])

@wrapper
@log
def comment():
    print('欢迎 %s 访问评论页面' % user['username'])

@wrapper
@log
def favorites():
    print('欢迎 %s 访问收藏页面' % user['username'])

flag = True

dict = {1: login, 2: register, 3: article, 4: diary, 5: comment, 6: favorites, 7: logout, 8: quit}

while flag:   #循环执行程序
    index()
    choice = input("请选择操作：").strip()
    if choice.isdigit():
        choice = int(choice)
        if 0 < choice <= len(dict):
                dict[choice]()
        else:
            print('输入有误，请重新输入')
    else:
        print('输入有误，请重新输入。')