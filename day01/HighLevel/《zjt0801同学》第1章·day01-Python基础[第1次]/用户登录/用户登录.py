username = 'zoujitao'
password = '123456'
count = 3
while count > 0:
    name = input('请输入你的账户：')
    if name == username:
        paword = input('请输入你的密码：')
        if paword == password:
            print('登录成功')
            exit(0)
        else:
            count = count - 1
            if count == 0:
                print('账户名或者密码错误，你已经没有机会了，game over...')
            else:
                print('账户名或者密码错误，你还有%s机会' % (count))
    else:
        count = count - 1
        if count == 0:
            print('账户名或者密码错误，你已经没有机会了，game over...')
        else:
            print('账户名或者密码错误，你还有%s机会' % (count))