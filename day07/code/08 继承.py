# class A:
#     def chi(self):
#         print("我要吃A")
#
#
# class B:
#     def chi(self):
#         print("我要吃B")
#
#
# class C(B, A):
#     def chi(self):
#         print("我要吃C")
#
#     def he(self):
#         # self.chi() # 调用的是自己类中的方法
#         super(B, self).chi() # 从C开始向下找一个
#         super().chi()
#         super(C, self).chi()
#
#         # (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>)
#
# # MRO  Method, Resolution, Order
#
#
#
# c = C()
# c.he()
# print(C.__mro__)

# class A:
#     def chi(self):
#         print("我要吃A")
#
# class B(A):
#     def chi(self):
#         print("我要吃B")
#
# class C(B):
#     def chi(self):
#         print("我要吃C")
#
# class D(C):
#     def chi(self):
#         print("我要吃D")
#         super(B, self).chi()


# d = D()
#
# print(D.__mro__)
#
# d.chi()


class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.staff_list = []

class Branch(School):
    def __init__(self, name, address, leader):
        self.leader = leader
        # 调用父类的构造
        super(Branch, self).__init__(name, address)


Branch("北大", '沙河', "alex")

# MRO ->  c3



