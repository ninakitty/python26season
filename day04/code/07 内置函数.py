# lst = [1,2,3]
#
# it = iter(lst)
# print(it.__next__())
# print(it.__next__())
# print(next(it))

# s = "1+1+9+18"
# ret = eval(s) # eval 执行代码. 有返回值
# print(ret)

# s = input('请输入一段你想执行的代码:')
# exec(s)
# print("哈哈哈哈")

# code = compile("for i in range(10):print(i)", "", "exec")
# exec(code)


# s = "[1,2,2,3,4,5]"
# lst = eval(s)
# print(lst)
#
#
# print(hash([1, 2, 3])) # 7124720865009418633
#
# import os
# s = "os"
# __import__(s)


# print(help(str))


# def func(a):
#     if callable(a):
#         a()
#     else:
#         print(a)
#
# def ha():
#     print("我是哈哈哈")
#
# func(ha)


# print(bin(20))
# print(oct(20))
# print(hex(20)) # 0-9abcdef

# print(divmod(10,3)) # // %
# print(pow(2,10))

# print(sum([12,2,1,2]))

# lst = [2,3,4,5,6]
# r = reversed(lst)
# for i in r:
#     print(i)

# s = slice(1, 5,2)
# ss = "hello,I'm good"
# print(ss[1:5:2])
#
# ss = "hello,I'm good"
# print(ss[s])
#
# ss = "hello,I'm good"
# print(ss[s])
#
# ss = "hello,I'm good"
# print(ss[s])
# ss = "hello,I'm good"
# print(ss[s])

# s = "周杰伦"
# print(s.center(20, "*"))
#
# print(format("周杰伦", "*>20"))
# print(format(18, "010b"))
# print(bin(18))

# s = "192.168.1.1"
# lst = s.split(".")
# for item in lst:
#     print(format(int(item), "08b"))

# print(format(1.23956789, ".2f"))

# # print(ord('中')) # unicode
# # print(chr(20013))
# for i in range(65536):
#     print(chr(i), end=" ")


# \\
# 转义字符


# s = "你好\啊"  # python中的字符串 str()
# print(s)
# print(repr(s)) # 官方提供的字符串表示形式


# print(r"我的天那\ 怎么不好使了") # 字符串原样输出


# s = {1,2,3}
# fs = frozenset(s)
# print(hash(fs))


#
# lst = [11,22,33,44]
#
# # for i in range(len(lst)):
# #     print(i)
# #     print(lst[i])
#
# for i, item in enumerate(lst, 100):
#     print(i)
#     print(item) # (索引, 元素)

# print(all([18, False, 12]))  # and  => bool
# print(any([19,0,22])) # or => bool


# lst1 = ["赵本山", "范伟", "小沈阳"]
# lst2 = ("乡村爱情", "卖乖", "不差钱")
# lst3 = ["白云", "黑土"]
#
# z = zip(lst1, lst2, lst3) # 水桶效应
# for item in z:
#     print(item)


# wei1 = [11,22.36,  8, 9, 12, 64]
# wei2 = [11,22.36,  8, 9, 12, 64]
# wei3 = [11,22.36,  8, 9, 12, 64]
# wei4 = [11,22.36,  8, 9, 12, 64]
# wei5 = [11,22.36,  8, 9, 12, 64]


# lst = [22,1,3,5,6,7]
# s = sorted(lst)
# print(s)

# lst = ["高进", "波多野结衣", "苍老师", "仓木麻衣", "红狗"]
# def func(item):  # item是列表中的每一个数据
#     return len(item) # 返回长度
#
# s = sorted(lst,key=lambda s: len(s))
# # 首先,打开这个可迭代对象. 然后获取到每一项数据. 把每一项数据传递给函数.
# # 根据函数返回的数据进行排序
# print(s)


# lst = [{"id":1, "name":'alex', "age":18},
#  {"id":2, "name":'wusir', "age":16},
#  {"id":3, "name":'taibai', "age":17}]
# # 用age排序
# # def func(d):
# #     return d['age']
#
# s = sorted(lst, key=lambda d: d['age'], reverse=True)
# print(s)


# lst = [18, 22, 66, 35, 1, 48]
#
# # 筛选出来. 大于20的数据
#
# f = filter(lambda n:n>20 , lst)  # 返回迭代器, 把可迭代对象中的每一项数据交给前面的函数. 由函数决定该数据是否保留
# for item in f:
#     print(item)


# lst = [{"id":1, "name":'alex', "age":18},
#  {"id":2, "name":'wusir', "age":16},
#  {"id":3, "name":'taibai', "age":17}]
#
# #  保留成年人  age >= 18
# f = filter(lambda x: x['age']>=18   , lst)
# print(list(f))


# lst = [2,5,3,2,4]
# m = map(lambda x: x*x, lst)
#
# for item in m:
#     print(item)


