"""
练习题：
1、简述变量命名规范
答：
    a.由字母、数字和下划线组成
    b.第一个字符不能是数字
    c.不能使用关键字
    d.不要太长
    e.要有意义
    f.驼峰式或下划线式间隔
    g.区分大小写
""""""
2、name = input(“>>>”) name变量是什么数据类型？
答：name的数据类型为str
""""""
3、if条件语句的基本结构？
a.      if 条件：
            执行内容
        else:
b.      if 条件：
            执行内容
c.      if 条件：
            执行内容
        elif:
            执行内容
        else:
                        
""""""
4、用print打印出下面内容：
文能提笔安天下,
武能上马定乾坤.
心存谋略何人胜,
古今英雄唯是君.
"""
# print('第4题')
# poem = """
# 文能提笔安天下,
# 武能上马定乾坤.
# 心存谋略何人胜,
# 古今英雄唯是君.
# """
# print(poem)

"""
5、利用if语句写出猜大小的游戏：
    设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；
    如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确。
"""
# print('第5题')
# idealNum = 66
# inputNum = int(input('请输入一个理想数字：'))
# if inputNum > idealNum:
#     print('结果大了！')
# elif inputNum < idealNum:
#     print('结果小了！')
# elif inputNum == idealNum:
#     print('结果正确')
"""
6、提示用户输入他的年龄, 程序进判断.
如果小于10, 提示小屁孩,
如果大于10, 小于于 20,提示青春期叛逆的小屁孩.
如果大于20, 小于30. 提示开始定性,开始混社会的小屁孩儿, 
如果大于30, 小于40. 体制看老大不小了, 赶紧结婚小屁孩儿.
如果大于40, 小于50. 提示家里有个不听话的小屁孩儿.
如果大于50, 小于60. 提示自己马上变成不听话的老屁孩儿.
如果大于60, 小于70. 提示活着还不错的老屁孩儿.
如果大于70, 小于于 90. 提示人生就快结束了的一个老屁孩儿.
如果大于90以上. 提示. 再见了这个世界.
"""
# print('第6题')
# inputAge = int(input('请输入年龄：'))
# if 90 < inputAge:
#     print('再见了这个世界')
# if 70 < inputAge <= 90:
#     print('人生就快结束了的一个老屁孩儿.')
# if 60 < inputAge <= 70:
#     print('活着还不错的老屁孩儿')
# if 50 < inputAge <= 60:
#     print('自己马上变成不听话的老屁孩儿')
# if 40 < inputAge <= 50:
#     print('家里有个不听话的小屁孩儿')
# if 30 < inputAge <= 40:
#     print('看老大不小了, 赶紧结婚小屁孩儿')
# if 20 < inputAge <= 30:
#     print('开始定性,开始混社会的小屁孩儿')
# if 10 < inputAge <= 20:
#     print('青春期叛逆的小屁孩')
# if inputAge <= 10:
#     print('小屁孩')

"""
7、单行注释以及多行注释？
#
'''、""""""
""""""
8、简述你所知道的Python3x和Python2x的区别？
    Python3x中print需要括号
    Python2x中print不需要括号
""""""
9、提示用户输入麻花藤. 判断用户输入的对不对. 如果对, 提示真聪明, 如果不对, 提示你是傻逼么
"""
# print('第9题')
# idealWord='麻花藤'
# inputWord=input('请输入"麻花藤"三个字符:')
# if inputWord==idealWord:
#     print('真聪明！')
# else:
#     print('你是傻逼么！')
"""
10、使用while循环输入 1 2 3 4 5 6     8 9 10
"""
# print('第10题')
# num = 1
# while num <= 10:
#     if num == 7:
#         num += 1
#         continue
#     print(num)
#     num += 1
# num = 0
# while num < 10:
#     num += 1
#     if num == 7:
#         continue
#     print(num)
"""
11、求1-100的所有数的和
"""
# print('第11题')
# num1 = 1
# total = 0
# while num1 <= 100:
#     total += num1
#     num1 += 1
# print(total)
"""
12、输出 1-100 内的所有奇数
"""
# print("第12题")
# num2 = 1
# while num2 <= 100:
#     print(num2)
#     num2 += 2
"""
13、输出 1-100 内的所有偶数
"""
# print("第13题")
# num3 = 2
# while num3 <= 100:
#     print(num3)
#     num3 += 2
"""
14、求1-2+3-4+5 ... 99的所有数的和

"""
# print('第14题')
# num4 = 1
# total = 0
# while num4 < 100:
#     if num4 % 2 == 1:
#         total = total + num4
#         num4 += 1
#     else:
#         total = total - num4
#         num4 += 1
# print(total)
