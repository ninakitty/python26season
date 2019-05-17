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
            user_file.write("admin:123456")
            user_file.close()
            exit("Initialize user information and run the program,user=admin,pwd=123456")


def login_index(func):
    def inner():
        # Number of times users can try
        number = 3
        # Number of passwords entered , {"user1":number,"user2":number,....}
        password_remainder_number = {}
        while True:
            user_input = input("请输入用户名>>>:")
            password_input = input("请输入密码>>>:")
            # password_input=getpass.getpass("Please input a password:")

            if user_lock(user_input):
                # Verify that user name and password are correct
                if user_info(user_input, password_input) == "Correct password":
                    print("\nWelcome to the staff information system\n")
                    # Execute the original function, then assign
                    ret = func()
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
