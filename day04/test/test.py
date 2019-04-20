# 迭代器
# lst = ['哈哈', '呵呵', '嘿嘿', '吼吼', '哄哄']  # 定义列表
# iterator = lst.__iter__()  # 获取迭代器

# print(iterator.__next__())  # 获取下一个
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())

# 使用while代替for迭代器
# while 1:
#     try:
#         print(iterator.__next__())
#     except Exception:
#         break

# # 判断是否是可迭代的对象
# from collections import Iterator, Iterable  # 导入迭代器和是否可迭代
#
# it = lst.__iter__()  # 获取迭代器
# print('lst', isinstance(lst, Iterable), '可迭代')
# print('lst', isinstance(lst, Iterator), '是迭代器')
# print('it', isinstance(it, Iterable), '可迭代')
# print('it', isinstance(it, Iterator), '是迭代器')
#
# temp_str = 111
#
#
# def iterable(n):  # 定义迭代函数
#     if isinstance(n, Iterable):  # 判断是否可迭代
#         for i in n:  # 可迭代则
#             print(i)
#     else:
#         print(n)
#
#
# iterable(temp_str)

# 生成器
# def gen():  # 构造生成器
#     print('hahah')
#     yield 1  # 产生结果
#     print('hehehe')
#     yield 2  # 产生结果
#
#
# res = gen()  # 获取生成器generator--electric generator发电机
# print(res)
# print(res.__next__())
# print(res.__next__())

# 生成器生成衣服
# def order():  # 生成器定义
#     for i in range(10000):  # 迭代1W件衣服
#         yield str(i) + '--clothes'  # 产生衣服
#
#
# clothes = order()  # 获取生成器
# print(clothes.__next__())  # 输出衣服
# print(clothes.__next__())
# print(clothes.__next__())

# 列表推导式 lst=[结果 for循环 if判断]
# lst = ['oldboy python %s season' % i for i in range(1, 27) if i % 2 == 0]
# print(lst)

# 把姓张的人检索出来, 放在一个新列表里
# lst = ["欧阳娜娜", "张崔猛", "欧阳难过", "张亚无照", "胡一飞", "胡怎么飞", "张炸辉"]
# lst2 = [i for i in lst if '张' in i]
# print(lst2)

# 使用列表推导式得到            [1, 4, 9, 16, 25, 36]
# 在[3,6,9]的基础上推到出[[1,2,3], [4,5,6],[7,8,9]]
#
# lst = [i*i for i in range(1, 7)]
# print(lst)
#
# lst2 = [i * 3 for i in range(1, 4)]
# print(lst2)
#
# lst3 = [[j for j in range(i - 2, i + 1)] for i in lst2]
# print(lst3)

# 字典推导式 {key:value for循环 if判断}
# 利用函数
# lst = ['昌平', '丰台', '海淀']
# for index, value in enumerate(lst):
#     print(index, value)
# dic = {index: lst[index] for index in range(len(lst))}
# dic2 = {index: value for index, value in enumerate(lst)}
# print(dic)
# print(dic2)

# lambda 匿名函数
# 使用lambda定义匿名函数,传入参数,返回参数长度
# fn = lambda x: len(x)
# print(fn('酒仙桥困惑'))

# sorted 排序 sorted(可迭代对象,key=函数名)
# 排序字符列表
# lst = ['张三丰', '赵敏', '努尔哈赤']
#
#
# # 定义排序函数
# def sort(item):
#     return len(item)
#
#
# print(sorted(lst, key=sort))

# 用age排序
# lst = [{"id": 1, "name": 'alex', "age": 18}, {"id": 2, "name": 'wusir', "age": 16},{"id": 3, "name": 'taibai', "age": 17}]
# def returnid(dic):#排序函数
#     return dic['age']
# print(sorted(lst,key=returnid))
# print(sorted(lst,key=lambda x:x['age']))

# 用filter过滤 #filter(函数,可迭代对象)
# it=filter(lambda dic:dic['age']>=18,lst)
# print(list(it))

# 装饰器雏形

# def func():  # 定义原始函数
#     print('初始函数')
#
#
# def wrapper(fn):  # 定义装饰器
#     def inner():  # 内层函数
#         print('初始函数执行之前')
#         fn()  # 执行原始函数
#         print('初始函数执行之后')
#
#     return inner  # 返回内层函数
#
#
# func = wrapper(func)  # 将装饰后的函数再次赋值给原函数名
# print(func.__closure__)  # 判断是否为一个闭包
# func()  # 执行原始函数名

def wrapper(fn):  # 定义装饰器
    def inner(*args, **kwargs):  # 内层待运行函数,添加*args,**kwargs聚合
        print('打开外挂')
        fn(*args, **kwargs)  # 在原函数上下游添加代码,添加*args,**kwargs打散
        print('关闭外挂')

    return inner  # 返回待运行函数


@wrapper  # 相当于---dnf = wrapper(dnf)  # 函数伪装--->使用@装饰器函数名称代替
def dnf(uname, upwd):  # 玩DNF
    print('玩DNF', uname, upwd)


@wrapper
def lol(qq):
    print('玩LOL', qq)


# dnf = wrapper(dnf)  # 函数伪装--->使用@装饰器函数名称代替
dnf('alex', '10086')  # 执行函数
lol('8993772')
