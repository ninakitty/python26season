# 1. 用户先给自己的账户充钱：比如先充3000元。
# 2. 页面显示 序号 + 商品名称 + 商品价格，如：
#         1 电脑 1999
#         2 鼠标 10
#         …
#         n 购物车结算
# 3. 用户输入选择的商品序号，然后打印商品名称及商品价格,并将此商品，添加到购物车，用户还可继续添加商品。
# 4. 如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# 5. 用户输入n为购物车结算，依次显示用户购物车里面的商品，数量及单价，若充值的钱数不足，则让用户删除某商品，直至可以购买，若充值的钱数充足，则可以直接购买。
# 6. 用户输入Q或者q退出程序。
# 7. 退出程序之后，依次显示用户购买的商品，数量，单价，以及此次共消费多少钱，账户余额多少。
money = int(input('请输入充值金额:'))
commodity = [
    {'name': '电脑', 'price': 1999},
    {'name': '鼠标', 'price': 10},
    {'name': '键盘', 'price': 50}
]
trolley = []
while True:
    print('序号   商品名称    商品价格')
    for index in range(len(commodity)):
        print(f' {index + 1}     {commodity[index]["name"]}       {commodity[index]["price"]}')
    print(' n     购物车结算')
    print(' Q     退出程序')
    choice = input('请输入序号添加到购物车,输入序号负数[如:-1]减少一件商品:')
    if choice.upper() == 'Q':  # 输入Q退出
        break
    elif choice.upper() == 'N':  # 输入n进入购车
        total = 0
        print('您选购的商品如下'.center(50, '*'))
        print(' 商品名称    商品价格     数量')
        for item in trolley:
            total += item['price'] * item['num']
            print(f'  {item["name"]}       {str(item["price"]).center(4, " ")}      {item["num"]}')
        if money<total:
            print('您充值的金额不足,请删除商品再来')
        else:
            confim=input('请确认是否购买Y/N:')
    elif choice.isdigit():  # 如果选择的是数字
        if 0 < int(choice) <= len(commodity):  # 判断序号是否大于0并小于等于列表长度
            dic = commodity[int(choice) - 1]  # 被中的商品字典
            dic.setdefault('num', 1)  # 设置字典num默认值
            flag = False  # 设置标记,确认购车中是否已存在此商品
            tempIndex = 0  # 确定已存在商品在购车中的位置
            for tIndex in range(len(trolley)):
                if dic['name'] == trolley[tIndex]['name']:  # 确认购车中是否存在已选商品
                    flag = True  # 设置标识
                    tempIndex = tIndex  # 设置索引
            if flag:  # 如果购车中已存在,修改num
                trolley[tempIndex]['num'] += 1
            else:  # 如果购车中不存在,添加商品
                trolley.append(dic)
            print(f'您选择的商品为{dic["name"]},价格为{dic["price"]}元'.center(50, '-'))
        else:
            print('您输入的序号错误!'.center(50, '-'))
    elif choice.startswith('-'):  # 如果输入负数
        choice = choice.strip('-')  # 去掉-
        if choice.isdigit():
            if 0 < int(choice) <= len(commodity):  # 判断序号是否大于0并小于等于列表长度
                pass
    else:
        print('您输入的序号错误!'.center(50, '-'))
    print('*'.center(50, '*'))
