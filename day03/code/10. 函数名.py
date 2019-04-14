# def func():
#     print("你好啊, 我叫赛利亚")
#
# # <function func at 0x000002A48AE288C8>
# a = func
# # <function func at 0x000002A48AE288C8>
# print(a)

# 函数名可以像变量一样进行赋值操作

# def func(an):
#     an()
#
# def fn():
#     print("我是可怜的fn")
#
# def gn():
#     print("滚蛋, 你才是赛利亚")
#
# func(fn) # 我是可怜的fn
# func(gn)

# 函数名可以作为参数传递


# def func():
#     name = "alex"
#     def inner():
#         print("我是inner")
#     return inner
#
# a = func()
# print(a)
#
# a()

# 函数名可以作为返回值返回

# name1 = "alex"
# name2 = "wusir"
# name3 = "太白"
#
# def fn1():
#     print("我是fn1")
# def fn2():
#     print("我是fn2")
# def fn3():
#     print("我是fn3")
# lst=[fn1, fn2, fn3]
#
# for item in lst:
#     item()

# def an():
#     pass # 过.
#
# an = 3
# print(an)



# a = 10
# def func():
#     b = 20
#     print(locals()) # 查看当前  局部
#
# # print(globals()) # 内置 + 全局
# # print(locals()) # 全局
#
# func()


# def func():
#     # global a # 把全局变量引入到局部
#     # a += 20 # a = a + 20
#     global a
#     a = 30
#
# func()
# print(a)
# a = 10
# def wai():
#     a = 10
#     def nei():
#         nonlocal a
#         a += 20
#     nei()
#     print(a)
# wai()

a = 1
def fun_1():
    a = 2
    def fun_2():
        nonlocal a
        a = 3
        def fun_3():
            a = 4
            print(a)#4
        print(a)#3
        fun_3()
        print(a)#3
    print(a)#2
    fun_2()
    print(a)#3
print(a)#1
fun_1()
print(a)#1

