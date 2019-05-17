file_path = 'user_list.txt'
flag = 0
ini_money = 0
user_goods = {}

def q():
    quit()

def login():
    global flag
    count = 0
    with open(file_path, encoding='utf-8') as f:
        while count < 4:
            user = input('请输入用户名: ').strip()
            pawd = input('请输入密码: ').strip()
            for i in f.readlines():
                if user in i.strip(',')[0] and pawd in i.strip(',')[1].strip('\n'):
                    print('登录成功')
                    flag = 1
                    main()
            else:
                if count != 3:
                    print('\034[用户不存在，还有 %s 次机会\034[0m' %(3 - count))
                else:
                    print('兄弟，等一年再来吧')
                    q()
                count += 1
                continue

def register():
    global flag
    while True:
        user = input('请输入用户名: ')
        with open(file_path, 'r', encoding='UTF-8') as f:
            info = f.readlines()
            for i in info:
                if user == i.split(',')[0].strip():
                    print('用户名已经存在')
                    break
            else:
                pawd = input('请输入密码: ')
                pawd_r = input('请再次输入密码: ')
                if pawd == pawd_r:
                    with open(file_path,'a', ) as f:
                        f.write(user + ','pawd + '\n')
                        f.flush()
                        print('用户注册成功')
                        flag = 1
                        main()

def pay(count=None):
    global ini_money
    with True:
        if count:
            if count > ini_money:
                c = count - ini_money
                ini_money += int(input('请输入充值金额，建议不小于%s:' %c))
                if ini_money < count:
                    shopping()
            else:
                count1 = user_goods_list()
                print('本次消费 %s 余额 %s ' %(count1, ini_money - count1))
                q()
        else:
            ini_money += int(input('请输入充值金额: '))
            print('充值 %s 成功' %ini_money)
            shopping()

def user_goods_list():
    if user_goods:
        count = 0
        for k, v in user_goods.items():
            count += v[1] * v[0]
            print('商品: %s 数量: %s ' %(k, v[1]))
            print('合计: %s' %count)
            return count
    else:
        print('购物车空了,赶紧去购物吧！')
        shopping()

def account(count):
    while True:
        if count > ini_money:
            cmd = int(input('余额不足，删除或充值 1/0: '))
            if cmd:
                name = input('选择要删除的商品名称: ')
                num = int(input('删除商品数量: '))
                user_goods[name][1] -= num
                if user_goods[name][1] <= 0:
                    del user_goods[name]
                user_goods_list()
            else:
                pay(count)
                break
        else:
            pay(count)

def shop():
    while True:
        goods = {'phone x': 5000, 'computer':8000, 'girl':10000}
        for k, v in goods.items():
            print(k, v)
        cmd = input('输入商品名: ')
        num = int(input('输入购买数量: '))
        if num:
            if cmd in goods:
                if cmd in user_goods:
                    user_goods[cmd][1] += num
                else:
                    user_goods[cmd] = [goods[cmd], num]
                count = user_goods_list()
                cmd1 = int(input('继续购物/结账 1/0:' ))
                if cmd1:
                    continue
                else:
                    account(count)
        else:
            print('你输入的号码有误，请重新输入')
            continue

def shopping():
    if flag:
        d = {'shop':shop, 'pay':pay, 'quit':q}
        for i in d:
            print(i)
        while True:
            cmd = input('输入你的选项; ')
            if cmd in d:
                d[cmd]()
            else:
                print('你输入的选项有误，请重新输入; ')
                continue
    else:
        print('未注册用户，请购物前请登录或者注册')
        main()

def main():
    d = {'login':login, 'register':register, 'shopping':shopping, 'quit':q}
    for k in d:
        print(k)
    while True:
        cmd = input('请输入你的选项: ')
        if cmd in d:
            d[cmd]()
        else:
            print('你的输入有误，请重新输入: ')

if __name__ == '__main__':
    main()







