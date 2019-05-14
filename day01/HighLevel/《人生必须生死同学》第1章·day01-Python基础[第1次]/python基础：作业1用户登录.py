#!/usr/bin/env python

user_name = 'Jeff'
user_password = 'abc'


available_count = 3
error_sum = 0

while available_count > 0:
    user_input_name = input('请输入用户名： ')
    user_input_password = input('请输入密码： ')

    if user_input_name == user_name and user_input_password == user_password:
        print('登录成功')
        break
    else:
        error_sum += 1
        available_count -= 1
        print('用户名或密码错误，请重新输入！','还可输入', available_count ,'次')
        if available_count == 0:
            print('已连续错误三次，程序退出')

