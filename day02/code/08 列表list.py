# lst = [1, None, True, False, "周杰伦", ["不能说的秘密", "头文字D", "大灌篮"]]
#
# print(lst)

# 和字符串差不多. 也具有索引和切片

# lst = ["山中小猎人", "黑猫警长", "七龙珠", "大象", "小白", "野原新之助", "海贼王"]

# print(lst[1])
# print(lst[-2])
# print(lst[1][2])
# print(lst[3][1][1])
# print(lst[1:6:2])

# lst = ["赵本山", "范伟", "高秀敏"] # 本山传媒
# lst.append("刘能") # 列表是可以发生改变的
# print(lst)

# lst.insert(1, "宋晓峰")
# print(lst)

# lst.extend(["郑伊健", "陈小春", "哈哈哥", "段坤", 1]) # 迭代新增. 把元素一个一个的拆开, 进行新增
# print(lst)




# lst = ["赵本山", "范伟", "高秀敏"] # 本山传媒
# item = lst.pop(1)
# print(lst)
# print(item)

# lst.remove("赵本山") # 删除某个元素
# print(lst)

# del lst[2]
# print(lst)

# lst.clear()
# print(lst)



# lst = ["赵本山", "范伟", "高秀敏"] # 本山传媒
# lst[2] = "文松"
# print(lst)

# lst = ["abc", "123", "李嘉诚", ["呵呵", "哈哈", "吼吼"]]
# 把abc变成大写
# lst[0] = lst[0].upper()
# print(lst)
# lst[3].append("嘻嘻")
# print(lst)

# lst = ["张无忌", "张三丰", "张翠山", "张丰毅", "666"]
# for item in lst:
#     print(item)


# 让用户输入一个加法运算: 3+8+4+6+9  想办法完成数学运算
# split("+")
# s = input("请输入一个加法运算:")
# lst = s.split("+")
# print(lst)
#
# sum = 0
# # 开始循环
# for item in lst:
#     sum += int(item)
# print(sum)


# lst = [11, 2, 3, 1, 5,7,8]
# lst.sort(reverse=False)
# print(lst)

lst = ["哈哈", "呵呵", "葱花饼"]

# lst.reverse()
# print(lst)

print(len(lst))

