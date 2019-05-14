'''
1. 三次重试机会
2. 每次输错误时显示剩余错误次数
'''

#解题思路
#1、存储正确的用户名和密码，以便于和用户输入进行比对;
#2、存储用户可输入的次数3，每输入一次，可输入次数减1，
#3、利用while循环，当可输入次数大于0时，进行输入用户名和密码的操作；
#4、如果输入用户名正确，再进行输入密码，如果输入密码错误，再次输入密码，直至次数用完；
#5、如果输入用户名错误，再进行输入用户名操作；

#实现代码如下
username = 'liusl'
password = '123456'
chance = 3

while chance > 0:#while循环，判断是否还有可尝试输入的机会
    if username == input('请输入用户名字：'):
        while chance > 0:#while循环，判断是否还有可尝试输入的机会，循环输入密码
            if password == input('请输入密码：'):
                print('登录成功')
                break#跳出输入密码的循环
            else:
                chance = chance-1#密码输入错误，可尝试输入的机会减1
                print('登录失败，剩余' + str(chance) + '机会')
        else:
            print('尝试次数已用完')
        break#跳出输入用户名和密码的循环
    else:
        chance = chance - 1#用户名输入错误，可尝试输入的机会减1
        print('登录失败，剩余' + str(chance) + '机会')
else:
    print('尝试次数已用完')

