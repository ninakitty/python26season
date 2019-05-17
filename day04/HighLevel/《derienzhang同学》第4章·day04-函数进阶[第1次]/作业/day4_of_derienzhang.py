#!/usr/bin/env python
# coding: utf-8

"""
Created by zwb on 2018/9/10

1. 启动程序时，首页显示msg信息;
2. 3~6需要经过用户身份验证;
3. 用户注册则会将相关账号和密码信息存入register.txt, 注册时会判断用户名是否已存在，如已存在则提示并注册失败;
4. 用户只有三次验证机会，账户信息从register.txt中获取，验证不通过退出程序，验证通过后会记录登录状态，进入其他页面不需要再次验证;
5. 访问页面时会输出作业要求内容，并进行下一次菜单选择；
6. 每一次执行各种功能函数会记录要求格式日志到文件operate.log;
7. 注销用户是去掉用户登录状态，下次进入其他页面需要再次登录验证;
8. 用户选择退出程序时，直接退出本程序;

"""

import time
import os
import sys


filename = 'register.txt' #定义账户信息存放文件

#用户登录验证
def verify(dic):
    i = 1
    try_times = 3  #3次重试机会

    while i <= try_times:
        username = input("Please input username：")
        password = input("Please input password：")
        if len(username) == 0 or len(password) == 0:
            print("username and password is not allowed to be empty.")
            continue
        elif dic.get(username, 0) == password:
            print("login success")
            global flag  #设置全局登录状态
            flag = 1
            global user #记录登录用户
            user = username
            break
        else:
            ts = try_times - i
            if ts > 0:
                print(
                    "username or password verification failed, please try again")
                print("remain retry times: {0}".format(ts))
            i += 1
    else:
        print("retry too many times, now exit")
        return -1  #如果验证失败，则返回-1


#从文件中获取用户账户信息
def acquire_account():
    dic = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip('\n')
            if not line:
                continue
            else:
                username = line.split(",")[0]
                password = line.split(",")[1]
                if username in dic:
                    continue
                else:
                    dic[username] = password
    return dic


#用户登录装饰器
def login(func):
    dic = acquire_account()  #从文件中获取账户名和密码信息
    def inner(*args, **kwargs):
        if flag == 0:
            res = verify(dic)  #获取验证结果
            if res == -1:
                return "登录失败"
        ret = func(*args, **kwargs)
        return ret
    return inner


#记录日志到文件
def writelog(logname, line):
    with open(logname, 'a', encoding='utf-8') as f:
        f.write("\n{0}".format(line))


#日志记录装饰器
def log(func):
    logname = "operate.log"  #记录日志文件
    def inner(*args, **kwargs):
        struct_time = time.localtime()
        ret = func(*args, **kwargs)
        now = time.strftime("%Y-%m-%d %H:%M:%S",struct_time)
        line = "{0} {1} 执行了函数: {2}".format(now, user, func.__name__)
        writelog(logname, line)
        return ret
    return inner


#获取对应执行函数名
def acquire_func(items, item_list, choice):
    func = items[item_list[int(choice)-1]]  #获取函数名
    return func

#注册账户入库
def writeaccount(filename, *args):
    username = args[0]
    password = args[1]
    bak = "{0}_bak".format(filename)
    global user
    user = username
    with open(filename,mode='r', encoding='utf-8') as f1,open(bak, mode='w',
                                                              encoding='utf-8') as f2:
        tag = 0
        for line in f1:
            if username in line.split(","):  #判断用户名存在，则返回注册失败
                print("此用户名已存在")
                ret = "{0}注册失败".format(username)
                tag = 1
                break
            f2.write(line)
        if tag == 0:
            line = ','.join(args)
            f2.write('\n{0}'.format(line))
    if tag == 0:  #只有当注册成功才操作文件覆盖
        os.remove(filename)
        os.rename(bak, filename)
        ret = "注册成功"
        global flag
        flag = 1
    return ret

@login
@log
def login_action():
    return "登录成功"

@log
def register():
    username = input("Please input username：")
    password = input("Please input password：")
    info = [username, password]
    ret = writeaccount(filename, *info)
    return ret

@login
@log
def article():
    return "欢迎{0}用户访问文章页面".format(user)

@login
@log
def diary():
    return "欢迎{0}用户访问日记页面".format(user)

@login
@log
def comment():
    return "欢迎{0}用户访问评论页面".format(user)

@login
@log
def collect():
    return "欢迎{0}用户访问评论页面".format(user)

@log
def logout():
    global flag
    flag = 0
    return "成功注销"
#    msg()

@log
def exit():
    return "退出程序"

# 首页信息, 并展示各个页面的输出结果
def msg():
    items = {
        "请登录":    "login_action",
        "请注册":    "register",
        "文章页面":   "article",
        "日记页面":   "diary",
        "评论页面":   "comment",
        "收藏页面":   "collect",
        "注销":      "logout",
        "退出程序":   "exit"
    }
    msg = "\n\n欢迎来到博客园首页"
    i = 1
    item_list = []  #后续根据用户选择序号，在items中定位执行函数
    for k in items:  #3.6以后字典是有序的
        msg += "\n{0}:{1}".format(i, k)
        item_list.append(k)
        i += 1
    print(msg)
    choice = input("请输入您的操作选项序号： ")
    func = acquire_func(items, item_list, choice)
    func = eval(func)  #获取执行函数名
    ret = func()
    if ret is not None:
        print("\n\n{0}".format(ret))
        if ret == "登录失败" or ret == "退出程序":
            global go_tag  #退出程序的标记位
            go_tag = False


if __name__ == '__main__':
    flag = 0   #用户登录状态标记位
    go_tag = True  #是否退出程序标记位
    user = "guest"  #访客用户名
    while go_tag:
        msg()
