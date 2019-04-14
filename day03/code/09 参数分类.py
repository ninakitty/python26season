# def chi(good_food, junk_food, soup, sweet):
#     print(good_food, junk_food, soup, sweet)

# chi("汉堡包", "辣条", "胡辣汤", "哈根达斯")
# chi(soup="疙瘩汤", sweet="沙琪玛", good_food="泡面", junk_food="烤鸭")
# chi("汉堡包","烤鸭", "疙瘩汤", sweet="沙琪玛")


# def luru(name, age, height, sex="男"):
#     print(name, age, sex, height)
#
# luru("alex", 56, 165)
# luru("wusir", 16, 195)
# luru("taibai", 36, 185)
# luru("女神",26, 160, "女")


# def chi(*food): # 接受到的是元祖
#     print(food) # 参数是food  * 表示动态接受参数
#
# chi("两碗大米饭", "地三鲜", "疙瘩汤", "东北大板")
# chi("大米饭", "地三鲜")


# def chi(**food): # 接受关键字参数,  接受到的是字典
#     print(food)
#
# # chi("胡辣汤", "猪蹄子", "肘子", "酱骨头") # 位置参数, 报错
# chi(a = "胡辣汤", b = "猪蹄子", c = "肘子", d = "酱骨头")

# # function
# def func(a, b, c, *args,**kwargs, d = 999):
#     print(a, b, c,d , args)
#
# func(1, 2,3,4,5,6,7,8,9, d=15)



# def func(*args, **kwargs): # 无敌传参
#     print(args, kwargs)
#
# func(1,2,3,4,5,6, a=18, b=19, c=20)

# print("周杰伦", "周润发", "周华健", sep="_sb_", end="哈哈哈哈啊哈哈")
# print("吃东西")


# def chi(*food): # 形参 . 动态接受位置参数, 打包成元组
#     print(food)
#
# lst = ["狮子头", "酱肘子", "烤鸭", "大腰子"]
#
# chi(*lst) # 实参, 把一个列表打散成位置参数


# def func(**kwargs): # 字典
#     print(kwargs)
#
# dic = {"a":1, "b":2, "c":3}
# func(**dic)  # 把一个字典打散成关键字参数
