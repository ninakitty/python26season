# lst = ["张无忌", "张国荣", "张三丰", "武则天", "秦始皇"]
# new_lst = [] # 小本本
# for item in lst:
#     if item.startswith("张"):  # 判断是否姓张
#         # 删除这个人
#         new_lst.append(item)
#
# for item in new_lst:
#     lst.remove(item)
#
# print(lst)

dic = {"k":123, "fsda":45}
for k in dic:
    dic.pop(k) # 报错, 循环的时候不能删除字典

