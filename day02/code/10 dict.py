# dic = {123:"李嘉诚", "哈哈":"马化腾", ("呵呵",):"马云", [1,2,3]:"呵呵呵呵呵"}
# print(dic)   # unhashable type: 'list'


# dic = {} # 空字典 dict()
#
# dic["赵本山"] = "刘老根"
# dic["王小利"] = "刘能"
# dic["赵本山"] = "阿水"   # key 不可以重复. 会把数据覆盖掉
#
# # setdefault()
# #
#
#
# print(dic)

# d =  {'赵本山': '阿水', '王小利': '刘能'}
# # 当key在字典中存在的时候, 不执行新增
# # 当key不存在的时候. 执行新增操作
#
# # 不论新增与否. 执行完新增流程之后. 使用key把value查询出来
# v = d.setdefault("rookie", "呵呵")
#
# print(v)



#
# # setdefault应用
# lst = [11,22,33,44,55,66,77,88]
# # dic = {"key1":[66,77,88], "key2":[11,22,33,44,55]}
#
# dic = {}
#
# for item in lst: # 11
#     if item < 66:
#         # if dic.get("key2")  != None: # 判断是否存在key2
#         #     dic['key2'].append(item) # 把数据添加到key2对应的列表中
#         # else:
#         #     dic['key2'] = []
#         #     dic['key2'].append(item)
#
#         dic.setdefault("key2", []).append(item)
#     else:
#         # if dic.get("key1")  != None: # 判断是否存在key2
#         #     dic['key1'].append(item) # 把数据添加到key2对应的列表中
#         # else:
#         #     dic['key1'] = []
#         #     dic['key1'].append(item)
#         dic.setdefault("key1", []).append(item)
#
# print(dic)



dic = {"佛教":"释迦摩尼", "道教":"太上老君","明教": "张无忌"}


# # print(dic.get("fkjhsdakjfjdasjfladsjflkadsjfkldsjfkladsjflkdsajfkleaw")) # 查询不到数据返回None
# print(dic["fjsadkljflasjklfjasdlf"]) # 会报错

# for k in dic:
#     print(k)
#     print(dic[k])

# print(dic.keys()) # 山寨列表, 盗版列表
# for k in dic.keys():
#     print(k)
#     print(dic[k])

# print(dic.values()) # 只有value
# for v in dic.values():
#     print(v)

# print(dic.items())

# for k, v in dic.items():
#     print(k)
#     print(v)


# a, b = (1, 2) # 解构, 解包.
# print(a)
# print(b)


# wangfeng = {
#     "name":"汪峰",
#     "age":45,
#     "wife":{
#         "name":"子怡",
#         "age":18,
#         "hobby":["汪峰", "演戏", "当导师"]
#
#     },
#     "children":[
#         {"name":"孩儿1", "age":6},
#         {"name":"孩儿2", "age":8},
#         {"name":"孩儿3", "age":10},
#     ]
# }
#
# print(wangfeng['children'][1]['age'])
# # 把汪峰第三个孩子的年龄增加10
# wangfeng['children'][2]['age'] = wangfeng['children'][2]['age'] + 10
# wangfeng['wife']['hobby'].append("上课看小说")
# print(wangfeng)

