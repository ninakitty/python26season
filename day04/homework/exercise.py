# 1、整理装饰器的形成过程，背诵装饰器的固定格式
# def wrapper(fn):  # 定义装饰器名称
#     def inner(*args, **kwargs):  # 定义要内部函数,实际操作内容将原函数包裹,在原函数上、下都可以执行内容,可使用无敌形参
#         print('函数执行前')  # 在函数执行前执行的代码
#         result = fn(*args, **kwargs)  # 要被装饰的函数,并将原结果返回值记录,形参引用inner参数
#         print('函数执行后')  # 在函数执行后要执行的代码
#         return result  # 将原函数返回值返回
#
#     return inner  # 将装饰后的函数返回
#
#
# @wrapper  # 使用语法糖装饰函数,实际已将原函数替换
# def game(args):
#     print(f'我要玩{args}游戏')
#     return 1
#
#
# res = game('lol')  # 相当于原调用方法不变
# print(res)

# 2、编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码’
# def wrapper(fn):
#     def inner(*args, **kwargs):
#         print('每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码');
#         result = fn(*args, **kwargs)
#         return result
#
#     return inner
#
#
# @wrapper
# def func():
#     print('我是被装饰函数')
#
#
# func()
# 3、编写装饰器,在每次执行被装饰函数之后打印一句’每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码
# def wrapper(fn):
#     def inner(*args, **kwargs):
#         result = fn(*args, **kwargs)
#         print('每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码')
#         return result
#
#     return inner
#
#
# @wrapper
# def fun(*args):
#     print('我是要被装饰的函数')
#     return args
#
#
# res = fun('forest gump')
# print(res)

# 4、编写装饰器,在每次执行被装饰函数之前让用户输入用户名,密码,给用户三次机会,登录成功之后,才能访问该函数.
# username = 'tom'  # 正确用户名
# password = 'jerry'  # 正确密码
#
#
# def wrapper(fn):  # 定义装饰器
#     def inner(*args, **kwargs):  # 内部函数
#         count = 3  # 计数
#         while count:
#             count -= 1  # 每次循环减1
#             uname = input('请输入用户名:').strip()  # 输入用户名
#             upwd = input('请输入密码:').strip() # 输入密码
#             if username == uname and password == upwd:  # 如果用户名密码验证成功
#                 result = fn(*args, **kwargs)  # 执行函数
#                 return result  # 返回函数结果
#             elif count:  # 用户名密码错误,计数不为0,打印剩余次数
#                 print(f'您的剩余尝试次数还有{count}次!请重试!')
#             else:  # 计数为0,显示结束
#                 print(f'您的剩余尝试次数还已用尽!')
#
#     return inner  # 返回装饰后函数
#
#
# @wrapper  # 装饰器语法糖
# def operation():
#     print('我是被装饰函数')
#
#
# operation()

# 5、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,只支持单用户的账号密码,给用
# 户三次机会），要求登录成功一次，后续的函数都无需再输入用户名和密码
#
# 帐号:tom,密码:jerry
# def login():  # 定义登录函数
#     filename = 'login_db'  # 记录帐号密码的文件名
#     count = 3  # 循环计数
#     login_flag = False  # 是否已登录标记
#     while count:
#         count -= 1  # 每次循环减1
#         username = input('请输入用户名:').strip()  # 输入用户名
#         password = input('请输入密码:').strip()  # 输入密码
#         with open(filename, mode='r', encoding='utf8') as file:  # 打开文件管道
#             uname, upwd = file.readline().strip().split(',')  # 读取第一行内容
#             if uname == username and upwd == password:
#                 login_flag = True
#                 return login_flag
#         if count:  # 用户名密码错误,计数不为0,打印剩余次数
#             print(f'您的剩余尝试次数还有{count}次!请重试!')
#         else:  # 计数为0,显示结束
#             print(f'您的剩余尝试次数还已用尽!')
#     return login_flag
#
#
# userislogin = False  # 是否登录标记
#
#
# def wrapper(fn):  # 定义装饰器
#     def inner(*args, **kwargs):  # 定义内部函数
#         global userislogin  # 引入全局变量--登录标记
#         if userislogin:  # 如果已登录
#             result = fn(*args, **kwargs)  # 执行原函数,接收返回结果
#             return result  # 返回结果
#         else:  # 如果未登录
#             res = login()  # 使用登录函数
#             if res:  # 如果登录成功
#                 userislogin = True  # 修改全局变量--是否已登录标记
#                 result = fn(*args, **kwargs)  # 执行原函数
#                 return result  # 返回结果
#             else:  # 如果登录不成功
#                 userislogin = False  # 全局变量为否
#
#     return inner  # 返回修饰过的函数
#
#
# @wrapper  # 装饰函数
# def fun1():
#     print('我是fun1')
#
#
# @wrapper
# def fun2():
#     print('我是fun2')
#
#
# @wrapper
# def fun3():
#     print('我是fun3')
#
#
# fun1()
# fun2()
# fun3()

