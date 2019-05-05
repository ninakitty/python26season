import os

# os.mkdir("abc/def") # 创建一个文件夹
# 创建文件夹
# os.makedirs("abc/def") # 创建多级目录

# os.removedirs("abc/def") # 删除多级目录. 上层目录是空
# os.rmdir("abc/def") # 删除文件夹

#
# print(os.listdir("abc")) # 列出文件夹内的所有文件的名字

# print(os.stat("02 Test.py"))

# os.system("dir")
# ret = os.popen("dir")
# print(ret.read())

# print(os.getcwd()) # 获取到当前工作目录
# os.chdir() # 改变工作目录

# print(os.path.abspath("abc")) # 把相对路径更换成绝对路径
# print(os.path.split("d:/sylar/relay/abc.txt")) # 切割, 获取到文件夹和文件


# print(os.path.exists("abc")) # 判断是否存在xxx文件或者文件夹

# print(os.path.isfile("abc"))
# print(os.path.isdir("abc"))

# 拼接路径
# print(os.path.join("hehe","哈哈哈哈", "sylar", "张三李四.txt"))
# print(os.path.getsize("01 今日内容大纲"))


# 请列出某个文件夹内所有的文件名字(包括子文件)
# 递归

# def func(filepath, n): # D:\PyCharmProject\周末26期\day01
#     lst = os.listdir(filepath)
#     for item in lst: # 文件名 day01
#         fp = os.path.join(filepath, item) # D:\PyCharmProject\周末26期\day01
#         if os.path.isdir(fp):
#             print("\t"*n, item)
#             func(fp, n+1) # 开始递归
#         else:
#             print("\t"*n,item) # 文件名
#             # open(fp,mode="w").write(123)
#
# func("D:/", 1)



