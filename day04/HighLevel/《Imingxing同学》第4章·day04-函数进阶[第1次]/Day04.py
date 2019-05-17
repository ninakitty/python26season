#!/usr/bin/env   python3
# -*- utf-8 -*-

'''
1、整理装饰器的形成过程，背诵装饰器的固定格式
'''

# # 首先定义好装饰器,并定义形参接收目标参数；
# # 定义装饰参数，为了通用处理接收的参数，使用*args和**args来使得可以接收任意参数；
# # 然后目标参数接收信息后执行，并将结果返回；
# # 最后通过return将装饰器内容和目标参数的执行结果作为返回值返回。
# def wrapper (fn) :
#     def inner (*args,**kwargs):
#         print("这是装饰之前")   # 在执行目标参数之前要执行的内容
#         set = fn(*args,**kwargs)
#         print("这是装饰之后")   # 在执行目标参数之后要执行的内容
#         return set
#     return inner
#
# # 调用装饰器，可使用@装饰器函数名称或者目标参数=装饰器（目标参数）两种方式调取装饰器；
# @wrapper
#
# # 定义目标函数
# def func():
#     print("这是被装饰的信息")
#
# # 执行目标函数
# func()


'''
2、编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码’
'''
# def wrapper(fn):
#     def inner(*args,**kwargs):
#         print("每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码")
#         ret = fn(*args,**kwargs)
#         return ret
#     return inner
#
# @wrapper
# def func():
#     print("这是目标参数")
#
# func()


'''
3、编写装饰器,在每次执行被装饰函数之后打印一句’每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码’
'''
# def wrapper(fn):
#     def inner(*args,**kwargs):
#         ret = fn(*args,**kwargs)
#         print("每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码")
#         return ret
#     return inner
#
# @wrapper
# def func():
#     print("这是目标参数")
#
# func()

'''
4、编写装饰器,在每次执行被装饰函数之前让用户输入用户名,密码,给用户三次机会,登录成功之后,才能访问该函数.
'''
# def wrapper(fn):
#     def inner(*args,**kwargs):
#         for i in range(3):
#             user = input("请输入用户名：")
#             pwd = input("请输入密码：")
#             if user == "admin" and pwd =="123":
#                 ret = fn(*args, **kwargs)
#                 return ret
#                 break
#             else:
#                 print("用户名/密码错误，请重新输入！")
#     return inner
#
# @wrapper
# def func():
#     print("恭喜你，登录成功！")
#
#
# func()

'''
5、编写装饰器，为多个函数加上认证的功能(用户的账号密码来源于文件,只支持单用户的账号密码,给用户三次机会)，要求登录成功一次，后续的函数都无需再输入用户名和密码
'''
# # 先创建一个密码文件
# with open("./user_list", mode="w", encoding="utf-8") as user_file:
#     user_file.write("用户名\t密码\n")
#     user_file.write("admin\t123\n")
#     user_file.write("admin1\t456\n")
#
# # 定义账号初始状态
# user_status = False
#
# # 定义装饰器内容
# def wrapper(fn):
#     def inner(*args,**kwargs):
#         global user_status
#         if user_status == True:
#             ret = fn(*args, **kwargs)
#             return ret
#         else:
#             count = 0
#             while count < 3:
#                 print(count)
#                 user = input("请输入用户名：")
#                 pwd = input("请输入密码：")
#                 with open("./user_list", mode="r", encoding="utf-8") as file:
#                     a = file.readline()
#                     for i in file:
#                         ii = i.strip().split()
#                         if user == ii[0] and pwd == ii[1]:
#                             user_status = True
#                             ret = fn(*args, **kwargs)
#                             return ret
#                     else:
#                         print("用户名/密码错误，请重新输入！")
#                         count += 1
#         exit()
#     return inner
#
# @wrapper
# def login():
#     print("恭喜您，登录成功！")
#
# @wrapper
# def sign():
#     print("恭喜您，注册成功！")
#
# @wrapper
# def quit():
#     print("退出成功！")
#
# login()
# sign()
# quit()

