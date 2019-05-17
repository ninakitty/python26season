'''
1、 文件a1.txt内容
序号 部门 人数 平均年龄 备注
1 python 30 26 单身狗
2 Linux 26 30 没对象
3 运营部 20 24 女生多
.......
通过代码，将其构建成这种数据类型：
[{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'备注':'单身狗'},......]
'''
# lst = []
# with open("a1.txt", mode="r", encoding="utf-8") as f:
#     title_lst = f.readline().strip().split()
#     for line in f:
#         content_lst = line.strip().split()
#         lst.append(dict(zip(title_lst, content_lst)))
#
# print(lst)

'''
2、 传入函数的字符串中,[数字]、[字母]、[空格] 以及 [其他]的个数，并返回结果。
'''
# def type_count(s):    #方法一 (当用户不输入汉字)
#     dic = {"Digit": 0, "Alpha": 0, "Space": 0, "Ether": 0}
#     for i in s:
#         if i.isdigit():
#             dic["Digit"] += 1
#         elif i.isspace():
#             dic["Space"] += 1
#         elif i.isalpha():
#             dic["Alpha"] += 1
#         else:
#             dic["Ether"] += 1
#     return dic
#
# print(type_count("azAZ 0189\t\n\r.="))

'''方法二 使用ord获取ascii码的值'''
# def type_count(s):
#     dic = {"Digit": 0, "Alpha": 0, "Space": 0, "Ether": 0}
#     for i in s:
#         i = ord(i)
#         if i == 9 or i == 10 or i == 13 or i == 32:   #\t \n \r 空格
#             dic["Space"] += 1
#         elif i >= 48 and i <= 57:     #数字0~9
#             dic["Digit"] += 1
#         elif (i >= 65 and i <= 90) or (i >= 97 and i <= 122):   #大小写字母
#             dic["Alpha"] += 1
#         else:
#             dic["Ether"] += 1
#     return dic
#
# print(type_count("azAZ 0189\t\n\r.="))

'''
3、 写函数，接收两个数字参数，返回比较大的那个数字。
'''
# def compare(n1, n2):
#     return n1 if n1 > n2 else n2    #三目运算
# print(compare(4, 8))

'''
4、 写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容
返回给调用者。
dic = {"k1": "v1v1", "k2": [11,22,33,44]}
PS:字典中的value只能是字符串或列表
'''
# def checkDicVal(dic):
#     for k, v in dic.items():
#         if len(v) > 2:
#             dic[k] = v[:2]
#     return dic
#
# dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
# print(checkDicVal(dic))

'''
5、 写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一
个字典，此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为
{0:11,1:22,2:33}。
'''
# def to_dic(lst):
#     return dict(zip(range(len(lst)), lst))
#
# print(to_dic([11, 22, 33]))

'''方法二'''
# def to_dic(lst):
#     return {k: v for k, v in enumerate(lst)}
#
# print(to_dic([11,22,33]))

'''
6、 写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，然后将这
四个内容传入到函数中，此函数接收到这四个内容，将内容追加到一个student_msg文件中。
'''
# def entry_info(name, gender, age, edu):
#     with open("student_msg", mode="a", encoding="utf-8") as f:
#         f.write("%s %s %s %s\n" % (name, gender, age, edu))
#
# entry_info("alex", "男", 30, "本科")

'''
7、 对第6题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。
'''
# def entry_info(name, age, edu, gender="男"):
#     with open("student_msg", mode="a", encoding="utf-8") as f:
#         f.write("%s %s %s %s\n" % (name, gender, age, edu))
#
# while 1:
#     username = input("Username (quit Q): ").strip()
#     if username.upper() == "Q":
#         break
#     gender = input("Gender (默认 男): ").strip()
#     age = input("Age: ").strip()
#     edu = input("Education: ").strip()
#     entry_info(username, age, edu) if gender == "" else entry_info(username, age, edu, gender)

'''
8、 写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作。
'''
# def edit_fcontent(filename, old, new):
#     with open(filename, mode="r", encoding="utf-8") as f1,\
#             open("%s.bak" %filename, mode="w", encoding="utf-8") as f2:
#         for i in f1:
#             f2.write(i.replace(old, new)) if old in i else f2.write(i)
#
#     import os
#     os.remove(filename)
#     os.rename("%s.bak" % filename, filename)
#
# edit_fcontent("student_msg", "女", "男")

