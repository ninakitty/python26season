# author:王锐
# date:2018/9/13-14

logined = False # 记录登陆状态

#登陆功能函数
def login():
    global logined
    count =0
    while count < 3:
        username = input('Username:').strip()
        password = input('Password:').strip()
        with open('register', encoding='utf-8') as f:
            for line in f:
                line_list = line.strip().split()
                if username == line_list[0] and password == line_list[1]:
                    print("登陆成功!")
                    # status_dic['username'] = username
                    # status_dic['status'] = True
                    logined = True
                    return True
                else:
                    print("用户名或者密码不对!")
    count += 1

#注册功能版块
def register(*args, **kwargs):
    flag = True
    while flag:
        username = input('请输入要注册的用户名:')
        f1 = open('register',encoding='utf-8')
        for i in f1:
            if username in i:
                print('用户名重复,请重新输入')
                f1.close()
                break
        else:
            f1.close()
            password = input('请输入要注册的密码:').strip()
            f2 = open('register','a+', encoding='utf-8')
            f2.write('\n'+username+' '+password+'\n')
            f2.flush()
            f2.close()
            print('恭喜你,注册成功')
            '''注册成功后完成自动登陆，到首页，这部分我没想出来。想着在回到Main()，
            那就又重新来，还得排除选择注册，想着调用login()，可是又不满足自动登陆
            '''
            login()
            return True

##登陆认证装饰器
def login_require(func):
    def inner(*args, **kwargs):
        if logined:
            return func(*args, **kwargs)
        else:
            print('账号或者密码错误，请先登录！')
            if login():
                return func(*args, **kwargs)
    return inner

# status_dic = {
#     'username': None,
#     'status': False,
# }

#注销版块
def logout():
    global logined
    global login_username
    if logined:
        logined = False
        login_username = None
        print("注销成功!")
    else:
        print("无用户登录信息.")

#日志记录装饰器
import time
def log(func):
    def inner(*args,**kwargs):
        x = time.localtime()
        print(time.strftime("%Y-%m-%d %H:%M:%S ",x)+"%s函数被执行了" % (func.__name__))
        ret=func(*args,**kwargs)
        return ret
    return inner

@login_require
@log
def article():
    print("welcome Article Page!")

@login_require
@log
def dairy():
    print("welcome Article Page!")

@login_require
@log
def comments():
    print("welcome Comments Page!")

@login_require
@log
def faroviates():
    print("welcome Faroviates Page!")

#主函数
def Main():
    func_list = [
        "请登录",
        "请注册",
        "文章页面",
        "日记页面",
        "评论页面",
        "收藏页面",
        "注销",
        "退出程序"
    ]
    print("欢迎来到博客园登陆首页")
    for index,item in enumerate(func_list):
        print(index+1,":",item)

    def select():
        user_choice = input("请输入您的选项>>>")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice == 1:
                login()
                #登陆成功后，让用户去选择要访问的Item，此处可能又更优写法，但是我还不会
                print('请输入要访问的选项[3,4,5,6,7,8]：')
                user_input = int(input('输入选项>>>'))
                if user_input == 3:
                    article()
                elif user_input == 4:
                    dairy()
                elif user_input == 5:
                    comments()
                elif user_input == 6:
                    faroviates()
                elif user_input == 7:
                    logout()
                elif user_input == 8:
                    exit(0)
                else:
                    print("不存在的选项")
            elif user_choice == 2:
                register()
            elif user_choice == 3:
                article()
            elif user_choice == 4:
                dairy()
            elif user_choice == 5:
                comments()
            elif user_choice == 6:
                faroviates()
            elif user_choice == 7:
                logout()
            elif user_choice == 8:
                exit(0)
            else:
                print("不存在的选项")

        else:
            print("没有您输入的选项")
            exit(0)
    select()

Main()