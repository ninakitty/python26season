class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def run(self):
        print("人会跑")

    def chi(self, food):
        print(f"{self.name}人吃 {food}")

p = Person("jay", 28, "男")
p.run()

# Person.chi(p)  # 是可以的. 但不要这么去用

# 打印出xxxx在吃xxxxx
p.chi("黄瓜")

