# ---------给装饰器传递参数
# def wrapper_out(flag):
#     def wrapper(fn):
#         def inner(*args, **kwargs):
#             if flag:
#                 print('function front')
#                 result = fn(*args, **kwargs)
#                 print('function after')
#             else:
#                 result = fn(*args, **kwargs)
#             return result
#
#         return inner
#
#     return wrapper
# @wrapper_out(1)
# def fun1():
#     print('fun1')
# @wrapper_out(0)
# def fun2():
#     print('fun2')
#
# fun1()
# fun2()

# -------分别放置日志
import time
def wrapper_out(filename):
    def log(fn):
        def inner(*args, **kwargs):
            ret = fn(*args, **kwargs)
            with open(filename, mode='a', encoding='utf8') as file:
                file.write(filename + ',' +time.strftime('%Y%m%d-%h%m%s',time.localtime()))
            return ret

        return inner

    return log


@wrapper_out('func1')
def func1():  # 日志放在func1.txt
    print("我是func1")


@wrapper_out('func2')
def func2():  # 日志放在func2.txt
    print("我是func2")


func1()
func2()
