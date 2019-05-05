from collections import defaultdict

d = defaultdict(lambda :123) # 默认值

print(d)
d['jay'] = "周杰伦"  # 添加新元素
print(d)

print(d['wlh']) # 查询不存在的数据.此时先执行新增, 然后是查询. setdefault
print(d)