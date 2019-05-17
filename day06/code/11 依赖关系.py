# 类与类之间最松散的一种关系
#  在执行某个方法的时候把另外一个类的对象传递进来

class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def play(self, dianhua): # 通过传参产生了联系
        print(self.name)
        print(dianhua.name)
        dianhua.yunxingWangZhe()

class Phone:
    def __init__(self, name, pinpai, price):
        self.name = name
        self.pinpai = pinpai
        self.price = price

    def yunxingWangZhe(self):
        print(self.name + "在打王者荣耀")

dh = Phone("Iphone7", "大苹果", 120)
dh2 = Phone("小米888888", "MI", 150)
p = Person("alex", "男")
p.play(dh2)


