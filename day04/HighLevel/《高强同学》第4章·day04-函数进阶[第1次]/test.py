#----* conding : utf-8 *----
import time

flag = False   #定义一个标识，登陆后用来保持登录状态
loop_n = True  #程序循环运行标识
current_time = str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

def blog(*args):
    global func_name
    global flag
    api_mapping = {
        "1" : "Home",
        "2" : "register",
        "3" : "Article",
        "4" : "Diary",
        "5" : "Remark",
        "6" : "Favorites",
        "7" : "logout",
        "8" : "u_exit"
    }
    print("""
        1  首 页
        2  注 册
        3  文章页面
        4  日志页面
        5  评论页面
        6  收藏页面
        7  注 销
        8  退出程序
    """)
    PlateId = input("欢迎来到博客园, 请输入你要访问的版块的编号：").strip()
    if PlateId.isdigit():   #判断输入编号是否是数字
        if PlateId in api_mapping.keys():  #判断输入的编号是否在网站api_mapping里
            ret = eval(api_mapping.get(PlateId)) #根据对用的版本编号取出对应的函数
            func_name = api_mapping[PlateId]
            print(ret())      #打印出函数执行后返回的值

def login(*args):
    global flag
    global username
    username = input("请输入你的用户名:").strip()
    password = input("请输入你的密码:")
    with open("users",mode="r", encoding="utf-8") as f:
        for line in f:
            dic = eval(line)  # 通过eval内置函数把返回line字符串类型转换成字典类型
            if username == dic['username'] and password == dic['password']:
                print("登录成功")
                flag = True
                break
        else:
            flag = False
            print ('用户名和密码错误，登录失败')

#登录装饰器定义
def wrapper(fn):
    def inner(*args):
        count = 0
        while count < 3:
            if flag == True:
                ret = fn()  #执行输入编号对应的函数
                return ret
            else: # 没登录
                login()
                count += 1
    return inner

#日志装饰器定义
def wrapper_log(fnlog):
    global func_name
    global username
    global current_time
    def inner(*args):
        ret = fnlog()
        with open('logfile',mode='a',encoding='utf-8') as f:
            msg = f"用户：{username} 在 {current_time} 执行了{str(func_name)}函数\n"
            f.write(msg)
        return ret
    return inner

def Home(*args):
    return ("\033[1;31;40m 欢迎来到博客园，请登录 \033[0m".center(50))


def register(*args):
    global flag
    username = input("请输入用户名：")
    password = input("请输入密码：")
    password2 = input("请再次输入密码：")
    if password == password2:
        with open('users',mode='a',encoding='utf-8') as f:
            reg_msg ={"username":username,"password":password}
            f.write(str(reg_msg) + "\n")
            flag = True
            return ("\033[1;31;40m 注册成功！ \033[0m".center(50))
    else:
        print("两次输入的密码不同，请重新输入")

@wrapper
@wrapper_log
def Article(*args):
    global username
    return ("\033[1;31;40m 欢迎%s用户访问，文章列表！\033[0m".center(50)%(username))

@wrapper
@wrapper_log
def Diary(*args):
    return ("\033[1;31;40m 欢迎%s用户访问，日志列表！\033[0m".center(50)%(username))

@wrapper
@wrapper_log
def Remark(*args):
    return ("\033[1;31;40m 欢迎%s用户访问，请输入您的评论！\033[0m".center(50)%(username))

@wrapper
@wrapper_log
def Favorites(*args):
    return ("\033[1;31;40m 欢迎%s用户访问，收藏成功！\033[0m".center(50)%(username))

@wrapper
@wrapper_log
def logout(*args):
    global flag
    flag = False
    return ("\033[1;31;40m 注销成功 \033[0m".center(50))

@wrapper
@wrapper_log
def u_exit(*args):
    global loop_n
    loop_n = False
    return ("\033[1;31;40m 退出程序！ \033[0m".center(50))

while loop_n:
    blog()