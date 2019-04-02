# while True:
#     print("还我钱")

# 准备一个变量来记录喷的次数
# count = 1
#
# while count <= 100:
#     print("还我钱", count)
#     count = count + 1
#
# print("下局再见")

# 从1数到100
# count = 1
# while count <= 100:
#     print(count)
#     count= count + 1

# 打印1-100之间所有的奇数
# count = 1
# while count <= 100:
#     print(count)
#     count= count + 1

# count = 1
# while count <= 100:
#     if count%2==1:
#         print(count)
#     count = count + 1


# 练习：
# 1+2+3+4+5+6+.....+100 = 5050
# 1+2 = 3
# 3+3 = 6
# 6+4
# sum = sum + count
# 把上一次计算的结果拿过来和下一个数进行加法计算

count = 1
sum = 0
while count <= 100:
    sum = sum + count
    count = count + 1
print(sum)



