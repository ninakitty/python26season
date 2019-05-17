#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time

# 默认登陆状态
logined = False

# 创建保存账户密码和日志的文件
def create_file(newfile):
    if not os.path.exists(newfile):
        f = open(newfile,'w')
        f.close()
create_file('log.txt')
create_file('user_ps.txt')

# 定义函数，判断输入账号是否为空，直至不为空
def input_info(data_type,get_data):
    while True:
        get_data = input('请输入%s：'%data_type)
        if len(get_data.strip()) == 0:
            continue
        else:
            break
    return get_data

# 以dict的形式提取数据，用于注册时候判断（user_ps.txt文件里保存了账号和密码）
def get_user_pass(txt):
    user_pwd = {}
    with open(txt,mode='r',encoding='utf-8') as f:
        for n in f:
            for p in [n.strip().split(',')]:
                user_pwd[p[0]] = p[1]
    return user_pwd

# 定义注册
def register():
    global logined
    user_pwd = get_user_pass('user_ps.txt')
    while True:
        user_name=input_info('注册账号','name')
        # 判断注册账号是否存在，已存在的话持续循环
        if user_name in user_pwd.keys():
            print('您输入的账号已存在，请重新输入：')
            continue
        else:
            password = input_info('账号密码', 'passwd')
            confirm_pass = input_info('确认密码','passwd')
            # 判断确认密码和密码是否一致
            if password != confirm_pass:
                print('您输入的确认密码与密码不一致，请重新输入:')
                continue
            else:
                print('恭喜您注册成功，请记住您的注册信息：\n您的账号是:%s\n您的密码是:%s'%(user_name,password))
                logined = True
                break
    # 注册用户保存至文件
    with open('user_ps.txt',mode='a',encoding='utf-8') as f:
        f.write(user_name+ ',' +password+ '\n')

# 日志记录，把print信息重定向至日志文件
def log(func):
    def inner(*args,**kwargs):
        ret = func(*args,**kwargs)
        logfile = open('log.txt',mode = 'a',encoding = 'utf-8')
        print ('%s %s函数被执行了' %(time.strftime('%Y-%m-%d %H:%M:%S'),func.__name__),file=logfile)
        logfile.close()
        return ret
    return inner

#  登陆
def login():
    global logined
    user_pwd = get_user_pass('user_ps.txt')
    # 登陆用户输入连续错误3次将不允许登陆
    count = 1
    while count < 4:
        get_user = input('用户名:')
        get_pawd = input('密码:')
        if get_user not in user_pwd.keys():
            print('账号或密码有误,请重新输入,超过3次将不允许登陆!')
            continue
        else:
        # 根据用户名获取用户密码[user_pwd 字典key获取value]
            password = user_pwd[get_user]
            if get_pawd != password:
                print('账号或密码有误,请重新输入,超过3次将不允许登陆!')
                continue
            else:
                logined = True
                print ('欢迎%s用户登录系统!' %get_user)
                break

# 公共函数
def public(func):
    def inner(*args,**kwargs):
        if logined:
            ret = func(*args,**kwargs)
            return ret
        else:
            login()
    return inner
# 文章页面
@public
@log
def web_page():
    print ('欢迎访问文章页面!' )
# 日志页面
@public
@log
def log_page():
    print ('欢迎访问日志页面!' )
# 评论页面
@public
@log
def comment_page():
    print ('欢迎访问评论页面!' )
# 收藏页面
@public
@log
def collection_page():
    print ('欢迎访问收藏页面!' )
# 注销
@public
@log
def log_out():
    global logined
    logined = False
    print ('您已经注销系统!')

# 定义系统首页信息
def home_page():
    while True:
        print ('''(1) 登陆\n(2) 注册\n(3) 文章页面\n(4) 日志页面\n(5) 评论页面\n(6) 收藏页面\n(7) 注销\n(8) 退出\n''')
        choice_lst = [1,2,3,4,5,6,7,8]
        choice = input_info('您要操作选项', 'choice')
        choice = int(choice)
        if choice in choice_lst:
            if choice == 1:
                login()
                continue
            elif choice == 2:
                register()
                continue
            elif choice == 3:
                web_page()
                continue
            elif choice == 4:
                log_page()
                continue
            elif choice == 5:
                comment_page()
                continue
            elif choice == 6:
                collection_page()
                continue
            elif choice == 7:
                log_out()
            elif choice == 8:
                break

        else:
            choice = input_info('正确的操作选项', 'choice')

# 登陆系统
home_page()














