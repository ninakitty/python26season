#!/usr/bin/env python
# -*- encoding:utf-8 -*-
# Author: Andrew.zhan
# Create by 2019 Apr 14
import os
import sys
import re

LOCAL_DIR = sys.path[0]


def practice_1():
    '''
    文件a1.txt内容
    序号      部门    人数       平均年龄      备注
    1       python    30         26         单身狗
    2       Linux     26         30         没对象
    3       运营部     20         24         女生多
    .......
    通过代码，将其构建成这种数据类型：
    [{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'备注':'单身狗'},......]
    '''
    result = []
    with open("a1.txt", 'r') as fp:
        title_line = fp.readline().strip().split()
        for line in fp:
            format_dict = {}
            for index, key in enumerate(title_line):
                format_dict[key] = line.strip().split()[index]
            result.append(format_dict)
    return result


def practice_2():
    '''
    传入函数的字符串中,[数字]、[字母]、[空格] 以及 [其他]的个数，并返回结果。
    '''
    # 注: isalpha 包含中文. 所以判断字母不宜用isalpha.
    find_word = re.compile(r"[a-z]|[A-Z]", re.S)
    def statistical(something):
        words = []
        numbers = []
        space = []
        other = []
        for i in something:
            # 数字 应该是不止阿拉伯数字 所以不宜用isdigit.
            if i.isnumeric():
                numbers.append(i)
                continue
            if find_word.findall(i):
                words.append(i)
                continue
            if i == " ":
                space.append(i)
                continue
            other.append(i)
        # print(words, numbers, space, other)
        return len(words), len(numbers), len(space), len(other)
    word_count, number_count, space_count, other_count = statistical("This is 测试 string, it include 字母 and 数字一2③.")
    print(f"word_count:{word_count}, number_count:{number_count}, space_count:{space_count}, other_count:{other_count}")


def practice_3():
    '''
    写函数，接收两个数字参数，返回比较大的那个数字。
    '''
    def compare(*args):
        # sort_list = list(args)
        # sort_list.sort(reverse=True)
        # return sort_list[0]
        return max(*args)
    print(compare(1, 2, 3, 4, 10, 9))


def practice_4(dic):
    '''
    写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
    dic = {"k1": "v1v1", "k2": [11,22,33,44]}
    PS:字典中的value只能是字符串或列表
    '''
    result = {}
    for k, v in dic.items():
        result[k] = v[:2]
    return result


def practice_5(lst):
    '''
    写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，
    此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为{0:11,1:22,2:33}。
    '''
    result = {}
    if isinstance(lst, list):
        for index, value in enumerate(lst):
            result[index] = value
    return result


def practice_6():
    '''
    写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，然后将这四个内容传入到函数中，
    此函数接收到这四个内容，将内容追加到一个student_msg文件中。
    '''
    def input_student_msg(name, gender, age, edu):
        # 老师上课让练习绝对路径
        with open(os.path.join(LOCAL_DIR, "student_msg.txt"), "a") as fp:
            fp.write("%s\t%s\t%s\t%s\n" % (name, gender, age, edu))
    user_input = input("请按顺序输入(姓名,性别,年龄,学历)逗号分隔:").strip().replace("，", ",")
    name, gender, age, edu = user_input.split(",")
    input_student_msg(name, gender, age, edu)


def practice_7():
    '''
    对第9题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。
    '''
    def input_student_msg(_fp, name, age, edu, gender="男"):
        _fp.write("%s\t%s\t%s\t%s\n" % (name, gender, age, edu))
        _fp.flush()

    fp = open("student_msg.txt", "a")
    while True:
        template = {"name": "姓名", "gender": "性别", "age": "年龄", "edu": "学历"}
        parameters = {}
        for k, v in template.items():
            user_input = input("请输入%s: " % v).strip()
            if user_input:
                parameters[k] = user_input
            if user_input in ["q", "Q"]:
                break
        if "q" in parameters.values() or "Q" in parameters.values():
            break
        input_student_msg(fp, **parameters)
    fp.close()


def practice_8():
    '''
    写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作。
    读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
    a = 10
    b = 20
    def test5(a,b):
        print(a,b)
    c = test5(b,a)
    print(c)
    '''
    pass
    '''
    答:
    代码会输出
    20 10
    None
    全局名称空间的a=10, b=20 传递给test5这个函数(b,a). test5内的局部名称空间中a获得的是外部传进来的20, b获得的是外部传进来的10.
    print(a,b)时,调用的是局部空间内的变量.所以输出为20,10
    由于函数没有返回值,所以print(c)的值为None
    '''


def practice_9():
    '''
    读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
    a = 10
    b = 20
    def test5(a,b):
        a = 3
        b = 5
        print(a,b)
    c = test5(b,a)
    print(c)
    '''
    pass
    '''
    答:
    代码会输出
    3 5
    None
    在test5内,局部名称空间中将局部变量a与b重新赋值了.那么print局部变量ab则会输出重新赋值后的3和5
    由于没有返回值,所以print(c)的结果为None
    '''


