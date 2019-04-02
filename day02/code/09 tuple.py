# t = tuple() # ()
# t.

# t = ("哈哈", "周杰伦", "爱上了", "冯提莫")
# # print(t[1::2])
#
# # for item in t:
# #     print(item)
#
# # t[1] = "孔明" # 'tuple' object does not support item assignment
# print(t)

# # 坑
# t = ("张无忌", "张大大", ["呵呵", "哈哈", "吼吼"], "张伯伦")
# t[1] = "哈哈哈哈" # 这里是改变了指向. 报错
# t[2].append("牛A") # 元组的不可变指的是内存指向的不可变
# print(t)


# t = (1) # 此时的小括号表示优先级
# print(type(t))
# print(t)


t = (1, ) # 此时的小括号表示优先级
print(type(t))
print(t)
