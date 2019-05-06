# # 求和
# def add(a, b):
#     return a + b
# #
# # # 生成器函数 0,1,2,3
# def test():
#     for r_i in range(4):
#         yield r_i
#
# g = test() # 创建一个生成器 0,1,2,3
#
# for n in [2, 10]:
#     g = (add(n, i) for i in g)
#
# n = 5
# print(list(g))


# 绕....
def mul():
    return [lambda x: i*x for i in range(4)]
print([m(2) for m in mul()])





