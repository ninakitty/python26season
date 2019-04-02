# 可以使用range让for循环数数
# lst = ["abc", "def","hij"]
# # for item in lst:
# #     print(item)


# for i in range(10): # 从0到9
#     print(i)

# for i in range(10, 20): # 10-19
#     print(i)

# for i in range(10, 20, 2): # 10 12 14 16 18
#     print(i)

# range能干嘛?
# 用range来遍历列表
lst = ["手机","callji","lunchuan","dnfyouxibi","有课一乐",11111,111111111111]

for i in range(len(lst)): # 遍历列表, 可以拿到索引和元素
    print(i+1, lst[i])


