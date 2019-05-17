# 1、整理装饰器的形成过程，背诵装饰器的固定格式
def wrapper(func):
    def inner(*args,**kwargs):
        res = func(*args,**kwargs)
        return res
    return inner
# 2、编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码’
def wrapper1(func):
    def inner(*args,**kwargs):
        print('每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码')
        res = func(*args,**kwargs)
        return res
    return inner
# 3、编写装饰器,在每次执行被装饰函数之后打印一句’每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码’
def wrapper2(func):
    def inner(*args,**kwargs):
        res = func(*args,**kwargs)
        print('每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码')
        return res
    return inner
# 4、编写装饰器,在每次执行被装饰函数之前让用户输入用户名,密码,给用户三次机会,登录成功之后,才能访问该函数.
# def login(func):
#     def inner(*args,**kwargs):
#         count = 0
#         dic = {}
#         with open('账号密码','r',encoding='utf-8') as f:
#             content = f.read()
#         while count<3:
#             username = input('输入账号：').strip()
#             password = input('输入密码：').strip()
#             if username + password in content :
#                 print('登录成功!')
#                 break
#             else:
#                 count +=1
#                 print('账号有误！')
#         res = func(*args,**kwargs)
#         return res
#     return inner
# @login
# def wahah():
#     pass
# wahah()
# 5、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,只支持单用户的账号密码,给用户三次机会），
# 要求登录成功一次，后续的函数都无需再输入用户名和密码
status = True
def login(func):
    def inner(*args,**kwargs):
        global status
        count = 0
        with open('账号密码','r',encoding='utf-8') as f:
            content = f.read()
        while status and count < 3:
            username = input('输入账号：').strip()
            password = input('输入密码：').strip()
            if username + password in content :
                status = False
                print('登录成功!')
                break
            else:
                count +=1
                print('账号有误！')
        res = func(*args,**kwargs)
        return res
    return inner
@login
def wahah():
    pass
@login
def shuangwaiwai():
    pass
wahah()
shuangwaiwai()
# 6、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,可支持多账号密码），
# 要求登录成功一次（给三次机会），后续的函数都无需再输入用户名和密码。

# 7、给每个函数写一个记录日志的功能，功能要求：每一次调用函数之前，要将函数名称，时间节点记录到log的日志中。
# 所需模块：
# import time
# struct_time = time.localtime()
# print(time.strftime("%Y‐%m‐%d %H:%M:%S",struct_time))
import time
def logger(func):
    def inner(*args,**kwargs):
        struct_time = time.localtime()
        line='%s调用%s'%(time.strftime('%Y-%m-%d %H:%M:S',struct_time),func.__name__)
        with open('用户日志','a',encoding='utf-8') as f:
            f.write(line)
        res = func(*args,**kwargs)
        return res
    return inner
@logger
def xiaoxixi():
    pass
xiaoxixi()