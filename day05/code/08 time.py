import time

# # 查看系统时间
# # 拿到的是一个数字
# # 从1970-01-01 00:00:00开始计算
# print(time.time())
#
# # 格式化时间
# print(time.strftime("%Y-%m-%d %H:%M:%S")) # format 格式要记住
#
# # 结构化时间
# print(time.localtime())


# n = 10000000
# # 时间戳转化成格式化时间
# # 1. 把时间戳转化成结构化时间
# struct_time = time.localtime(n)
# print(struct_time)
# # 2. 把结构化时间转化成格式化时间
# s = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
# print(s)


# # 把字符串转化成数字(时间戳)
# s = input("请输入一个时间(%Y-%m-%d %H:%M:%S):") # 1970-04-27 01:46:40
# # 1.把字符串转化成结构化时间
# struct_time = time.strptime(s, "%Y-%m-%d %H:%M:%S") # p:parse
# print(struct_time)
# # 2. 把结构化时间转化成数字
# n = time.mktime(struct_time)
# print(n)




s1 = "1989-01-02 12:00:00"
n1 = time.mktime(time.strptime(s1, "%Y-%m-%d %H:%M:%S"))

s2 = "1989-01-02 14:35:00"
n2 = time.mktime(time.strptime(s2, "%Y-%m-%d %H:%M:%S"))

diff = abs(n2 - n1) # 1000000
diff_min = diff//60 # 90分钟  => 1小时30分钟

display_hour = diff_min // 60   # 小时 1
display_min = diff_min % 60 # 分钟 30


print(f"{display_hour}小时{display_min}分钟")

