
def func():
    pass

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def chi(self): # 实例方法
        print("哈哈哈")



    @classmethod
    def lei(cls):
        pass



    @staticmethod
    def jing():
        pass

# # <function func at 0x00000148183D99D8>
# print(func)
# p = Person()
# # <bound method Person.chi of <__main__.Person object at 0x0000023B3F757C50>>
# print(p.chi) #  method
#
# # 函数是不绑定在任何对象上的
# # 方法是绑定在对象上的

# Person.chi()
p = Person("alex", 18)
# p.chi()

# Person.chi(p) #  访问类的名称空间中的一个函数
# print(Person.chi) # 函数


# # <bound method Person.lei of <class '__main__.Person'>>
# print(Person.lei)
# # <bound method Person.lei of <class '__main__.Person'>>
# print(p.lei)

# # <function Person.jing at 0x0000029833869C80>
# # <function Person.jing at 0x0000029833869C80>
# print(Person.jing)
# print(p.jing)


# 如何用程序判断方法和函数
# __iter__
# __next__

# from types import FunctionType, MethodType
#
# print(isinstance(func, FunctionType))
# print(isinstance(func, MethodType))
