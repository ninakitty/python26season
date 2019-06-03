# import module
#
# print(module.name)
# module.func()
# p = module.Person('李四', 20)
# p.chi()

'''
:type#返回类型
:isinstance#是否是某类型
:issubclass#是否是子类
'''

#
# class Animal:
#     pass
#
#
# class Cat(Animal):
#     pass
#
#
# a = Animal()
# c = Cat()
# print(type(a))
# print(isinstance(a, Animal))
# print(isinstance(c, Animal))
# print(isinstance(a, Cat))
# print(issubclass(Cat, Animal))


# 反射
# import daniu
#
#
# def shui():
#     print('它很能睡')
#
#
# setattr(daniu, 'shui', shui)  # 定义一个新函数
# delattr(daniu, 'chi')  # 删除一个新函数
#
# while True:
#     gn = input('请输入一个大牛的功能:')
#     if gn == 'exit':
#         break
#     if hasattr(daniu, gn):  # 是否有这个属性
#         fn = getattr(daniu, gn)  # 获取这个属性
#         if callable(fn):  # 是否可被调用
#             fn()
#         else:
#             print(fn)
#     else:
#         print('没有这个属性')


# 约束

# 约束:第一种方法
# class Foo:
#     def login(self):
#         raise NotImplementedError('未重写login()方法')
#
#
# class Member(Foo):
#     def login(self):
#         print('member login()')
#
#
# class Member_admin(Foo):
#     def login(self):
#         print('member_admin login()')
#
#
# class Admin(Foo):
#     def login(self):
#         print('admin login()')
#
#
# # 主入口
# def fun(obj):
#     obj.login()
#
#
# m = Member()
# ma = Member_admin()
# a = Admin()
#
# fun(m)
# fun(ma)
# fun(a)

# 约束:第二种
from abc import ABCMeta, abstractmethod


class Foo(metaclass=ABCMeta):
    @abstractmethod
    def login(self): pass


class Member(Foo):
    def login(self):
        print('member login()')


m = Member()
