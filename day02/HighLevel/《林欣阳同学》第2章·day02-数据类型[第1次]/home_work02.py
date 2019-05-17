# 输入非数字异常处理
try:
    account = int(input('请输入你要充值的金额：'))
    #定义商品列表
    goods = [
        {'goods_name':'电脑','price':4000},
        {'goods_name':'鼠标','price':60},
        {'goods_name': '键盘', 'price':999},
        {'goods_name':'显示器','price':2000},
        {'goods_name':'windows','price':600},
    ]
    #商品打印
    for index,i in enumerate(goods):
        print(index+1,i['goods_name'],i['price'])
    print('n 购物车结算')
    #购物车字典
    shop_cart = {}
    my_bool = True
    while my_bool:
        # 输入序号去除首尾特殊字符，转换成小写，函数链式调用
        buy = input('请输入需要购买商品的序号，输入n为结算，输入q退出：').strip().lower()
        #判断是否是数字
        if buy.isdigit():
            buy = int(buy)
            # 显示时索引加了1，所以用户输入的要减一
            buy -=1
            # 判断加入购物车的商品在不在购物车中，在数量加一，不在就新增
            if buy not in shop_cart:
                shop_cart[buy] = {'goods_name': goods[buy]['goods_name'], 'price': goods[buy]['price'],'amount': 1}
            else:
                shop_cart[buy]['amount'] += 1
            print('商品：{} 单价：{} 加入购物车成功！'.format(goods[buy]['goods_name'],goods[buy]['price']))
        elif buy == 'n':
            while True:
                # 总价
                total_price = 0
                # 遍历购物车 算出总价
                for j,k in shop_cart.items():
                    total_price += k['price']*k['amount']
                    print('序号：{},商品名：{},单价：{},数量：{}'.format(j+1,k['goods_name'],k['price'],k['amount']))
                print('总价：{}'.format(total_price))
                # 入数金额小于总价删除商品 总价减去购物车价格得出差价
                if account < total_price:
                    print('余额不足,还差{}元'.format(total_price-account))
                    del_goods = input('请输入你要删除的商品序号：').strip()
                    if del_goods.isdigit():
                        del_goods = int(del_goods)-1
                        del_price = shop_cart.pop(del_goods)
                        print(shop_cart)
                    else:
                        print('请输入正确的数字！')
                else:
                    print('购买成功')
                    print('本次消费：{} 元，余额：{}'.format(total_price,account-total_price))
                    my_bool = False
                    break
        elif buy == 'q':
            break
        else:
            print('请输入正确的数字！')
    else:
        print('欢迎下次光临')
except ValueError:
    print('麻烦你，输入数字！再见')