def practice_10(*args):
    '''
    写函数,传入函数中多个实参(均为可迭代对象如字符串,列表,元祖,集合等),将每个实参的每个元素依次添加到函数的动态参数args里面.
    例如传入函数两个参数[1,2,3] (22,33)最终args为(1,2,3,22,33)
    '''
    print(args)


def practice_11(**kwargs):
    '''
    写函数,传入函数中多个实参(实参均为字典),将每个实参的键值对依次添加到函数的动态参数kwargs里面.
    例如传入函数两个参数{‘name’:’alex’} {‘age’:1000}最终kwargs为{‘name’:’alex’ ,‘age’:1000}
    '''
    print(kwargs)


def practice_12():
    '''
    下面代码成立么?如果不成立为什么报错?怎么解决?
    题目一:
        a = 2
        def wrapper():
            print(a)
        wrapper()
    答: 成立,局部空间可以调用全局空间的变量.

    题目二:
        a = 2
        def wrapper():
            a += 1
            print(a)
        wrapper()
    答: 不成立, 局部空间内不能直接修改全局空间的变量.
        如果要修改, 需要先使用global命令.

    题目三:
        def wrapper():
            a = 1
            def inner():
                print(a)
            inner()
        wrapper()
    答: 成立. 调用外层名称空间变量.

    题目四:
        def wrapper():
            a = 1
            def inner():
                a += 1
                print(a)
            inner()
        wrapper()
    答: 不成立, a += 1所在名称空间不能修改上一层的局部变量.
        如果要修改,需要先使用nonlocal命令.
    '''
    pass


def practice_13():
    '''
    写函数,接收两个数字参数,将较小的数字返回.
    '''
    def compare(*args):
        # sort_list = list(args)
        # sort_list.sort()
        # return sort_list[0]
        return min(*args)
    print(compare(1, 2, 3, 4, 10, 9))


def practice_14(iteration):
    '''
    写函数,接收一个参数(此参数类型必须是可迭代对象),将可迭代对象的每个元素以’_’相连接,形成新的字符串,并返回.
    例如传入的可迭代对象为[1,'老男孩','武sir']返回的结果为’1_老男孩_武sir’
    '''
    result = "_".join([str(i) for i in iteration])
    return result


def practice_15(*args):
    '''
    写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
    例如：如:min_max(2,5,7,8,4) 返回:{‘max’:8,’min’:2}(此题用到max(),min()内置函数)
    '''
    # 使用max和min的确要比转列表然后排序然后再取头尾这样来的要快.因为max和min相当于冒泡排序只做两次冒泡而已.
    max_number = max(*args)
    min_number = min(*args)
    return {"max": max_number, "min": min_number}


def practice_16(num):
    '''
    写函数，传入一个参数n，返回n的阶乘
    例如:cal(7)  计算7*6*5*4*3*2*1
    '''
    result = 1
    for i in range(2, num+1):
        result *= i
    return result


def practice_17():
    '''
    写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
    例如：[(‘红心’，2),(‘草花’，2), ...(‘黑桃’，‘A’)]
    '''
    mapping = {1: "A",
               11: "J",
               12: "Q",
               13: "K"}
    colors = ("红心", "草花", "方片", "黑桃")
    result = ["大王", "小王"]
    for num in range(1, 14):
        for color in colors:
            card_num = mapping.get(num) if num in mapping else num
            result.append((color, card_num))
    return result


def practice_18():
    '''
    有如下函数:
    def wrapper():
        def inner():
            print(666)
    wrapper()
    你可以任意添加代码,用两种或以上的方法,执行inner函数.
    '''
    # 方法1:
    def wrapper():
        def inner():
            print(666)
        inner()
    wrapper()

    # 方法2:
    def wrapper():
        def inner():
            print(666)
        return inner
    wrapper()()

    # 方法3:
    def wrapper(func):
        def inner():
            print(666)
        return inner

    @wrapper
    def test_func():
        pass
    test_func()


if __name__ == "__main__":
    # print(practice_1())
    # practice_2()
    # practice_3()
    # print(practice_4({"k1": "v1v1", "k2": [11,22,33,44]}))
    # print(practice_5([11, 22, 33]))
    # practice_6()
    # practice_7()
    # practice_10(*[1, 2, 3], *(22, 33), *{4, 5, 6}, *(7, 8, 9))
    # practice_11(**{'name': 'alex'}, **{'age': 1000})
    # practice_13()
    # print(practice_14([1, '老男孩', '武sir'])) or print(practice_14("string"))
    # print(practice_15(2, 5, 7, 8, 4))
    # print(practice_16(7))
    # print(practice_17())
    practice_18()
