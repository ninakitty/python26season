# -*- encoding:utf-8 -*-
count=0
while count< 3:
    username = input("请输入账号：")
    password = input("请输入密码：")
    if username=="jiaodian" and password=="123456":
        print("登录成功")
        # continue
        break
    else:
        if (2-count) == 0:
            print("连续登录3次失败，账户被锁，请联系管理员。")
        else:
            print("账号或密码错误，还有"+str(2-count)+"次尝试机会")
        count = count + 1





