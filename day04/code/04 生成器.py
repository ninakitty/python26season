# def order():
#     lst = []
#     for i in range(10000):
#         lst.append("衣服"+str(i))
#
#     return lst
#
# lst = order()
# print(lst)

# def func():
#     print("哈哈哈")
#     yield 1 # 有yield 就是一个生成器函数. 会创建一个生成器对象给你
#     print("吼吼吼")
#     yield 2 # 可以把一个函数分段执行
#     print("犀利malidou , 哈哈哈啊哈哈哈a")
#
# gen = func()  # generator  生成器
# # 生成器本质是一个迭代器
# # print(dir(gen))
#
# # 需要执行__next__ 才会让生成器执行一次
# ret = gen.__next__() # 执行到下一个yield
# print(ret)
#
# ret2 = gen.__next__()
# print(ret2)
#
# gen.__next__()

# 应用

# def order():
#     for i in range(10000):
#         yield "衣服"+str(i)
#
# gen = order() # 定义, 创建一个生成器对象
#
# print( order().__next__())
# print( order().__next__())
# print( order().__next__())
# print( order().__next__())


def func():
    print("韭菜盒子")
    s1 = yield 1
    print("s1=", s1)
    print("沙琪玛")
    s2 = yield 2
    print("s2=", s2)
    print("盒饭")
    s3 = yield 3
    print("s3=", s3)
    print("混沌")
    s4 = yield 4

gen = func()

print(gen.__next__()) # send可以给上一个yield位置传值

ret1 = gen.send("周润发")
ret2 = gen.send("周杰伦")
ret3 = gen.send("周笔畅")

print("===============")
print(ret1)
print(ret2)
print(ret3)


