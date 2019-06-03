# # class Person:
# #     def __init__(self):
# #         print("我是init")
# #     # 在对象()的时候自动调用
# #     def __call__(self, *args, **kwargs):
# #         print("我是call")
# #     # with的时候自动调用
# #     def __enter__(self):
# #         print("我是enter")
# #     # 离开with的时候自动调用
# #     def __exit__(self, exc_type, exc_val, exc_tb):
# #         print("我是exit")
# #     # 执行[]
# #     def __getitem__(self, item):
# #         print("我是getitem")
# #         return "哈哈"
# #     #  执行p[key] = value
# #     def __setitem__(self, key, value):
# #         print(key)
# #         print(value)
# #     # __hash__ = None
# #     def __hash__(self):
# #         print("我是哈希")
# #         return 1
# #
# # p = Person()
# # # p()
# #
# # # with p:
# # #     print("我是with")
# #
# # print(p["as"])
# #
# # p["吴孟达"] = "大佬"
# #
# # # hash(p)
# #
# # dic = {p:"value"} #  当字典存储数据的时候. 自动根据key计算hash值. 默认执行__hash__
# #
# #
# #
#
#
# class A:
#     def __init__(self):
#         print("哈哈")
#
#     def __getitem__(self, item):
#         print(f"我是getitem = > {item}")
#         return "呵呵"
#
#     # __hash__ = None
#     def __hash__(self):
#         print("我是可哈希的")
#         return 123456
#
#     def __eq__(self, other):
#         print("这格式eq")
#         return True
#     def __add__(self, other):
#         print("我是加")
#
# # a = A()
# # # a["嘚瑟"]
# # # dic["key"]
# # # list
# # s = set()
# # s.add("我是字符串")
# # s.add((1,2,3))
# # s.add(a) #  判断是否可哈希
# # # s.add([1,2,3])
# # # dic = {}
#
# a = A()
# b = A()
# print(a + b)


class A(object):
    def __init__(self):
        print("我是A的Init")

    def __new__(cls, *args, **kwargs):
        print("我是new")
        return object.__new__(cls)


a = A() # 默认找 object中的__new__ ==> 开辟内存

# 单例模式
# 在内存中保存一个对象. 反复的使用

# ....
# 恶汉式
class Singlton:
    __instance = None # 保存对象

    def __init__(self):
        print("我是init")

    # 高并发情况下. 单利有问题
    def __new__(cls, *args, **kwargs):
        if Singlton.__instance: # 判断是否存在对象
            return Singlton.__instance
        else: # 不存在, 就创建一个新的
            obj = object.__new__(cls)
            Singlton.__instance = obj # 把新的对象更新到类变量
            return Singlton.__instance # 返回对象


s1 = Singlton()
s2 = Singlton()
print(id(s1), id(s2))