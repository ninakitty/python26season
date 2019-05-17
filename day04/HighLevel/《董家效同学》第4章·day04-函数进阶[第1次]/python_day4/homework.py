#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 全局变量用于判断用户是否登陆
import time
logined = False
user_name =''
def init():
    global  logined
    while True:
        print('''
        欢迎来到博客园首页
        1:请登录
        2:请注册
        3:文章页面
        4:日记页面
        5:评论页面
        6:收藏页面
        7:注销
        8:退出程序
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
            user_login()
        elif user_answer == 2:
            register()
        elif user_answer == 3:
            title_page(user_name)
        elif user_answer == 4:
            diary_page(user_name)
        elif user_answer == 5:
            review_page(user_name)
        elif user_answer == 6:
            collect_page(user_name)
        elif user_answer == 7:
            if logined:
                logout_page(user_name)
                logined = False
            else:
                print("用户还没有登陆，请登陆用户后再选择此项")
        elif user_answer == 8:
            exit(0)
        else:
            print("您输入的内容不是我们的选择范围，请重新输入。")
            continue
def log(func):
    def inner(name,*args,**kwargs):
        ret = func(name,*args,**kwargs)
        f_w = open('log',mode='a')
        f_w.write('%s %s have performed %s \n'%(name,time.strftime('%Y-%m-%d %H:%M:%S'),func.__name__))
        f_w.close()
        return ret
    return inner

def login(func):
    '''
    登陆装饰器函数
    '''
    def inner(*args,**kwargs):
        '''登陆逻辑'''
        global logined
        if not logined:
            user_login()
            ret = func(*args, **kwargs)  # 被装饰的函数
            return ret
        else:
            ret = func(*args, **kwargs)   # 被装饰的函数
            return ret
    return inner

def user_login():
    '''
    登陆模块
    '''
    global  logined
    global  user_name
    print("--------------登陆----------------")
    count = 1
    while True:
        if  count <4:
            name = input("请输入用户名:")
            password = input("请输入密码:")
            #以默认的r模式(可读模式打开文件)
            f_r = open('register')
            for i in f_r:
                info = i.split(' ')
                if name == info[0] and password == info[1].strip():
                    print("--------登陆成功----------")
                    logined = True
                    user_name = name
                    f_r.close()
                    #返回1用于判断是否成功登陆。
                    return 1
            else:
                print('-----用户名或者密码错误------')
                count +=1
                f_r.close()
        else:
            print("你输入密码次数超过限制")
            exit(0)
def register():
    '''
    注册模块
    '''
    print("--------------注册----------------")
    while True:
        name = input("请输入用户名:")
        f_r = open('register')
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
    f_w =open('register',mode='a')
    f_w.write('\n%s' % (user_info) )
    print("您已经注册成功，谢谢")
    f_w.close()


@log
@login
def title_page(name):
    '''
    访问文章界面
    '''
    print('%s 欢迎访问文章界面' %(name))


@log
@login
def diary_page(name):
    '''
    访问日记界面
    '''
    print('%s 欢迎访问日记界面' %(name))

@log
@login
def review_page(name):
    '''
    访问评论界面
    '''
    print('%s 欢迎访问评论界面' % (name))

@login
@log
def collect_page(name):
    '''
    访问收藏界面
    '''
    global  logined
    logined = False
    print('%s 欢迎访问收藏界面' % (name))

@log
@login
def logout_page(name):
    '''
    访问注销界面
    '''
    print('该 %s 已经登出' % (name))

init()