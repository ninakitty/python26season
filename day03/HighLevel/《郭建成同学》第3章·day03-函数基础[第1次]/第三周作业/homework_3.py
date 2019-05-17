# 1、文件a1.txt内容
"""
序号部门人数平均年龄备注1
python    30         26         单身狗2
Linux     26         30         没对象3
运营部     20         24         女生多
.......通过代码，将其构建成这种数据类型：
[{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'备注':'单身狗'},......]
"""

# lis = []
# f = open("homework_test.txt","r",encoding="utf-8")
# title = f.readline()
# title_list = title.strip().split()
# for line in f:
#     line_list = line.strip().split()
#     dic = {}
#     for i in range(len(title_list)):
#         dic[title_list[i]] = line_list[i]
#     lis.append(dic)
# print(lis)

# 2、写函数，计算传入函数的字符串中,[数字]、[字母]、[空格] 以及 [其他]的个数，并返回结果。
# def func(str_input):
#     count_num = 0
#     count_alp = 0
#     count_space = 0
#     count_others = 0
#     for i in str_input:
#         if i.isdigit():
#             count_num+=1
#         elif i.isalpha():
#             count_alp+=1
#         elif i.isspace():
#             count_space+=1
#         else:
#             count_others+=1
#     return count_num,count_alp,count_space,count_others
# print(func('+0-0skahe817jashf wet1'))


# # 3、写函数，接收两个数字参数，返回比较大的那个数字。
# def compare_func(a,b):
#     return a if a>b else b

# 4、写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# PS:字典中的value只能是字符串或列表

# def check(dic_index):
#     dic_1 = {}
#     for i,v in dic_index.items():
#         if len(v) > 2:
#             dic_1[i] = v[:2]
#     return dic_1
#
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# print(check(dic))

#5、 写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一
# 个字典，此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为
# {0:11,1:22,2:33}。

# def transform(lis):
#     if type(lis) == list:
#         dic = {}
#         for i in range(len(lis)):
#             dic[i] = lis[i]
#         return dic
#     else:
#         return False
#
# lis_1 = [11,22,33]
# print(transform(lis_1))

# 6、 写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，然后将这
# 四个内容传入到函数中，此函数接收到这四个内容，将内容追加到一个student_msg文件中。

# def write_file(name,sex,age,education):
#     f = open("student_msg",mode="a",encoding="utf-8")
#     f.write(f"{name,sex,age,education}")
# write_file("zhangsan","nan",22,"benke")

# 7、 对第6题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。

# def entrying():
#     while 1:
#         user_input = input("请输入任意键继续，输入Q或者q键退出：").upper()
#         if user_input == "Q":
#             break
#         else:
#             name = input("请输入你的姓名：")
#             age = input("请输入你的年龄：")
#             education = input("请输入你的学历：")
#             sex = input("请输入你的性别：")
#
#             def write_file(name,age,education,sex = "男"):
#                 f = open("student_msg",mode="a",encoding="utf-8")
#                 f.write(f"{name,age,education,sex}")
#
#             write_file(name, age, education, sex="男")
#             break
# entrying()


# 8、 写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作。
#
# def func(file_name,old_content,new_content):
#     with open(file_name,"r",encoding="utf-8") as f1,open("新文件","w",encoding="utf-8") as f2:
#         for line in f1:
#             if old_content in line:
#                 line = line.replace(old_content,new_content)
#             f2.write(line)
#
#     import os
#
#     os.remove(file_name)
#     os.rename("新文件",file_name)
# func("三国演义","孙悟空","猪八戒")


# # 8读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
# a=10
# b=20
# def test5(a,b):
#                 print(a,b)
# c = test5(b,a)
# print(c)
"""
打印出来a的值是20，b的值是10，c的值是None，因为传入的值分别是20和10，所以打印出来是20和10，
即a的值是20，b的值是10，将函数赋值给c。但是函数体没有返回任何值，默认为None，所以c的值是None
"""

# 9、读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
# a=10
# b=20
# def test5(a,b):
#     a=3
#     b=5
#     print(a,b)
# c = test5(b,a)
# print(c)
"""
打印出来a的值是3，b的值是5，c的值是None,因为传入的值分别是20和10，但是函数体内对a和b重新赋值，作为局部变量，打印出来的值
a的值是3，b的值是5，将函数赋值给c。但是函数体没有返回任何值，默认为None，所以c的值是None
"""

