#: @author: zhangji
#: @Time:   2018/9/13 00:02
#: @Email:  492577928@qq.com
# -*- encoding:utf-8 -*-

#定义首页
def head():
    print("""欢迎来到博客园首页
1:请登录
2:请注册
3:文章页面
4:日记页面
5:评论页面
6:收藏页面
7:注销
8:退出程序          
""".strip())

flag = False
#定义一个全局变量，用来判断账号是否登陆
name = ""
#定义个全局变量，用来存放当前登陆用户



#定义登陆函数
def login():
    global flag  #引用全局变量flag  接收登陆状态
    global name  #引用全局变量name，接收登陆后的用户名
    number = 3
    while number >0:
        user_name = input("请输入你的用户名: ".strip())
        user_passwd = input("请输入你的密码: ".strip())
        with open("register", encoding="utf-8") as f:
        #文件操作打开已经存好的用户信息
            for i in f:
                k = i.strip().split("&&")
                if user_name == k[0] and user_passwd == k[1]:
                    print("登陆成功")
                    flag = True        #修改登陆状态
                    name = user_name    #将当前登陆的用户赋值给全局变量name
                    break
            else:
                number = number - 1   #每登陆失败一次，次数-1
                if number == 0: #判断登陆次数是否用完，次数用完就退出程序
                    print("账户或密码错误，登陆失败,你还有%s次机会" % (number))
                    exit()
                else:   #如果次数还有剩余，则告诉用户剩余次数
                    print("账户或密码错误，登陆失败,你还有%s次机会" %(number))
                continue
            break




#定义注册函数
def register():
    global flag #应用全局变量，如果用户注册成功，修改用户状态为登陆
    global name #应用全局变量，如果用户注册成功，将该用户赋值给name
    while 1:
    #定义循环如果提示账户已存在还可以重新注册
        your_name = input("请输入你要注册的账户名: ".strip())
        your_passwd = input("请输入你的密码: ".strip())
        #获取用户输入的信息
        with open("register",encoding="utf-8") as f:
        #以读的方式打开用户信息文件
            for line in f:
                line = line.strip().split("&&")
                #去掉空格，过滤&&中间字符，直接得到账户和密码信息
                if your_name == line[0]:
                #判断输入的账户是否已存在
                    print("此账户已存在,请重新输入")
                    break
            else:
            #不存在就进行注册
                with open("register",mode="a",encoding="utf-8") as f2:
                #已追加写的方式打开用户信息文件
                    f2.write('\n'+your_name+"&&"+your_passwd)
                    #追加写入用户名和密码
                    print("注册成功")
                    flag = True         #注册成功，即修改用户登陆状态为登陆
                    name = your_name    #将注册的新用户名赋值给全局变量name
                    break




#定义打印日志的装饰器
import time     #引用时间模块
def log(func):
    global name
    def inner(*args,**kwargs):
        ret = func(*args,**kwargs)
        with open("log",mode="a",encoding="utf-8") as f:
        #以追加写的方式打开log日志文件
            f.write("\n%s 在%s 执行了 %s函数" %(name,time.strftime("%Y-%m-%d %H:%M:%S"),func.__name__))
            #追加写入当前用户name，当前执行时间，当前调用的函数名称
        return ret
    return inner



#定义判断用户是否登录的装饰器
def login_status(func):
    def inner(*args,**kwargs):
        global flag     #引用全局变量
        if flag == False:   #判断flag值，如果是False则表示没有登录，然后提示用户进行登录
            print("您还没有登录，请先登陆")
            login()     #调用登录函数，让用户进行登录
        else:   #如果不是False则表示用户已经登录，那就返回用户想要调用的函数
            set = func(*args,**kwargs)
            return set
    return inner





#定义文章页面函数
@login_status   #给文章页面函数添加判断用户是否登录的装饰器
@log            #给文章页面函数添加打印日志的装饰器
def weizhang():
    print("欢迎%s访问文章页面！" %(name))


#定义日记页面
@login_status   #给日记页面函数添加判断用户是否登录的装饰器
@log            #给日记页面函数添加打印日志的装饰器
def riji():
    print("欢迎%s访问日记页面！" % (name))


#定义评论页面
@login_status   #给评论页面函数添加判断用户是否登录的装饰器
@log            #给评论页面函数添加打印日志的装饰器
def pinglun():
    print("欢迎%s访问评论页面！" % (name))

#定义收藏页面
@login_status   #给收藏页面函数添加判断用户是否登录的装饰器
@log            #给收藏页面函数添加打印日志的装饰器
def shoucang():
    print("欢迎%s访问收藏页面！" % (name))


#定义流程控制函数
def main():
    global flag #引用全局变量flag
    global name #引用全局变量name
    while True:
        head()  #调用首页函数，显示首页
        choice = input("请输入选项: ".strip())
        #获取用户输入
        if choice.isdigit():
            #判断是否输入的是数字
            choice = int(choice)
            #将输入的数据内容转化为int类型
            if choice == 1:
                login()     #调用登录函数
                continue
            elif choice == 2:
                register()  #调用注册函数
                continue
            elif choice == 3:
                weizhang()  #调用文章页面函数
                continue
            elif choice == 4:
                riji()      #调用日记页面函数
                continue
            elif choice == 5:
                pinglun()   #调用评论页面函数
                continue
            elif choice == 6:
                shoucang()  #调用收藏页面函数
                continue
            elif choice == 7:
                flag = False    #将全局变量修改为False,即表示用户没有登录了，即注销。
                name = ""       #清空name变量，回收用户名
                print("注销成功")
                continue
            elif choice == 8:
                print("退出程序")
                break
        else:#如果用户输入不是数字，提示用户输入有误
            print("输入有误请重新输入")
        break


main()  #调用流程控制函数