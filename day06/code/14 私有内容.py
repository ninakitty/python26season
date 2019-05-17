class Person:
    __name = "哈哈"
    def __init__(self, secrect):
        self.__secrect = secrect

    def dalaba(self):
        return self.__secrect

    def __chi(self):
        print("很能吃")

p = Person("今天吃了500块钱的馒头")
# print(p.__secrect)  # 这里不能访问
print(p.dalaba())
p.__chi()
