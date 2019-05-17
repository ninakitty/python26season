# 1)，启动程序，首页面应该显示成如下格式：
# #     欢迎来到博客园首页
# #     1:请登录
# #     2:请注册
# #     3:文章页面
# #     4:日记页面
# #     5:评论页面
# #     6:收藏页面
# #     7:注销
# #     8:退出程序
# # 2)，用户输入选项，3~6选项必须在用户登录成功之后，才能访问成功。
# # 3)，用户选择登录，用户名密码从register文件中读取验证，三次机会，
# #         没成功则结束整个程序运行，成功之后，可以选择访问3~6项，访问页面之前，
# #         必须要在log文件中打印日志，日志格式为-->用户:xx 在xx年xx月xx日 执行了 %s函数，
# #         访问页面时，页面内容为：欢迎xx用户访问评论（文章，日记，收藏）页面
# # 4)，如果用户没有注册，则可以选择注册，注册成功之后，可以自动完成登录，然后进入首页选择。
# # 5)，注销用户是指注销用户的登录状态，使其在访问任何页面时，必须重新登录。

# -*- coding:utf-8 -*-
import time

def login():
    #执行登录操作
    count = 0
    while True:
        r_name = input('请输入已注册账号>>>>>>').strip()
        r_pwd = input('请输入已注册密码>>>>>>').strip()
        use_pwd = r_name + ',' + r_pwd + '\n'               #帐号密码拼接
        with open('register',mode='r',encoding='utf-8') as f:
            for i in f:               #读取帐号密码
                if use_pwd == i:      #帐号密码有效性验证
                    ret = i.split(',')
                    print('登录成功')
                    return True,ret[0]    #登录后返回登陆成功标记、用户名
            print('账号或密码不正确')
        if count == 2:                #登录三次失败，返回登陆失败标记False结束整个程序
            return  False,'登录失败'
        else:count += 1

def regiest():
    #注册
    flag = True         #标志位用于结束循环
    while flag:
        l = []           #接收文件中所有帐号信息存入列表，判断帐号唯一性
        r_name = input('注册账号>>>>>>').strip()
        with open('register',mode='r',encoding='utf-8') as f,open('register',mode='a',encoding='utf-8') as f1:
            for i in f:                      #遍历所有帐号密码，并将帐号加入列表l
                s = i.strip().split(',')
                l.append(s[0])
            if r_name not in l and r_name != "":    #判断注册帐号是否唯一和非空
                r_pwd = input('注册密码>>>>>>').strip()
                if r_pwd != "":   #判断密码是否非空
                    use_pwd = r_name + ',' + r_pwd + '\n'
                    f1.write(use_pwd)
                    print('注册成功,已自动登陆')
                    return True,r_name
                else:print('非法字符，请重新输入')
            elif r_name in l:    #判断账号已存在，则直接跳转到登陆
                print('该账号已存在，请输入账号密码登陆')
                ret = login()
                return ret
            else:print('非法字符，请重新输入')

def log(func):
    #日志装饰器
    def inner(*args,**kwargs):
        strtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())      #时间格式化
        with open('log',mode='a',encoding='utf-8') as f:
            f.write('用户: %s %s 执行了 %s函数'% (args[0],strtime,func.__name__) + '\n')    #写入文件，并移动文件指针到下一行开始
        ret = func(*args,**kwargs)
        return print(ret)
    return inner

@log
def article_page(username):
    #文章页面
    return '欢迎%s用户访问文章页面'% username
@log
def diary_page(username):
    #日记页面
    return '欢迎%s用户访问日记页面'% username
@log
def comment_page(username):
    #评论页面
    return '欢迎%s用户访问评论页面'% username
@log
def collect_page(username):
    #收藏页面
    return '欢迎%s用户访问收藏页面'% username


def mian():
    flag = True           # 循环标志位
    login_flag = False    #登陆状态标志位
    username = ''         #用户名局部变量赋值
    while flag:
        print('''欢迎来到博客园首页
1:请登录
2:请注册
3:文章页面
4:日记页面
5:评论页面
6:收藏页面
7:注销
8:退出程序
''')
        chooise = input('请选择要访问页面的序号>>>').strip()
        if chooise.isdigit():
            if chooise == '1':
                ret = login()            #接收登陆函数返回值
                flag = ret[0]            #接收登陆状态，并赋值给循环标记位flag
                login_flag = ret[0]      #接收登陆状态，赋值给登陆标志位
                username = ret[1]        #接收登陆用户名
            elif chooise == '2':
                ret = regiest()
                flag = ret[0]
                login_flag = ret[0]
                username = ret[1]
            elif chooise == '3':
                if login_flag == True:        #判断是否登陆
                    article_page(username)     #已登陆后，取登陆函数返回的用户名变量username传参,执行相应的函数
                else:print('请先进行登录')
            elif chooise == '4':
                if login_flag == True:
                    diary_page(username)
                else:print('请先进行登录')
            elif chooise == '5':
                if login_flag == True:
                    comment_page(username)
                else:print('请先进行登录')
            elif chooise == '6':
                if login_flag == True:
                    collect_page(username)
                else:print('请先进行登录')
            elif chooise == '7':       #重置登陆状态为False
                login_flag = False
            elif chooise == '8':      #改变循环标志位结束整个程序
                flag = False
            else:print('请输入正确的序号')
        else:print('请输入数字')


mian()