'''
8、读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
a=10
b=20
def test5(a,b):
    print(a,b)
c = test5(b,a)
print(c)
'''
#a = 20 b = 10 c = None
#因为调用函数test5的时候,两个实参名和两个形参名反了,所以,在函数test5内打印的结果就是 20 10
#因为函数test5没有返回值,所以c为None

'''
9、 读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
a=10
b=20
def test5(a,b):
    a=3
    b=5
    print(a,b)
c = test5(b,a)
print(c)
'''
#a = 3 b = 5 c = None
#因为打印出来的a和b都是在函数test5内重新声明赋值后的值
#因为函数test5没有返回值,所以c为None

'''
10、 写函数,传入函数中多个实参(均为可迭代对象如字符串,列表,元祖,集合等),将每个实参的每个元素依次
添加到函数的动态参数args里面.
例如 传入函数两个参数[1,2,3] (22,33)最终args为(1,2,3,22,33)
'''
# def func(*args):
#     print(args)
# func(*[1,2,3], *(22,33))

'''
11、 写函数,传入函数中多个实参(实参均为字典),将每个实参的键值对依次添加到函数的动态参数kwargs
里面.
例如 传入函数两个参数{'name': 'alex'} {'age' :1000}最终kwargs为{‘name’:’alex’ ,‘age’:1000}
'''
# def func(**kwargs):
#     print(kwargs)
# func(**{'name': 'alex'}, **{'age' :1000})

'''
12、 下面代码成立么?如果不成立为什么报错?怎么解决?
题目一：
a = 2
def wrapper():
    print(a)
wrapper()
题目二：
a = 2
def wrapper():
    a += 1
    print(a)
wrapper()
题目三：
def wrapper():
    a = 1
    def inner():
        print(a)
    inner()
wrapper()
题目四：
def wrapper():
    a = 1
    def inner():
        a += 1
        print(a)
    inner()
wrapper()
'''
#题目一,成立

'''题目二,不成立,因为a是全局变量,在函数体内没有声明变量a,所以不能改变a的值,解决方法如下:'''
# a = 2
# def wrapper():
#     global a
#     a += 1
#     print(a)
# wrapper()

'''题目三,成立'''
# def wrapper():
#     a = 1
#     def inner():
#         print(a)
#     inner()
# wrapper()

'''题目四,不成立,因为变量a在函数inner内没有声明赋值,可以使用nonlocal解决,代码如下:'''
# def wrapper():
#     a = 1
#     def inner():
#         nonlocal a
#         a += 1
#         print(a)
#     inner()
# wrapper()

'''
13、 写函数,接收两个数字参数,将较小的数字返回.
'''
# def return_min(n1, n2):
#     return n1 if n1 < n2 else n2    #三目运算
# print(return_min(4, 2))

'''
14、 写函数,接收一个参数(此参数类型必须是可迭代对象),将可迭代对象的每个元素以_’相连接,形成新的字
符串,并返回.
例如 传入的可迭代对象为[1,'老男孩','武sir']返回的结果为1_老男孩_武sir’
'''
# def to_str(*args):
#     return "_".join(str(i) for i in args)
#
# print(to_str(*[1,'老男孩','武sir']))

'''
15、 写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
例如：如:min_max(2,5,7,8,4) 返回:{‘max’:8,’min’:2}(此题用到max(),min()内置函数)
'''
# def min_max(*args):
#     return {'max': max(args), 'min': min(args)}
# print(min_max(2, 5, 7, 8, 4))

'''
16、 写函数，传入一个参数n，返回n的阶乘
例如:cal(7) 计算7*6*5*4*3*2*1
'''
# def cal(n):
#     fac = 1
#     for i in range(1, n+1):
#         fac *= i
#     return fac
#
# print(cal(7))

'''
17、 写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃’，‘A’)]
'''
# def card():
#     num_lst = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
#     kind_lst = ["红心", "草花", "方块", "黑桃"]
#     return list(zip(num_lst*len(kind_lst), kind_lst*len(num_lst)))
#
# print(card())

'''
18、 有如下函数:
def wrapper():
    def inner():
        print(666)
wrapper()
你可以任意添加代码,用两种或以上的方法,执行inner函数.
'''
# def wrapper():    #方法一
#     def inner():
#         print(666)
#     inner()
# wrapper()

'''方法二 函数名可以作为返回值返回'''
# def wrapper():
#     def inner():
#         print(666)
#     return inner
# wrapper()()

