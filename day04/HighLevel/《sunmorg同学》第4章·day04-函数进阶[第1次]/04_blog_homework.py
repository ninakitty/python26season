# -*- coding:utf-8 -*-
# Author：sunmorg

import time

login_flag = False
username = ''
userpwd = ''


def print_func():
    """
    打印程序信息
    :return:
    """
    return ('''
欢迎来到博客园首页
    1:请登录
    2:请注册
    3:文章页面
    4:日记页面
    5:评论页面
    6:收藏页面
    7:注销
    8:退出程序''')


def interactive(num):
    """
    执行要用户选择的操作
    :param num:
    :return:
    """
    menu_dic = {
        '1': login,
        '2': register,
        '3': article_web,
        '4': log_web,
        '5': comment_web,
        '6': collection_web,
        '7': logout,
        '8': exit_sys
    }
    if num in menu_dic.keys():
        menu_dic[num]()
    else:
        print("对不起，没有找到该选项！")


def check_login(func):
    """
    装饰器，用来检测登录
    :param func: 传入的方法
    :return: inner 返回被装饰后的方法
    """
    def inner(*args, **kwargs):
        if login_flag:
            result = func(*args, **kwargs)
            return result
        else:
            login()
    return inner


def write_log(func):
    """
    装饰器，用来写日志
    :param func:
    :return:
    """
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("func_log.log", mode="a", encoding="utf-8") as f:
            now_time = time.strftime("%Y-%m-%d %H:%M:%S")
            func_name = func.__name__
            func_log = '用户：%s 在 %s 执行了 %s 函数\n' % (username, now_time, func_name)
            f.write(func_log)
        return result
    return inner


def login():
    global login_flag, username, userpwd
    if login_flag:
        print("您已登入账号 %s ，若需要切换账号请先注销！" % username)
    else:
        login_count = 0
        while not login_flag and login_count < 3:
            login_name = input("请输您的用户名：").strip()
            login_pwd = input("请输入您的密码：").strip()
            with open('register.txt', mode='r', encoding='utf-8') as f:
                for line in f:
                    user_info = line.strip().split(',')
                    if login_name == user_info[0] and login_pwd == user_info[1]:
                        login_flag = True
                        username = login_name
                        userpwd = login_pwd
                        break
            if not login_flag:
                login_count += 1
                print("用户名或密码错误，请重新输入！")
        if login_count == 3:
            exit_prt("您已试完三次机会，程序自动退出！欢迎下次使用！")


def register():
    """
    注册方法
    :return:
    """
    global login_flag, username, userpwd
    if login_flag:
        print("现您已登录用户%s，如需注册请注销当前账户！" % username)
    else:
        right_register = False
        while not right_register:
            register_name = input("请输入要注册的用户名：").strip()
            register_pwd = input("请输入您的密码：").strip()
            re_register_pwd = input("请重新输入您的密码：").strip()
            is_register = False
            with open('register.txt', mode='r', encoding='utf-8') as f:
                for line in f:
                    user_info = line.strip().split(',')
                    if register_name in user_info:
                        is_register = True
                        break
            if is_register:
                print("该用户名不可用，请重新注册！")
            else:
                if register_pwd == re_register_pwd:
                    with open('register.txt', mode='a', encoding='utf-8') as f:
                        f.write("%s,%s\n"%(register_name, register_pwd))
                    right_register = True
                    login_flag = True
                    username = register_name
                    userpwd = register_pwd
                    print("注册成功，现已登入您的账号！")
                else:
                    print("两次密码不一致，请重新注册！")


@check_login
@write_log
def article_web():
    """
    访问文章页
    :return:
    """
    print('欢迎%s用户访问文章页面' % username)


@check_login
@write_log
def log_web():
    """
    访问日记页
    :return:
    """
    print('欢迎%s用户访问日记页面' % username)


@check_login
@write_log
def comment_web():
    """
    访问评论页
    :return:
    """
    print('欢迎%s用户访问评论页面' % username)


@check_login
@write_log
def collection_web():
    """
    访问收藏页
    :return:
    """
    print('欢迎%s用户访问收藏页面' % username)


def logout():
    """
    注销方法
    :return:
    """
    global login_flag, username, userpwd
    if login_flag:
        print("您已成功注销 %s 账户，欢迎下次再来！" % username)
        login_flag = False
        username = ''
        userpwd = ''
    else:
        print("您还未登录，请先登录！")


def exit_sys():
    """
    退出系统方法
    :return:
    """
    exit_prt("再见%s！，下次来的时候会有不一样的收获哦！" % username)


def exit_prt(msg):
    """
    结束程序，并输出信息
    :param msg:
    :return:
    """
    exit(msg.center(30, '*'))


if __name__ == '__main__':
    while True:
        print(print_func())
        chooseNum = input("您想干点啥嘞？请选择吧：").strip()
        interactive(chooseNum)