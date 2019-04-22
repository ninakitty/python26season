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
#             uname = input('请输入用户名:')  # 输入用户名
#             upwd = input('请输入密码:')  # 输入密码
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

def login():  # 定义登录函数
    filename = 'login_db'  # 记录帐号密码的文件名
    count = 3  # 循环计数
    login_flag = False  # 是否已登录标记
    while count:
        count -= 1  # 每次循环减1
        username = input('请输入用户名:')  # 输入用户名
        password = input('请输入密码:')  # 输入密码
        with open(filename, mode='r', encoding='utf8') as file:  # 打开文件管道
            for line in file:  # 循环每行内容
                uname, upwd = line.strip().split(',')
                if uname == username and upwd == password:
                    login_flag = True
                    break
                elif count:  # 用户名密码错误,计数不为0,打印剩余次数
                    print(f'您的剩余尝试次数还有{count}次!请重试!')
                else:  # 计数为0,显示结束
                    print(f'您的剩余尝试次数还已用尽!')
    return login_flag


def wrapper(fn):
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        return result

    return inner

# @wrapper
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
