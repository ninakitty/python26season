# # # coding:utf-8
# # """
# #     先来个import this 放松下心情
# # """
# # import this

# # # The Zen of Python, by Tim Peters

# # # Beautiful is better than ugly.
# # # Explicit is better than implicit.
# # # Simple is better than complex.
# # # Complex is better than complicated.
# # # Flat is better than nested.
# # # Sparse is better than dense.
# # # Readability counts.
# # # Special cases aren't special enough to break the rules.
# # # Although practicality beats purity.
# # # Errors should never pass silently.
# # # Unless explicitly silenced.
# # # In the face of ambiguity, refuse the temptation to guess.
# # # There should be one-- and preferably only one --obvious way to do it.
# # # Although that way may not be obvious at first unless you're Dutch.
# # # Now is better than never.
# # # Although never is often better than *right* now.
# # # If the implementation is hard to explain, it's a bad idea.
# # # If the implementation is easy to explain, it may be a good idea.
# # # Namespaces are one honking great idea -- let's do more of those!

# # if True:
# #     print("True")
# # elif 1 == 1:
# #     print("1 == 1")
# # else:
# #     print("else")


# # print("""   文能提笔安天下,  
# #     武能上马定乾坤.  
# #     心存谋略何人胜,  
# #     古今英雄唯是君.""")

# # num1 = 66
# # tmp_num = 0
# # print("猜大小游戏，数字在0-100之间，请输入一个数字")
# # while True:
# #     tmp_num = int(input(">>>："))
# #     if tmp_num > 66:
# #         print("您输入的数字太大了，请重新输入")
# #     elif tmp_num < 66:
# #         print("您输入的数字太小了，请重新输入")
# #     elif tmp_num == num1:
# #         print("恭喜，猜对了")
# #         break


# # age = int(input("请输入你的年龄："))
# # if age <= 10:
# #     print("小屁孩")
# # elif age > 10 and age <= 20:
# #     print("青春期叛逆的小屁孩")
# # elif age > 20 and age <= 30:
# #     print("开始定性，开始混社会的小屁孩")
# # elif age > 30 and age <= 40:
# #     print("看老大不小了，赶紧结婚的小屁孩")
# # elif age > 40 and age <= 50:
# #     print("家里有个不听话的小屁孩")
# # elif age > 50 and age <= 60:
# #     print("自己马上变成不听话的老屁孩")
# # elif age > 60 and age <= 70:
# #     print("活着还不错的老屁孩儿")
# # elif age > 70 and age <= 90:
# #     print("人生就快结束了的一个老屁孩儿")
# # elif age > 90:
# #     print("再见了这个世界")


# # # 这个单行注释
# # '''
# #     这是多
# #     行注释
# # '''
# # """
# #     这也是多
# #         行注释
# # """

# # if "麻花藤" == input("请输入麻花藤 >>>: "):
# #     print("真聪明")
# # else:
# #     print("你是傻逼么？")

# # count = 0
# # tmp = []
# # while True:
# #     tmp.append(int(input(">>>: ")))
# #     count += 1
# #     if count == 10:
# #         break

# # for i in tmp:
# #     print(i)

# sum = 0
# for i in range(101):
#     sum += i
# print(sum)

# for i in range(1,100,2):
#     print(i)

# for i in range(2,101,2):
#     print(i)

# sum = 0
# for i in range(1,100,2):
#     sum += i
# for i in range(2,100,2):
#     sum -= i

# print(sum)

"""
    以下是用户登陆
"""

import getpass

def Login():
    try_count = 3 # 允许尝试的次数
    pwd_dict = {"zmf96":"zmf97","admin":"admin123"}
    print("***请输入用户名及密码***")
    for i in range(try_count):
        user_name = input("User: ")
        user_pwd = getpass.getpass()
        if user_name in pwd_dict.keys() and user_pwd == pwd_dict[user_name]:
            print("【登陆成功】")
            break
        else:
            print("【登陆失败】用户名或密码不正确，请重试（剩余尝试次数：{n})".format(n = try_count-i-1))

if __name__ == "__main__":
    Login()