'''
6、编写装饰器，为多个函数加上认证的功能(用户的账号密码来源于文件,可支持多账号密码)，要求登录成功一次(给三次机会)，后续的函数都无需再输入用户名和密码。
'''
# # 先创建一个密码文件
# with open("./user_list", mode="w", encoding="utf-8") as user_file:
#     user_file.write("用户名\t密码\n")
#     user_file.write("admin\t123\n")
#     user_file.write("admin1\t456\n")
#
# # 定义账号初始状态
# user_info = {}
# user_list = {}
#
# # 定义装饰器内容
# def wrapper(fn):
#     def inner(*args,**kwargs):
#         with open("./user_list", mode="r", encoding="utf-8") as file:
#             a = file.readline()
#             for i in file:
#                 ii = i.strip().split()
#                 user_info.setdefault(ii[0],False)
#                 user_list[ii[0]] = ii[1]
#
#         user = input("请输入用户名：").strip()
#
#         if user in user_info.keys() and user_info[user] == True:
#             ret = fn(*args, **kwargs)
#             return ret
#
#         else:
#             print("该账号未登录,请重新登录!")
#             count = 0
#             while count < 3:
#                 user = input("请输入用户名：").strip()
#                 pwd = input("请输入密码：").strip()
#                 for k,v in user_list.items():
#                     if user == k and pwd == v:
#                         user_info[k] = True
#                         print(user_info)
#                         ret = fn(*args, **kwargs)
#                         return ret
#
#                 else:
#                     print("用户名/密码错误，请重新输入！")
#                     count += 1
#
#     return inner
#
# @wrapper
# def login():
#     print("恭喜您，登录成功！")
#
# @wrapper
# def sign():
#     print("恭喜您，注册成功！")
#
# @wrapper
# def quit():
#     print("退出成功！")
#
# login()
# sign()
# quit()




'''
7、给每个函数写一个记录日志的功能，
功能要求:每一次调用函数之前，要将函数名称，时间节点记录到log的日志中。 所需模块:
import time
struct_time = time.localtime()
print(time.strftime("%Y‐%m‐%d %H:%M:%S",struct_time)) 
'''
# import time
# struct_time = time.localtime()
# t = time.strftime("%Y‐%m‐%d %H:%M:%S",struct_time)
#
# def wrapper(fn):
#     def inner(*args,**kwargs):
#         print(fn.__name__)
#         with open("./logs",mode="a",encoding="utf-8") as log:
#             log.write(t+"\t")
#             log.write(fn.__name__+"\n")
#         ret = fn(*args,**kwargs)
#         return ret
#     return inner
#
# @wrapper
# def func():
#     print("这是第一个函数")
# @wrapper
# def func1():
#     print("这是第二个函数")
# @wrapper
# def func2():
#     print("这是第三个函数")
#
# func()
# func1()
# func2()
# with open("./logs",mode="r") as ll:
#     a = ll.read()
#
# print(a)



