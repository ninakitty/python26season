
# # 先有图纸. 先写类
# class Car:
#     # 飞
#     def fly(self):
#         print("车会飞")
#     # 跑
#     def run(self):
#         print("车能跑")
#
#     # 上西天
#     def gotohell(self):
#         print("上西天")
#
# # 造车
# # 创建对象 类名()
# c = Car()
# c.fly()
# c.run()
# c.gotohell()
#
# c2 = Car()
# c2.fly()
# c2.run()
# c2.gotohell()
#
# lst1 = list()
# lst2 = list()
#
# "aba".split()
#
#
# lst1.append(123)
# lst1.append(456)
# print(lst1)
# print(lst2)


# 先有图纸. 先写类
class Car:
    # self 是对象本身
    # 飞
    def fly(self):
        print("车会飞")
    # 跑
    def run(self):
        print("车能跑")
    # 上西天
    def gotohell(self):
        print("上西天")

    # 初始化操作
    def __init__(self, color, price, pinpai):
        print(self)
        self.color = color
        self.price = price
        self.pinpai = pinpai


lst = list()

c = Car("红色", 1.25, "发啦率") #  车没有属性
print(c.color)

# print(c.color)
# c.set("绿色", 12.5, "法拉利")
# print(c.color)
# print(c)

c2 = Car("绿色", 1.25, "玛莎拉蒂")
print(c2.color)







