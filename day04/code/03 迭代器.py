# for i in 123:
#     print(i)

# print(dir(str))  # '__iter__'
# print(dir(list)) # '__iter__'
# print(dir(dict)) # '__iter__'

# print("__iter__" in dir(set))

# lst = ["烂片", "妇联No", "蜘蛛侠", "超人", "蝙蝠侠"]
# it = lst.__iter__() # iterator 迭代器
# print(it) #  '__iter__', '__next__'
#
# # for el in it:
# #     print(el)
#
# # 从迭代器获取到数据: __next__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
#
# # StopIteration 停止迭代. 没有数据了
# print(it.__next__())

# for循环的内部原理
# for循环内部使用的是迭代器
# lst = ["张无忌","张三丰", "张翠山", "张天宝"]
#
# it = lst.__iter__()
#
# while 1:
#     try:
#         n = it.__next__()
#         print(n)
#     except StopIteration:
#         break

# lst = [12,3,4,5]  # 可迭代对象   => __iter__
# it = lst.__iter__() # 迭代器  =>  __next__, __iter__
# print(it.__next__())

from collections import Iterable, Iterator

lst = [1,2,3]
print(isinstance(lst, Iterable)) # 判断列表是否是可迭代的
print(isinstance(lst, Iterator)) # 判断列表是否是是迭代器

it = lst.__iter__()
print(isinstance(it, Iterable)) # 判断列表是否是可迭代的
print(isinstance(it, Iterator)) # 判断列表是否是是迭代器

def func(n):
    if isinstance(n, Iterable): # 判断是否是可迭代对象
        for item in n:
            print(item)
    else:
        print(n)


func(123)