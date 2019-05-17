'''
作业题目：
模拟博客园登录
    作业需求:
    1)，启动程序，首页面应该显示成如下格式：
        欢迎来到博客园首页
        1:请登录
        2:请注册
        3:文章页面
        4:日记页面
        5:评论页面
        6:收藏页面
        7:注销
        8:退出程序
    2)，用户输入选项，3~6选项必须在用户登录成功之后，才能访问成功。
    3)，用户选择登录，用户名密码从register文件中读取验证，三次机会，
            没成功则结束整个程序运行，成功之后，可以选择访问3~6项，访问页面之前，
            必须要在log文件中打印日志，日志格式为-->用户:xx 在xx年xx月xx日 执行了 %s函数，
            访问页面时，页面内容为：欢迎xx用户访问评论（文章，日记，收藏）页面
    4)，如果用户没有注册，则可以选择注册，注册成功之后，可以自动完成登录，然后进入首页选择。
    5)，注销用户是指注销用户的登录状态，使其在访问任何页面时，必须重新登录。
'''
def mk_file(): #判断文件是否存在,不存在则创建空文件
    if not os.path.exists(register_file):
        f = open(register_file, mode="w", encoding="utf-8")
        f.close()

def get_file_content(): #读取文件内容,返回一个字典
    mk_file()
    with open(register_file, mode="r", encoding="utf-8") as f:
        content = f.read().strip()
        if content != "":
            content = eval(content)
        else:
            content = {}
        return content

def edit_file_content(usr_dic): #修改文件内容
    with open(register_file, mode="w", encoding="utf-8") as f:
        f.write(str(usr_dic))

def login(): #用户登录
    global username
    usr_dic = get_file_content()
    if username != "":  #检查用户是否已登录
        if usr_dic.get(username, {}) != {}:
            if usr_dic[username]["status"] == "logged":
                return
    for i in range(3, 0, -1):  # 三次机会
        while 1:
            print("\033[31;0m请先登录\033[0m".center(50, "*"))
            name = input("Login Username: ").strip()
            if name == "":
                print("\033[31;0m用户名不能为空.\033[0m")
                continue
            pwd = input("Login Password: ").strip()
            if pwd == "":
                print("\033[31;0m密码不能为空.\033[0m")
                continue
            if name in usr_dic:
                if usr_dic[name]["pwd"] == pwd: #验证通过
                    usr_dic[name]["status"] = "logged"
                    username = name
                    edit_file_content(usr_dic)
                    print("\033[32;0m恭喜您,用户名%s登录成功.\033[0m" % name)
                    return
            if i == 1:    #验证失败
                exit("\033[31;0m用户名或密码错误,您的账号已锁住.\033[0m")
            else:
                print("\033[31;0m用户名或密码错误,您还有%d次机会.\033[0m" % (i-1))
                break

def register(): #用户注册
    global username
    while 1:
        name = input("Register Username: ").strip()
        pwd = input("Register Password: ").strip()
        if name != "" and pwd != "": #用户名和密码的合法性
            if len(name) < 3 and len(name) > 30:
                print("\033[31;0m用户名长度为3~30.\033[0m")
                continue

            if len(pwd) < 6 and len(pwd) > 20:
                print("\033[31;0m用户密码长度为6~20.\033[0m")
                continue

            usr_dic = get_file_content()
            if name in usr_dic: #检查用户名是否存在
                print("\033[31;0m注册失败,用户名%s已存在.\033[0m" % name)
                continue
            else:   #不存在,则添加用户名和密码
                usr_dic.setdefault(name, {"pwd": pwd, "status": "logged"})
                edit_file_content(usr_dic)
                username = name
                login()
                print("\033[32;0m恭喜您,账号%s注册成功.\033[0m" % name)
                return
        else:
            print("\033[31;0m用户名和密码不能为空.\033[0m")

def write_log(auth_flag):    #装饰器函数,也是一个闭包函数,记录日志
    def auth(func):
        def record_log():
            if auth_flag:   #需要登录
                login()
            time_lst = time.strftime("%Y %m %d", time.localtime()).split()
            with open(log_file, mode="a", encoding="utf-8") as f: #追加日志
                f.write("用户:%s 在%s年%s月%s日 执行了 %s函数\n" % (username, time_lst[0], time_lst[1], time_lst[2], func.__name__))
            return func()    #调用被装饰函数
        return record_log
    return auth

@write_log(1) # 这里相当于 xx = write_log(1) 和 article_page = xx(artical_page)
def article_page(): #文章页面
    print("\033[32;0m欢迎%s用户访问文章页面.\033[0m".center(50, "*") % username)

@write_log(1)
def diary_page():   #日记页面
    print("\033[32;0m欢迎%s用户访问日记页面.\033[0m".center(50, "*") % username)

@write_log(1)
def comment_page(): #评论页面
    print("\033[32;0m欢迎%s用户访问评论页面.\033[0m".center(50, "*") % username)

@write_log(1)
def collect_page(): #收藏页面
    print("\033[32;0m欢迎%s用户访问收藏页面.\033[0m".center(50, "*") % username)

@write_log(0) #这里相当于 xx = write_log(0) 和 article_page = xx(artical_page)
def logout():   #注销
    global username
    usr_dic = get_file_content()
    usr_dic[username]["status"] = "logout"
    edit_file_content(usr_dic)
    print("\033[32;0m用户%s已成功注销.\033[0m" % username)
    username = ""

import os
import time
menu = ["请登录", "请注册", "文章页面", "日记页面", "评论页面", "收藏页面", "注销", "退出程序"] #菜单列表
register_file = "register" #用户注册文件
log_file = "log"    #日志文件
username = ""   #用户名,默认为空
print("\033[32;0m欢迎%s来到博客园首页\033[0m".center(50, "*") % username)
while 1:
    for k, item in enumerate(menu, 1):  #显示菜单
        if username == "":
            print("%d:%s" % (k, item))
        else:
            if k <= 2:
                continue
            print("%d:%s" % (k, item))

    user_choice = 1 #定义用户选择的菜单序号默认为1
    while 1:    #用户选择菜单序号
        user_choice = input("请输入菜单序号: ").strip()
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice >=1 and user_choice <= len(menu):
                break
            else:
                print("\033[31;0m输入有误,请重新输入菜单序号!\033[0m")
        else:
            print("\033[31;0m输入有误,请重新输入菜单序号!\033[0m")

    if user_choice == 1:    #登录
        login()
    elif user_choice == 2:  #注册
        print("\033[31;0m请先注销.\033[0m") if username != "" else register()
    elif user_choice == 3:  #文章页面
        article_page()
    elif user_choice == 4: #日记页面
        diary_page()
    elif user_choice == 5:  #评论页面
        comment_page()
    elif user_choice == 6: #收藏页面
        collect_page()
    elif user_choice == 7:  #注销
        logout() if username != "" else print("\033[31;0m您还没有登录,不能注销.\033[0m")
    else:   #退出程序
        exit("\033[32;0m退出程序.\033[0m")
