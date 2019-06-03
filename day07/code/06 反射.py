# import daniu
# # 由我来确定要执行的是那一个功能
#
# while 1:
#     gn = input("请输入你要测试的功能:") # "Person"
#     # 判断是否存在"chi"这个东西
#     # attribute
#     # 判断xxx模块(对象) 是否有xxx属性
#     if hasattr(daniu, gn):
#         # 从xxx对象中获取xxx属性
#         fn = getattr(daniu, gn)
#         # 判断是否可以被调用  + ()
#         if callable(fn):
#             p = fn() # 没效果
#         else:
#             print(fn)
#     else:
#         print('没有这个功能')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def haha(self):
        print("哈哈")

p = Person("alex", 28)

# print(hasattr(p, "haha"))
# fn = getattr(p, "haha")
# fn()


# delattr(p, "name")
# # print(p.name)
#
# p2 = Person("wusir", 22)
# print(p2.name) # ????


# setattr(p, "address", "北京市八大胡同")
# setattr(p, "name", "胡辣汤")
#
# print(p.address)
# print(p.name)

# setattr(p, "chi", lambda : print("我要吃"))
# print(p.chi)

# setattr(Person, "chi", lambda self:print("我要吃"))
# p.chi()
