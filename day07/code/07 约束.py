# class Foo:
#     def login(self):
#         # python约束的第一套方法
#         # 报错, 爆出异常
#         raise NotImplementedError("没有重写这个Login")
#
# # 普通人
# class Member(Foo):
#     def login(self):  # 方法的重写
#         print("普通人登录")
#
# # 吧务
# class Member_admin(Foo):
#     def login(self): # 想要的是login, 写的是denglu
#         print("吧务登录")
#
# # 管理员
# class Admin(Foo):
#     def login(self):
#         print("管理员登录")
#
# # 项目经理
# def login(obj):
#     obj.login()
#
# m = Member()
# ma = Member_admin()
# a = Admin()
#
# login(m)
#
#
# login(ma)
# login(a)


from abc import ABCMeta, abstractmethod

class Foo(metaclass=ABCMeta): # 抽象类
    @abstractmethod # 抽象方法
    def login(self):pass

# 普通人
class Member(Foo):
    def login(self):  # 方法的重写
        print("普通人登录")

m = Member()

