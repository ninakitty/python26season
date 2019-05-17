#!/usr/bin/env python
# -*- encoding:utf-8 -*-
# Author: Andrew.zhan
# Create by 2019 Apr 13
'''
作业题目：
用函数完成登录注册以及购物车的功能

作业需求:
1，启动程序，用户可选择四个选项：登录，注册，购物，退出。
2，用户注册，用户名不能重复，注册成功之后，用户名密码记录到文件中。
3，用户登录，用户名密码从文件中读取，进行三次验证，验证不成功则退出整个程序。
4，用户登录成功之后才能选择购物功能进行购物，购物功能（就是将购物车封装到购物的函数中）。
5，退出则是退出整个程序。
'''

import json
import sys


def portal(session=False):
    print("[主界面]")
    api_mapping = {
        "1": login,  # 登录方法
        "2": register,  # 注册方法
        "3": shopping,  # 购物方法
        "4": logout,  # 退出方法
    }
    while True:
        # 第一次打开首页时,由于未登录过,所以没有session,不会显示当前用户.
        navigation = "1,登录\n2,注册\n3,购物\n4,退出\n(当前用户 %s)" % (session if session else "[未登录]")
        print(navigation)
        # 获取用户选项, get_user_selected方法用来规避一些错误输入.
        user_selected = get_user_selected(api_mapping, session)
        # 根据用户选项,调用相应的方法.
        session = api_mapping[user_selected](session)


def get_user_selected(api_mapping, session=False):
    while True:
        user_selected = input("请输入编号: ").strip()
        # 这里判断只有当用户输入的为主界面索引号时才会继续进行下一步操作.
        if user_selected in api_mapping:
            # 据题意, 未登录情况不能进入购物页面.
            if not session and user_selected == "3":
                print("请先登录再购物.")
                continue
            break
        print("输入有误,请重新输入.")
    # 返回用户输入的主界面索引号.
    return user_selected


def register(*args):
    print("[用户注册页面]")
    username = None
    while True:
        if not username:
            username = input("请输入用户名: ")
            # 判断用户是否存在. 如果存在就username清空,并continue,重新键入用户名. 反之username=用户键入值
            if username in USERS_INFO:
                username = None
                print("用户已存在,请重新输入.")
                continue
        passwd = input("请输入密码: ")
        confirm = input("请再次输入密码: ")
        # 这里就判断两次密码是否一致,如果不一致则continue. 重新输入两次.
        if passwd != confirm:
            print("两次密码不一致,请确认后再次输入.")
            continue
        break
    # 到这里时, 用户名无冲突, 两次密码一致. 那么将该用户信息加入到全局常量USERS_INFO中. 注册成功.
    USERS_INFO[username] = passwd
    print("注册成功.")
    # 将全局常量 USERS_INFO 保存入db文件.
    save_data()
    # 注册成功后自动跳转到登录页面.
    return login()


def login(*args):
    print("[用户登录页面]")
    # 据题意尝试三次密码后就结束进程. 所以只循环三次.
    for i in range(0, 3):
        remain_chance = 3 - i
        print("请输入用户名与密码(剩余%s机会)" % remain_chance)
        username = input("用户名: ")
        passwd = input("密码: ")
        # 从用户信息常量中判断用户名与密码是否一致.
        if USERS_INFO.get(username) == passwd:
            print("登录成功.")
            return username
    # 如果走到这里,代表登录失败了.那么依题意退出.
    print("尝试错误次数过多,程序退出.")
    logout()


# 这里直接套用上节课作业代码.就不重写了.
def shopping(username=None):
    print("购物页面")
    import operation
    operation.main(username)


def logout(*args):
    sys.exit()


def load_usersinfo():
    global USERS_INFO
    try:
        # 如果文件太大了.就最好使用readline来组合数据.
        with open("usersinfo.txt", 'r', encoding="utf-8") as fp:
            USERS_INFO = json.loads(fp.read())
    except(Exception):
        USERS_INFO = {}


def save_data():
    # 保存与读取数据这里其实主要目的是练习写入与读取文件的操作.
    with open("usersinfo.txt", 'w') as fp:
        fp.write(json.dumps(USERS_INFO))


def main():
    # 获取用户信息,赋值给全局常量USERS_INFO, {"username": "passwd", ...}
    load_usersinfo()
    # 进入首页
    portal()


if __name__ == "__main__":
    main()
