
print("哈哈哈哈哈哈ah")

name = "alex"

def change():
    global name
    name = "wusir"


def func():
    print("我是func")

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def chi(self):
        print("人喜欢吃东西")

# 模块名 #
# __main__  当前py文件作为启动文件
# master     当py文件作为模块被导入的时候
# print(__name__)

# 测试代码


# 被称为程序的入口
if __name__ == '__main__':
    p = Person("alex", 18)
    p.chi()
