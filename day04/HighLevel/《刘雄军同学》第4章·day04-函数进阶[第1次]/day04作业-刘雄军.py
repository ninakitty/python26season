# -*- coding: utf-8 -*-
# 作业题目: 模拟博客园登录
#
# 作业需求:
#
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
status_dic = {
                'username': None,
                'status': False
             }

flag1 = True

def login(*args,**kwargs):      #定义登录函数login
    count = 0
    while count < 3:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        with open('register',encoding='utf-8') as f1:
            for line in f1:
                line_lst = line.strip().split()
                if username == line_lst[0] and password == line_lst[1]:
                    print('登录成功')
                    status_dic['username'] = username
                    status_dic['status'] = True
                    return True
            else:
                print('输入不正确，请重新输入,还剩%s机会' % (2-count))
                if count == 2: return Quit()
            count += 1

def register(*args, **kwargs):
    flag = True
    while flag:
        username = input('请输入要注册的用户名:')
        f1 = open('register',encoding='utf-8')
        for i in f1:
            if username in i:
                print('用户名重复,请重新输入')
                f1.close()
                break
        else:
            f1.close()
            password = input('请输入要注册的密码:').strip()
            f2 = open('register',mode='a',encoding='utf-8')
            f2.write('\n{}\t{}'.format(username, password))
            f2.close()
            print('恭喜你,注册成功!')
            status_dic['username'] = username
            status_dic['status'] = True
            return True

def wrapper(func):
    def inner(*args,**kwargs):
        if status_dic['status']:
            ret = func(*args,**kwargs)
            return ret
        else:
            print('请先进行登录!')
            if login():
                ret = func(*args, **kwargs)
                return ret
    return inner

def log_record(func):
    def inner(*args,**kwargs):
        struct_time = time.localtime()
        time_now = time.strftime("%Y-%m-%d %H:%M:%S",struct_time)
        with open('log_func','a',encoding='utf-8') as f1:
            f1.write('用户:%s 在%s 执行了 %s函数\n'%(status_dic['username'],time_now,func.__name__))
        ret = func(*args,**kwargs)
        return ret
    return inner

@wrapper
@log_record
def article():
    print('欢迎%s访问文章页面' % status_dic['username'])

@wrapper
@log_record
def diary():
    print('欢迎%s访问日记页面' % status_dic['username'])

@wrapper
@log_record
def comment():
    print('欢迎%s访问评论页面' % status_dic['username'])

@wrapper
@log_record
def favorite():
    print('欢迎%s访问收藏页面' % status_dic['username'])

def login_out():    #注销函数
    status_dic['username'] = None
    status_dic['status'] = False
    print('注销成功')

def Quit():
    global flag1
    flag1 = False
    return flag1

choice_dict = {
                1: login,
                2: register,
                3: article,
                4: diary,
                5: comment,
                6: favorite,
                7: login_out,
                8: Quit
               }


while flag1:
    msg = '''
    欢迎来到博客园首页
    1:请登录
    2:请注册
    3:文章页面
    4:日记页面
    5:评论页面
    6:收藏页面
    7:注销
    8:退出程序
    '''
    print(msg)
    choice = input('请输入您选择的序号:').strip()
    if choice.isdigit():
        choice = int(choice)
        if 0 < choice <= len(choice_dict):
                choice_dict[choice]()
        else:
            print('输入错误，请重新输入')

    else:
        print('您输入的数字不正确，请重新输入。')

