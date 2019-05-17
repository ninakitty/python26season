#!/usr/bin/env python
# -*- encoding:utf-8 -*-
# Author: Andrew.zhan
# Create by 2019 Apr 22
'''
1)，启动程序，首页面应该显示成如下格式：
    欢迎来到博客园首页
    1:请登录
    2:请注册
    3:文章页面
    4:日记页面
    5:评论页面
    6:收藏页面
    7:注销
    8:退出程序
2)，用户输入选项，3~6选项必须在用户登录成功之后，才能访问成功。
3)，用户选择登录，用户名密码从register文件中读取验证，三次机会，
        没成功则结束整个程序运行，成功之后，可以选择访问3~6项，访问页面之前，
        必须要在log文件中打印日志，日志格式为-->用户:xx 在xx年xx月xx日 执行了 %s函数，
        访问页面时，页面内容为：欢迎xx用户访问评论（文章，日记，收藏）页面
4)，如果用户没有注册，则可以选择注册，注册成功之后，可以自动完成登录，然后进入首页选择。
5)，注销用户是指注销用户的登录状态，使其在访问任何页面时，必须重新登录。
'''
import json
import datetime
import sys

SESSION = {}


# 检测登录的装饰器
def check_login(func):
    def inner(*args, **kwargs):
        # 如果没有获取到Session信息那么代表还没有登录过.
        if not SESSION.get("username"):
            login()  # 登录方法内, 成功:写session, 失败:退出进程.
        write_log(func.__name__)   # 写日志
        func(*args, **kwargs)    # 如果走到这里,那么代表必然是验证成功并且写了session的用户.
    return inner


def write_log(func_name):
    now = datetime.datetime.now()    # 获取当前时间点
    # 组装日志信息
    log_record = "用户:{user} 在{year}年{month}月{day}日 {hour}时{minute}分{second}秒 执行了 {func}函数\n".format(**{
        "user": SESSION["username"],
        "year": now.year,
        "month": now.month,
        "day": now.day,
        "hour": now.hour,
        "minute": now.minute,
        "second": now.second,
        "func": func_name,
    })
    # 写入日志文件
    with open("execution.log", 'a', encoding="utf-8") as fp:
        fp.write(log_record)


def load_userdb():
    '''
    该方法会获得USERS_INFO这个常量,如果register.txt内有数据,则读取.
    如果没有数据,则新建.
    USERS_INFO 内为用户的验证信息 数据结构: {username: passwd, ...}
    '''
    global USERS_INFO
    try:
        with open("register.txt", "r", encoding="utf-8") as fp:
            USERS_INFO = json.loads(fp.read())
    except Exception as e:
        USERS_INFO = {}


def save_userdb():
    with open("register.txt", "w", encoding="utf-8") as fp:
        fp.write(json.dumps(USERS_INFO))


# 打印页面信息的方法
def print_info(page_name):
    print("欢迎:%s 用户, 访问[%s]页面." % (SESSION["username"] if SESSION.get("username") else "[未登录]", page_name))


def login():
    load_userdb()    # 获取注册的用户信息, 用户注册信息写在USERS_INFO常量内.
    for i in range(3):
        username = input("请输入用户名: ").strip()
        passwd = input("请输入密码: ")
        if USERS_INFO.get(username) == passwd:      # 验证三次, 成功:写session, 失败:退出进程.
            SESSION["username"] = username
            return True
    quit_system(1)     # 据题意,登录失败直接退出.


def logout():
    SESSION["username"] = False
    print("已注销")


def quit_system(status=0):
    print("进程结束")
    sys.exit(status)


def view_register():
    print_info("注册")
    while True:
        username = input("请输入用户名: ")
        if username in USERS_INFO:
            print("用户名已存在, 请重新输入.")
            continue
        passwd = input("请输入密码: ")
        verify_passwd = input("请确认密码: ")
        if passwd != verify_passwd:
            print("两次密码不一致,请确认后重新输入.")
            continue
        print("注册成功")
        USERS_INFO[username] = passwd
        break
    save_userdb()      # 这里会将USERS_INFO落地.


@check_login
def view_article():
    print_info("文章")


@check_login
def view_diary():
    print_info("日志")


@check_login
def view_discuss():
    print_info("论坛")


@check_login
def view_collector():
    print_info("收藏")


def navigation():
    mapping = {
        "1": {"name": "登录", "func": login},
        "2": {"name": "注册", "func": view_register},
        "3": {"name": "文章", "func": view_article},
        "4": {"name": "日记", "func": view_diary},
        "5": {"name": "评论", "func": view_discuss},
        "6": {"name": "收藏", "func": view_collector},
        "7": {"name": "注销", "func": logout},
        "8": {"name": "退出进程", "func": quit_system},
    }
    while True:
        print_info("首页")
        # for的内容是展示导航信息.
        for index, func_info in mapping.items():
            print("%s: %s" % (index, func_info["name"]))
        user_selected = input("请输入选项: ")
        # 这里获取用户选择,并排除异,
        if user_selected not in mapping:
            print("输入有误,请重新输入.")
            continue
        # 执行对应的方法.
        mapping[user_selected]["func"]()


def main():
    # 获取用户信息,赋值给全局常量USERS_INFO, {"username": "passwd", ...}
    load_userdb()
    # 进入导航页面
    navigation()


if __name__ == "__main__":
    main()
