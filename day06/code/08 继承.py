# class NiuMoWang:
#     def fly(self):
#         print("牛魔王会飞")
#
# class HongHaiEr(NiuMoWang):
#     pass
#
#
# hhe = HongHaiEr()
# hhe.fly()  # 通过子类的对象访问父类中的方法
#
#
# class Talk:
#     def qq(self):
#         pass
#
#     def wechat(self):
#         pass
#
# class Phone(Talk):
#     def call(self):
#         pass
#
#
# class Computer(Talk):
#     def play(self):
#         pass
#
# c = Computer()
# c.qq()
# c.wechat()
# c.play()
# c.call()

#
# class Fa:
#     def chi(self):
#         print("Fa")
#
# class Die:
#    pass
# class Ba:
#     def chi(self):
#         print("Ba")
#
# class Ma:
#     def chi(self):
#         print("Ma")
#
# class Son(Die, Fa, Ba, Ma): # 先找亲爹. 然后找后面的干爹
#     def chi(self):
#         print("SON")
# s = Son()
# s.chi()
# # mro: METHOD RESOLUTION ORDER, C3 算法

# 猫是动物    动物是会动的.  => 猫是会动的



class Animal:
    def dong(self):
        print("在动")

class Cat(Animal):
    def eatFish(self):
        print("猫爱吃鱼")

class LiuLangCat(Cat):
    pass


class Employee:
    pass

class Teacher(Employee):
    pass


class Role:
    def bit(self, diren):
        pass

class Plant(Role):
   pass


class Jiang(Role):
   pass


