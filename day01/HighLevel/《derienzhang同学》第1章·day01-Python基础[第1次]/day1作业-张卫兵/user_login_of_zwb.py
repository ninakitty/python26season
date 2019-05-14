#!/usr/bin/env python
# coding: utf-8

"""
Created by zwb on 2018/8/12
"""

i = 1
try_times = 3
user = 'zwb'
passwd = '123456'

while i <= try_times:
    username = input("Please input username：")
    password = input("Please input password：")
    if len(username) == 0 or len(password) == 0:  #判断用户名和密码不为空，为空不作为计数并重新输入
        print("username and password is not allowed to be empty.")
        continue
    elif username == user and password == passwd:
        print("login success")
        break
    else:
        ts = try_times - i
        if ts > 0:  # 如果第三次输入错误就直接跳出循环并提示重试次数过多，程序退出
           print("username or password verification failed, please try again")
           print("remain retry times: {0}".format(ts))
        i += 1
else:
    print("retry too many times, now exit")