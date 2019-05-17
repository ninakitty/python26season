# from urllib.request import urlopen
# import re
#
# website = 'http://2019.ip138.com/ic.asp'
# content = urlopen(website).read().decode('gbk')
# item = re.finditer(r'您的IP是：\[(?P<IP>.*?)\] 来自：(?P<come>.*?)</center>', content)
# for i in item:
#     print(i.group('IP'))
#     print(i.group('come'))
#
#
# class Car(object):
#     color = '111'
#
#     def fly(self):
#         print('车能飞')
#
#     def run(self):
#         print('车能跑')
#
#     def gotohell(self):
#         print('上西天')
#
#     def __init__(self, color, price, make):
#         self.color = color
#         self.price = price
#         self.make = make
#
#
# c1 = Car('黄',12.5, '法拉利')
# c2 = Car('绿色', 90, '奥拓')
# print(Car.color)
# # print(c2.color)

#
# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def chi(self, something):
#         print(f'{self.name}在吃{something}')
#
#
# p = Person('张三', 20, '男')
# p.chi('香蕉')

# # 汪峰 在开演唱会
# class Singer:
#     def __init__(self, name, age, salary, songs):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.songs = songs
#
#     def song(self, song):
#         print(self.name, '在唱', song)
#
#     def vocal_concert(self):
#         for item in self.songs:
#             self.song(item)
#
#
# s = Singer('汪峰', 50, 200, ['歌1', '歌3', '歌3'])
# s.vocal_concert()
# s.song('石器时代的歌')


# 写银行帐户,存钱,取钱
# class Account:
#     def __init__(self, user, passwd, money):
#         self.user = user
#         self.passwd = passwd
#         self.money = money
#
#     def get_money(self, get_num):
#         self.money -= get_num
#         print(f'取出{get_num},帐户余额:{self.money}')
#
#     def save_money(self, save_num):
#         self.money += save_num
#         print(f'存入{save_num},帐户余额:{self.money}')
#
#     def show_money(self):
#         print(f'您的余额:{self.money}')
#
#     def verify(self, fn):  # 验证
#         flag = False
#
#         def inner(*args, **kwargs):
#             name = input('请输入帐号:')
#             password = input('请输入密码:')
#             if self.user == name and self.passwd == password:
#                 res = fn(*args, **kwargs)
#                 return res
#             else:
#                 return flag
#
#         return inner()
#
#
# a1 = Account('张三', '111', 200)
# a1.show_money()
# a1.save_money(100)
# a1.show_money()

# class Father:
#     print('父类中的打印')
#
#     def onfoot(self):
#         print('父类onfoot')
#
#
# class Son(Father):
#     pass
#
#
# son = Son()
# son.onfoot()


# class Person:
#     Country = '大清'
#
#     def __init__(self, name, birthyear, gender):
#         self.name = name
#         self.birthyear = birthyear
#         self.gender = gender
#
#     def eat(self):
#         print('吃')
#
#     @staticmethod
#     def drink():
#         print('喝')
#
#     @staticmethod
#     def sleep():
#         print('睡')
#
#     @property
#     def age(self):
#         return 2019 - self.birthyear
#
#     def age(self, value):
#         self.age = value
#
#
# p1 = Person('tom', 1980, 'male')
# print(p1.age)

# 依赖关系
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def play(self, phone):  # 此处形成依赖关系
#         phone.wangzherongyao()
#
#
# class Phone:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def wangzherongyao(self):
#         print(self.name, '打王者荣耀')
#
#
# person1 = Person('jerry', 10)
# phone1 = Phone('mi', 200)
# phone2 = Phone('Iphone', 100)
# person1.play(phone1)
# person1.play(phone2)

# 关联关系
# class Teacher:
#     def __init__(self, name, students=[]):
#         self.name = name
#         self.students = students
#
#     def lesson(self):
#         print(self.name, '在上课')
#         for stu in self.students:
#             stu.study()
#
#
# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     def study(self):
#         print(self.name, '在学习')
#
#
# student_list = []
# for i in range(1, 5):
#     student = Student(f'学生{i}')
#     student_list.append(student)
#
# teacher = Teacher('Tom', student_list)
# teacher.lesson()

# 面试题
# def mul():
#     return [lambda x: x * i for i in range(4)]
#
#
# print([m(2) for m in mul()])
