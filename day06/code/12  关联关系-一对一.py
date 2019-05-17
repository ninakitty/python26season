
class Boy:
    def __init__(self, name, age, girlFriend = None):
        self.name = name
        self.age = age
        self.grilFriend = girlFriend

    def watch(self):
        if self.grilFriend:
            print(f"{self.name}和{self.grilFriend.name}看电影")
        else:
            print("单身狗没有权利看电影")

class Girl:
    def __init__(self, name, age):
        self.name = name
        self.age = age

g = Girl("苍老师", 35)
b = Boy("alex", 18)

# print(b.grilFriend.name)
b.watch()

