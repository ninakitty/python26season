# def a(**kwargs):
#     return kwargs
#
# f = open(r"a1.txt",mode="r",encoding='utf-8')
# for line in f:
#     a(**line)
# import copy
# a = [1,2,3,4,["a","b","c"]]
# b = copy.copy(a)
# print(id(a),id(b))
# #a.append("5")
# # print(a,b)
# b.append("6")
# # print(a,b)
# print(id(a),id(b))
# print("------------------------------------------------------------------------")
# c = copy.deepcopy(a)
# print(id(a),id(b))
# a.append(6)
# c.append(7)
# # print(a,c)
# # print(id(a),id(c))
# a = [11,2,3,4]
# f = open(r"a1.txt",mode="a",encoding='utf-8')
# f.write("ccccc")
# f.close()
# f = open(r"a1.txt",mode="r",encoding="utf-8")
# for line in f:
#     print(line)

# with open(r"a1.txt",mode="a",encoding='utf-8') as f:
#     f.write("\nddddddddddccccfadfadfaddd")
# total_price = 0
# with open(r"a1.txt",mode="r",encoding="utf-8") as f:
#     for line in f:
#         total_price += int(line.strip( ).split()[1])*int(line.strip( ).split()[2])
# print(total_price)

# with open(r"a1.txt",mode="a",encoding="utf-8") as f:
#     for line in f:
#         line.strip().startswith("apple")
#         line.strip().replace("apple","banana")

# count = 0
# a = "abcd34faf"
# for i in a:
#     count +=1
#     print(i)

# def test(s1):
#     return s1
#
# ret = test("aaa")
# print(ret)

# def info(name,sex,age=20):
#     return("你的名字是：%s性别是：%s年龄是：%s"%(name,sex,age))
#
# ret1 = info("mcl","man")
# print(ret1)
# a = [2,3,4,5]
# b = {"a":"aa","b":"bb","c":"cc"}
# def info(*args,**kwargs):
#     print(args,kwargs)
#
#
# info(1,2,3,4,a = "test1",b="test2")
# info(*a,**b)
# with open(r"a1.txt",mode="r",encoding="utf-8") as f:
#    l = []
#    f1 = f.readline().split()
#    for i in f:
#        dic = {}
#        for k in range(len(f1)):
#            dic[f1[k]] = i.split()[k]
#            l.append(dic)
# print(l)
#


# def three(a,b):
#     if int(a) > int(b):
#         return a
#     else:
#         return b
# ret = three(5,2)
# print(ret)

#第四题
# a = {"a":1,"b":123456,"c":"lkjh","d":"9","e":"11111"}
#
# def four(**kwargs):
#     for key,values in kwargs.items():
#         if len(str(values)) >2:
#             kwargs[key] = (str(values)[:2])
#     return kwargs
#
#
# ret = four(**a)
# print(ret)

#第五题
# def five(*args):
#     dist = {}
#     for index,values in enumerate(args):
#         dist[index] = values
#     return dist
#
# l = [1,2,3,4,5,6,11111,11111,3333]
# ret = five(*l)
# print(ret)

#第六题

# def sign_up(username,password):
#     dit = {}
#     with open(r"userfile", mode="a", encoding="utf-8") as f:
#         for line in f:
#             if username not in line:
#                 user = input("请输入您想要注册的用户名：")
#                 passwd = input("请输入你的密码")
#                 dit[user] = passwd
#                 f.write("\ndit")




#

import os

def test_file():
    ret = os.path.getsize("user")
    if ret == 0:
        print("请注册")

def login():
    user = input("请输入用户名：")
    with open(r"user",mode="r",encoding="utf-8") as f:
        for line in f:
            if user == line.strip().split(",")[0]:
                password = input("请输入密码:")
                count = 0
                while count < 3:
                    if password == line.strip().split(",")[1]:
                        print("登录成功")
                        break
                    else:
                        password = input("密码错误请重新输入密码：")
                        count +=1
                break
#    print("用户名不存在请注册")

def register():
    user = input("请输入注册的用户名：")
    with open(r"user", mode="r+", encoding="utf-8") as f:
        for line in f:
            if user != line.strip().split(",")[0]:
                password = input("请输入密码:")
                f.write(user+","+password+"\n")
                break
            else:
                print("用户名存在")
def shopping():
    shopping_car = []
    sum_amount = 0
    amount = int(input("请输入你的充值金额:"))
    sum_amount += amount
    payment = 0
    print("你可以输入Q或者q结束，按n或者N进行结算")
    print("你的总金额为:%s" % sum_amount)
    print("--------------------------")
    shopping_list = [{"电脑": 1999}, {"鼠标": 10}, {"iphone": 6000}, {"相机": 13000}]
    for index, value in enumerate(shopping_list):
        print(index + 1, value)
    print("-------------------------")
    while True:
        choice = input("请输入你想选购的商品或者输入n结算:")
        if choice.isdigit():
            if int(choice) < len(shopping_list) + 1:
                shopping_car.append(shopping_list[int(choice) - 1])
                #            print(shopping_list[int(choice) - 1])
                print("你已经购买了%s" % (shopping_car))
            else:
                print("请重新输入正确的编号")
        else:
            if str(choice) == "Q" or str(choice) == 'q':
                shopping_list.clear()
                print("再见")
                break
            elif choice == "N" or choice == "n":
                for i in shopping_car:  # 循环购物车列表
                    payment += int(list(i.values())[0])  # 购物车总钱数
                while payment > sum_amount:  # 比较总钱数和购物总价格
                    for index1, value1 in enumerate(shopping_car):
                        print(index1 + 1, value1)

                    del_shopping = int(input("商品总额大于你的钱数，请删除一些商品（序列号）:"))
                    #                print(sum_amount)
                    print("购物总价格为:%s" % payment)
                    payment -= (list(shopping_car[del_shopping - 1].values())[0])  # 剩余购物总钱数
                    shopping_car.pop(del_shopping - 1)
            break
    print("你已购东西为：%s，剩余金额为:%s元" % (shopping_car, sum_amount - payment))

while True:
    choice = input("请输入你的选择：login|register|shopping|q:")
    if choice == "register":
        register()
    elif choice == "login":
        ret = os.path.getsize("user")
        if ret == 0:
            register()
            login()
        else:
            login()
        print("登录成功可以开始购物")
        shopping()
    elif choice == "shopping":
        print("先登录")
        login()
        print("登录成功可以开始购物")
        shopping()
    elif choice == "q":
        print("拜拜")
        exit()








