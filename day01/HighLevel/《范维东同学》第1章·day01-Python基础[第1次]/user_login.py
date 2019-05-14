#!/usr/bin/env python

# 登入用户的初始化账号密码为 admin/123456
_user = "admin"
_password = "123456"


# 循环三次，登入成功break直接跳出while循环，登入失败count减1,直到count 小于0为止。
count = 3

while count > 0 :
    user = input("请输入用户名:")
    password = input("请输入密码:")
    if _user == user and _password == password:
        print("登入成功")
        break
    else:
        count = count - 1
        print("登入失败,剩余",count,"次机会")
