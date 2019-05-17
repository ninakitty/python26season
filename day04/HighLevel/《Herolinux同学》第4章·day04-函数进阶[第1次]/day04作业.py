# 练习题：
# 1、整理装饰器的形成过程，背诵装饰器的固定格式
'''
1、定义目标函数
2、定义装饰器函数
3、将目标函数赋值给装饰器，
@装饰器
目标函数
4、调用函数
5、装饰器执行
6、装饰器内执行目标函数，获取函数返回值
7、返回函数返回值
'''
# def wrapper(func):
#     def inner(*args,**kwargs):
#         print("函数执行前动作")
#         ret=func(*args,**kwargs)
#         print("函数执行后动作")
#         return ret
#     return inner
#
# @wrapper
# def dest(arg1,arg2):
#     print("执行目标函数.....")
#     return arg1,arg2
# print(dest("first","second"))


# 2、编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码’
# def wrapper(func):
    # def inner(*args,**kwargs):
    #     print("每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码")
    #     ret=func(*args,**kwargs)
    #     return ret
    # return inner
#
# @wrapper
# def dest():
#     print("from dest functions...")
#     return True


# dest()

# 3、编写装饰器,在每次执行被装饰函数之后打印一句’每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码’
# def wrapper(func):
#     def inner(*args,**kwargs):
#         ret=func(*args,**kwargs)
#         print("每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码")
#         return ret
#     return inner
#
# @wrapper
# def dest():
#     print("from dest functions")
#     return True
#
# dest()


# 4、编写装饰器,在每次执行被装饰函数之前让用户输入用户名,密码,给用户三次机会,登录成功之后,才能访问该函数.
# def wrapper(func):
#     def inner(*args,**kwargs):
#         for count in range(3):
#             user=input("用户名>>:").strip()
#             upwd=input("密码>>:").strip()
#             if user == "hero" and upwd == "123":
#                 ret=func(*args,**kwargs)
#                 return ret
#             else:
#                 print("用户名或密码错误")
#         else:
#             print("登陆次数用尽，登陆失败")
#     return inner
#
# @wrapper
# def dest():
#     print("from dest functions ")
#
# dest()



# 5、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,只支持单用户的账号密码,给用户三次机会），
# 要求登录成功一次，后续的函数都无需再输入用户名和密码

# import json
#
# with open("messages",mode="wt",encoding="utf-8") as f:
#     json.dump({"user":"hero","passwd":"123"},f)
# Tag=False
# def auth(func):
#     def inner(*args,**kwargs):
#         global Tag
#         if Tag:
#             ret = func(*args, **kwargs)
#             return ret
#         with open("messages", mode="rt", encoding="utf-8") as f:
#             data = json.load(f)
#         for count in range(3):
#             user = input("user>>:").strip()
#             upwd = input("passwd>>:").strip()
#             if user == data["user"] and upwd == data["passwd"]:
#                 Tag=True
#                 ret=func(*args,**kwargs)
#                 return ret
#             else:
#                 print("用户名密码错误")
#         else:
#             print("登陆次数用尽，登陆失败")
#     return inner
#
# @auth
# def shop():
#     print("from shop")
#
# @auth
# def game():
#     print("from game")
#
# @auth
# def fight():
#     print("from fight")
#
# shop()
# game()
# fight()

# 6、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,可支持多账号密码），
# 要求登录成功一次（给三次机会），后续的函数都无需再输入用户名和密码。
# import json,os
# user1="test"
# user2="test2"
# user3="test3"
# pwd="123"
#
# with open("test",mode="wt",encoding="utf-8") as f1,open("test2",mode="wt",encoding="utf-8") as f2,open("test2", mode="wt", encoding="utf-8") as f3:
#     dic1={"user":user1,"passwd":pwd}
#     dic2={"user":user2,"passwd":pwd}
#     dic3={"user":user3,"passwd":pwd}
#     json.dump(dic1,f1)
#     json.dump(dic2,f2)
#     json.dump(dic3,f3)
#
# Tag=False
# def wrapper(func):
#     def inner(*args,**kwargs):
#         global Tag
#         if Tag:
#             ret = func(*args, **kwargs)
#             return ret
#         for count in range(3):
#             user=input("user>>:").strip()
#             upwd=input("passwd>>:").strip()
#             if user in os.listdir():
#                 with open(user,mode="rt",encoding="utf-8") as f:
#                     data=json.load(f)
#                     if data["passwd"] == upwd:
#                         Tag=True
#                         ret=func(*args,**kwargs)
#                         return ret
#             print("用户名或密码错误")
#         else:
#             print("登陆次数用尽，登陆失败")
#     return inner
#
# @wrapper
# def func1():
#     print("from func1")
#
# @wrapper
# def func2():
#     print("from func2")
#
# @wrapper
# def func3():
#     print("from func3")
#
# func1()
# func2()
# func3()


# 7、给每个函数写一个记录日志的功能，功能要求：每一次调用函数之前，要将函数名称，时间节点记录到log的日志中。
# 所需模块：
# import logging.config,time
# LOG_PATH="access.log"
# data=time.strftime('%Y-%m-%d %H:%M:%S')
# def write_log(func):
#     def inner(*args,**kwargs):
#         with open(LOG_PATH,"at",encoding="utf-8") as f:
#             f.write("[%s] 使用函数%s\n" %(data,func.__name__))
#         ret=func(*args,**kwargs)
#         return ret
#     return inner
# @write_log
# def func1():
#     print("from func1")
#
# @write_log
# def func2():
#     print("from func2")
#
# func1()
# func2()
