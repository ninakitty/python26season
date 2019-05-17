# class Phone:
#     def __init__(self, pinpai, price, color, cpu, memory, xiangsu):
#         pass
#     def call(self):
#         pass
#     def play(self):
#         pass
#     def takePhoto(self):
#         pass
#     def video(self):
#         pass
#     def music(self):
#         pass
#     def send(self, message):
#         pass
#
# p1 = Phone(xxxxxx)









# 汪峰 开演唱会


# Singer
#   属性: name. salary, gender, songs
#   动作: 唱歌, 开演唱会
# 汪峰开演唱会

class Singer:
    def __init__(self, name, salary, gender, songs=[]):
        self.name = name
        self.salary = salary
        self.gender = gender
        self.songs = songs

    def sing(self, song):
        print(f"{self.name}在唱{song}")

    def yanchang(self):
        # 从头唱到尾
        for item in self.songs: # 歌曲
            self.sing(item)


wf = Singer("汪峰", 12000, "男", ["怒放的生命", "北京 北京", "飞的更高"])

wf.sing("青花瓷")

wf.yanchang()


# 写一个银行账户. 存钱, 取钱    动作
class Account:
    def __init__(self, card, password, money=0):
        self.card = card
        self.password = password
        self.money = money

    def save(self):
        # 思路一, 从外界传递卡号和money
        # if card == self.card:
        #     self.money += money
        # 思路二, 内部直接获取到卡号和money
        card = input("请输入你的卡号:")
        if self.card == card:
            money = int(input("请输入你要存的钱"))
            self.money += money
        else:
            print("卡号不对")

    def get(self):
        card = input("请输入卡号")
        psw = input("请输入密码")
        if card == self.card and psw == self.password:
            money = int(input("请输入取款金额:"))
            if money <= self.money:
                print("取钱成功")
                self.money -= money
            else:
                print("余额不足")
        else:
            print("账号或密码错误")


    def display(self):
        print(self.money)

acc = Account("10086", "123456", 5800)
acc.get()
acc.get()
acc.display()
