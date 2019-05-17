'''
1、整理装饰器的形成过程，背诵装饰器的固定格式
'''
'''开放封闭原则:为了保证程序的稳定性,和功能的可开放性,在不修改目标函数源代码和调用方式的情况下,对目标函数增加新功能'''
# def wrapper(func):  #1.装饰器函数 3.调用装饰器函数
#     def inner(*args, **kwargs):  #4.内部函数(动态位置形参,动态关键字形参) 7.调用装饰器内部函数
#         print("调用被装饰函数前的操作.")   #8.调用被装饰函数前增加的代码块
#         ret = func(*args, **kwargs)     #9.调用被装饰函数(不定位置实参,不定关键字实参)
#         print("调用被装饰函数后的操作.")   #13.调用被装饰函数后增加的代码块
#         return ret  #14.被装饰函数的返回值
#     return inner    #5.返回装饰器内部函数名
#
# @wrapper    # 2.调用装饰器函数,这里等同于 fn = wrapper(fn) 语法糖 10.调用被装饰函数
# def func():    #被装饰函数(动态位置参数,动态关键字参数)
#     print("func is running...")  #11.执行被装饰函数体
#
# func()   #6.调用被装饰函数

'''
2、编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需
求添加代码’
'''
# def wrapper(func):  #装饰器函数
#     def inner(*args, **kwargs): #装饰器内部函数
#         print("每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码")
#         return func(*args, **kwargs) #调用被装饰函数
#     return inner    #返回装饰器函数内部函数名
#
# @wrapper    # 这里等同于fn = wrapper(fn)
# def func():    #被装饰函数
#     print("func is running...")
#
# func()   #调用函数

'''
3、编写装饰器,在每次执行被装饰函数之后打印一句’每次执行完被装饰函数之后都得先经过这里,这里根据
需求添加代码’
'''
# def wrapper(func):  #装饰器函数
#     def inner(*args, **kwargs): #装饰器内部函数
#         ret = func(*args, **kwargs) #调用被装饰函数
#         print("每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码")
#         return ret  #返回被装饰函数的返回值
#     return inner    #返回装饰器函数内部函数名
#
# @wrapper    # 这里等同于fn = wrapper(fn)
# def func():    #被装饰函数
#     print("func is running...")
#
# func()

'''
4、编写装饰器,在每次执行被装饰函数之前让用户输入用户名,密码,给用户三次机会,登录成功之后,才能访
问该函数.
'''
# def user_auth(func):  #装饰器函数
#     def inner(*args, **kwargs):  #装饰器内部函数
#         for i in range(3, 0, -1):
#             while 1:
#                 print("\033[31;0m请先登录\033[0m".center(50, "*"))
#                 name = input("Username: ").strip()
#                 if name == "":
#                     print("\033[31;0m用户名不能为空.\033[0m")
#                     continue
#                 pwd = input("Password: ").strip()
#                 if pwd == "":
#                     print("\033[31;0m密码不能为空.\033[0m")
#                     continue
#                 if name == userinfo_dic["username"] and pwd == userinfo_dic["pwd"]:  #认证通过
#                     print("\033[32;0m登录成功.\033[0m")
#                     return func(*args, **kwargs)  #调用目标函数
#                 else:   #认证失败
#                     if i == 1:
#                         exit("\033[31;0m用户名或密码错误.程序自动退出.\033[0m")
#                     else:
#                         print("\033[31;0m用户名或密码错误.您还有%s次机会哦.\033[0m" % (i-1))
#                         break
#
#     return inner    #返回装饰器函数内部函数名
#
# @user_auth    # 这里等同于fn = wrapper(fn)
# def func():    #目标函数
#     print("func is running...")
#
# userinfo_dic = {"username": "alex", "pwd":"123456"} #保存用户名和密码
# func()

