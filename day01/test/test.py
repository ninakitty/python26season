n = 0
user = 'admin'
passwd = '123456'
while n <= 3:
    if n == 3:
        print("您输入的错误次数过多，账号冻结，请联系管理员处理！")
        break
        print("1111")
    user1 = input("请输入用户名：")
    if user1 == user:
        passwd1 = input("请输入密码：")
        n = n + 1
        if passwd1 == passwd:
            print("恭喜你，登录成功！")
        else:
            print("输入密码错误，请重新登录！")
    else:
        print("输入用户名错误，请重新登录！")
        n = n + 1
        continue
