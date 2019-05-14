#-*-coding:utf-8-*-
__author__ = 'dengpeng'
#定义用户名和密码
u_name='dengpeng'
p_word='oldboy-123'
#定义重试次数
count=3
while True:
    #输入用户名密码
    username = input("输入用户名：")
    password = input("输入密码：")

    #判断用户名正确
    if username==u_name:

    #密码正确，打印登录成功，退出循环
        if  password==p_word:
            print("登录成功")
            break
        else:
    #密码不对，重试次数次数为0时，退出循环
            if count==0:
                print("已达到最大重试次数，账号已锁定，请稍后再试！")
                break
    # 用户名正确，密码不对，次数减1
            else:
                print("密码错误，还可输入%s次，请重新输入" % count)
                count -= 1

    else:
        #用户名不存在时，打印用户名不存在，重新输入
        print("用户名不存在，请重新输入！")