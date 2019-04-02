#    0123
# s = "alex"

# # 从字符串中获取到某一个字符
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
#
# print(s[-1])
# print(s[-2])
# print(s[-3])
# print(s[-4])
#
# print(s[10086]) # string index out of range 索引越界
#     0 12 3 4 5 6 7 89

# s = "周的杰阿里里伦巴巴的呵呵"  #  把周杰伦 拼接成一个新的字符串并打印
# s2 = s[0]+s[2] + s[6]
# print(s2)

# 切片
#            45 6 7 8
# s = "成龙吴京赵四刘能印度啊三"
# print(s[4:8])   # 顾头不顾尾

# s = "Java,Python,Php,C++"
# print(s[5:11])
# print(s[10086:10089])
# print(s[:4]) # Java  从开始切
# print(s[4:]) #  从4到结束
# print(s[:]) # 从头到尾

# print(s[-5:-2]) # 从左到右切
# print(s[-2:-5]) #  从右向左切,. 获取不到数据


# 从右向左切 + 步长

# s = "好好学习天天向上"

# print(s[-2:-6:-1]) #  步长: 控制方向. + 向右, - 向左
# print(s[1:4:2])

# s = "123456789"
# # print(s[::2])
# # 8642
# print(s[-2::-2])
# print(s[7::-2])



# s = "alEx Love Piqi and zhu5mingfang"
# s1 = s.capitalize() # 把首字母变成大写
# print(s1)
# s2 = s.title() # 把单词的首字母大写
# print(s2)

# s3 = s.upper() # 大写
# print(s3)

# verify_code = "Axbn" # AXBN
#
# uv_code = input(f"请输入验证码{verify_code}:")
#
# if verify_code.upper() == uv_code.upper():  # 忽略大小写
#     print("验证码正确")
# else:
#     print("验证码错误")

# print(s.lower())

# s2 = "БBß" # 俄美德
# print(s2.lower())
# print(s2.casefold())

# 切来切去
# s = "张无忌"
# s1 = s.center(10, "*") # 把字符串拉长成10个单位,让原来的字符串居中
# print(s1)

# s = "你好啊\t我叫赛利亚" # \t 转义字符
# print(s.expandtabs(32)) # 改变字符串中\t的长度

# strip() 默认去掉左右两端的空白(空格, \t, \n)
# s = "     哈哈, 我是赛利亚       "
# s2 = s.strip()
# print(s2)

# uname = input("请输入用户名:").strip() # 用户输入的内容一定要过滤掉左右脸孤单得空白
# upwd = input("请输入密码:").strip()
# if uname == "alex" and upwd == "123":
#     print("登录成功")
# else:
#     print("登录失败")

# s = "sbalex_peiqisb"
# s1 = s.strip("sb") # 去掉左右两端的sb
# print(s1)

# s = "jinjiao_sb_nezha_sb_taibai_sb_peiqi"
# s1 = s.replace("sb", "dsb")
# print(s1)

# msg = input("请输入你的留言:")
# if "苍老师" in msg:
#     msg = msg.replace("苍老师", "***")
#
# print(msg)

# s = "少林寺      吐鲁番\n海南岛\t北戴河"
# lst = s.split() # 默认用空白切割
# print(lst)

# 1   jay  2:30   吃烧烤
# 2   wlh  3:50    游泳
# 3   my   4:50   逛淘宝

# print("我叫%s, 来自%s, 喜欢干%s" % ("alex", "山东", "佩奇"))
# print("我叫{}, 来自{}, 喜欢干{}".format("alex", "山东", "太白"))
# print("我叫{1}, 来自{2}, 喜欢干{0}".format("alex", "山东", "太白"))
# print("我叫{name}, 来自{address}, 喜欢干{hobby}".format(name="alex", address="山东", hobby="太白"))


# 以xxx开头
# s = "alex 特别喜欢他的特斯拉"
# print(s.startswith("alex")) # 判断
# print(s.endswith("特斯拉")) # 判断

# s = "efgabcd"
# print(s.count("a"))

# print(s.find("z")) # 返回索引, 如果没有, 返回-1
# print(s.index("z")) #  找到了返回索引, 找不到. 报错


# s = "1234567壹一贰叁仟伍佰六十六"
# # print(s.isalpha())
# # print(s.isdigit()) # 判断是否是阿拉伯数字
# # print(s.isnumeric())
# print(s.isalnum()) # 是否是数字和字母组成


# s = "250"
# print(len(s)) # len叫内置函数.和print是一样


# 使用for循环来遍历字符串
# s = "谁家的小孩哈哈fasfasf" # 7 最大索引: 6
# for a in s:     # 把字符串中每一个字符拿出来给前面的变量a
#     print(a)

# index = 0
# while index < len(s):
#     print(s[index])
#     index += 1 # index = index + 1

