import time
#第一题:装饰器格式
# def wrapper(fn):                 #把目标函数传入到装饰器内
#     def inner(*args,**kwargs):   #此处使用无敌传参,是为了给目标函数传递参数,* 和 ** 代表参数的聚合
#         """执行目标函数前"""
#         ret = fn(*args,**kwargs) #此处执行目标函数,* 和 ** 代表参数的打散
#         """执行目标函数后"""
#         return ret
#     return inner
#
# @wrapper     #调用装饰器,和 func = wrapper(func)相同
# def func(name,passwd):
#     pass
# func(name,passwd)  #执行函数

# # 第二题:按要求编写装饰器
# def wrapper(fn):
#     def inner(*args,**kwargs):
#         print("每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码")
#         ret = fn(*args,**kwargs)
#         print("目标函数执行之后")
#         return ret
#     return inner
#
# @wrapper
# def func(Hero_Name,Book_Name):
#     print ("姓名".center(10),"书名".center(10))
#     print(Hero_Name.center(10),Book_Name.center(6))
#     return "作者: 金庸"
# ret = func("张无忌","倚天屠龙记")
# print(ret)
#
# print("*" * 50)
# #第三题
# def wraaper(fn):
#     def inner(*args,**kwargs):
#         print("目标函数执行之前")
#         ret = fn(*args,**kwargs)
#         print("每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码")
#         return ret
#     return inner
#
# @wraaper
# def func1(Hero_Name,Book_Name):
#     print("姓名".center(10), "书名".center(10))
#     print(Hero_Name.center(10), Book_Name.center(6))
#     return "作者: 金庸"
#
# ret = func1("扫地僧", "天龙八部")
# print(ret)

# # #第四题
# #定义用户列表
# user_list= [{"admin":"123"},
#             {"root":"123"},
#             ]

# #定义装饰器
# def wraaper(fn):
#     def login():
#         num = 1  #定义num用来控制用户输入错误次数后跳出
#         while num < 4:
#             user = input("请输入用户名:")
#             passwd = input("请输入密码:")
#             for item in user_list:
#                if user in item.keys() and passwd in item.values():  #判断用户名和密码是否在user_list中
#                         ret = fn()    #执行目标函数
#                         return ret
#             else:
#                 num += 1
#                 print("用户名或密码错误,请重试!剩余%s次" % (4 - num))
#     return login
#
# @wraaper
# def test():
#     print("终于见到你")
# #login函数执行
# test()

# #第五题
# '''
# 编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,只支持单用户的账号密码,给用户三次机会），要求登录成功一次，后续的函数都无需再输入用户名和密码
# '''
# #定义一个保持会话的标识
#
# flag = False
#
# def blog(*args):
#     global flag
#     api_mapping = {
#         "1" : Home,
#         "2" : GuestBook,
#         "3" : Favorites,
#         "4" : logout
#     }
#     print("""
#         欢迎来到博客园!
#         1、首页
#         2、留言板
#         3、收藏夹
#         4、退出
#     """)
#     PlateId = input("请输入你要访问的版块：").strip()
#     if PlateId.isdigit():
#         if PlateId in api_mapping.keys():
#             ret = api_mapping.get(PlateId)
#             print(type(ret()))
#
# def login(*args):
#     global flag
#     username = input("用户名: ").strip()
#     password = input("密码: ")
#     with open('users', mode='r', encoding='utf-8') as f:
#         for i in f:
#             i = eval(i)  #通过内置函数eval()把遍历出的字符串字典格式转换成字典
#             if username == i["username"] and password == i["password"]:
#                 flag = True
#                 print("登陆成功")
#                 break
#         else:
#             print('登录失败')
#             flag = False
#
#
# def wrapper(fn):
#     # global flag
#     def inner(*args):
#         num = 0
#         while num < 3:
#             if flag == True:
#                 ret = fn()
#                 return ret
#             else:
#                 login()
#                 num += 1
#     return inner
#
#
# def Home():
#     return ("欢迎来到博客园！")
#
# @wrapper
# def GuestBook(*args):
#     return ("请输入您的留言!")
#
# @wrapper
# def Favorites(*args):
#     return ("添加收藏夹成功！")
#
# @wrapper
# def logout(*args):
#     global flag
#     flag = False
#     return ("退出登录")
#
#
# while 1:
#     blog()

# #第六题
# '''
# 编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,只支持单用户的账号密码,给用户三次机会），要求登录成功一次，后续的函数都无需再输入用户名和密码
# '''
# #定义一个保持会话的标识
#
# flag = False
#
# def blog(*args):
#     global flag
#     api_mapping = {
#         "1" : Home,
#         "2" : GuestBook,
#         "3" : Favorites,
#         "4" : logout
#     }
#     print("""
#         欢迎来到博客园!
#         1、首页
#         2、留言板
#         3、收藏夹
#         4、退出
#     """)
#     PlateId = input("请输入你要访问的版块：").strip()
#     if PlateId.isdigit():
#         if PlateId in api_mapping.keys():
#             ret = api_mapping.get(PlateId)
#             print(type(ret()))
#
# def login(*args):
#     global flag
#     username = input("用户名: ").strip()
#     password = input("密码: ")
#     with open('users', mode='r', encoding='utf-8') as f:
#         for i in f:
#             i = eval(i)  #通过内置函数eval()把遍历出的字符串字典格式转换成字典
#             if username == i["username"] and password == i["password"]:
#                 flag = True
#                 print("登陆成功")
#                 break
#         else:
#             print('登录失败')
#             flag = False
#
#
# def wrapper(fn):
#     # global flag
#     def inner(*args):
#         num = 0
#         while num < 3:
#             if flag == True:
#                 ret = fn()
#                 return ret
#             else:
#                 login()
#                 num += 1
#     return inner
#
#
# def Home():
#     return ("欢迎来到博客园！")
#
# @wrapper
# def GuestBook(*args):
#     return ("请输入您的留言!")
#
# @wrapper
# def Favorites(*args):
#     return ("添加收藏夹成功！")
#
# @wrapper
# def logout(*args):
#     global flag
#     flag = False
#     return ("退出登录")
#
#
# while 1:
#     blog()

