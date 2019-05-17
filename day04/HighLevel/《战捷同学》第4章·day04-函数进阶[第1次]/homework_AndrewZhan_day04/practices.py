#!/usr/bin/env python
# -*- encoding:utf-8 -*-
# Author: Andrew.zhan
# Create by 2019 Apr 21
import json
import sys
import time


def practice_1():
    '''
    1、整理装饰器的形成过程，背诵装饰器的固定格式
    '''
    # 装饰器(三层是为了接收装饰器的参数, flask,bottle等web框架经常会用到这种装饰器) *必会技能*
    def outer(*args, **kwargs):
        def wrapper(fn):        # fn是被装饰的函数对象
            print(args[0])  # 1, 输出1    # 实在不太善于用语言解释,我让每个参数值按输出顺序打印吧.

            def inner(*in_args, **in_kwargs):
                print(in_args[0])  # 3, 输出3
                result = fn(*in_args, **in_kwargs)  # 调用原func1, result接收的是func1的return.
                print(in_kwargs["k"] + 1)  # 7, 输出7
                return result

            print(kwargs["k"])  # 2, 输出2
            return inner

        return wrapper

    @outer(1, k=2)   # 无论func1被不被调用,这里outer函数return出来的wrapper在这行就已经被调用了.
    def func1(*args, **kwargs):
        print(args[0] + 1)  # 4, 输出4
        print("5,我是被装饰的函数func1")  # 5, 输出"5,我是被装饰的函数func1"
        print(kwargs["k"])  # 6, 输出6
        return "8,Done."

    # 此时的func1其实已经被inner替换掉了.
    print(func1(3, k=6))  # 8, 输出"8,Done."

    # ----------输出----------:
    '''
    1
    2
    3
    4
    5,我是被装饰的函数func1
    6
    7
    8,Done.
    '''


def practice_2():
    '''
    2、编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码’
    '''
    def wrapper(func):
        def inner(*args, **kwargs):
            print('每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码')
            func(*args, **kwargs)
        return inner

    @wrapper
    def execution_func():
        print("我是被装饰的函数")

    execution_func()


def practice_3():
    '''
    3、编写装饰器,在每次执行被装饰函数之后打印一句’每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码’
    '''
    def wrapper(func):
        def inner(*args, **kwargs):
            func(*args, **kwargs)
            print('每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码')
        return inner

    @wrapper
    def execution_func():
        print("我是被装饰的函数")

    execution_func()


def practice_4():
    '''
    4、编写装饰器,在每次执行被装饰函数之前让用户输入用户名,密码,给用户三次机会,登录成功之后,才能访问该函数.
    '''
    def login():
        # 验证简单写了.
        for i in range(3):
            print("剩余 %s 次机会" % (3-i))
            username = input("请输入用户名: ").strip()
            passwd = input("请输入密码: ").strip()
            if username == "u1" and passwd == "123":      # for三次, 如果成功了那么就直接return True了
                return True
        return False                                      # 如果走到这一步,那么说明前面3次都错了,return False就好了.

    def wrapper(func):
        def inner(*args, **kwargs):
            if login():
                return func()      # 只有login函数成功后才会调用被装饰的porta函数.
            print("登录失败了.")    # 因为上面直接return了func(), 所以能走到这里说明login肯定是False.
        return inner

    @wrapper
    def portal():
        print("登录后可见")
        return True
    portal()


def practice_5():
    '''
    5、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,只支持单用户的账号密码,给用户三次机会），
    要求登录成功一次，后续的函数都无需再输入用户名和密码
    '''
    # 老师上课讲的, 用flag的方式.
    Flag = False

    def login():
        if Flag:
            return True
        # 验证简单写了.
        # 用户信息 user1:123, user2:123, user3:123 三个用户.
        with open("user_info_db.txt", 'r', encoding='utf-8') as fp:
            users_info = json.loads(fp.read())
        for i in range(3):
            print("剩余 %s 次机会" % (3 - i))
            username = input("请输入用户名: ").strip()
            passwd = input("请输入密码: ").strip()
            if passwd == users_info.get(username):
                return True
        return False

    def wrapper(func):
        def inner(*args, **kwargs):
            if login():
                nonlocal Flag
                Flag = True
                return func()      # 只有login函数成功后才会调用被装饰的porta函数.
            print("登录失败了.")    # 因为上面直接return了func(), 所以能走到这里说明login肯定是False.
            sys.exit(1)
        return inner

    @wrapper
    def func1():
        print("功能1")

    @wrapper
    def func2():
        print("功能2")

    @wrapper
    def func3():
        print("功能3")

    func1()
    func2()
    func3()


def practice_6():
    '''
    6、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,可支持多账号密码），
    要求登录成功一次（给三次机会），后续的函数都无需再输入用户名和密码。
    '''
    # 老师上课讲的, 用flag的方式.
    Flag = False

    def login():
        if Flag:
            return True
        # 验证简单写了.
        # 用户信息 user1:123, user2:123, user3:123 三个用户.
        with open("user_info_db.txt", 'r', encoding='utf-8') as fp:
            users_info = json.loads(fp.read())
        for i in range(3):
            print("剩余 %s 次机会" % (3 - i))
            username = input("请输入用户名: ").strip()
            passwd = input("请输入密码: ").strip()
            if passwd == users_info.get(username):
                return True
        return False

    def wrapper(func):
        def inner(*args, **kwargs):
            if login():
                nonlocal Flag
                Flag = True
                return func()      # 只有login函数成功后才会调用被装饰的porta函数.
            print("登录失败了.")    # 因为上面直接return了func(), 所以能走到这里说明login肯定是False.
            sys.exit(1)
        return inner

    @wrapper
    def func1():
        print("功能1")

    @wrapper
    def func2():
        print("功能2")

    @wrapper
    def func3():
        print("功能3")

    func1()
    func2()
    func3()


def practice_7():
    '''
    7、给每个函数写一个记录日志的功能，
    功能要求：每一次调用函数之前，要将函数名称，时间节点记录到log的日志中。
    所需模块：
    import time
    struct_time = time.localtime()
    print(time.strftime("%Y‐%m‐%d %H:%M:%S",struct_time))
    '''
    def write_log(func_name):
        struct_time = time.localtime()
        now_time = time.strftime("%Y‐%m‐%d %H:%M:%S", struct_time)
        log_record = "%s Function_name: %s\n" % (now_time, func_name)  # 格式化好日志每行内容,然后下面写入日志.
        with open("exec.log", "a", encoding="utf-8") as fp:
            fp.write(log_record)

    def loger(fn):
        def inner(*arg, **kwargs):
            write_log(fn.__name__)   # 将被装饰的函数的函数名传给写入log日志的函数.
            fn(*arg, **kwargs)
        return inner

    @loger
    def func1():
        print("我是func1")

    @loger
    def func2():
        print("我是func2")

    @loger
    def func3():
        print("我是func3")

    for i in range(1, 4):
        exe_func_cmd = "func%s()" % i
        time.sleep(1)          # 为了让日志时间戳有一点差别,sleep1秒再执行.
        exec(exe_func_cmd)     # 上课讲了exec的用法, 最好不要执行用户所输入的内容. 在这个场景使用还不错.


def main():
    # practice_1()
    # practice_2()
    # practice_3()
    # practice_4()
    # practice_5()
    # practice_6()
    practice_7()


if __name__ == "__main__":
    main()

