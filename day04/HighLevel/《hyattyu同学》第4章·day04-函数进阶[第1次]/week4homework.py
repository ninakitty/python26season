logined = False
loginuser = None
import time
import sys
def login():
    global logined
    if not logined:
        userinfofile = open("userinfo",'r',encoding='utf-8')
        username = []
        password = []
        for line in userinfofile:
            line = line.strip()
            username.append(line.split(" ")[0])
            password.append(line.split(" ")[1])

        inputAccount = input("请输入用户名")
        inputPwd = input("请输入密码")
        userinfofile.close()
        for index in range(len(username)):
            if username[index] == inputAccount:
                if password[index] == inputPwd:
                    global loginuser
                    loginuser = inputAccount
                    print("登陆成功")
                    logined = True
                    return True
                else:
                    print("用户名或密码错误")
                    return False
        print("用户不存在")
    else:
        print("用户已经登陆")
    return False

def wrapper(func):
    def inner(*args,**kwargs):
        if logined:
            ret = func(*args,**kwargs)
            return ret
        else:
            if login():
                ret = func(*args,**kwargs)
                with open('log', 'a', encoding='utf-8') as logfile:
                    logfile.write('用户:%s 在%s 执行了 %s函数\n' % (loginuser, time.strftime("%Y-%m-%d"),func.__name__))
                return ret
    return inner

def register():
    inputAccount = input("请输入用户名")
    inputPwd = input("请输入密码")
    userinfofile = open("userinfo", 'a', encoding='utf-8')
    userinfofile.write(inputAccount + " " + inputPwd+"\n")
    print("注册成功")
    global logined
    logined = True
    userinfofile.close()
@wrapper
def diary():
    print("欢迎来到%s的日记界面"%loginuser)
@wrapper
def article():
    print("欢迎来到%s的文章界面"%loginuser)
@wrapper
def favourate():
    print("欢迎来到%s的收藏界面" % loginuser)

@wrapper
def comment():
    print("欢迎来到%s的评论界面" % loginuser)

def logout():
    global loginuser
    loginuser = False

while True:
    print('''
        1:请登录
        2:请注册
        3:文章页面
        4:日记页面
        5:评论页面
        6:收藏页面
        7:注销
        8:退出程序
    ''')

    inputfunc = input("请输入需要的操作")

    if int(inputfunc)==1:
        login()
    elif int(inputfunc)==2:
        register()
    elif int(inputfunc)==3:
        article()
    elif int(inputfunc)==4:
        diary()
    elif int(inputfunc)==5:
        comment()
    elif int(inputfunc)==6:
        favourate()
    elif int(inputfunc) == 7:
        logout()
    elif int(inputfunc)==8:
        sys.exit()
