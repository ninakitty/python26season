# !/usr/bin/python
# -*- coding:utf-8 -*-

user = "oldboy"
passwd = "oldboy123"
count = 3

while count > 0:
    username = input('请输入用户名：')
    password = input('请输入密码：')
    if username == user and password == passwd:
        print("验证通过")
        break
    else:
        print('输入有误')
    count = count - 1
    print('剩余错误次数：', count, '次')
