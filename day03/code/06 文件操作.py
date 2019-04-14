# 向文件插一根管子.
# f:文件句柄
# f = open("斗破苍穹.txt", mode="r", encoding="utf-8") # read读
# # content = f.read(5) # 读取n个字符
# # print(content)
#
# # line1 = f.readline() # 每次读取一行内容
# # print(line1.strip()) # 取代两端的空白: 空格, \t, \n
# #
# # line2 = f.readline() #  下一次读取. 从上一次读取位置
# # print(line2.strip())
# #
# # line3 = f.readline()
# # print(line3.strip())
#
# for line in f:  # 循环一次读取一行
#     print(line.strip())
#
# print(f.readlines())  # 没用.


# import os
# f = open(f"../day01/斗破苍穹.txt", mode="r", encoding="utf-8")
#
# print()
#
# for line in f:
#     print(line.strip())
# # 1. 绝对路径.
# # 2. 相对路径
# #   从文件夹出去.      ../
# #   进入文件夹         文件夹名字


# f = open("fruit.txt", mode="r", encoding="utf-8")
#
# result = []
# for line in f:
#     lst = line.strip().split(",") # [1, 香蕉, 9]
#     dic = {"id":lst[0], "name":lst[1], "price":lst[2]}
#     result.append(dic) # 把字典添加到列表中
#
# print(result)



# # 比较难
# f = open("fruit.txt", mode="r", encoding="utf-8")
#
# title_str = f.readline().strip() # "id,名字,库存"
# title_list = title_str.split(",") # [id, 名字, 库存]
#
# result = []
# for line in f:
#     content_list = line.strip().split(",") # [1, 香蕉, 8]
#     dic = {} # 创建一个字典
#     for i in range(len(title_list)):
#         dic[title_list[i]] = content_list[i] # 给字典新增
#     result.append(dic)
# print(result)


# f = open("haha", mode="a", encoding="utf-8") # 创建文件
# f.write("今天天气不错")
# f.write("特别适合钓鱼")


# # 文件复制
# f1 = open("c:/time.jpg", mode="rb") # 不能解码
# f2 = open("d:/胡一菲.jpg", mode="wb")
# for line in f1:
#     f2.write(line)

# f = open("haha", mode="r+", encoding="utf-8")
# content = f.read()
# f.write("周杰伦")
# print(content)



# 文件修改
#
# import os
#
# f1 = open("alex", mode="r", encoding="utf-8")
# f2 = open("alex_2", mode="w", encoding="utf-8")
# for line in f1:
#     line = line.replace("_sb_", "_dsb_")
#     f2.write(line)
#
# f1.close() # 记着要关闭连接
# f2.flush() # 刷新管道
# f2.close() # 关闭连接
#
# # 把原来的文件删除
# os.remove("alex")
# # 把新文件的名字, 更改为原来文件的名字
# os.rename("alex_2", "alex")


# # with语句 可以自动关闭连接
# with open("alex", mode="r", encoding="utf-8") as f1,\
#         open("alex_222222", mode="w", encoding="utf-8") as f2:
#     for line in f1:
#         f2.write(line)
