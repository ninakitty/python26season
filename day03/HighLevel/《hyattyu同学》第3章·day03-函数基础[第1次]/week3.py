import sys
print('''
1.登陆
2.注册
3.购物
4.退出
''')
def login():
    userinfofile = open("userinfo",'r',encoding='utf-8')
    username = []
    password = []
    for line in userinfofile:
        line = line.strip()
        username.append(line.split(" ")[0])
        password.append(line.split(" ")[1])

    inputAccount = input("请输入用户名")
    inputPwd = input("请输入密码")
    userinfofile.close()
    for index in range(len(username)):
        if username[index] == inputAccount:
            if password[index] == inputPwd:
                print("登陆成功")
                return True
            else:
                print("用户名或密码错误")
                return False
    print("用户不存在")
    return False

def register():
    inputAccount = input("请输入用户名")
    inputPwd = input("请输入密码")
    userinfofile = open("userinfo", 'a', encoding='utf-8')
    userinfofile.write(inputAccount + " " + inputPwd+"\n")
    print("注册成功")
    userinfofile.close()


def shopping():
    money = int(input("请输入充值金额").strip())
    # money=10000;
    item_list = [
        {"name": "iphone4", "price": 1000},
        {"name": "iphone5", "price": 2000},
        {"name": "iphone6", "price": 3000},
        {"name": "iphone7", "price": 4000},
        {"name": "iphone8", "price": 5000},
        {"name": "iphoneX", "price": 6000}
    ]
    i = 0
    for item in item_list:
        print("编号：{} 商品：{} 价格：{}".format(i+1, item["name"], item["price"]))
        i += 1
    shopping_list = {}
    sum_price = 0
    balance = money
    while True:
        item_number = int(input("请输入要购买的商品编号").strip())-1
        if item_number > len(item_list) :
            print("输入错误，请重新输入")
            continue
        if int(item_list[item_number]["price"]) < balance:
            shopping_list[item_list[item_number]["name"]] = item_list[item_number]["price"]
            sum_price = sum_price + int(item_list[item_number]["price"])
            balance = money - sum_price
            print("购物车商品{}".format(shopping_list))
            print("余额{}".format(balance))
            quit = input("是否继续购物Y/Q")
            if quit.upper() == "Q":
                for shoppingitem in shopping_list:
                    print("商品 {} 价格 {}".format(shoppingitem, shopping_list[shoppingitem]))
                break
        else:
            print("余额不足")
            quit = input("是否继续购物Y/Q")
            if quit.upper() == "Q":
                for shoppingitem in shopping_list:
                    print("商品{} 价格 {}".format(shoppingitem, shopping_list[shopping_item]))
                break

            while True:
                delet_item = int(input("请选择要删除的商品").strip())
                flag = False
                for shopping_item in shopping_list:
                    if item_list[delet_item]["name"] == shopping_item:
                        del shopping_list[shopping_item]
                        print("删除成功")
                        flag = True
                        break
                    else:
                        print("商品不在购物车")
                if flag:
                    break
            print("购物车商品{}".format(shopping_list))
            balance = balance + int(item_list[item_number]["price"])
            sum_price = sum_price - int(item_list[item_number]["price"])

choice = input("请输入数字选择需要的服务")


if choice=='1':
    loginresult = login()
elif choice == '2':
    register()
elif choice == '3':
    #if login():
    shopping()
elif choice =='4':
    print ('退出')
    sys.exit()
else:
    pint ('输入错误')