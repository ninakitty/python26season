# 作业需求
# 1. 三次重试机会
# 2. 每次输错误时显示剩余错误次数

count =  1
a = 2
while count <= 3:
    Username = input('请输入用户名：')
    Password = int(input('请输入密码：'))
    if Username == 'admin':
        if Password == 123456:
            print('登录成功')
            break
        else:
            print('账号密码错误,剩余错误次数为:',int(a))
    else:
        print('账号密码错误,剩余错误次数为:',int(a))
    count = count + 1
    a = a -1