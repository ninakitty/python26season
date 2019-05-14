username = 'Alan'
password = 123456
count = 1
while count <= 3:
    value_username = input('请输入您的名字: ')
    value_password = int(input('请输入您的密码: '))
    if username == value_username and password == value_password:
        print('登录成功')
        break
    else:
        print('请重新输入')
    count +=1
    if count == 2:
        print('还有二次机会')
    elif count == 3:
        print('最后一次机会')



