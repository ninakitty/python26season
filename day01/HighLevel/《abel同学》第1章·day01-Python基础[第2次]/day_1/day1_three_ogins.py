#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Abel He

# 用户名,密码
user_name = "abel"
user_password = "abel123"

# 可尝试次数
counter = 3
while counter > 0:
    name = input("请输入用户名>>>")
    password = input("请输入密码>>>")
    # 每成功输入一次用户名和密码,减少一次可登陆次数
    counter -= 1
    if name == user_name and password == user_password:
        print("\nWelcome To The World Of Python ！！！！")
        break
    # 为了0次时不打印可尝试次数
    if counter == 0:
        continue
    else:
        print("\n用户名或密码错误,请再次输入,剩余尝试次数 %s 次\n" % counter)
else:
    print("\n用户名或密码错误次数过多，禁止登陆！")
