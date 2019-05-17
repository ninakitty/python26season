# class Foo:
#     f = "哈哈哈"
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#
# f = Foo(1,2,3)
#
# f.d = "哈哈"


# class Person:
#     country = "大清" # 类变量可以共享出去. 修改的时候只能是类名去访问
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def chi(self):
#         print(self.name+"在吃东西")
#
#     @classmethod
#     def sleep(cls): # class
#         print(cls, "sleep在执行")
#
#     @staticmethod
#     def drink():
#         print("我就是一个静态方法")
#
# # Person.sleep()
# # print(Person)
#
# Person.drink()
#
#
# #
# # p1 = Person("蔡徐坤", 28, "男")
# # p2 = Person("高进", 29, "男")
# # p3 = Person("伊丽莎白鼠", 129, "男")
# #
# # # # 大清亡了
# # # p1.country = "民国"
# # # p2.country = "民国"
# # # p3.country = "民国"
# # # p1.country = "民国"
# # Person.country = "民国"
# #
# # print(p1.country)
# # print(p2.country)
# # print(p3.country)
# #
# # p1.chi()
#
# dic = dict.fromkeys("周杰伦", "蔡徐坤")
# print(dic)
#
#
# class Reader:
#
#     def readExcel(self):
#         pass
#
#     @staticmethod
#     def readDoc():
#         pass
#
#     @staticmethod
#     def readPdf():
#         pass
#
# r = Reader()
# r.readDoc()
#
# Reader.readDoc()









class Person:
    def __init__(self, name, birthYear, gender):
        self.name = name
        self.birthYear = birthYear
        self.gender = gender


    @property  # 把一个方法编程了一个属性
    def age(self):
        print("哈哈哈")
        # 计算年龄
        return 2019 - self.birthYear

p1 = Person("蔡徐坤", 1988, "男")
p2 = Person("高进", 1932, "男")
p3 = Person("伊丽莎白鼠", 1887, "男")

#
print(p1.birthYear)
print(p1.age)  # 用的时候是属性. 本质是方法
print(p2.age)

# 回去自己搜. 如何能够 p1.age = 18

# 属性: 名字, 年龄, 性别....
# 动作: 年龄