#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/6 20:21
# @Author  : Abel
# @File    : staff_info.py
# @Software: PyCharm
import os


def add_user_lock(user_name):
    """
    This function is used to lock users
    :param user_name: User entered name  , type str
    :return:
    """
    with open("user_lock", "a") as user_lock_file:
        user_lock_file.write(user_name+"\n")
    return True


def user_lock(user_name):
    """
    Determine whether the user is locked
    :param user_name: User entered name  , type str
    :return: True indicating unlocked ,  False indicating locked
    """
    if os.path.exists("user_lock"):
        with open("user_lock", "r") as user_lock_file:
            for line in user_lock_file:
                user = line.strip()
                if user == user_name:
                    return False
            return True
    else:
        return True


def user_info(user_name, user_password):
    """
    Get user info file and read username password
    If no user info file exist , Create file and create username password
    default user = admin ,password = 123456
    :param user_name: User entered name , type str
    :param user_password: User entered password , type str
    :return: Correct password ,  Password Error  or exit()
    """
    if os.path.exists("user_info"):
        with open("user_info", "r") as user_file:
            for line in user_file:
                user_info_temp = line.strip().split(":")
                user = user_info_temp[0]
                password = user_info_temp[1]
                if user == user_name:
                    if password == user_password:
                        return "Correct password"
                    else:
                        return "Password Error"
            return False
    else:
        with open("user_info", "a") as user_file:
            user_file.write("admin:123456\n")
            user_file.close()
            exit("Initialize user information and run the program,user=admin,pwd=123456")


def user_register(*args):
    """
    用户注册方法
    :param args:用户登陆状态,{"name","user_name"},未登陆为{"name": ""}
    :return:True / False
    """
    if args[0]["name"]:
        # 判断时否已经登陆,已登陆则不能注册
        return False
    else:
        user_input = input("请输入要注册的用户名>>>:")
        password_input = input("请输入要注册用户的密码>>>:")
        # 判断用户注册的用户名是否已经存在
        if user_info(user_input, password_input):
            print("注册失败,用户名{name}已存在".format(name=user_input))
            return False
        else:
            with open("user_info", "a") as user_file:
                # 不存在将用户的注册信息写入文件内
                user_file.write("{name}:{password}\n".format(name=user_input, password=password_input))
                user_file.close()

            # 并自动登陆,{"name","user_input"}
            args[0]["name"] = user_input
            return args


def login_index(func):
    def inner(*args, **kwargs):
        # If the user has already logged in, there is no need to login. --> args = {"name","username"}
        if args[0]["name"]:
            ret = func(*args, **kwargs)
            return ret
        # Number of times users can try
        number = 3
        # Number of passwords entered , {"user1":number,"user2":number,....}
        password_remainder_number = {}
        while True:
            user_input = input("请输入要登陆的用户名>>>:")
            password_input = input("请输入要登陆用户的密码>>>:")
            # password_input=getpass.getpass("Please input a password:")

            if user_lock(user_input):
                # Verify that user name and password are correct
                if user_info(user_input, password_input) == "Correct password":
                    args[0]["name"] = user_input
                    # Execute the original function, then assign
                    print("登陆成功")
                    ret = func(*args, **kwargs)
                    return ret

                if user_info(user_input, password_input) == "Password Error":
                    #  User name and password 1 times, add to dictionary, Start counting {"user1":number}
                    if not password_remainder_number.get(user_input):
                        password_remainder_number[user_input] = number

                    password_remainder_number[user_input] -= 1
                    user_number = password_remainder_number[user_input]
                    if user_number < 1:
                        print("User %s is locked" % user_input)
                        # lock users
                        if add_user_lock(user_input):
                            return False
                    print("Sorry, the user or password is wrong, the remaining attempt %d times \n" % user_number)
                    continue

                else:
                    print("Invalid user,Please enter again")
                    continue
            else:
                # locked exit
                print("Locked user")
                return False
    # Decoration result
    return inner
