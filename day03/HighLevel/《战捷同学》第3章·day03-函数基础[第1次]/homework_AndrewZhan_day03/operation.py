#!/usr/bin/evn python
# -*- encoding:utf-8 -*-
# Author: Andrew.zhan
# Create by 2019 Apr 14
import sys


class Person(object):
    """
    用户功能
    """
    __user_id = 1

    def __init__(self, name):
        self.name = name
        self.user_id = Person.__user_id
        self.wallet = 0
        self.shoppings = {}
        Person.__user_id += 1

    def recharge(self, money):
        self.wallet += money
        return self.wallet

    def add_product(self, product):
        # product数据格式为: {"id": 1, "name": "电脑", "cost": 1999}
        product_id = product["id"]
        if product_id not in self.shoppings:
            self.shoppings[product_id] = []
        self.shoppings[product_id].append(product)
        return self.shoppings

    def del_product(self, product_id):
        if product_id in self.shoppings and self.shoppings[product_id] and isinstance(self.shoppings[product_id], list):
            if len(self.shoppings[product_id]) == 1:
                self.shoppings.pop(product_id)
            else:
                self.shoppings[product_id].pop()
        return self.shoppings

    def cashier(self):
        cost_list = []
        for product_id, products_list in self.shoppings.items():
            for product_info in products_list:
                cost_list.append(product_info["cost"])
        total = sum(cost_list)
        cashier_success = True if total <= self.wallet else False
        if cashier_success:
            self.wallet -= total
        return {"cashier_success": cashier_success, "total": total, "wallet": self.wallet, "products": self.shoppings}


def input_float(show_msg):
    msg = input("请输入%s: " % show_msg).strip()
    try:
        msg_int = float(msg)
        return msg_int
    except(Exception):
        print("%s必须为数字" % show_msg)
        return input_float(show_msg)


def input_int(show_msg):
    msg = input("请输入%s: " % show_msg).strip()
    try:
        msg_int = int(msg)
        return msg_int
    except(Exception):
        print("%s必须为整数" % show_msg)
        return input_int(show_msg)


def get_user_selected():
    special_key = ["Q", "q", "n", "N"]

    def input_choice(show_msg):
        msg = input("请输入%s(按n/N结算,按Q/q退出): " % show_msg).strip()
        try:
            if msg in special_key:
                return msg
            msg_int = int(msg)
            return msg_int
        except(Exception):
            print("%s必须为整数" % show_msg)
            return input_choice(show_msg)

    user_selected = input_choice("商品编号")
    if user_selected in special_key:
        return user_selected
    if user_selected < 1 or user_selected > len(store):
        print("选择有误,请在商品列表范围内选择,请重新输入.")
        return get_user_selected()
    return user_selected


store = [
    {"name": "电脑", "cost": 1999},
    {"name": "鼠标", "cost": 10},
    {"name": "键盘", "cost": 50},
    {"name": "音响", "cost": 998},
    {"name": "信仰灯", "cost": 300},
]


def main(username="Andrew"):
    user_object = Person(username)
    recharge_money = input_float("充值金额")
    user_object.recharge(recharge_money)
    print("账户余额: %s" % user_object.wallet)

    while True:
        # 为了用上课时候说的商品索引方法,所以使用了+1和-1这种操作.个人感觉其实用字典会更好一些.
        for i in range(0, len(store)):
            print("[%s] %s\t价格: %s" % (i + 1, store[i]["name"], store[i]["cost"]))
        user_selected_id = get_user_selected()
        # user_selected_id值的范围为Q/q/N/n或商品索引号. 这里判断一下,如果为Q/q那么就直接可以退出了.
        if user_selected_id in ["Q", "q"]:
            break
        # 如果为商品索引号,则进行放入购物车的动作.
        if isinstance(user_selected_id, int):
            # 因为要用索引号的方法来选择商品,所以这里需要拼装商品id的操作,有商品id方便以后对商品的操作.
            # 所以上面如果使用字典来定义store的话,这里就不需要拼接id的操作了.
            product = {"id": user_selected_id}
            product.update(store[user_selected_id - 1])
            user_object.add_product(product)
        # 这里是结账的操作,午休要结束了,格式化字符串这块就先凑合怼上了.
        if user_selected_id in ["n", "N"]:
            result = user_object.cashier()
            while not result["cashier_success"]:
                print("余额不足,请删除一些商品.\n商品ID\t商品名称\t单价\t数量")
                for product_id, product_info in result["products"].items():
                    print("%s\t%s\t%s\t×%s" % (
                        product_id, product_info[0]["name"], product_info[0]["cost"], len(product_info)))
                select_del_id = input_int("要删除的商品编号")
                user_object.del_product(select_del_id)
                result = user_object.cashier()
            print("结账成功. 共消费: %s\t余额: %s\t已购买商品列表:\n商品ID\t商品名称\t单价\t数量" % (result["total"],
                                                                           result["wallet"]))
            for product_id, product_info in result["products"].items():
                print("%s\t%s\t%s\t×%s" % (
                    product_id, product_info[0]["name"], product_info[0]["cost"], len(product_info)))
            break
    sys.exit(0)


if __name__ == "__main__":
    main()
