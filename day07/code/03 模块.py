# 导入一个模块
# 1.判断内存中是否有master
# 2.如果有, 直接拿过来使用,
# 3.如果没有, 会开辟一个内存空间
# 4. 在该内存空间中执行模块中的代码
# 5. 默认把名称空间的名字引入进来

# 导入模块的规范:
# 1.导入模块写在py文件的最开始
# 2. 顺序:
#   1. 内置模块
#   2. 第三方模块
#   3. 自己定义的模块

# import json
# import time
# import master # 本质就是一个对象
# # print(master.name)
# # master.change()
# # print(master.name)
#
# name = "女神"
#
# def change():
#     global name # 自己模块里的东西
#     name = '吴超'
#
# change()
# print(master.name)
#
# master.change()
# print(master.name)



# print(master.name)
# master.func()
#
# # p = master.Person("alex", 18)
# # p.chi()
# import master
# from master import name
#
# name = "呵呵"
# print(master.name)


# D:\python3
# /user
import os
# print("/"+os.path.sep)  # 文件路径分隔符

# open("../day06/01 今日内容大纲  \table")

import master

