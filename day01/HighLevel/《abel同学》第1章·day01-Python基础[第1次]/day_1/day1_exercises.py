#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Abel He

"""
练习题：
"""

print("""
1、简述变量命名规范
   由字母,数字,下划线_,组成.
   不能以数字开头
   不能使用python中的关键字
   具有描述性
   不能用中文或中文拼音
   分为驼峰型(VariableName)和下划线型(variable_name)

2、name = input(">>>") name变量是什么数据类型？
   name的数据类型为str
   判断方式type(name)

3、if条件语句的基本结构？
   if 判断条件 :
       代码块
""")


print("""
4、用print打印出下面内容：
            文能提笔安天下,
            武能上马定乾坤.
            心存谋略何人胜,
            古今英雄唯是君.
""")


print("""
5、利用if语句写出猜大小的游戏：设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，
   则显示猜测的结果小了;只有等于66，显示猜测结果正确。
""")
number = input("请输入数字猜大小>>>")
number = int(number)
if number == 66:
    print("666,猜对啦！")
if number > 66:
    print("大了")
if number < 66:
    print("小了")


print("""
6、提示用户输入他的年龄, 程序进判断.如果小于10, 提示小屁孩, 如果大于10, 小于于 20, 提示青春期叛逆的小屁孩. 如果大于20,
   小于30. 提示开始定性, 开始混社会的小屁孩儿, 如果大于30, 小于40. 提示.老大不小了, 赶紧结婚小屁孩儿. 如果大于40,
   小于50. 提示家里有个不听话的小屁孩儿. 如果大于50, 小于60. 提示自己马上变成不听话的老屁孩儿.如果大于60, 小于70. 提示活
   着还不错的老屁孩儿. 如果大于70, 小于于 90. 提示.人生就快结束了的一个老屁孩儿. 如果大于90以上. 提示. 再见了这个世界.
   """)

age = input("请输入年龄>>>")
age = int(age)

if age > 90:
    print("再见了这个世界")
elif age >= 70:
    print("人生就快结束了的一个老屁孩儿")
elif age >= 60:
    print("活着还不错的老屁孩儿")
elif age >= 50:
    print("马上变成不听话的老屁孩儿")
elif age >= 40:
    print("家里有个不听话的小屁孩儿")
elif age >= 30:
    print("老大不小了, 赶紧结婚小屁孩儿")
elif age >= 20:
    print("开始定性, 开始混社会的小屁孩儿")
elif age >= 10:
    print("青春期叛逆的小屁孩")
else:
    print("小屁孩")

print("""
7、单行注释以及多行注释？
        单行注释: # 注释内容
        多行注释: '''注释内容'''
      """)


print("""
8、简述你所知道的Python3x和Python2x的区别？
    python2:冗余,重复,不规范.
    python3:优美,简单,清晰.
""")


print("""
9、提示用户输入麻花藤. 判断用户输入的对不对. 如果对, 提示真聪明, 如果不对, 提示你是傻逼么
""")
user_input = input("请输入'麻花藤'>>>")
if user_input == "麻花藤":
    print("真聪明")
else:
    print("是不是打错字了 ?")


print("""
10、使用while循环输入 1 2 3 4 5 6 ... 8 9 10
""")
number = 1
while number <= 10:
    if number != 7:
        print(number)
    number += 1


print("11、求1-100的所有数的和")
number1 = 1
count = 0
while number1 <= 100:
    count += number1
    number1 += 1
print(count)


print("12、输出 1-100 内的所有奇数")
number2 = 1
while number2 <= 100:
    num_temp = number2 % 2
    if num_temp != 0:
        print(number2)
    number2 += 1


print("13、输出 1-100 内的所有偶数")
number3 = 1
while number3 <= 100:
    num_temp = number3 % 2
    if num_temp == 0:
        print(number3)
    number3 += 1

print("14、求1-2+3-4+5 ... 99的所有数的和")
number4 = 1
sum1 = 0
while number4 <= 100:
    num_temp = number4 % 2
    if num_temp != 0:
        sum1 += number4
    else:
        sum1 -= number4
    number4 += 1
print(sum1)