'''
5、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,只支持单用户的账号密码,给用
户三次机会），要求登录成功一次，后续的函数都无需再输入用户名和密码
'''
# def user_auth(func):  #装饰器函数
#     def inner(*args, **kwargs): #装饰器内部函数
#         global auth_flag
#         if auth_flag: #已登录
#             return func(*args, **kwargs)  # 调用目标函数
#
#         for i in range(3, 0, -1): #三次认证机会
#             while 1:
#                 print("\033[31;0m请输入正确的用户名和密码\033[0m".center(50, "*"))
#                 name = input("Username: ").strip()
#                 if name == "":
#                     print("\033[31;0m用户名不能为空.\033[0m")
#                     continue
#                 pwd = input("Password: ").strip()
#                 if pwd == "": #用户名和密码不能为空
#                     print("\033[31;0m密码不能为空.\033[0m")
#                     continue
#                 user_dic = {}
#                 with open(filename, mode="r", encoding="utf-8") as f: #读文件userinfo.txt
#                     user_dic = eval(f.read().strip())   #获取文件的内容,转化为字典类型
#
#                 if name == user_dic["username"] and pwd == user_dic["pwd"]: #认证通过
#                     auth_flag = 1
#                     print("\033[32;0m登录成功.\033[0m")
#                     return func()  # 调用目标函数
#                 else:   #认证失败
#                     if i == 1:
#                         exit("\033[31;0m用户名或密码错误.程序自动退出.\033[0m")
#                     else:
#                         print("\033[31;0m用户名或密码错误.您还有%s次机会哦.\033[0m" % (i-1))
#                         break
#     return inner    #返回装饰器函数内部函数名
#
# @user_auth    #这里等同于fn1 = wrapper(fn1)
# def func1():
#     print("func1 is running...")
#
# @user_auth  #这里等同于fn2 = wrapper(fn2)
# def func2():
#     print("func2 is running...")

# auth_flag = 0 #用户登录标记 0未登录,1已登录
# filename = "userinfo.txt"
# func1()
# func2()

'''
6、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,可支持多账号密码），要求登
录成功一次（给三次机会），后续的函数都无需再输入用户名和密码。
'''
# def user_auth(func):  #装饰器函数
#     def inner(*args, **kwargs): #装饰器内部函数
#         global login_flag
#         if login_flag: #用户已登录
#             return func(*args, **kwargs)  # 调用目标函数
#
#         user_dic = {}
#         with open(filename, mode="r", encoding="utf-8") as f: #获取用户文件内容,转换为字典
#             user_dic = eval(f.read().strip())
#         for i in range(3, 0, -1): #三次机会
#             while 1:
#                 print("\033[31;0m请先登录\033[0m".center(50, "*"))
#                 name = input("Login Username: ").strip()
#                 if name == "":
#                     print("\033[31;0m用户名不能为空.\033[0m")
#                     continue
#                 pwd = input("Login Password: ").strip()
#                 if pwd == "":
#                     print("\033[31;0m密码不能为空.\033[0m")
#                     continue
#                 if name in user_dic:
#                     if user_dic[name]["pwd"] == pwd:    #认证通过
#                         login_flag = 1
#                         print("\033[32;0m登录成功.\033[0m")
#                         return func(*args, **kwargs)  # 调用目标函数
#                 if i == 1:      #认证失败
#                     exit("\033[31;0m用户名或密码错误.程序自动退出.\033[0m")
#                 else:
#                     print("\033[31;0m用户名或密码错误.您还有%s次机会哦.\033[0m" % (i-1))
#                     break
#     return inner    #返回装饰器函数内部函数名
#
# @user_auth    # 这里等同于fn1 = wrapper(fn1)
# def func1():
#     print("func1 is running...")
#
# @user_auth  #这里等同于fn2 = wrapper(fn2)
# def func2():
#     print("func2 is running...")
#
# filename = "userinfo-more.txt"
# login_flag = 0
# func1()
# func2()

'''
7、给每个函数写一个记录日志的功能，
功能要求：每一次调用函数之前，要将函数名称，时间节点记录到log的日志中。
所需模块：
import time
struct_time = time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S",struct_time))
'''
# import time
#
# def write_log(func):    #装饰器函数,也是一个闭包函数
#     def inner(*args, **kwargs):    #装饰器内部函数
#         with open("log", mode="a", encoding="utf-8") as f:  #追加写文件
#             f.write("%s\t%s\n" % (func.__name__, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
#         return func(*args, **kwargs)    #调用目标函数
#     return inner    #返回装饰器函数的内部函数
#
# @write_log  #调用装饰器函数,等同于 func1 = write_log(func1)
# def func1():
#     print("func1 is running...")
#
# @write_log  #调用装饰器函数,等同于 func1 = write_log(func1)
# def func2():
#     print("func2 is running...")
#
# func1()
# func2()



