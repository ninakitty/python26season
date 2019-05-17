#!/usr/bin/env python
# coding=UTF-8
'''
@Version: 0.0.1
@Description: file content
@Author: zmf96
@LastEditors: zmf96
@Date: 2019-04-18 21:45:21
@LastEditTime: 2019-04-18 23:03:39
'''


from cmd import Cmd
import os 
import sys
import getpass

'''
    1，启动程序，用户可选择四个选项：登录，注册，购物，退出。
    2，用户注册，用户名不能重复，注册成功之后，用户名密码记录到文件中。
    3，用户登录，用户名密码从文件中读取，进行三次验证，验证不成功则退出整个程序。
    4，用户登录成功之后才能选择购物功能进行购物，购物功能（就是将购物车封装到购物的函数中）。
        1. 用户先给自己的账户充钱：比如先充3000元。
        2. 页面显示 序号 + 商品名称 + 商品价格，如：
            1 电脑 1999 
            2 鼠标 10
            …
            n 购物车结算
        3. 用户输入选择的商品序号，然后打印商品名称及商品价格,并
            将此商品，添加到购物车，用户还可继续添加商品。
        4. 如果用户输入的商品序号有误，则提示输入有误，并重新输入。
        5. 用户输入n为购物车结算，依次显示用户购物车里面的商品，
            数量及单价，若充值的钱数不足，则让用户删除某商品，直到可以购买，若充值的钱数充足，则可以直接购买。
        6. 用户输入Q或者q退出程序。
        7. 退出程序之后，依次显示用户购买的商品，数量，单价，以及
            此次共消费多少钱，账户余额多少。
    5，退出则是退出整个程序。

'''

class Shopping(Cmd):
    """
        this is shopping demo
    """
    try_count = 3 # 允许尝试的次数
    pwd_dict = {"zmf96":"zmf97"}
    monery = {}
    prompt = "Shopping Trolley>"
    intro = "    Welcome to shopping \n \t regin login shopping exit"

    user_online = None
    gwc = {
        '1':["电脑",1999,0],
        '2':["鼠标",49,0],
        '3':["键盘",99,0],
        '4':["耳机",101,0],
        '5':["摄像头",99,0]
    }
    wares = {
        '1':["电脑",1999],
        '2':["鼠标",49],
        '3':["键盘",99],
        '4':["耳机",101],
        '5':["摄像头",99]
    }

    def __init__(self):
        Cmd.__init__(self)
        
    def do_regin(self,line):
        with open("auth.txt","a+") as f:
            user = input("***请输入要注册的用户名***").strip()
            pwd = input("***请输入密码***").strip()
            pwd2 = input("***请再次输入密码***").strip()
            if pwd == pwd2:
                f.write(f"{user} {pwd}\n")
                print(" 【注册成功！】")
                with open("monery.txt",'a+') as monery:
                    monery.write(f"{user} 0 \n")
                return
        print("输入有误，请重新开始注册！！！")
    
    def do_login(self,line):
        print("***请输入用户名及密码***")
        with open("auth.txt",'r') as f:
            tmp_lines = f.readlines()
            for auth in tmp_lines:
                lst = auth.strip().split()
                self.pwd_dict[lst[0]] = lst[1]
        for i in range(self.try_count):
            user_name = input("User: ")
            user_pwd = getpass.getpass()
            if user_name in self.pwd_dict.keys() and user_pwd == self.pwd_dict[user_name]:
                print("【登陆成功】")
                self.user_online = user_name
                break
            else:
                print("【登陆失败】用户名或密码不正确，请重试（剩余尝试次数：{n})".format(n = self.try_count-i-1))

    
    def do_add_monery(self,line):
        if self.user_online == None:
            print(" 【请先登录 login or register】")
            return
        print(f"现在账户余额 {self.get_monery()} ,请及时给账户充值！" )
        tmp_monery = int(input("请输入充值金额：").strip())
        with open("monery.txt",'r+') as f:
            m = f.readlines()
            for line in m:
                lst = line.strip().split()
                self.monery[lst[0]] = lst[1]  
            f.seek(0)
            for k,v in self.monery.items():
                if k == self.user_online:
                    v = int(v)
                    v += tmp_monery
                f.write(f"{k} {v}\n")
                
    def get_monery(self):
        '''
        @description: 
        @param {type} 
        @return: 返回当前 user_online账号余额
        '''
        with open("monery.txt",'r',encoding='utf-8') as f:
            m = f.readlines()
            for line in m:
                lst = line.strip().split()
                self.monery[lst[0]] = int(lst[1])
        if self.user_online not in self.monery.keys():
            return 0  
        return self.monery[self.user_online]
        
    def do_shopping(self,line):
        if self.user_online == None:
            print(" 【请先登录 login or register】")
            return
        while True:
            print("欢迎开始购物")
            print("序号\t商品\t价格")
            for item in self.wares.items():
                print(f"{item[0]}\t{item[1][0]}\t{item[1][1]}")
            userinput = input("请输入商品序号：(Q. 退出程序 n. 结算购物车 )").strip()
            if userinput in self.wares.keys():
                self.gwc[userinput][2] += 1
                print(f"{userinput} {self.wares[userinput]}")
            elif userinput == "n":
                print("购物车中商品如下：")
                print("序号\t商品\t价格\t 数量")
                sum =0
                for item in self.gwc.items():
                    print(f"{item[0]}\t{item[1][0]}\t{item[1][1]}\t{item[1][2]}")
                    sum = sum +  item[1][1]*item[1][2]
                print(f"购物车内商品总价为:{sum}")
                
                if sum > self.get_monery():
                    print("充的钱不够啊，请删除部分商品,或者充值吧 add_monery")
                    tmp = input("请输入要删除的购物车中的商品序号:")
                    if tmp in self.gwc.keys():
                        self.gwc[tmp][2] -= 1
                else:
                    self.monery[self.user_online] -= sum
                    for item in self.gwc.items():
                        item[1][2] = 0
                    print(f"购买成功！本次共消费{sum},账户余额{self.monery[self.user_online]}")
            elif userinput == "q" or userinput == "Q":
                return 
            else:
                print("输入有误，请重新输入!")


    def do_hello(self,line):
        """
            this is do_hello doc
        """
        print("    Welcome to shopping \n \t regin login shopping exit")
    
    def help_hello(self):
        print("     打印欢迎信息")

    def emptyline(self,line):
        print("【Info】 Please enter a command")
        
    def default(self, line):
        print("【Error】Please check your input: %s " % line)

    def do_exit(self,line):
        print("Bye Exit")
        return True
    
    def do_quit(self,line):
        print("Bye Quit")
        return True
    

def main():
    try:
        shopping = Shopping()
        shopping.cmdloop()
    except Exception as e:
        print(e)
        exit()

if __name__ == '__main__':
    main()
    