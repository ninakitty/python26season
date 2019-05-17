#!/usr/bin/env/python
#-*- coding:utf-8 -*-
#author: zhangliang

#1、计算两个格式化时间之间差了多少年月日时分秒
import time
def timestamp1(start_time, end_time):
    start = time.mktime(time.strptime(start_time, '%Y-%m-%d %H:%M:%S'))
    end = time.mktime(time.strptime(end_time, '%Y-%m-%d %H:%M:%S'))
    dif_time = end - start
    struct_time = time.gmtime(dif_time)
    print('差%d年%d月%d天%d小时%d分钟%d秒'%(struct_time.tm_year - 1970, struct_time.tm_mon - 1,
                                       struct_time.tm_mday - 1, struct_time.tm_hour,
                                       struct_time.tm_min, struct_time.tm_sec))
timestamp1("2014-02-21 08:30:20", "2018-08-02 21:10:58")

# 2、计算当前时间所在月1号的时间戳'''
def get_month_first():
    str_time = time.strftime('%Y-%m')
    struct_time = time.strptime(str_time,'%Y-%m')  #'2018-08'
    return time.mktime(struct_time)
print(get_month_first())

# 3、生成一个 6 位随机验证码(包含数字和大小写字母)
import random
def check_code(n = 6):
    check = ""
    for i in range(n):
        current_code = random.randrange(n)
        if current_code == i:
            temp = str(random.randrange(0, 9))
        elif current_code > i:
            temp = chr(random.randrange(65, 90))
        else:
            temp = chr(random.randrange(97, 122))
        check += temp
    return check
res = check_code(6)
print(res)

# 4、发红包、制定金额和个数随机分配红包金额  开始没思路 跟着张开老师直播代码写了一遍
import random
def send_hb(money, num):
    r = random.sample(range(1, money * 100), num - 1)
    r.extend([0, money * 100])
    r.sort()
    return [(r[i + 1] - r[i]) / 100 for i in range(num)]
print(send_hb(200, 10))

# 5、分别列出给定目录下所有的文件和文件夹
import os
def all_file_dir(path):
    path_list = os.listdir(path)
    dic = {'文件夹': [], '文件': []}
    for i in path_list:
        if os.path.isdir(i):
            dic['文件夹'].append(i)
        else:
            dic['文件'].append(i)
    return ('%s目录内所有文件夹:\n%s\n%s\n目录内所有文件:\n%s\n'%(path, dic['文件夹'], path, dic['文件']))
print(all_file_dir("D:/23期上课内容/day02"))

#6、获取当前文件所在目录
print(os.getcwd())

#7、在当前目录下创建一个文件夹、在这个文件夹下创建一个文件
import os
def create_dir(file_dir, file_name):
    flag = os.getcwd()                  # 获取当前目录
    # 判断该文件夹是否存在，存在则删除
    if os.path.isdir(file_dir):
        os.chdir(file_dir)
        # 循环删除该文件夹内的文件
        for i in os.listdir(os.getcwd()):
            os.remove(i)
        # 退出到原来的目录，执行删除该文件夹
        os.chdir(flag)
        os.removedirs(file_dir)
    # 如果没有该文件夹，则执行创建操作
    os.mkdir(file_dir)
    os.chdir(file_dir)
    open(file_name, 'w').close()

# 8、计算器
import re  #导入re模块

#加法运算
add = re.compile(r'(-?\d+\.?\d*\+-\d+\.?\d*)|(-?\d+\.?\d*\+\d+\.?\d*)')
#减法规则
sub = re.compile(r'(-?\d+\.?\d*--\d+\.?\d*)|(-?\d+\.?\d*-\d+\.?\d*)')
#乘法规则
mul = re.compile(r'(\d+\.?\d*\*-\d+\.?\d*)|(\d+\.?\d*\*\d+\.?\d*)')
#除法规则
div = re.compile(r'(\d+\.?\d*/-\d+\.?\d*)|(\d+\.?\d*/\d+\.?\d*)')
#查询最内层括号
bracket = re.compile(r'\([^()]+\)')
#验证括号是否运算完毕
c_f = re.compile(r'\(?\+?-?\d+\)?')
#去括号规则
strip = re.compile(r'[^(].*[^)]')

#计算表达式中的加法运算
def add_method(s):
    exp = re.split(r'\+', add.search(s).group())
    return s.replace(add.search(s).group(), str(float(exp[0]) + float(exp[1])))

#计算表达式中的减法运算
def sub_method(s):
    exp = sub.search(s).group()
    if exp.startswith('-'):
        exp = exp.replace('-', '+')
        res = add_method(exp).replace('+', '-')
    else:
        exp = re.split(r'-', exp)
        res = str(float(exp[0]) - float(exp[1]))
    return s.replace(sub.search(s).group(), res)

#计算表达式中的乘法运算
def mul_method(s):
    exp = re.split(r'\*', mul.search(s).group())
    return s.replace(mul.search(s).group(), str(float(exp[0]) * float(exp[1])))

#计算表达式中的除法运算
def div_method(s):
    exp = re.split(r'/', div.search(s).group())
    return s.replace(div.search(s).group(), str(float(exp[0]) / float(exp[1])))

def calc():
    while True:
        s = input('请输入要计算的表达式(\033[31;1m注意：退出，输入q\033[0m): ').strip()
        if s == 'q':
            print("即将退出！！！")
            break
        else:
            #按空格将表达式进行分割
            s = ''.join([x for x in re.split('\s+', s)])
            #表达式首尾是否有括号
            if not s.startswith('('):
                s = str('(%s)' % s)
            #表达式存在括号
            while bracket.search(s):
                # 将表达式中--运算替换为+运算
                s = s.replace('--', '+')
                # 将最内层括号的值赋值给s_search
                s_search = bracket.search(s).group()
                #判断除法运算是否存在
                if div.search(s_search):
                    #执行除法运算
                    s = s.replace(s_search, div_method(s_search))
                #判断乘法运算是否存在
                elif mul.search(s_search):
                    #执行乘法运算
                    s = s.replace(s_search, mul_method(s_search))
                #判断减法运算是否存在
                elif sub.search(s_search):
                    #执行减法运算
                    s = s.replace(s_search, sub_method(s_search))
                #判断加法是否存在
                elif add.search(s_search):
                    #执行加法运算
                    s = s.replace(s_search, add_method(s_search))
                #判断括号内有没有运算
                elif c_f.search(s_search):
                    #无运算去掉括号
                    s = s.replace(s_search, strip.search(s_search).group())
            print('结果是： %s' %(s))
#调用计算器
calc()
