name = '张三'


def func():
    print('我是func')


class Person():
    def __init__(self, p_name, age):
        self.name = p_name
        self.age = age

    def chi(self):
        print(f'{self.name}在吃')


if __name__ == '__main__':
    p = Person('tom', 20)
    p.chi()
