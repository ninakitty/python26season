'''
1、计算两个格式化时间之间差了多少年月日时分秒
'''
# import time
#
# def diff_date(date_str1, date_str2):
#     diff_second = int(abs(time.mktime(time.strptime(date_str1, "%Y-%m-%d %H:%M:%S")) -   # 取两个时间的秒差值
#                           time.mktime(time.strptime(date_str2, "%Y-%m-%d %H:%M:%S"))))
#     struct_time = time.localtime(diff_second)  # 结构化时间
#     diff_year = struct_time.tm_year - 1970
#     diff_mon = struct_time.tm_mon - 1
#     diff_day = struct_time.tm_mday - 1
#     diff_hour = struct_time.tm_hour - 8  # 东八区
#     if diff_hour < 0:
#         diff_day -= 1
#         diff_hour += 24
#
#     if diff_day < 0:
#         diff_mon -= 1
#         diff_day += 30
#
#     if diff_mon < 0:
#         diff_year -= 1
#         diff_mon += 12
#     return diff_year, diff_mon, diff_day, diff_hour, struct_time.tm_min, struct_time.tm_sec
#
# print("两个格式化时间之间差了%d年%d月%d日%d时%d分%d秒" % diff_date("1989-01-28 06:23:05", "2019-5-6 08:43:10"))

'''
2、计算当前时间所在月1号的时间戳
'''
# import time
# def get_day1_time():
#     now_year_mon = time.strftime("%Y-%m") + "-01"  # 当前时间所在月1号
#     return time.mktime(time.strptime(now_year_mon, "%Y-%m-%d"))
#
# print(get_day1_time())

'''
3、生成一个6位随机验证码(包含数字和大小写字母)
'''
# import random
#
# print("".join(random.sample('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 6)))  # 方法一
#
# def get_vcode(v_len):   # 方法二
#     vcode = ""
#     for i in range(v_len):
#         num = chr(random.randint(48, 57))  # 数字0-9
#         upper_letter = chr(random.randint(65, 90))  # 大写字母A-Z
#         lower_letter = chr(random.randint(97, 122))  # 小写字母a-z
#         vcode += random.choice([num, upper_letter, lower_letter])
#     return vcode
#
# print(get_vcode(6))

'''
4、发红包、制定金额和个数随机分配红包金额
原理: 
    总金额 = 总金额
    总金额 = 元素1-0 + 元素2-元素1 + 元素3-元素2 + 元素4-元素3 + 元素5-元素4 + 总金额-元素5
'''
# import random
#
# def red_envelope(total_money=10.0, count=5):  # 总金额有可能为浮点数
#     temp_lst = random.sample(range(1, int(total_money*100)), count+1)  # 创建一个长度为count+1的列表
#     temp_lst[0], temp_lst[-1] = 0, total_money*100  # 设置第一个元素值为0, 最后一个元素值为总钱数*100
#     temp_lst.sort()  # 列表排序
#     lst = []
#     for i in range(count):   # 红包数量
#         lst.append((temp_lst[i+1] - temp_lst[i])/100)  # 列表后一个元素减前一个元素
#     return lst, sum(lst)
#
# print(red_envelope(0.1, 8))

'''
5、分别列出给定目录下所有的文件和文件夹
'''
# import os
#
# def get_folder_list1(path):  # 方法一
#     if os.path.isdir(path):  # 判断是否是目录
#         for file in os.listdir(path):   # 列出目录下所有的文件和文件夹
#             sub_path = os.path.join(path, file)  # 目录拼接
#             if os.path.isdir(sub_path):  # 判断子文件是否是文件夹
#                 folder_lst.append(file)  # 添加到文件夹列表
#                 get_folder_list1(sub_path)   # 递归调用
#             else:
#                 file_lst.append(file)   # 添加到文件列表
#         return folder_lst, file_lst
#     else:
#         return -1, -1  # 目录有问题, 没找到
#
# def get_folder_list2(path):  # 方法二
#     folder_lst2, file_lst2 = [], []
#     if os.path.isdir(path):
#         for root, folder_lst, file_lst in os.walk(path):
#             folder_lst2 += folder_lst
#             file_lst2 += file_lst
#         return folder_lst2, file_lst2
#     else:
#         return -1, -1  #目录有问题,没找到
#
# folder_lst = []
# file_lst = []
# path = r"F:\2019老男孩周末26期\day05"
# print("文件夹: %s\n文件: %s" % get_folder_list1(path))  # 方法一
# print("文件夹: %s\n文件: %s" % get_folder_list2(path))  # 方法二

'''
6、获取当前文件所在目录
'''
# import os
# print(os.getcwd())

'''
7、在当前目录下创建一个文件夹、在这个文件夹下创建一个文件
'''
# import os
#
# def create_folder_file(folder, file):
#     if not os.path.exists(folder):  # 判断文件夹是否存在
#         os.makedirs(folder)  # 不存在,则创建
#     with open(os.path.join(folder, file), mode="w", encoding="utf-8"):  # 创建空文件
#         pass
#
# create_folder_file("folder", "file_name")

'''
8、计算某路径下所有文件和文件夹的总大小
'''
# import os
#
# def convert_size(func):  # 单位换算
#     def inner(*args):
#         size = func(*args)
#         if size > 1024*1024*1024:
#             size = format(size / 1024 / 1024 / 1024, ".2f") + "GB"
#         elif size > 1024 * 1024:
#             size = format(size / 1024 / 1024, ".2f") + "MB"
#         elif size > 1024:
#             size = format(size / 1024, ".2f") + "KB"
#         else:
#             size = str(size)+"byte"
#         return size
#     return inner
#
# @convert_size
# def get_folder_size1(path): # 方法一
#     total_size = 0
#     for root, folder_lst, file_lst in os.walk(path):
#         for file in file_lst:
#             total_size += os.path.getsize(os.path.join(root, file))
#     return total_size
#
# @convert_size
# def get_folder_size2(path):   # 方法二
#     global total_size   # 引用全局变脸
#     if os.path.isdir(path):  # 判断是否是文件夹
#         for file in os.listdir(path):  # 列出目录下所有的文件和文件夹
#             sub_path = os.path.join(path, file)  # 目录拼接
#             if os.path.isdir(sub_path):  # 判断是否是文件夹
#                 get_folder_size2(sub_path)  # 递归调用
#             else:
#                 total_size += os.path.getsize(sub_path)  # 累加文件大小
#         return total_size
#     elif os.path.isfile(path):  # 是文件直接返回
#         return os.path.getsize(path)
#     else:  # 没找到
#         return -1
#
# total_size = 0
# path = r"F:\2019老男孩周末26期"
# print(get_folder_size1(path))  # 方法一
# print(get_folder_size2(path))  # 方法二
