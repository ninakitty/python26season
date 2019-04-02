"""
用户登录程序
需求：
    1、三次重试机会
    2、每次重试显示剩余错误次数
"""
userName = 'tom'  # 存储的用户名
passWord = 'jerry'  # 存储的密码

loginCount = 3  # 限制登录次数

nameFlag = False  # 确认登录用户名是否正确

while loginCount:
    if nameFlag:  # 判断用户名是否正确
        loginPassWord = input('请输入您的密码：')  # 要求输入的密码
        if loginPassWord == passWord:  # 判断密码是否相符
            print('登录成功，欢迎光临', loginName)
            break
        else:
            loginCount = loginCount - 1  # 计数次数减1
            if loginCount == 0:
                print("登录次数已用尽！！！")
                break
            print('登录失败，密码错误！剩余重试次数', loginCount)
    else:  # 用户名不正确
        loginName = input('请输入您的用户名：')  # 要求输入的用户名
        # 判断用户名是否相同
        if loginName == userName:
            # 设置用户名输入正确标记
            nameFlag = True
            loginPassWord = input('请输入您的密码：')  # 要求输入的密码
            if loginPassWord == passWord:
                print('登录成功，欢迎光临', loginName)
                break
            else:
                loginCount = loginCount - 1
                if loginCount == 0:
                    print("登录次数已用尽！！！")
                    break
                print('登录失败，密码错误！剩余重试次数', loginCount)
        else:  # 用户名不相符
            loginCount = loginCount - 1
            if loginCount == 0:
                print("登录次数已用尽！！！")
                break
            print('登录失败，用户名错误！剩余重试次数', loginCount)
