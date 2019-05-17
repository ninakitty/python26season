# 1)，启动程序，首页面应该显示成如下格式：
#     欢迎来到博客园首页
#     1:请登录
#     2:请注册
#     3:文章页面
#     4:日记页面
#     5:评论页面
#     6:收藏页面
#     7:注销
#     8:退出程序
# 2)，用户输入选项，3~6选项必须在用户登录成功之后，才能访问成功。
# 3)，用户选择登录，用户名密码从register文件中读取验证，三次机会，
#         没成功则结束整个程序运行，成功之后，可以选择访问3~6项，访问页面之前，
#         必须要在log文件中打印日志，日志格式为-->用户:xx 在xx年xx月xx日 执行了 %s函数，
#         访问页面时，页面内容为：欢迎xx用户访问评论（文章，日记，收藏）页面
# 4)，如果用户没有注册，则可以选择注册，注册成功之后，可以自动完成登录，然后进入首页选择。
# 5)，注销用户是指注销用户的登录状态，使其在访问任何页面时，必须重新登录。
import time
import sys,os
login_times = 3#剩余登陆次数
logined = False #记录登陆状态
userinfo_dic = {}#存放用户名和密码
username = [] #记录当前登陆的用户名
exit_q = False#退出程序
def login_aut(func):
#登陆验证装饰器
#对用户输入的用户名和密码验证，userinfo文件是否存在该用户名和密码
    with open('userinfo.txt', 'r', encoding='utf-8') as f:
        for line in f:
            userinfo_list = line.strip().split(' ')#将文件中的用户名和密码分割成一个列表
            userinfo_dic[userinfo_list[0]] = userinfo_list[1] #将文件中的用户名和密码组成一个字典
    def inner(*args,**kwargs):
        global logined
        global login_times
        global exit_q
        if not logined:
            while login_times>0:
                user_name = input('name>>>').strip()
                user_psd = input('psd>>>').strip()
                if user_name in userinfo_dic and user_psd == userinfo_dic[user_name]:
                    logined = True
                    username.append(user_name)
                    break #登陆成功之后结束循环
                else:
                    login_times -= 1
                    print('账号或密码错误！！剩余重试次数%d'%login_times)
            if login_times == 0:#错误三次时，退出程序
                print('剩余输入次数为0，程序结束！！')
                sys.exit()
        if logined == True:
            ret = func(*args,**kwargs)
            return ret
    return inner

def my_log(func):#记录日志
    def inner(*args,**kwargs):
        str_time = time.localtime()
        my_str_time = time.strftime('%Y-%m-%d %H:%M:%S')
        str_log = username[0]+' '+my_str_time+' '+'运行了'+ func.__name__ + '\n'
        with open('log.txt','a+',encoding='utf-8') as f:
            f.write(str_log) #将函数执行日志记录在log.txt文件中
        ret = func(*args,**kwargs)
        return ret
    return  inner

def login():#登录
    global logined
    global login_times
    while login_times > 0:
        user_name = input('name>>>').strip()
        user_psd = input('psd>>>').strip()
        if user_name in userinfo_dic and user_psd == userinfo_dic[user_name]:
            logined = True
            username.append(user_name)
            print('登陆成功',username)
            break  # 登陆成功之后结束循环
        else:
            login_times -= 1
            print('账号或密码错误！！剩余重试次数%d' % login_times)
    if login_times == 0:#输错三次，结束程序
        print('剩余输入次数为0，程序结束！！')
        sys.exit()

def register():#注册
    global logined,username
    r_name = input('输入想要注册的用户名>>').strip()
    r_psd = input('输入想要注册的密码>>').strip()
    with open('userinfo.txt','a+',encoding='utf-8') as f:
        f.write(r_name+' '+r_psd+'\n')
        print('%s注册成功！！'%r_name)
        logined =True
        username = []#清除登录用户，并将登录用户修改为当前注册用户
        username.append(r_name)
@login_aut
@my_log
def article():
    print('文章页面！！！')

@login_aut
@my_log
def diary():
    print('日记页面！！！')

@login_aut
@my_log
def comment():
    print('评论页面！！！')

@login_aut
@my_log
def collection():
    print('收藏页面！！！')

def exit_func():#退出登录
    global logined
    global username
    username.pop()#删除用户登录状态
    logined = False
    print('退出登录')
def close_func():#结束程序
    print('退出程序')
    sys.exit()

def home_page():
    print('''欢迎来到博客园首页
        1:请登录
        2:请注册
        3:文章页面
        4:日记页面
        5:评论页面
        6:收藏页面
        7:注销
        8:退出程序''')
home_page()
while not exit_q:
    user_choice = input('请输入您的选择>>>').strip()
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice == 1:#用户选择登录
            login()
        elif user_choice == 2:#用户选择注册
            register()
            home_page()
        elif user_choice == 3:#访问文章页面
            article()
        elif user_choice == 4:#访问日记页面
            diary()
        elif user_choice == 5:#访问评论页面
            comment()
        elif user_choice == 6:#访问收藏页面
            collection()
        elif user_choice == 7:#注销登录
            exit_func()
        elif user_choice == 8:#退出程序
            close_func()
        else:
            print('请输入数字1-8中任意一个数字！！！')
    else:
        print('请输入数字！！！')