def mul():
    return [lambda x: i*x for i in range(4)]
    # lst = []
    # for i in range(4):
    #     def fn(x):
    #         return x * i
    #     lst.append(fn)
    # return lst


print([m(2) for m in mul()])
#1. 给出结果 [6,6,6,6]
#2. 请修改代码. 得到你想要的结果  0,2,4,6
