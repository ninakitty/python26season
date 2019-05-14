# 练习题：
# 1、简述变量命名规范
#     变量定义的规则：
#     变量名只能是 字母、数字或下划线的任意组合
#     变量名的第一个字符不能是数字
#     系统关键字不能声明为变量名，比如：if,elif,print,return, for,while,import,def等

# 2、name = input(“>>>”) name变量是什么数据类型？
#    name变量是字符串类型

# 3、if条件语句的基本结构？
#     if 条件表达式：
#         语句
#     else：
#         语句

# 4、用print打印出下面内容：文能提笔安天下,  武能上马定乾坤.  心存谋略何人胜,  古今英雄唯是君.
#   print("文能提笔安天下,  武能上马定乾坤.  心存谋略何人胜,  古今英雄唯是君")

# 5、利用if语句写出猜大小的游戏：设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；
#     如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确。
# target = 66
# user_guess = int(input("please guess a number>>>"))
# if user_guess > target:
#     print('your guess is grater than target!')
# elif user_guess < target:
#     print('your guess is samller than target!')
# else:
#     print('Congratutations, you guess it!')

# 6、提示用户输入他的年龄, 程序进判断.如果小于10, 提示小屁孩, 如果大于10, 小于于 20, 提示青春期叛逆的小屁孩.
#     如果大于20, 小于30. 提示开始定性, 开始混社会的小屁孩儿, 如果大于30, 小于40. 体制看老大不小了, 赶紧结婚
#     小屁孩儿. 如果大于40, 小于50. 提示家里有个不听话的小屁孩儿. 如果大于50, 小于60. 提示自己马上变成不听话
#     的老屁孩儿.如果大于60, 小于70. 提示活着还不错的老屁孩儿. 如果大于70, 小于于 90. 提示人生就快结束了的一个
#     老屁孩儿. 如果大于90以上. 提示. 再见了这个世界.

# user_age = int(input("please guess a number>>>"))
# if user_age < 10:
#     print('小屁孩!')
# elif user_age <= 20:
#     print('青春期叛逆的小屁孩')
# elif user_age <= 30:
#     print('提示开始定性, 开始混社会的小屁孩儿')
# elif user_age <= 40:
#     print('体制看老大不小了, 赶紧结婚小屁孩儿')
# elif user_age <= 50:
#     print('家里有个不听话的小屁孩儿孩')
# elif user_age <= 60:
#     print('自己马上变成个不听话的老屁孩儿')
# elif user_age <= 70:
#     print('活着还不错的老屁孩儿')
# elif user_age <= 90:
#     print('人生就快结束的老屁孩儿')
# else:
#     print('再见了这个世界')


# 7、单行注释以及多行注释？
# 单行注释用#号，多行注释用成对的3个单引号或者双引号

# 8、简述你所知道的Python3x和Python2x的区别？
# Python3.X 源码文件默认使用utf - 8编码，而2.x不是,中文字不能在其中正常打印显示，但是在3.x中可以正常显示

# 9、提示用户输入麻花藤. 判断用户输入的对不对. 如果对, 提示真聪明, 如果不对, 提示你是傻逼么
# s = "麻花藤"
# user_input = input('请输入您的**码>>>')
# if user_input == s:
#     print("真聪明")
# else:
#     print("你是傻逼么")

# 10、使用while循环输出 1 2 3 4 5 6 7 8 9 10
# i = 1
# while i < 11:
#     print(i)
#     i +=1

# 11、求1-100的所有数的和
# i=0
# sum = 0
# while i < 100:
#     i +=1
#     sum +=i
# print(i)
# print(sum)

# 12、输出 1-100 内的所有奇数
# i=0
# while i < 100:
#     i += 1
#     if i%2 != 0:
#         print(i)

# 13、输出 1-100 内的所有偶数

# i=1
# while i < 100:
#     i += 1
#     if i%2 == 0:
#         print(i)

# 14、求1-2+3-4+5 ... 99的所有数的和
# i,s1,s2,sum = 0,0,0,0
# while i < 99:
#     i +=1
#     if i%2 != 0:
#         s1 +=i
#
#     if i%2 == 0:
#         s2 +=i
#
# print(s1)
# print(s2)
# sum = s1 - s2
# print(sum)

# 用户登录
# 1. 三次重试机会
# 2. 每次输错误时显示剩余错误次数


# logined = False
# user,passwd = 'allen','abc123'
# count =0
# while count < 3:
#     username = input('Username:')
#     password = input('Password:')
#     if username == user and password == passwd:
#         print('Login successful!')
#         exit(0)
#     else:
#         count += 1
#         remain = 3 - count
#         print('Invlida username or Password! Please try again! You have %s chance!'%remain)



