'''
用函数完成登录注册以及购物车的功能
作业需求:
1，启动程序，用户可选择四个选项：登录，注册，购物，退出。
2，用户注册，用户名不能重复，注册成功之后，用户名密码记录到文件中。
3，用户登录，用户名密码从文件中读取，进行三次验证，验证不成功则退出整个程序。
4，用户登录成功之后才能选择购物功能进行购物，购物功能（就是将购物车封装到购物的函数中）。
5，退出则是退出整个程序。
'''
'''
分析:将用户信息保存到文件userinfo.txt(不考虑多个账号同时使用)
存储格式为{"alex":{"pwd":"123456", "status":"logged", "money": 8000, "shopping":{}},
            "wusir":{"pwd": "123456", "status":"logout","money": 6000, "shopping":{}},
            ......
            }
'''
filename = "userinfo.txt"
usr = ""
#用户注册
def register():
    while 1:
        usr = input("Register Username: ").strip()
        pwd = input("Register Password: ").strip()
        # 判断用户名和密码是否合法
        if usr != "" and pwd != "":
            if len(usr) < 3 or len(usr) > 30:
                print("\033[31;0m用户名的长度必须在3~30.\033[0m")
                continue

            if len(pwd) < 6 or len(pwd) > 20:
                print("\033[31;0m密码的长度必须在6~20.\033[0m")
                continue

            # 读文件判断用户是否存在,存在则提醒已存在,不存在则直接添加
            with open(filename, mode="r", encoding="utf-8") as f1,\
                    open("%s.bak" % filename, mode="w", encoding="utf-8") as f2:
                content = f1.read().strip()
                usr_dic = {}
                if content != "":
                    usr_dic = eval(content)
                if usr in usr_dic:
                    print("\033[31;0m注册失败, 用户名: %s已存在!\033[0m" % usr)
                    return
                else:
                    usr_dic[usr] = {"pwd": pwd}
                    f2.write(str(usr_dic))

            import os
            os.remove(filename)
            os.rename("%s.bak" % filename, filename)
            print("\033[32;0m恭喜您,用户名: %s注册成功!\033[0m" % usr)
            return True
        else:
            print("\033[31;0m用户名和密码不能为空!\033[0m")

#用户登录
def login():
    while 1:
        usr = input("Login Username: ").strip()
        pwd = input("Login Password: ").strip()
        # 判断用户名和密码是否为空
        if usr != "" and pwd != "":
            #判断文件是否存在,不存在直接创建空文件
            import os
            if not os.path.exists(filename):
                f = open(filename, mode="w", encoding="utf-8")
                f.close()

            #读文件,判断用户名和密码是否正确
            with open(filename, mode="r", encoding="utf-8") as f:
                content = f.read().strip()
                usr_dic = {}
                if content != "":
                    usr_dic = eval(content)
                if usr in usr_dic:
                    #登录成功
                    if usr_dic[usr]["pwd"] == pwd:
                        return usr
                #用户密或密码错误
                return
        else:
            print("\033[31;0m用户名和密码不能为空.\033[0m")

#记录用户信息
def record_stat(usr, stat="logged", money=0, shopping={}):
    with open(filename, mode="r", encoding="utf-8") as f1,\
            open("%s.bak" % filename, mode="w", encoding="utf-8") as f2:
        usr_dic = eval(f1.read().strip())
        usr_dic[usr]["status"] = stat
        usr_dic[usr]["money"] = usr_dic[usr].get("money", 0) + money
        if shopping != {}:
            sp_dic = usr_dic[usr].get("shopping", {})
            new_dic = shopping
            for k, v in sp_dic.items():
                if k in shopping:
                    v[2] += shopping[k][2]
                new_dic[k] = v
            usr_dic[usr]["shopping"] = new_dic
        f2.write(str(usr_dic))

    import os
    os.remove(filename)
    os.rename("%s.bak" % filename, filename)

#获取用户信息
def get_userinfo(usr):
    with open(filename, mode="r", encoding="utf-8") as f:
        usr_dic = {}
        content = f.read().strip()
        if content != "":
            usr_dic = eval(content)
        return usr_dic.get(usr, {})

# 用户充值
def recharge(usr):
    while 1:
        money = input("请输入您要充值的金额(元): ").strip()
        if money.isdigit():
            money = int(money)
            #获取账号余额
            usr_dic = get_userinfo(usr)
            money_total = usr_dic.get("money", 0) + money
            print("\033[31;0m恭喜您,成功充值%d元! 您的账号余额为%d元.\033[0m" % (money, money_total))
            #记录用户充值金额
            record_stat(usr, money=money)
            break
        else:
            print("输入有误,请重新输入!")
    return money_total

