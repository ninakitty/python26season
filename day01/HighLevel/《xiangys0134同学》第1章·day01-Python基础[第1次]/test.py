#!/usr/bin/env python
# -*- coding:utf-8 -*-
#用户登陆,用户登陆三次则提示失败
uname = 'alex'
upass = '123'
i = 1
count = 3
while i <= count:
    name = input('请输入用户名:')
    password = input('请输入密码:')
    #判断用户名、密码是否为空
    if name != '' and password != '':
        #判断输入用户名、密码是否与uname、upass一样
        if name == uname and upass == password:
            print('登陆成功')
            break
        else:
            print('登陆失败,还有'+ str(count-i) + '次机会')
            i += 1
    else:
        print('用户名密码不能为空,重新输入' + '登陆失败,还有'+ str(count-i) + '次机会')
        i += 1
else:
    print('三次输入失败')