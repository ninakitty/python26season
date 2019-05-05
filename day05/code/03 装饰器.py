# def wrapper_out(flag): # 带参数的装饰器
#     def wrapper(fn):
#         def inner(*args, **kwargs):
#             if flag: # 判断flag是否为真.
#                 print("问问alex, 市场行情怎么样")
#                 ret = fn(*args, **kwargs)
#                 print("alex骗我")
#             else:
#                 ret = fn(*args, **kwargs)
#             return ret
#         return inner
#     return wrapper
#
# @wrapper_out(True)
# def yue():
#     print("约个大美女")
#
# @wrapper_out(False)
# def lvxing():
#     print("旅行")
#
# yue()
# lvxing()

# def log_out(filename="default.log"):
#     def log(fn): # 记录日志
#         def inner(*args, **kwargs):
#             ret = fn(*args, **kwargs)
#             # 记录日志
#             print("我要记录日志, 记录在:"+filename)
#             return ret
#         return inner
#     return log
#
# @log_out("func1.txt")
# def func1(): # 日志放在func1.txt
#     print("我是func1")
#
# @log_out("func2.txt")
# def func2(): # 日志放在func2.txt
#     print("我是func2")
#
#
# func1()
# func2()


def wrapper1(fn):
    def inner(*args, **kwargs):
        print("warpper1_前")
        ret = fn(*args, **kwargs)
        print("warpper1_后")
        return ret
    return inner

def wrapper2(fn):
    def inner(*args, **kwargs):
        print("warpper2_前")
        ret = fn(*args, **kwargs)
        print("warpper2_后")
        return ret
    return inner

def wrapper3(fn):
    def inner(*args, **kwargs):
        print("warpper3_前")
        ret = fn(*args, **kwargs) # 目标
        print("warpper3_后")
        return ret
    return inner



@wrapper1
@wrapper2
@wrapper3
def func():
    print("我是目标")
    return 1

func()  # 执行目标函数
