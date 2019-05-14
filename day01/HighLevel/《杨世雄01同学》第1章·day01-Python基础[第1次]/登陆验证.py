#!/usr/bin/env python
#-*- coding:utf-8 -*-
username = 'Mark'
password = '123456'#初始化定义用户名密码
count = 3
while count >0:#判断循环次数
    count -= 1  # 计数
    input_username = input('Please input your username:')
    input_password = input('Please input your password:')
    if input_username == username:#判断用户名是否正确
        if input_password == password:#判断密码是否正确
            print('success login...')
            break
        else:#密码不正确
            print('the password is wrong! you still could try',count,'times!')
    elif input_password == password:#如果用户名正确，判断密码是否正确
        print('the username is wrong, you still could try',count,'times!')
    else:#用户名密码均不正确
        print('the username and the password are wrong! you still could try',count,'times!')
    if count == 0: #判断错误次数，告知退出情况
        print('you have try 3 times, please connact the manager for help!')

