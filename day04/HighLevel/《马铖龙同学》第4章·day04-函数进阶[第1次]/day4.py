
# 1)，启动程序，首页面应该显示成如下格式：
#     欢迎来到博客园首页
#     1:请登录
#     2:请注册
#     3:文章页面
#     4:日记页面
#     5:评论页面
#     6:收藏页面
#     7:注销
#     8:退出程序
# 2)，用户输入选项，3~6选项必须在用户登录成功之后，才能访问成功。
# 3)，用户选择登录，用户名密码从register文件中读取验证，三次机会，
#         没成功则结束整个程序运行，成功之后，可以选择访问3~6项，访问页面之前，
#         必须要在log文件中打印日志，日志格式为-->用户:xx 在xx年xx月xx日 执行了 %s函数，
#         访问页面时，页面内容为：欢迎xx用户访问评论（文章，日记，收藏）页面
# 4)，如果用户没有注册，则可以选择注册，注册成功之后，可以自动完成登录，然后进入首页选择。
# 5)，注销用户是指注销用户的登录状态，使其在访问任何页面时，必须重新登录。

import time
listname = []  #记录登录用户列表
listuser = [] #记录所有用户列表
logind = False
def logwrapper(func):   #记录日志装饰器
    def inner(*args,**kwargs):
        ret = func()
        struct_time = time.localtime()
        end_time = time.strftime("%Y-%m-%d %H:%M:%S",struct_time)
        with open(r"log.txt",mode="a+",encoding="utf-8") as f:
            f.write("用户:    " + listname[0] + " " + end_time +  "   执行了 "+  func.__name__ + "\n") #将日志写入文件
        return ret
    return inner

def loginwrapper(func):  #用户登录装饰器
    def inner(*args,**kwargs):
        global logind
        if not logind :
            for i in range(3):
                user = input("输入用户名：")
                password = input("输入密码：")
                with open(r"register.txt",mode="r",encoding="utf-8") as f:
                    for line in f:
                        if user != line.strip().split(",")[0] or password != line.strip().split(",")[1]:
                            logind = False
                        else:
                            logind = True
                            listname.append(user)
                            ret = func(*args, **kwargs)
                            return ret
        if logind:
            ret = func(*args, **kwargs)
            return ret

    return inner



@loginwrapper
@logwrapper
def login():
    print("已登录")
@logwrapper
def register():
    global logind
    user = input("请输入您要注册的名字：")
    with open(r"register.txt",mode="r+",encoding="utf-8") as f:
        for line in f:
            listuser.append(line.strip().split(",")[0])
        if user not in listuser:
            password = input("请输入密码：")
            f.write(user + "," + password + "\n")
            listname.append(user)
            logind = True
        else:
            print("已注册,请直接选择登录")

@loginwrapper
@logwrapper
def article():
    print("欢迎%s用户访问文章" %listname[0])

@loginwrapper
@logwrapper
def diary():
    print("欢迎%s用户访问日记" %listname[0])

@loginwrapper
@logwrapper
def discuss():
    print("欢迎%s用户访问评论"  %listname[0])

@loginwrapper
@logwrapper
def collect():
    print("欢迎%s用户访问收藏" %listname[0])

@logwrapper
def logoff():
    global logind
    if logind:
        logind = False
        print("已经注销")
    else:
        print("没有登录")



def firstpage():
    print("""
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    欢迎来到博客园
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    1:请登录
    2：请注册
    3：文章页面
    4：日记页面
    5：评论页面
    6：收藏页面
    7：注销
    8：退出程序
    """)
    choice = int(input("请输入你的选择："))
    if choice == 1:
        login( )
    elif choice == 2:
        register()
    elif choice ==  3:
        article()
    elif choice == 4:
        diary()
    elif choice == 5:
        discuss()
    elif choice == 6:
        collect()
    elif choice == 7:
        logoff()
    elif choice == 8:
        exit()

while True:
    firstpage()
