import time

# 1、计算两个格式化时间之间差了多少年月日时分秒
# time1 = '2018-03-30 14:20:35'
# time2 = '2019-03-30 14:20:35'
#
#
# def str_time_to_timestamp(in_time):  # 字符串转换成时间戳
#     time_style = '%Y-%m-%d %H:%M:%S'
#     structtime = time.strptime(in_time, time_style)  # 结构化时间
#     timestamp = time.mktime(structtime)  # 生成时间戳
#     return timestamp
#
#
# time1 = str_time_to_timestamp(time1)
# time2 = str_time_to_timestamp(time2)
# time_diff = abs(time2 - time1)
# struct_time = time.gmtime(time_diff)  # 生成0时区的结构化时间
#
# print(
#     f'两个时间相差{struct_time.tm_year - 1970}年,{struct_time.tm_mon - 1}月,{struct_time.tm_mday - 1}天,{struct_time.tm_hour}时,{struct_time.tm_min}分,{struct_time.tm_sec}秒')

# 2、计算当前时间所在月1号的时间戳
# import time
# day = '01'
# now_time = time.localtime()
# str_time = f'{now_time.tm_year}-{now_time.tm_mon}-{day}'  # 将当前时间转换为当月1日字符格式
# struct_time = time.strptime(str_time, '%Y-%m-%d')  # 结构化时间
# timestamp = time.mktime(struct_time)  # 转换为时间戳
#
# print(f'{day}号的时间戳为:{timestamp}')

# 3、生成一个6位随机验证码(包含数字和大小写字母)
import random

'''
num:48-57
upper:65-90
lower:97-122
'''

#
#
# def random_code(choice_len):
#     number = [x for x in range(48, 58)]  # 数字
#     upper_char = [y for y in range(65, 91)]  # 大写字母
#     lower_char = [z for z in range(97, 123)]  # 小写字母
#     all_list = [y for x in [number, upper_char, lower_char] for y in x]  # 合并
#     random_str = ''  # 随机码
#     for _ in range(choice_len):
#         random_str = random_str + chr(random.choice(all_list))  # 拼接
#     return random_str
#
#
# code = random_code(6)
# print("随机码:", code)

# 4、发红包、制定金额和个数随机分配红包金额
# def red_packet(money, number):
#     lst = []
#     residue = money  # 剩余金额
#     if number <= 0:
#         return '请使用大于0以上的个数'
#     if number == 1:
#         return [money]
#     number = number - 1  # 分配次数
#     while number:
#         min_money = 0.01
#         max_money = residue - min_money * number  # 最大值为余额减最小值乘剩余个数,此值可调整,越小越平均
#         number -= 1
#         temp = round(random.uniform(min_money, max_money), 2)  # 随机生成金额并四舍五入
#         lst.append(temp)
#         residue = round(residue - temp, 2)  # 相应余额减去生成金额
#         if number == 0:  # 最后一次
#             lst.append(round(residue, 2))
#     return lst
#
#
# result = red_packet(10, 5)
# print('红包列表为:',result)

# 5、分别列出给定目录下所有的文件和文件夹
# import os
#
#
# def open_dirs(adir, n):  # 传入目录和制表符位数
#     if os.path.isdir(adir):  # 判断传入文件是否是文件夹
#         list_dir = os.listdir(adir)
#         for item in list_dir:
#             cur_path = os.path.join(adir, item)  # 拼接路径
#             if os.path.isdir(cur_path):
#                 print('\t' * n, item)
#                 open_dirs(cur_path, n + 1)  # 递归
#             else:
#                 print('\t' * n, item)
#     else:
#         print('Not a directory!')
#
#
# open_dirs('.', 0)

# 6、获取当前文件所在目录
# import os
#
# filepath = os.getcwd()  # 当前目录
# print(filepath)

# 7、在当前目录下创建一个文件夹、在这个文件夹下创建一个文件
# import os
#
# in_dir = 'insert_dir'
# if not os.path.isdir(in_dir):  # 如果不存在,创建
#     os.mkdir(in_dir)
# os.chdir(in_dir)  # 改变目录
# with open('insert_file', mode='w', encoding='utf8') as file:  # 创建文件,写入内容
#     file.write('insert_content')

# 8、计算某路径下所有文件和文件夹的总大小
import os


def count_dir(a_dir):
    summary = 0
    list_dir = os.listdir(a_dir)  # 列出文件夹下内容
    for item in list_dir:
        cur_path = os.path.join(a_dir, item)  # 拼接路径
        if os.path.isdir(cur_path):
            summary += os.stat(cur_path).st_size  # 计算大小
            count_dir(cur_path)  # 递归
        else:
            summary += os.stat(cur_path).st_size
    return summary


print(count_dir('.'))
