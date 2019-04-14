# #  浅拷贝1
# lst1 = ["张无忌", "霍建华", "古天乐", "大张伟"]
#
# # 1. copy()
# lst2 = lst1.copy()
#
# lst1.append("刘德华")
#
# print(id(lst1))
# print(id(lst2))
# print(lst1) # ['张无忌', '霍建华', '古天乐', '大张伟', '刘德华']
# print(lst2) # ['张无忌', '霍建华', '古天乐', '大张伟']


# # 浅拷贝2
# lst1 = ["张无忌", "霍建华", "古天乐", ["周笔畅", "冯提莫"], "大张伟"]
#
# # 浅拷贝 - 拷贝第一层
# lst2 = lst1.copy()  # [:]
#
# lst1[3].append("张柏芝")
#
# print(id(lst1))
# print(id(lst2))
# print(lst1)
# print(lst2)

# 深拷贝
# import copy
# lst1 = ["张无忌", "霍建华", "古天乐", ["周笔畅", "冯提莫"], "大张伟"]
#
# lst2 = copy.deepcopy(lst1) # 深拷贝
# lst1[3].append("张柏芝")
#
# print(id(lst1))
# print(id(lst2))
# print(lst1)
# print(lst2)


lst1 = ["张无忌", "霍建华", "古天乐", "大张伟"]

lst2 = lst1 # 没有创建新内容

print(id(lst1))
print(id(lst2))
print(lst1)
print(lst2)