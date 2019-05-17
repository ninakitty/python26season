# author:王锐
# date:2018/9/13

#  1.为了不改变原函数的代码，而为函数添加新的功能模块，就有了装饰器。装饰器固定格式如下：
# def decorator(func):
#     def inner(*args,**kwargs):
#         #被装饰函数执行之前代码段
#         ret = func(*args,**kwargs)
#         #装饰函数执行之后代码段
#         return ret
#     return inner


# 2.答题如下：
# def decorator(func):
#     def inner(*args,**kwargs):
#         print("每次执行完被装饰函数之前都得经过这里，这里根据需要添加代码")
#         ret = func(*args,**kwargs)
#         return ret
#     return inner
#
# @decorator
# def test():
#     print('in the test')
#
# test()


# 3.答题如下：
# def decorator(func):
#     def inner(*args,**kwargs):
#         ret = func(*args,**kwargs)
#         print("每次执行完被装饰函数之后都得经过这里，这里根据需要添加代码")
#         return ret
#     return inner
#
# @decorator
# def test():
#     print('in the test')
#
# test()


# 4.答题如下：
# user,passwd='allen','abc123'
# flag = False # 标记位，控制循环体结束
# def auth(func):
#     def deco(*args,**kwargs):
#         count = 3 # 计数器，每输入一次密码减少1
#         global flag
#         while not flag:
#             if count == 0:
#                      flag = True
#             else:
#                 username = input('Username:')
#                 password = input('Password:')
#
#                 if user == username and passwd == password:
#                     print("Login Successfull!")
#                     flag = True
#                     func(*args,**kwargs)
#                 else:
#                     print("Invalid password or username!")
#                 count = count - 1
#     return deco
#
# @auth
# def index():
#     print("welcome Index Page!")
#
# index()


# 5.答题如下:
# logined = False # 记录登陆状态
# def auth(func):
#     def deco(*args,**kwargs):
#         global logined
#         if not logined:
#             count = 3 # 计数器，每输入一次密码减少1
#             flag = False  # 标记位，控制循环体结束
#             while not flag:
#                 if count == 0:
#                          flag = True
#                          exit(0) # 如果三次密码输错，直接结束，其他被装饰函数功能模块也无法访问
#                 else:
#                     username = input('Username:').strip()
#                     password = input('Password:').strip()
#                     with open('user', encoding='utf-8') as f:
#                         for i in f:
#                             user, passwd = i.strip().split(' ')
#                         if user == username and passwd == password:
#                             print("Login Successfull!")
#                             flag = True
#                             logined = True
#                             func(*args, **kwargs)
#                         else:
#                             print("Invalid password or username!")
#                     count = count - 1
#         else:    # 如果登陆状态为True，那么访问后续被装饰函数不需要登陆认证，直接执行被装饰函数函数体
#             ret = func(*args,**kwargs)
#             return ret
#
#     return deco
#
# @auth
# def index():
#     print("welcome Index Page!")
#
# @auth
# def home():
#     print("welcome Index Home!")
#
# @auth
# def bbs():
#     print("welcome Index BBS!")
#
#
# home()
# bbs()
# index()


# '''6.再5的基础上追加一层循环，读取文件里的账号信息，应该会用到readline逐行读取账号密码信息，
#     然后用字符处理分片，文件操作和字符处理不熟练，需要加强复习知识点'''


# 7.答题如下：
# import time
# def log(func):
#     def inner(*args,**kwargs):
#         x = time.localtime()
#         print(time.strftime("%Y-%m-%d %H:%M:%S ",x)+"%s函数被执行了" % (func.__name__))
#         ret=func(*args,**kwargs)
#         return ret
#     return inner
#
# @log
# def func1():
#     print('in func1')
#
# @log
# def func2():
#     print('in func2')
#
# @log
# def func3():
#     print('in func3')
#
# func1()
# time.sleep(2)
# func2()
# time.sleep(2)
# func3()
