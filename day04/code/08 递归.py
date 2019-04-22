# i = 0
# def func():
#     global i
#     i+=1
#     print("哈哈", i)
#     func()
#
# # 容易报错. 超过递归的最大深度.
# # 永远不可能超过1000
# func()

# 递归的用法
# 二分法查找

# lst = [12,24,53,67,108,267]  # 10亿
# # O(N)
# # 不许用in

# n = 798
# for i in range(len(lst)):
#     if lst[i] == n:
#         print("找到了")
#         print(i)
#         break
# else:
#     print("没有")


# 二分法查找


# # # 必须有序
# lst = [12,24,53,67,108,267]
#
# n = 108
#
# left = 0
# right = len(lst) - 1 # 右边界
#
# while left <= right:
#     mid = (left + right)//2
#     if n > lst[mid]:
#         left = mid+1
#     elif n < lst[mid]:
#         right = mid-1
#     else:
#         print("找到了")
#         print(mid)
#         break
# else:
#     print("没有")


def binarySearch(lst, n, left, right):
    if left <=right: # 判断是否已经查找完毕
        mid = (left+right)//2 #  计算中间
        if n > lst[mid]: # 数据比中间大
            left = mid + 1 #  做边界拉倒右边
            # 进入递归
            return binarySearch(lst, n, left, right)
        elif n < lst[mid]:
            right = mid - 1
            return binarySearch(lst, n, left, right)
        else:
            print("找到了")
            return mid
    else:
        print("没找到")
        return -1


lst = [12,24,53,67,108,267]
n = 108

ret = binarySearch(lst, n, 0, len(lst)-1)
print(ret)


# 树形结构遍历