# #第七题
# current_time = time.strftime('%Y-%m-%d %H:%M:%S')
# func_list = {
#     "1" : "func_A",
#     "2" : "func_B"
#     }
#
# def wrapper07(fn07):
#     global func_name
#     global current_time
#     def inner(*args):
#         ret = fn07()
#         with open('log07',mode='a',encoding='utf-8') as f:
#             msg = f"函数名：{func_name} 时间：{current_time}\n"
#             f.write(msg)
#         return ret
#     return inner
#
# @wrapper07
# def func_A(*args):
#     return ("我是函数A")
#
# @wrapper07
# def func_B(*args):
#     return ("我是函数B")
#
# while 1:
#     print("""
#     1  函数一
#     2  函数二
#     """)
#     num = input("请输入您要执行的函数：").strip()
#     if num.isdigit():
#         if num in func_list.keys():
#             ret = eval(func_list[num])
#             func_name = func_list[num]
#             print(ret())

# #作业
# flag = False   #定义一个标识，登陆后用来保持登录状态
# loop_n = True  #程序循环运行标识
# current_time = str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
#
# def blog(*args):
#     global func_name
#     global flag
#     api_mapping = {
#         "1" : "Home",
#         "2" : "register",
#         "3" : "Article",
#         "4" : "Diary",
#         "5" : "Remark",
#         "6" : "Favorites",
#         "7" : "logout",
#         "8" : "u_exit"
#     }
#     print("""
#         1  首 页
#         2  注 册
#         3  文章页面
#         4  日志页面
#         5  评论页面
#         6  收藏页面
#         7  注 销
#         8  退出程序
#     """)
#     PlateId = input("欢迎来到博客园, 请输入你要访问的版块的编号：").strip()
#     if PlateId.isdigit():   #判断输入编号是否是数字
#         if PlateId in api_mapping.keys():  #判断输入的编号是否在网站api_mapping里
#             ret = eval(api_mapping.get(PlateId)) #根据对用的版本编号取出对应的函数
#             func_name = api_mapping[PlateId]
#             print(ret())      #打印出函数执行后返回的值
#
# def login(*args):
#     global flag
#     global username
#     username = input("请输入你的用户名:").strip()
#     password = input("请输入你的密码:")
#     with open("users",mode="r", encoding="utf-8") as f:
#         for line in f:
#             dic = eval(line)  # 通过eval内置函数把返回line字符串类型转换成字典类型
#             if username == dic['username'] and password == dic['password']:
#                 print("登录成功")
#                 flag = True
#                 break
#         else:
#             flag = False
#             print ('用户名和密码错误，登录失败')
#
# #登录装饰器定义
# def wrapper(fn):
#     def inner(*args):
#         count = 0
#         while count < 3:
#             if flag == True:
#                 ret = fn()  #执行输入编号对应的函数
#                 return ret
#             else: # 没登录
#                 login()
#                 count += 1
#     return inner
#
# #日志装饰器定义
# def wrapper_log(fnlog):
#     global func_name
#     global username
#     global current_time
#     def inner(*args):
#         ret = fnlog()
#         with open('logfile',mode='a',encoding='utf-8') as f:
#             msg = f"用户：{username} 在 {current_time} 执行了{str(func_name)}函数\n"
#             f.write(msg)
#         return ret
#     return inner
#
# def Home(*args):
#     return ("\033[1;31;40m 欢迎来到博客园，请登录 \033[0m".center(50))
#
#
# def register(*args):
#     global flag
#     username = input("请输入用户名：")
#     password = input("请输入密码：")
#     password2 = input("请再次输入密码：")
#     if password == password2:
#         with open('users',mode='a',encoding='utf-8') as f:
#             reg_msg ={"username":username,"password":password}
#             f.write(str(reg_msg) + "\n")
#             flag = True
#             return ("\033[1;31;40m 注册成功！ \033[0m".center(50))
#     else:
#         print("两次输入的密码不同，请重新输入")
#
# @wrapper
# @wrapper_log
# def Article(*args):
#     global username
#     return ("\033[1;31;40m 欢迎%s用户访问，文章列表！\033[0m".center(50)%(username))
#
# @wrapper
# @wrapper_log
# def Diary(*args):
#     return ("\033[1;31;40m 欢迎%s用户访问，日志列表！\033[0m".center(50)%(username))
#
# @wrapper
# @wrapper_log
# def Remark(*args):
#     return ("\033[1;31;40m 欢迎%s用户访问，请输入您的评论！\033[0m".center(50)%(username))
#
# @wrapper
# @wrapper_log
# def Favorites(*args):
#     return ("\033[1;31;40m 欢迎%s用户访问，收藏成功！\033[0m".center(50)%(username))
#
# @wrapper
# @wrapper_log
# def logout(*args):
#     global flag
#     flag = False
#     return ("\033[1;31;40m 注销成功 \033[0m".center(50))
#
# @wrapper
# @wrapper_log
# def u_exit(*args):
#     global loop_n
#     loop_n = False
#     return ("\033[1;31;40m 退出程序！ \033[0m".center(50))
#
# while loop_n:
#     blog()