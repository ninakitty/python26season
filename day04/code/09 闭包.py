
# 在内层函数中使用外层函数中的变量
# 1. 保护变量
# 2. 让一个变量常驻内存   => 爬虫

def outer():
    a = 10
    def inner():
        print(a)  # 闭包
    return inner

fn = outer()
ret = fn()
print(fn.__closure__) # (<cell at 0x0000022DD94F85B8: int object at 0x0000000054436D30>,) 是闭包
print(ret)

# def func1():
#     a = 10
#     print(a)
# print(func1.__closure__) # None不是一个闭包