# 10、 写函数,传入函数中多个实参(均为可迭代对象如字符串,列表,元祖,集合等),将每个实参的每个元素依次
# 添加到函数的动态参数args里面.
# 例如 传入函数两个参数[1,2,3] (22,33)最终args为(1,2,3,22,33)
# li = [1,2,3]
# tu = (22,33)
# def scatter(*args):
#     lis = []
#     for i in args:
#         for ii in i :
#             lis.append(ii)
#     lis  = tuple(lis)
#     print(lis)
# scatter(li,tu)


# def scatter(*args):
#     print(args)
# scatter(*li,*tu)


# 11、 写函数,传入函数中多个实参(实参均为字典),将每个实参的键值对依次添加到函数的动态参数kwargs里面.
# 例如 传入函数两个参数{‘name’:’alex’} {‘age’:1000}最终kwargs为{‘name’:’alex’ ,‘age’:1000}
#


# dic_1 = {"name":"alex"}
# dic_2 = {"age":1000}
# def scatter(**dic):
#     print(dic)
# scatter(**dic_1,**dic_2)



# 12、 下面代码成立么?如果不成立为什么报错?怎么解决?
# 题目一：成立
# a = 2
# def wrapper():
#     print(a)
# wrapper()
# # 成立

# 题目二：不成立，不能改变全局变量
# a = 2
# def wrapper():
#     global a   #增加此行代码进行修改
#     a += 1
#     print(a)
# wrapper()


# 题目三：成立
# def wrapper():
#     a = 1
#     def inner():
#         print(a)
#     inner()
# wrapper()


# 题目四：不成立，不能修改上层的局部变量
# def wrapper():
#     a = 1
#     def inner():
#         nonlocal a
#         a += 1
#         print(a)
#     inner()
# wrapper()

# 13、 写函数,接收两个数字参数,将较小的数字返回.

# def func(a,b):
#     return a if a<b else b
# print(func(1,2))


# 14、 写函数,接收一个参数(此参数类型必须是可迭代对象),将可迭代对象的每个元素以’_’相连接,形成新的字符串,并返回.
# 例如 传入的可迭代对象为[1,'老男孩','武sir']返回的结果为’1_老男孩_武sir’
# li = [1,'老男孩','武sir']
# def connect(args):
#     s = ""
#     for i in args:
#         s = s + str(i) + "_"
#     s = s[:-1]
#     return s
# print(connect(li))

# li = [1,'老男孩','武sir']
# def connect(args):
#     s = "_"
#     for i,v in enumerate(args):
#         li[i] = str(v)
#         ret = s.join(li)
#     return ret
# print(connect(li))

# 15、 写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
# 例如：如:min_max(2,5,7,8,4) 返回:{‘max’:8,’min’:2}(此题用到max(),min()内置函数)
# def min_max(*args):
#     dic = {}
#     max_1 = max(args)
#     min_1 = min(args)
#     dic["max"] = max_1
#     dic["min"] = min_1
#     return dic
# print(min_max(2,5,7,8,4))


# 16、 写函数，传入一个参数n，返回n的阶乘
# 例如:cal(7) 计算7*6*5*4*3*2*1

# def factorial(n):
#     sum = 1
#     while n>0:
#         sum = sum*n
#         n-=1
#     return sum
# print(factorial(3))




# 17、 写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
# 例如：[(‘红心’，2), (‘草花’，2), …(‘黑桃’，‘A’)]
#
# def card():
#     lis_1 = []
#     lis_2 = []
#     for i in range(2,11):
#         lis_1.append(i)
#     lis_1.extend(["J", "Q", "K", "A"])   #lis_1是1-13
#     for i in lis_1:
#         for k in ["黑桃", "红桃", "方块", "草花"]:
#             a = (k,i)
#             lis_2.append(a)
#     return lis_2
#
# print(card())



# 18、 有如下函数:
# 你可以任意添加代码, 用两种或以上的方法, 执行inner函数
# 第一种方法
# def wrapper():
#         def inner():
#             print(666)
#         inner()
# wrapper()



# # 第二种
# def wrapper():
#     def inner():
#         print(666)
#     return inner
# wrapper()()