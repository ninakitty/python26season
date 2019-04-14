# while 1:
#     print("1.打开手机")
#     print("2.打开陌陌")
#     print("3.找一个你心仪的他")
#     print("4.出来吃饭聊天看电影")
#     print("5........")


# 定义函数
# def yue():
#     print("1.打开手机")
#     print("2.打开陌陌")
#     print("3.找一个你心仪的他")
#     # return  #  函数执行到return之后会终止函数的执行
#     print("4.出来吃饭聊天看电影")
#     print("5........")
#
# # 调用函数
# ret = yue()
# print(ret)


#
# def yue():
#     print("1.打开手机")
#     print("2.打开陌陌")
#     print("3.找一个你心仪的他")
#     print("4.出来吃饭聊天看电影")
#     print("5........")
#     return "大妈"  # 返回大妈
#
# # 调用函数
# ret = yue()
# print(ret)


# def yue():
#     print("1.打开手机")
#     print("2.打开陌陌")
#     print("3.找一个你心仪的他")
#     print("4.出来吃饭聊天看电影")
#     print("5........")
#     return "大妈", "大爷", "阿凡达", "张天宝"  # 返回元组
#
# # 调用函数
# ret = yue()
# print(ret)

# 写一个登陆功能. alex, 123 正确的用户名密码,  返回 True, False

def login():
    username = input("请输入用户名:").strip()
    password = input("请输入密码:").strip()

    if username == "alex" and password == "123":
        return True
    else:
        return False


if login():
    print("欢迎进入到xxxx系统")
else:
    print("用户名或密码错误. ")
