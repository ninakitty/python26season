import os

# 1、 文件a1.txt内容
# 序号 部门 人数 平均年龄 备注
# 1 python 30 26 单身狗
# 2 Linux 26 30 没对象
# 3 运营部 20 24 女生多
# .......
# 通过代码，将其构建成这种数据类型：
# [{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'备注':'单身狗'},......]
# lst = []  # 定义要求所需列表
# with open('a1.txt', mode='r', encoding='utf8') as file:  # 打开文件,只读模式,编码使用utf8
#     titleLine = file.readline().strip().split(' ')  # 读取第一行内容做为标题,去除两端空白,将使用空格分割
#     for line in file:  # 继续读取剩余内容
#         dic = {}  # 定义临时存储字典
#         content = line.strip().split(' ')  # 将每行内容去除两端空白,用空格分割
#         for index in range(len(content)):  # 按照内容长度,索引循环
#             dic[titleLine[index]] = content[index]  # 将每项内容与标题加入字典
#         lst.append(dic)  # 将临时存储字典放入列表
# print(lst)


# 2、 传入函数的字符串中,[数字]、[字母]、[空格] 以及 [其他]的个数，并返回结果。
# def count_input(input_str):  # 定义计算字符串内容函数
#     count_num = 0  # 计数数字
#     count_alpha = 0  # 计数字母
#     count_space = 0  # 计数空白
#     count_other = 0  # 计数其他
#     for char in input_str:  # 循环输入的每个字符
#         if char.isdigit():  # 判断是否为数字
#             count_num += 1
#         elif char.isalpha():  # 判断是否为字母
#             count_alpha += 1
#         elif char.isspace():  # 判断是否为空白
#             count_space += 1
#         else:
#             count_other += 1
#     return {'num': count_num, 'alpha': count_alpha,
#             'space': count_space, 'other': count_other}
#
#
# result = count_input('12 3 qwe$中文')
# print(result)


# 3、 写函数，接收两个数字参数，返回比较大的那个数字。
# def compare(num1, num2):
#     return num1 if num1 > num2 else num2
#
#
# result = compare(21, 2)
# print(result)


# 4、 写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容
# 返回给调用者。
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# PS:字典中的value只能是字符串或列表

# def check_len(in_dic):  # 定义函数
#     dic = {}  # 定义临时字典
#     if isinstance(in_dic, dict):  # 判断传入的类型是否为字典
#         for key, value in in_dic.items():  # 迭代出字典中的key,value
#             if isinstance(value, str) or isinstance(value, list):  # 判断value是否为字符串或列表
#                 dic[key] = value[:2]  # 对字符串或列表进行切片
#             else:
#                 return '字典中的值不是"字符串"或"列表"'
#         return dic
#     return '请将参数更改为字典'
#
#
# result = check_len({1: "12221", 2: [1, 2, 3, 4]})
# print(result)


# 5、 写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一
# 个字典，此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为
# {0:11,1:22,2:33}

# def transform(input_list):  # 定义转换函数
#     if isinstance(input_list, list):  # 判断传入参数是否为列表
#         dic = {}  # 定义临时字典
#         for index in range(len(input_list)):  # 迭代出传入列表每个索引
#             dic[index] = input_list[index]  # 将列表的索引做为字典的key,列表内容做为value
#         return dic
#     else:
#         return '请传入列表数据类型'
#
#
# result = transform([11, 22, 33])
# print(result)

# 6、 写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，然后将这
# 四个内容传入到函数中，此函数接收到这四个内容，将内容追加到一个student_msg文件中。

# def student(name, gender, age, education):  # 定义学生函数
#     filename = 'student_msg'  # 文件名称
#     with open(filename, mode='a', encoding='utf8') as f:  # 以追加方式打开管道
#         content = f'{name}\t{gender}\t{age}\t{education}\n'
#         f.write(content)  # 写入内容
#
#
# name = input('请输入姓名:')
# gender = input('请输入性别:')
# age = input('请输入年龄:')
# education = input('请输入学历:')
# student(name, gender, age, education)

# 7、 对第9题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。
#
# def student(name, age, education, gender="男"):  # 定义学生函数,gender默认为男
#     filename = 'student_msg'  # 文件名称
#     with open(filename, mode='a', encoding='utf8') as f:  # 以追加方式打开管道
#         content = f'{name}\t{gender}\t{age}\t{education}\n'
#         f.write(content)  # 写入内容#
#
#
# while 1:
#     exit = input('如果输入Q则退出,回车键继续:').upper()  # 输入Q退出
#     if exit == 'Q':
#         break
#     name = input('请输入姓名:').strip()
#     gender = input('请输入性别:').strip()
#     age = input('请输入年龄:').strip()
#     education = input('请输入学历:').strip()
#     if gender == '女':  # 性别为女时传入参数gender
#         student(name, age, education, gender)
#     else:  # 否则不传入参数gender
#         student(name, age, education)

# 8、 写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作。
#
# def modify_file(file_name, old_content, new_content):  # 定义函数,传入文件名,修改内容,新内容
#     if os.path.isfile(file_name):  # 判断文件是否存在
#         with open(file_name, mode='r', encoding='utf8') as old_file, \
#                 open(file_name + '.bak', mode='w', encoding='utf8') as new_file:
#             # 原文件读方式打开,新文件写方式打开
#             for line in old_file:  # 迭代每行文件
#                 new_file.write(line.replace(old_content, new_content))  # 替换新内容,写入新文件
#         os.remove(file_name)  # 删除原文件
#         os.rename(file_name + '.bak', file_name)  # 修改新文件名,变为原文件名
#         return '内容批量修改完成'
#
#     else:
#         return '文件不存在!'
#
#
# filename = input('请输入要修改的文件名:')
# old_content = input('请输入要修改内容:')
# new_content = input('请输入新内容:')
# print(modify_file(filename, old_content, new_content))


