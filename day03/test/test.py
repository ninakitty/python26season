# def prime(n): #质数
#     if n <= 1:
#         return 0
#     for i in range(2, n):
#         if n % i == 0:
#             return 0
#     return 1
#
#
# if __name__ == "__main__":
#     n = 100000
#     resault = 707829217
#     lst = []
#     for i in range(2, n + 1):
#         if prime(i):
#             lst.append(i)
#     print(lst)
#     for i in lst:
#         for j in lst:
#             if i * j == resault:
#                 print(i, j)
# lst = ["独孤求败", "乔峰", "扫地僧", "乔峰", '郭靖', "郭靖"]
# lst = list(set(lst))
# print(lst)
# f = open('文本文件.txt', mode='r', encoding='utf-8')
# for line in f:
#     print(line.strip())
# with open('文本文件.txt', 'r', encoding='utf8') as f:
#     for line in f:
#         print(line.strip())
#

# 读取文件,每一行做为标题
# fruit = []
# f = open('fruit.txt', mode='r', encoding='utf8')
# title = f.readline().strip().split(',')  # 获取标题
# for line in f:  # 迭代每行
#     dic = {}  # 新建临时字典
#     content = line.strip().split(',')  # 分割每行内容
#     for index in (len(title)):  # 迭代每个列表位置
#         dic[title[index]] = content[index]  # 字典添加内容
#     fruit.append(dic)  # 列表添加字典
# print(fruit)

# f = open('haha.txt', mode='a', encoding='utf8')
# f.write('aaaaaaaaaaaaaaaaaa')
# f.write('bbbbbbbbbbbbbbbbb')


# def aaa():
#     print('sssssss')
#     print('ddddddddd')
#
#
# aaa()
#
# def login():
#     name = input('请输入用户名:')
#     passwd = input('请输入密码:')
#     if name == 'alex' and passwd == '123':
#         return True
#     return False
#
#
# resl = login()
# print(resl)

# def yue(tools):
#     print(f'use {tools} do it!')
#
#
# yue('wechat')
# yue('momo')

def compare(x, y):
    # if x > y:
    #     return x
    # return y
    return x if x > y else y


big = compare(11, 22)
print(big)
