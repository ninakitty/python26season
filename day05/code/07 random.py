# 暴击
# 75
# 产生一个1-100之间的随机数

import random

# print(random.random()) # 从0-1之间的小数
#
# print(random.uniform(1,20)) # 从1-20之间的随机小数
#
# print(random.randint(5, 20)) # 从5-20的随机整数
#
#
# lst = ["张三丰", "张翠山", "张无忌"]
# print(random.choice(lst))
# print(random.sample(lst, 2)) # 从列表中随机拿出来两个


lst = ["张三丰", "张翠山", "张无忌"]

random.shuffle(lst) # 打乱列表的顺序

print(lst)