# 读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
# a = 10
# b = 20
# def test5(a, b):
#     print(a, b)
# c = test5(b, a)
# print(c)

# 答:打印出来a是20,b是10,c是None
# b做为实参传入函数中形a的位置,a以实参传入形参b的位置,相当于位置进行了调换.函数没有返回值,c为None.

# 9、 读代码，回答：代码中, 打印出来的值a, b, c分别是什么？为什么？
# a = 10
# b = 20
# def test5(a, b):
#     a = 3
#     b = 5
# print(a, b)
# c = test5(b, a)
# print(c)
# 答:打印出的结果a是10,b是20,c是None
# 作用域范围问题,函数内部的a,b不能修改全局变量a,b的值

# 10、 写函数,传入函数中多个实参(均为可迭代对象如字符串,列表,元祖,集合等),将每个实参的每个元素依次
# 添加到函数的动态参数args里面.
# 例如 传入函数两个参数[1,2,3] (22,33)最终args为(1,2,3,22,33)

# def many_args(*arg):  # 定义函数
#     args = []  # 动态参数
#     for item in arg:  # 迭代每个参数
#         args.extend(item)  # 扩展list
#     return args
#
#
# result = many_args([1, 2, 3], (22, 33))
# print(result)

# 11、 写函数,传入函数中多个实参(实参均为字典),将每个实参的键值对依次添加到函数的动态参数kwargs
# 里面.
# 例如 传入函数两个参数{‘name’:’alex’} {‘age’:1000}最终kwargs为{‘name’:’alex’ ,‘age’:1000}

# def many_kwargs(*args):  # 定义函数
#     kwargs = {}  # 动态参数
#     for item in args:  # 迭代每个参数
#         for key, value in item.items():  # 迭代参数中的字典
#             kwargs[key] = value  # 添加key,value至动态参数
#     return kwargs
#
#
# result = many_kwargs({'name': 'alex'}, {'age': 1000})
# print(result)

# 12、 下面代码成立么?如果不成立为什么报错?怎么解决?
# 题目一：
# a = 2
# def wrapper():
#     print(a)
# wrapper()
# 答:成立,函数可以使用全局变量

# 题目二：
# a = 2
# def wrapper():
#     a += 1
# print(a)
# wrapper()
# 答:不成立,函数内部未定义变量a,不能直接修改全局变量

# 题目三：
# def wrapper():
#     a = 1
#     def inner():
#         print(a)
#     inner()
# wrapper()
# 答:成立,内部函数可调用外部函数中的变量

# 题目四：
# def wrapper():
#     a = 1
#     def inner():
#         a += 1
#         print(a)
#     inner()
# wrapper()
# 答:不成立,内部函数未定义变量a,不能直接修改外部函数的变量

# 13、 写函数,接收两个数字参数,将较小的数字返回.
# def compare_min(x, y):
#     return x if x < y else y
#
#
# result = compare_min(1, 2)
# print(result)

# 14、 写函数,接收一个参数(此参数类型必须是可迭代对象),将可迭代对象的每个元素以’_’相连接,形成新的字
# 符串,并返回.
# 例如 传入的可迭代对象为[1,'老男孩','武sir']返回的结果为’1_老男孩_武sir’
#
# def underline(iteration):  # 定义函数
#     for index in range(len(iteration)):  # 迭代参数中每个元素索引
#         iteration[index] = str(iteration[index])  # 将每个元素转换为字符
#     temp_str = '_'.join(iteration)  # 利用join拼接出新的字符
#     return temp_str
#
#
# result = underline([1, '老男孩', '武sir'])
# print(result)


# 15、 写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
# 例如：如:min_max(2,5,7,8,4) 返回:{‘max’:8,’min’:2}(此题用到max(),min()内置函数)
# def min_max(*args):
#     min_num = min(args)
#     max_num = max(args)
#     return {'max': max_num, 'min': min_num}
#
#
# result = min_max(2, 5, 7, 8, 4)
# print(result)

# 16、 写函数，传入一个参数n，返回n的阶乘
# 例如:cal(7) 计算7*6*5*4*3*2*1
# def cal(num):
#     factorial = 1  # 阶乘结果
#     for i in range(1, num + 1):  # 迭代每个元素
#         factorial *= i  # 每次与阶乘结果相乘
#     return factorial
#
#
# print(cal(7))

# 17、 写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
# 例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃’，‘A’)]
# def poker():  # 定义函数
#     pokers = []  # 定义扑克牌列表
#     color = ['红心', '草花', '方片', '黑桃']  # 定义牌色
#     transform = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}  # 待转换牌面
#     for num in range(1, 14):  # 迭代1-13
#         for item in color:  # 迭代颜色
#             if num in transform:  # 如果牌面为1,11,12,13转换为A,J,Q,K
#                 num = transform[num]
#             pokers.append((item, num))  # 将组合好元组加入至列表
#     return pokers
#
#
# print(poker())

# 18、 有如下函数:
# def wrapper():
#     def inner():
#         print(666)
#
#
# wrapper()
# 你可以任意添加代码,用两种或以上的方法,执行inner函数.

# 方法一
# def wrapper():
#     def inner():
#         print(666)
#
#     return inner  # 将inner返回
#
#
# wrapper()()

# 方法二
# def wrapper():
#     def inner():
#         print(666)
#
#     inner()  # 在wrapper内部执行inner
#
#
# wrapper()