'''
作业题目: 模拟博客园登录
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
# import getpass
# import time
#
# operate_time = time.strftime("%Y‐%m‐%d %H:%M:%S", time.localtime())
#
# # 创建密码文件
# with open("./register", mode="w", encoding="utf-8") as user_file:
#     user_file.write("用户名\t密码\n")
#     user_file.write("admin\t123\n")
#     user_file.write("admin1\t456\n")
#
# # 定义账号初始状态
# user_status = {}
# user_pwd = {}
# with open("./register", mode="r", encoding="utf-8") as file:
#     a = file.readline()
#     for i in file:
#         ii = i.strip().split()
#         user_status.setdefault(ii[0], False)
#         user_pwd[ii[0]] = ii[1]
#
# # 创建日志文件
# with open("./logs", mode="w", encoding="utf-8") as log:
#     log.write("用户名\t时间\t操作内容\n")
#
# # 定义装饰器登录认证判断
# def wrapper(fn):
#     def inner(*args, **kwargs):
#         # 这里主要用来获取当前登录用户的用户名，现在还不知道怎么获取。所以只能使用让用户自己录入来代替
#         username = input("请输入用户名：").strip()
#         if user_status[username] == True:
#             with open("./logs", mode="a", encoding="utf-8") as log:
#                 log.write("%s\t在%s\t执行了%s函数\n" % (username, operate_time, fn.__name__))
#             print("欢迎%s用户访问%s页面！" % (username, fn.__name__))
#             ret = fn(*args, **kwargs)
#             start_up()
#             return ret
#         else:
#             print("该账号尚未登录，请重新登录！")
#             login()
#     return inner
#
#
# def login():
#     count = 0
#     while count < 3:
#         username = input("登录用户名：").strip()
#         password = getpass.getpass("登录密码：")
#         if username in user_pwd.keys() and password == user_pwd[username]:
#             user_status[username] = True
#             with open("./logs", mode="a", encoding="utf-8") as log:
#                 log.write("%s\t在%s\t执行了%s函数\n" % (username, operate_time, login.__name__))
#             print("登录成功！")
#             start_up()
#             break
#         elif username not in user_pwd.keys():
#             while True:
#                 a = input("该账号未注册，是否去注册？(y/n)：")
#                 if a.lower() == "y":
#                     sign()
#                 elif a.lower() == "n":
#                     login()
#                 else:
#                     print("输入错误，请重新输入！")
#                     continue
#         else:
#             print("用户名/密码错误，请重新输入！")
#             count += 1
#
#
# def sign():
#     username = input("注册用户名：").strip()
#     if username in user_pwd.keys():
#         print("当前用户名已注册！")
#         sign()
#     else:
#         while True:
#             pwd = getpass.getpass("请输入密码：")
#             enter_pwd = getpass.getpass("请再输入一次：")
#             if pwd != enter_pwd:
#                 print("两次密码输入不一致，请重新输入！")
#                 continue
#             else:
#                 user_status[username] = True
#                 with open("./register", mode="a", encoding="utf-8") as user_file:
#                     user_file.write("%s\t%s\n" % (username, pwd))
#                 with open("./logs", mode="a", encoding="utf-8") as log:
#                     log.write("%s\t在%s\t执行了%s函数\n" % (username, operate_time, sign.__name__))
#                 print("注册成功！")
#                 start_up()
#                 break
#
#
# @wrapper
# def article():
#     print("这是文章页面。")
#
#
# @wrapper
# def diary():
#     print("这是日记页面")
#
#
# @wrapper
# def discuss():
#     print("这是评论页面")
#
#
# @wrapper
# def collection():
#     print("这是收藏页面")
#
#
# def log_off():
#     username = input("请输入要注销的用户：").strip()
#     user_status[username] = False
#     with open("./logs", mode="a", encoding="utf-8") as log:
#         log.write("%s\t在%s\t执行了%s函数\n" % (username, operate_time, log_out.__name__))
#     print("注销成功!")
#     start_up()
#
#
# def log_out():
#     print("退出程序!")
#     exit()
#
#
# menu = ["请登录", "请注册", "文章页面", "日记页面", "评论页面", "收藏页面", "注销", "退出程序"]
# func_list = [login, sign, article, diary, discuss, collection, log_off, log_out]
# menu_list = {}
#
#
# def start_up():
#     for n, m in enumerate(menu):
#         menu_list[n + 1] = m
#     for k, v in menu_list.items():
#         print(k, v, end="\n")
#     while True:
#         user_choose = input("请选择要使用的功能选项:").strip()
#         if user_choose.isdigit():
#             user_choose = int(user_choose)
#             if user_choose in menu_list.keys():
#                 print("访问%s页面" % menu_list[user_choose])
#                 func_list[user_choose -1]()
#
#         else:
#             print("您输入的选项有误,请正确输入!")
#
#
# start_up()