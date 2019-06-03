# a = 10
# print(type(a))
# print(int)
#
# class Person:
#     pass
#
# p = Person()
# print(type(p))
# print(Person)


# class Animal:
#     pass
#
# class Cat(Animal):
#     pass
#
# c = Cat()
#
# print(type(c)) # <class '__main__.Cat'>
#
# print(isinstance(c, Cat))
# print(isinstance(c, Animal)) # xxx对象是否是xxx类型的(向上判断)
#
# a = Animal()
# print(isinstance(a, Animal))
# print(isinstance(a, Cat)) # False

# class Animal:
#     pass
#
# class Cat(Animal):
#     pass
#
# print(issubclass(Animal, Cat)) # False
# print(issubclass(Cat, Animal)) # True


def func(a, b):
    """
    求和
    :param a:  第一个数据
    :param b:  第二个数据
    :return:   两个数据的和
    """
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        return a + b
    else:
        return "错误"

class Person:
    pass

p = Person()
print(func(2.2, 1))
