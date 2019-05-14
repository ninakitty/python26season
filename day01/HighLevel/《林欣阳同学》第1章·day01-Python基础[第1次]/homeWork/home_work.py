user_name = 'admin'
pass_word = 'admin'
i = 3
while i > 0:
    user = input('请输入用户名:')
    passWord = input('请输入密码:')
    #输出正确
    if user == user_name and passWord == pass_word:
        print('登入成功！')
        break
    #输出错误
    else:
        i -= 1
        if i == 0:
            print('用户名或密码错误，请您明天再来！')
            break
        else:
            print('用户名或密码错误，您还有{}机会'.format(i))
