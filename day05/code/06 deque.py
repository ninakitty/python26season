# lst = ["张一山", "杨紫", "周冬雨"]
#
#
# lst.append("张一山")
# lst.append("杨紫")
# lst.append("周冬雨")
#
# ret = lst.pop()
# print(ret)
# ret = lst.pop()
# print(ret)
# ret = lst.pop()
# print(ret)

# import queue
#
# q = queue.Queue() # 创建队列
# q.put("张一山")
# q.put("王大拿")
# q.put("王木生")
#
#
# print(q.get())
# print(q.get())
# print(q.get())

from collections import deque

# 双向队列
d = deque()

d.append("牡丹花")
d.appendleft("樱桃花")
d.append("腊梅")
d.append("兰花")
d.appendleft("罂粟花")

# "罂粟花","樱桃花","牡丹花","腊梅","兰花"

print(d.pop())# "兰花"
print(d.popleft()) # "罂粟花"
print(d.pop())# "腊梅"
print(d.popleft()) #"樱桃花"
print(d.popleft()) # "牡丹花"


dic = {"jay":123, "wlh":456}
print(dic)

