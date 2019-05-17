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

logined = False   #登录验证

def log(func):
    #记录用户访问日志
    def inner(*args,**kwargs):
        ret = func(*args,**kwargs)
        with open('log','a+',encoding='utf-8') as f:
            f.write('%s %s %s  被执行了\n'%(args,time.strftime('%Y-%m-%d %H:%M:%S'),func.__name__))
        return ret
    return inner

def check_login(func):
    # 检查用户访问权限
    def inner(*args, **kwargs):
        if logined:
            ret = func(*args,**kwargs)
            return ret
        else:
            print("请先登录".center(20,'-'))
    return inner

def create_user(username,password):
    #注册用户
    global logined
    print('注册界面'.center(20, '-'))
    with open('register', 'a+', encoding='utf-8') as f:
        for i in range(3):
            re_pw = input('请再次输入您的密码：').strip()
            if re_pw == password:
                f.write(username + ':' + password + '\n')
                logined = True
                return True
            else:
                print('密码不一致，请重新输入密码')
    return False

def user_login(username,password):
    #登录用户
    global logined
    print('登录界面'.center(20,'-'))
    with open('register', 'a+', encoding='utf-8') as f:
        f.seek(0)
        users = {}
        for line in f:
            v = line.strip().split(':')
            users[v[0]] = v[1]
            if username in users and password == users[username]:
                logined = True
                return True
    return False

def user_exist(username):
    #检查用户是否已存在
    with open('register', 'a+', encoding='utf-8') as f:
        f.seek(0)
        user = {}
        for line in f:
            v = line.strip().split(':')
            user[v[0]] = v[1]
            if username in user:
                return True
            else:
                return False

@check_login
@log
def page(username):
    print('欢迎%s访问文章页面'.center(30,'-')%(username))

@check_login
@log
def diary(username):
    print('欢迎%s访问日记页面'.center(30,'-')%(username))

@check_login
@log
def comment(username):
    print('欢迎%s访问评论页面'.center(30,'-')%(username))

@check_login
@log
def favorites(username):
    print('欢迎%s访问收藏页面'.center(30,'-')%(username))

def logout(username):
    global logined
    print('%s 已注销'.center(20,'-')%(username))
    logined = False

def quit():
    print('退出成功'.center(20, '-'))
    exit()

def start():
    #主程序
    while True:
        print('欢迎来博客园\n 1:登录\n 2:注册\n 3:文章页面\n 4:日记页面\n 5:评论页面\n 6:收藏页面\n 7:注销\n 8:退出')
        choice = input('请输入您的选择：').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice < 9:
                if choice == 1:   #登录
                    for i in range(3):
                        username = input("请输入用户名：")
                        password = input("请输入密码：")
                        is_login = user_login(username, password)
                        if is_login:
                            print(username, 'welcome to blog')
                            break
                        else:
                            print("无此用户或密码有误，请再次输入用户名和密码")
                elif choice == 2:  #注册
                    for i in range(3):
                        username = input("请输入用户名：")
                        password = input("请输入密码：")
                        is_exist = user_exist(username)
                        if is_exist:
                            print("该用户已存在，请重新输入其他用户名")
                        else:
                            result = create_user(username, password)
                            if result:
                                print('%s 注册成功' % (username))
                                break
                            else:
                                print("输入超出次数，注册失败")
                elif choice == 3:
                    page(username)
                elif choice == 4:
                    diary(username)
                elif choice == 5:
                    comment(username)
                elif choice == 6:
                    favorites(username)
                elif choice == 7:
                    logout(username)
                elif choice == 8:
                    quit()
            else:
                print('已超过所选范围，请重新输入1-8的数字')
        else:
            print('您输入有错，请重新输入1-8的数字')
start()
