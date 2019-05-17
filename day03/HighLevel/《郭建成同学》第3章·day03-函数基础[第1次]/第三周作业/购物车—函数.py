flag = True
# 登陆功能
def login():
    global flag
    n = 0
    with open("用户信息", "r", encoding="utf-8") as f:
        while n < 3:
            user_input_name = input("请输入您的用户名：").strip()
            user_input_pwd = input("请输入您的密码：").strip()
            for line in f :
                new_line = line.strip().split(" ")
                if user_input_name == new_line[0] and user_input_pwd == new_line[1]:
                    print("登陆成功")
                    flag = False
                    break
            else:
                print("用户名或密码错误，请重新输入：")
                n += 1
                continue
            break
        shopping()

# 注册功能
def register():
    # 先读再写入
    with open("用户信息", "r+", encoding="utf-8") as f:
        while 1:
            user_name = input("请输入您要注册的用户名：").strip()
            user_password = input(("请输入您的密码：").strip())
            for line in f:
                new_line = line.strip().split(" ")
                if user_name == new_line[0]:
                    print("用户名已存在，请重新输入：")
                    break
                else:

                    f.write("\n"+user_name+" "+user_password)
                    print("注册成功")
            break

# 购物功能

def shopping():
    global flag
    if flag == False:             #判断是否登陆
        product_list = [{"name": "电脑", "price": 1999},
                        {"name": "鼠标", "price": 500},
                        {"name": "键盘", "price": 999},
                        {"name": "低音炮", "price": 2222},
                        {"name": "硬盘", "price": 666}
                        ]
        shopping_car = {}
        flag = True
        while flag:
            # 用户先给自己的账户充钱
            user_account = input("please input your money:").strip()
            # 判断输入是否合法
            if user_account.isdigit():
                user_account = int(user_account)
                break
            else:
                print("invalid input")
        while flag:
            for i, v in enumerate(product_list):
                print("{}\t{}\t{}".format(i + 1, v["name"], v["price"]))
                # 用户输入自己想要的商品编号
            user_choice = input("请选择商品编号[exit:q or Q,Shopping settlement:n or N]: ").strip()
            # 判断输入是否合法
            if user_choice.isdigit():
                user_choice = int(user_choice)
                if user_choice > 0 and user_choice < len(product_list)+1:
                    # 将购买得商品放入购物车
                    if user_choice not in shopping_car:
                        shopping_car[user_choice] = {"name": product_list[user_choice - 1]["name"],
                                                     "price": product_list[user_choice - 1]["price"],
                                                     "account": 1
                                                     }
                    else:
                        shopping_car[user_choice]["account"] += 1
                    print(
                        "商品：{},价格：{}，已添加到购物车".format(shopping_car[user_choice]["name"], shopping_car[user_choice]["price"]))
                else:
                    print("输入有误，请重新输入：")
                    # 另一种情况，退出，直接退出程序即可
            elif user_choice in ["q", "Q"]:
                flag = False
                print("欢迎下次光临")
                break
                # 结算情况
            elif user_choice in ["n", "N"]:
                # 展示给顾客自己买的商品，进行购物车得遍历
                print("您想要购买的商品如下：")
                for id, value in shopping_car.items():
                    print("{}.{}\t单价:{}\t数量{}".format(id, value["name"], value["price"], value["account"]))
                    # 计算一下自己的账户的钱是否够支付买的东西，进行个循环，直到可以购买
                while True:
                    sum = 0
                    # 计算购物费用，遍历price
                    for id, value in shopping_car.items():
                        sum += value["price"] * value["account"]
                        # 钱够的话直接购买
                    if user_account >= sum:
                        user_balance = user_account - sum
                        print("您已经成功购买下述商品，", f"您本次消费{sum}元，账户余额{user_balance}元，", "欢迎下次光临")
                        for id, value in shopping_car.items():
                            print("{}.{}\t单价：{}\t数量：{}".format(id, value["name"], value["price"], value["account"]))
                        flag = False
                        break
                            #     余额不足的情况
                    else:
                        print("但是您的余额不足，请删除一些商品再结算")
                        # 同上，就是进行合法性判断和将选中的购物车商品删除
                        user_choice_2 = input("请选择你要删除的商品的编号：").strip()
                        if user_choice_2.isdigit():
                            user_choice_2 = int(user_choice_2)
                            if user_choice_2 in shopping_car:
                                shopping_car[user_choice_2]["account"] -= 1
                                if not shopping_car[user_choice_2]["account"]:
                                    sum -= int(shopping_car[user_choice_2]["price"])
                                    del shopping_car[user_choice_2]
                            else:
                                print("输入有误")
                        else:
                            print("请输入商品编号")
            else:
                print("输入有误，请重新输入：")

    else:
        print("您还没有登陆，请先登陆")
        login()
# 刚开始展示给用户的内容
def show():
    str = "欢迎进入购物系统"
    print(str.center(20,"="))
    print("1、注册\n"
          "2、登陆\n"
          "3、购物\n"
          "4、退出")

# 程序启动
def start():
    while True:
        show()
        user_choice = input("请输入您的选择：").strip()
        if user_choice == "1":
            register()
        elif user_choice == "2":
            login()
            break
        elif user_choice == "3":
            shopping()
            break
        elif user_choice == "4":
            break
        else:
            print("输入有误，请重新输入：")
start()
