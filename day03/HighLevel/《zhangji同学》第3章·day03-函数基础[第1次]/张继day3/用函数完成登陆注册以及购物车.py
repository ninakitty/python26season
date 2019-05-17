#: @author: zhangji
#: @Time:   2018/9/7 00:50
#: @Email:  492577928@qq.com
# -*- encoding:utf-8 -*-

###定义提示函数
def select():
    print("""
1 登陆
2 注册
3 购物
4 退出
    """.strip())

###定义登陆函数
def login():
    global flag
    number = 3
    while number >0:
        user_name = input("请输入你的用户名: ")
        user_passwd = input("请输入你的密码: ")
        with open("用户信息", encoding="utf-8") as f:
        #文件操作打开已经存好的用户信息
            for i in f:
                k = i.strip().split("&&")
                if user_name == k[0] and user_passwd == k[1]:
                    print("登陆成功")
                    flag = False
                    break
            else:
                number = number - 1
                print("账户或密码错误，登陆失败,你还有%s次机会" %(number))
                continue
            break


##定义注册函数
def register():
    while 1:
    #定义循环如果提示账户已存在还可以重新注册
        your_name = input("请输入你要注册的账户名: ")
        your_passwd = input("请输入你的密码: ")
        #获取用户输入的信息
        with open("用户信息",encoding="utf-8") as f:
        #以读的方式打开用户信息文件
            for line in f:
                line = line.strip().split("&&")
                #去掉空格，过滤&&中间字符，直接得到账户和密码信息
                if your_name == line[0]:
                #判断输入的账户是否已存在
                    print("此账户已存在,请重新输入")
                    break
            else:
            #不存在就进行注册
                with open("用户信息",mode="a",encoding="utf-8") as f2:
                #已追加写的方式打开用户信息文件
                    f2.write('\n'+your_name+"&&"+your_passwd)
                    #追加写入用户名和密码
                    print("注册成功")
                    break


##定义购物车函数
def shoping():
    if flag == False:  # 判断有没有登录
        product_dic = {}
        #定义空字典，用来接受商品清单
        shop_card = {}
        #定义购物车字典，用来接受用户购物的商品信息和数量
        with open("商品清单",encoding="utf-8") as f_list:
            for i in f_list:
                k = i.strip().split(" ")
                for j in range(len(k)):
                    product_dic[k[0]] = [k[1],k[2]]
        #打开文件商品清单，将文件读出来，并已字典的方式存到product_dic中
        money = input("请输入充值金额: ")
        if not money.isdigit():
            print("输入有误")
            exit()
        #判断用户输入的是否为数字
        fei_yong = 0
        # 定义初始费用
        while True:
            for m in product_dic:
                print(m, product_dic[m][0], product_dic[m][1])
            #打印商品信息
            buy = input('请输入您要购买的商品序号(N/结算 -- Q/退出):')
            if buy.isdigit() and 0 < int(buy) <= len(product_dic):
            #判断用户输入的是否是商品清单的序号
                int_index = int(buy)
                if shop_card.get(int_index) == None:
                #判断是否是第一次购买改商品，如果是第一次购买，数量=1
                    shop_card[int_index] = 1
                    fei_yong = fei_yong + int(product_dic[str(int_index)][1])
                    #计算购买此商品产生的费用
                    print("你已选购商品%s,数量%s" % (product_dic[str(int_index)][0],shop_card[int_index]))
                else:
                #如果不是第一次购买，则商品数量+1
                    shop_card[int_index] =  shop_card[int_index] + 1
                    fei_yong = fei_yong + int(product_dic[str(int_index)][1])
                    # 计算购买此商品产生的费用
                    print("你已选购商品%s,数量%s" % (product_dic[str(int_index)][0],shop_card[int_index]))

            elif buy.upper() == 'N':
            #结算功能
                    if int(money) - fei_yong >= 0:
                    #判断用户充值金额是否能够支付购物产生的费用
                        for p in shop_card:
                            print(f'您购买的商品是{product_dic[str(p)][0]},单价{product_dic[str(p)][0][1]},数量{shop_card[p]}')
                    else:
                    #如果不够支付消费，则提示余额不足
                        print('余额不足')
                        print("已购商品清单》》》》》")
                        for n in shop_card:
                            print("序号:%s    商品名称:%s    单价:%s   数量:%s" %(n,product_dic[str(n)][0],product_dic[str(n)][1],shop_card[n]))
                        #打印用户已购买的商品详细信息

                        str_del = input('请选择要删除的商品序号:')
                        #让用户选择要删除的商品

                        if shop_card[int(str_del)] == 1:
                        # 判断这个商品在购物车中是不是就是一个
                            shop_card.pop(int(str_del))
                            # 是一个的时候就直接把这个商品从购物车中删除
                            fei_yong = fei_yong - int(product_dic[str(str_del)][1])
                            #计算删除此商品后的费用
                        else:
                            shop_card[int(str_del)] = shop_card[int(str_del)] - 1
                            # 说明购物车中这个商品不止一个,对这个商品的数量进行-1
                            fei_yong = fei_yong - int(product_dic[str(str_del)][1])
                            # 计算删除此商品后的费用

            elif buy.upper() == 'Q':
                # 退出
                print(f'您此次购物消费了{fei_yong},剩余余额{int(money) - fei_yong}')
                #打印，本次购物的消费和余额
                break
            else:
                print('输入有误,请重新输入!')
    else:
    # 没有登录的话执行登录函数
        print('您还没有登录,请先登录!')
        login()
        shoping()


flag = True
#定义一个变量，用来判断用户是否登录
def main():
#定义main函数完成流程控制
    while True:
        select()
        #调用提示函数，让用户选择操作
        choice = input('请输入选项:')
        if choice == '1':
            login()
            #调用登录函数
            continue
        elif choice == '2':
            register()
            #调用注册函数
            continue
        elif choice == '3':
            shoping()
            #调用购物函数
            continue
        elif choice == '4':
            break
            #退出程序
        else:
            print('输入有误,请重新输入')
        break
main()









