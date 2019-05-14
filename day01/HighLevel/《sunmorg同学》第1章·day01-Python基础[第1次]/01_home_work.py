#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：sunmorg

count = 3
user = 'sunmorg'
pwd = '123456'
while True:
    username = input("请输入用户名：")
    passwd = input("请输入密码：")
    if username == user and passwd == pwd:
        print('登入成功！欢迎用户：' + username)
        break
    else:
        count -= 1
        print('用户名或密码错误！请重试，还剩' + str(count) + '次机会！')
        if count == 0:
            print('所剩机会为0，程序退出！')
            break