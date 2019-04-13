# modelList = [['test6', 'zktmq-hotel'], ['default', 'java-doc'], ['test6', 'zkt-passport']]
# mailDict = {}  # 定义邮件内容
# for i in modelList:  # 遍历每行内容
#     if i[0] in mailDict:  # 如果内容中有这个key
#         lineList = mailDict[i[0]]  # 拿出全部值
#         lineList.append(i[1])  # 追加值
#         mailDict[i[0]] = lineList  # 放入邮件内容中
#     else:  # 如果内容中没有这个key
#         mailDict[i[0]] = [i[1], ]  # 新建一个key
# print(mailDict)
# on the class
# # 使用常规方法
# name = input("name:")
# age = input("age:")
# job = input("job:")
# info = """
# --------------info--------------
# name=%s
# age=%20.f
# job=%s
# """ % (name, float(age), job)
# print(info)

# #使用字符串模板方式
# info = f"""
# --------------info--------------
# name={name}
# age={float(age)}
# job={job}
# """
# print(info)

# 判断是否在某个输入内容中,,,,
# content = input('please input content:')
# exist = '波多野结衣' in content
# print(exist)
#
# username = 'admin'
# passwd = '123'
# loginName = input('please input username:')
# loginPasswd = input("please input passwd:")
# if username == loginName and passwd == loginPasswd:
#     print("login success!")
# else:
#     print("username or passwd error!")

# 判断某人的留言当中是否包含了"波多老师"或者"苍老师"

# content = input('请输入内容:')
# if '波多老师' in content or '苍老师' in content:
#     print('包含非法内容')
# else:
#     print("不包含非法内容")

# print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# print(0 or 3 or 2 or 2)
# print(0 and 1 or 2 and 0 or 1 or 2 and 3)
# 0 or 0 or 1 or 3
# 0 or 1 or 3
# 1 or 3
# 1
#
# count = 0
# while count < 100:
#     count += 1
#     print(count)

# # 编码和解码
# s = '编码和解码'
# # 编码
# utf8EnCode = s.encode("utf-8")
# gbkEnCode = s.encode('gbk')
# print("utf8Code--->", utf8EnCode)
# print("gbkCode--->", gbkEnCode)
# # 解码
# utf8Decode = utf8EnCode.decode("utf-8")
# gbkDeCode = gbkEnCode.decode("gbk")
# print('utf8Decode--->', utf8Decode)
# print("gbkDecode--->", gbkDeCode)
# # 转码
# utf8s = b'\xe7\xbc\x96\xe7\xa0\x81\xe5\x92\x8c\xe8\xa7\xa3\xe7\xa0\x81'
# print(utf8s.decode())

# s = "周的杰阿里里伦巴巴的呵呵"  # 把周杰伦 拼接成一个新的字符串并打印
# name = s[0] + s[2] + s[6]
# print(name)
# # 切片
# s = "Java,Python,Php,C++"
# print(s[5:11])
# s = "123456789"
# print(s[::2])
# print(s[-2::-2])
# string upper 使用
# code = 'Adef'
# verifyCode = input(f'please input verify"{code}":')
# if code.upper() == verifyCode.upper():
#     print('正确')
# else:
#     print("错误")
# s = 't'
# for i in s:
#     print(i)
# list 操作
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.append(10)
# print(list1)
# list1.insert(1, 20)
# print(list1)
# list1.extend(list2)
# print(list1)
# list1 = [1, 2, 3]
# list1.pop()
# print(list1)
# list1.remove(2)
# print(list1)
# del list1[2]
# print(list1)
# list1.clear()
# print(list1)
# 要求输入"3+4+5+2"组成的字符串,计算出加法结果
# inputContent = input('please input content:')
# contentList = inputContent.split("+")
# total = 0
# for item in contentList:
#     total += int(item)
# print(total)
# x = []
# for i in range(len(x)):
#     print(i)
# else:
#     print('111')
# dic={}
# print(dic.get('ss'))

lis = [1, 2, 3, 4, 5, 5, 4, 3, 4, 2, 1]
dic = {}
for i in lis:
    dic[i] = dic.get(i, 0) + 1

print(dic)
