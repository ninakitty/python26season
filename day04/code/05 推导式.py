# lst = []
# for i in range(1, 27):
#     lst.append("python周末班%s" % i)
#
# print(lst)

# lst = ["python周末班%s" % i for i in range(1, 27) if i%2==0 ]
# print(lst)
#
# # 把姓张的人检索出来, 放在一个新列表里  startswith
# lst = ["欧阳娜娜", "张崔猛", "欧阳难过", "张亚无照", "胡一飞", "胡怎么飞", "张炸辉"]
# print([name for name in lst if name.startswith("张") ])
# 使用列表推导式得到            [1, 4, 9, 16, 25, 36]
# print([ i*i for i in range(1, 7)])
# 在[3,6,9]的基础上推到出[[1,2,3], [4,5,6],[7,8,9]]
# print([[i-2, i-1, i] for i in [3,6,9]])

# # {0:"张三丰", 1:"张无忌",2:"张翠山"}
# lst = ["张三丰", "张无忌", "张翠山"]
# print({ i:lst[i] for i in range(len(lst))})
# print({i for i in range(10)})





gen = (i for i in range(10))

# print(lst.__next__())
# for item in lst:
#     print(item)

print(list("我的天那")) #  => for循环  => 把每一项添加到列表中
print(list(gen)) # 拿空生成器


# def func():
#     print(111)
#     yield 222
#
# # 惰性机制
# g = func()
# g1 = (i for i in g)
# g2 = (i for i in g1)
#
# print(list(g1)) # [222]
# print(list(g2)) # []
# print(list(g)) # []
