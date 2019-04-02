
# num = input("请问老男孩现在有多少学生了:")
#
# if int(num) > 100:
#     print("提车")
#     print("洗脚城")
# print("上课")


# # 如果兜里的钱 超过2000 ， 吃龙虾, 如果钱小于2000 吃泡面
# money = input("请输入你兜里的钱:")
# if int(money) > 2000:
#     print("吃龙虾")
# else: # 否则.
#     print("吃泡面")
#
# print("洗脚")

# # 输入分数。 判断级别
# score = int(input("请输入分数:"))
#
# if score >= 90:
#     print("优秀")
# elif score >= 80:
#     print("良好")
# elif score >= 70:
#     print("中等")
# elif score >= 60:
#     print("及格")
# else:
#     print("不及格")


#
gender = input("请输入你的性别:")
if gender == "女": # == 表示判断， = 赋值

    age = int(input("请输入你的年龄:"))
    if age > 80:
        print("去隔壁， wusir等着你呢.")
    else:
        print("来吧， 我家的西瓜又大又甜")
else:
    print("去隔壁， alex等着你呢")