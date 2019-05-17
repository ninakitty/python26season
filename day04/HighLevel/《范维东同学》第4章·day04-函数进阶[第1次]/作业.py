#!/usr/bin/nev python
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

"""导入Time模块"""
import time

"""首页信息"""
index_info = """
        欢迎来到博客园首页
    1:请登录
    2:请注册
    3:文章页面
    4:日记页面
    5:评论页面
    6:收藏页面
    7:注销
    8:退出程序

"""

"""日志模块"""
def logs(func):
    def inner(*args,**kwargs):
        ret = func(*args,**kwargs)
        date = time.strftime( '%Y-%m-%d %H:%M:%S')
        print("%s:"% user_login + date)
        return ret
    return inner

"""登入装饰器"""
def login_decorator(func):
    def inner(*args,**kwargs):
        if status == True:
            ret = func(*args,**kwargs)
            return ret
        else:
            login_info()
            ret = func(*args,**kwargs)
            return ret
    return inner

"""用户登入模块"""
user_login = False
status = False
def login_info():
    global user_login
    global status
    if status == True:
        print("已有用户，请先注销！")
    else:
        for count in range(2,-1,-1):
            user = input("Input UserName:")
            password = input("Input Password:")
            with open("register",mode="r",encoding="utf-8") as f:
                for i in f:
                    if i.split(",")[0].strip() == user and i.split(",")[1].strip() == password :
                        print("hello,登入成功！")
                        user_login = i.split(",")[0].strip()
                        status = True
                        return
                else:
                    print("账号密码错误,请重新输入!")
                    print("您当前剩余%s次机会！" % count)
        return

"""用户注册模块"""
def register():
    print("欢迎注册博客园!")
    user = input("Input UserName:")
    password = input("Input Password:")
    with open("register", mode="r", encoding="utf-8") as f:
        for i in f:
            if i.split(",")[0].strip() == user:
                print("用户已被注册！")
                return
    with open("register", mode="a", encoding="utf-8") as f:
        f.write(user + "," + password + "\n")
    print("hello，注册成功！")

"""注销用户"""
def cancellation():
    global user_login
    global status
    user_login = 0
    status = False
    print("用户已注销！")

"""文章页面"""
@logs
@login_decorator
def article_info():
    print("文章页面")

"""日记页面"""
@logs
@login_decorator
def diary_info():
    print("日记页面")

"""评论页面"""
@logs
@login_decorator
def comment_info():
    print("评论页面")

"""收藏页面"""
@logs
@login_decorator
def collection_info():
    print("收藏页面")

"""主程序"""
def run():
    print(index_info)
    while True:
        option = input("请输入您想要选择的选项[1-8] 打印首页[9]:")
        if option.isdigit():
            option = int(option)
            if option == 1:
                login_info()
            elif option == 2:
                register()
            elif option == 3:
                article_info()
            elif option == 4:
                diary_info()
            elif option == 5:
                comment_info()
            elif option == 6:
                collection_info()
            elif option == 7:
                cancellation()
            elif option == 8:
                print("您退出了整个程序！")
                exit()
            elif option == 9:
                print(index_info)
            else:
                print("您输入的有误，请按照要求输入[1-8] 打印首页[9]:")
        else:
            print("您输入的有误，请按照要求输入[1-8] 打印首页[9]:")

"""程序开始"""
run()