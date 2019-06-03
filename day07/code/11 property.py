class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name+"_sb"

    @name.setter  # p.name = 值
    def name(self, _name):
        self.__name = _name


p = Person("alex")
print(p.name)

p.name = "哈哈"
print(p.name)