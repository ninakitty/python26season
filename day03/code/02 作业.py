# li = ["苍老师", "波多野结衣", "麻生希", "仓木麻衣"]
#
# msg = input("请输入您的评论:")
#
# for item in li:
#     if item in msg: # 找到了敏感词
#         msg = msg.replace(item, "*"*len(item))
#
# print(msg)

# lst = [{"name":"鼠标", "price":10},
#        {"name":"键盘", "price":20},
#        {"name":"游艇", "price":999},
#        {"name":"美女", "price":1998},
#        ]
#
# for i in range(len(lst)):
#     print(i+1, lst[i]['name'], lst[i]['price'])
#
# num = int(input("请输入你要的商品:"))
# print(lst[num-1])


dic = {"name":"鼠标", "price":10}
for k in dic:
    dic.pop(k)  # dictionary changed size during iteration