#购物功能
def shopping(usr):
    shopping_lst = [("电脑", 2999), ("鼠标", 30), ("键盘", 80), ("音响", 888), ("耳机", 60)]
    shopping_carts = {}

    print("\033[32;0m欢迎来到淘宝电脑城\033[0m".center(50, "*"))
    money = recharge(usr)  #账号充值
    Flag = 1
    while 1:
        #显示商品
        print("\033[32;0m商品列表\033[0m".center(50, "*"))
        print("编号\t商品名称\t商品价格")
        for i, v in enumerate(shopping_lst, 1):
            print("%d\t\t%s\t\t%s" % (i, v[0], v[1]))
        print("n\t\t商品结算")
        print("q\t\t退出")

        #用户选择商品
        choice = input("请输入您要购买的商品编号: ").strip()
        if choice.isdigit():
            choice = int(choice)
            if choice >= 1 and choice <= len(shopping_lst):
                sp_name = shopping_lst[choice-1][0]
                sp_price = shopping_lst[choice-1][1]
                #判断商品是否已在购物车
                if choice in shopping_carts:
                    shopping_carts[choice][2] += 1
                else:
                    shopping_carts[choice] = [sp_name, sp_price, 1]
                print("恭喜您,成功将商品: \033[32;0m%s\033[0m添加购物车!" % sp_name)
            else:
                print("\033[31;0m商品不存在\033[0m")
        elif choice.upper() == "N":
            while 1:
                #判断购物车是否为空
                if shopping_carts == {}:
                    print("\033[33;0m购物车空空如也!请先选择您要购买的商品,再来结算吧.\033[0m")
                    break
                #显示购物车商品
                print("\033[32;0m购物车商品信息\033[0m".center(50, "*"))
                print("序号\t商品名称\t商品单价\t商品数量")
                consume_total = 0
                for i in shopping_carts:
                    goods = shopping_carts[i]
                    print("%s\t\t%s\t\t%s\t\t\t%s" % (i, goods[0], goods[1], goods[2]))
                    consume_total += goods[1] * goods[2]

                #钱够
                if money - consume_total >= 0:
                    money -= consume_total
                    print("\033[31;0m恭喜您,商品结算成功,本次消费共: %d元, 账号余额为%d元.\033[0m" % (consume_total, money))
                    Flag = 0
                    #更新用户余额和已购买商品信息
                    record_stat(usr, shopping=shopping_carts, money=-consume_total)
                    return shopping_carts
                else:
                    print("\033[31;0m商品总金额: %d元, 您还差 %d元.\033[0m" % (consume_total, consume_total-money))
                    del_choice = input("请选择您要删除的商品序号: ").strip()
                    if del_choice.isdigit():
                        del_choice = int(del_choice)
                        if del_choice in shopping_carts:
                            shopping_carts[del_choice][2] -= 1
                            if shopping_carts[del_choice][2] == 0:
                                del shopping_carts[del_choice]
                        else:
                            print("\033[31;0m输入有误,请重新输入!\033[0m")
                    else:
                        print("\033[31;0m输入有误,请重新输入!\033[0m")
        elif choice.upper() == "Q":
            break
        else:
            print("\033[31;0m商品不存在!\033[0m")

choice_lst = ["登录", "注册", "购物", "退出"]
print("\033[32;0m欢迎来到淘宝购物城\033[0m".center(50, "*"))
choice = ""

while 1:
    #显示4个选项
    for i in choice_lst:
        print(i)
    choice = input("请输入你要选的选项: ").strip()
    # 判断用户输入的选项
    if choice in choice_lst:
        if choice == "登录":
            #可以进行三次验证
            for i in range(2, -1, -1):
                usr = login()
                if usr:
                    print("\033[32;0m恭喜您,账号: %s登录成功!\033[0m" % usr)
                    #登录成功后,记录登录状态
                    record_stat(usr)
                    break
                else:
                    if i == 0:
                        print("\033[31;0m用户名或密码错误,您的账号已被锁住.\033[0m")
                    else:
                        print("\033[31;0m用户名或密码错误,您还有%d次机会.\033[0m" % i)
        elif choice == "注册":
            register()
        elif choice == "购物":
            usr_dic = get_userinfo(usr)
            if usr_dic == {}:
                print("\033[31;0m请先登录再购物!\033[0m")
            else:
                usr_dic = get_userinfo(usr)
                if usr_dic.get("status", 0) != "logged":
                    print("\033[31;0m请先登录再购物!\033[0m")
                else:
                    shopping(usr)
        elif choice == "退出":
            print("欢迎下次光临".center(50, "*"))
            #修改用户的登录状态
            if usr != "":
                record_stat(usr, stat="logout")
            break
    else:
        print("输入错误, 请重新输入!")