# 6、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,可支持多账号密码），要求登
# 录成功一次（给三次机会），后续的函数都无需再输入用户名和密码。
# 帐号1:tom,密码:jerry
# 帐号2:hello,密码:kitty
# def login():  # 定义登录函数
#     filename = 'login_db'  # 记录帐号密码的文件名
#     count = 3  # 循环计数
#     login_flag = False  # 是否已登录标记
#     while count:
#         count -= 1  # 每次循环减1
#         username = input('请输入用户名:').strip()  # 输入用户名
#         password = input('请输入密码:').strip()  # 输入密码
#         with open(filename, mode='r', encoding='utf8') as file:  # 打开文件管道
#             for line in file:  # 循环每行内容
#                 uname, upwd = line.strip().split(',')  # 分割每行内容
#                 if uname == username and upwd == password:
#                     login_flag = True
#                     return login_flag
#         if count:  # 用户名密码错误,计数不为0,打印剩余次数
#             print(f'您的剩余尝试次数还有{count}次!请重试!')
#         else:  # 计数为0,显示结束
#             print(f'您的剩余尝试次数还已用尽!')
#     return login_flag
#
#
# userislogin = False  # 是否登录标记
#
#
# def wrapper(fn):  # 定义装饰器
#     def inner(*args, **kwargs):  # 定义内部函数
#         global userislogin  # 引入全局变量--登录标记
#         if userislogin:  # 如果已登录
#             result = fn(*args, **kwargs)  # 执行原函数,接收返回结果
#             return result  # 返回结果
#         else:  # 如果未登录
#             res = login()  # 使用登录函数
#             if res:  # 如果登录成功
#                 userislogin = True  # 修改全局变量--是否已登录标记
#                 result = fn(*args, **kwargs)  # 执行原函数
#                 return result  # 返回结果
#             else:  # 如果登录不成功
#                 userislogin = False  # 全局变量为否
#
#     return inner  # 返回修饰过的函数
#
#
# @wrapper  # 装饰函数
# def fun1():
#     print('我是fun1')
#
#
# @wrapper
# def fun2():
#     print('我是fun2')
#
#
# @wrapper
# def fun3():
#     print('我是fun3')
#
#
# fun1()
# fun2()
# fun3()

# 7、给每个函数写一个记录日志的功能，
# 功能要求：每一次调用函数之前，要将函数名称，时间节点记录到log的日志中。
# 所需模块：
# import time
# struct_time = time.localtime()
# print(time.strftime("%Y‐%m‐%d %H:%M:%S",struct_time))

import time  # 导入time模块


def write_file_wrapper(fn):  # 定义日志装饰器
    def inner(*args, **kwargs):  # 定义内部函数
        filename = 'exec_function_log'  # 记录日志文件名称
        function_name = fn.__name__  # 函数名称
        execute_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 获取当前时间并格式化字符
        with open(filename, mode='a', encoding='utf8') as file:  # 打开文件管道
            content = function_name + ',' + execute_time + '\n'  # 拼接待写入内容
            file.write(content)  # 写入
        result = fn(*args, **kwargs)  # 执行被装饰函数
        return result  # 返回函数结果

    return inner  # 返回装饰后函数


@write_file_wrapper  # 语法糖装饰
def fun1():
    print('我是fun1')


@write_file_wrapper
def fun2():
    print('我是fun2')


@write_file_wrapper
def fun3():
    print('我是fun3')


fun1()
fun2()
fun3()
