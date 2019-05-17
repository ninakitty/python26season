# 1、整理装饰器的形成过程，背诵装饰器的固定格式
'''
def wrapper(f):
    def inner(*args, **kwargs):
        ret = f(*args, **kwargs)
        return ret
    return inner
'''

# 2、编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需
# 求添加代码’
'''
def wrapper(f):
    def inner(*args, **kwargs):
        print('每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码')
        ret = f(*args, **kwargs)
        return ret
    return inner
'''

# 3、编写装饰器,在每次执行被装饰函数之后打印一句’每次执行完被装饰函数之后都得先经过这里,这里根据
# 需求添加代码’
'''
def wrapper(f):
    def inner(*args, **kwargs):
        ret = f(*args, **kwargs)
        print('每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码')
        return ret
    return inner
'''

# 4、编写装饰器,在每次执行被装饰函数之前让用户输入用户名,密码,给用户三次机会,登录成功之后,才能访
# 问该函数.
'''
def wrapper(f):
    def inner(*args, **kwargs):
        times = 0  # tried times
        userinfo = []
        username_list = []
        with open('jd_userinfo', encoding='utf-8') as file:
            for line in file:
                username_list.append(line.strip().split('|')[0])
                userinfo.append(line.strip().split('|'))

        username = input('Please input your username:').strip()

        if username in username_list:
            password = input('Please input your password:').strip()
            while 1:
                if [username, password] in userinfo and times < 2:
                    ret = f(*args, **kwargs)
                    return ret
                elif [username, password] not in userinfo and times < 2:
                    times += 1
                    print('Invalid Password, left %d times!' % (3-times))
                    password =input('Please input your password again:').strip()
                elif [username, password] not in userinfo and times >= 2:
                    print('Invalid Password, tried 3 times, your account has been locked!!')
                    break

        elif username not in username_list:
            print('Invalid username!')
    return inner

@wrapper
def f():
    print("login success!")

f()
'''

# 5、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,只支持单用户的账号密码,给用
# 户三次机会），要求登录成功一次，后续的函数都无需再输入用户名和密码

'''
login_status = {
    'username': None,
    'status': False,
}

def wrapper(f):
    def inner(*args, **kwargs):
        if login_status['status']:
            ret = f(*args, **kwargs)
            return ret
        else:
            userinfo = []
            username_list = []
            with open('jd_userinfo', encoding='utf-8') as file:
                for line in file:
                    username_list.append(line.strip().split('|')[0])
                    userinfo.append(line.strip().split('|'))

            username = input('Please input your username:').strip()

            if username in username_list:
                password = input('Please input your password:').strip()
                for times in range(0, 3):
                    if [username, password] in userinfo and times < 2:
                        ret = f(*args, **kwargs)
                        login_status['status'] = True
                        login_status['username'] = username
                        return ret
                    elif [username, password] not in userinfo and times < 2:
                        times += 1
                        print('Invalid Password, left %d times!' % (3-times))
                        password =input('Please input your password again:').strip()
                    elif [username, password] not in userinfo and times >= 2:
                        print('Invalid Password, tried 3 times, your account has been locked!!')
            elif username not in username_list:
                print('Invalid username!')
    return inner

@wrapper
def func1():
    print(111)

@wrapper
def func2():
    print(222)

@wrapper
def func3():
    print(333)

func1()
func2()
func3()
'''

# 6、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,可支持多账号密码），要求登
# 录成功一次（给三次机会），后续的函数都无需再输入用户名和密码。
'''
login_status = {
    'TM_username': None,
    'TM_status': False,
    'JD_username': None,
    'JD_status': False,
}

def account(Flag):
    def wrapper(f):
        def inner(*args, **kwargs):
            account_book = Flag.lower()+'_userinfo'
            account_username = Flag+'_username'
            account_status = Flag+'_status'

            if login_status[account_status]:
                ret = f(*args, **kwargs)
                return ret
            else:
                userinfo = []
                username_list = []

                with open(account_book, encoding='utf-8') as file:
                    for line in file:
                        username_list.append(line.strip().split('|')[0])
                        userinfo.append(line.strip().split('|'))

                username = input('Please input your %s account username:' % Flag).strip()

                if username in username_list:
                    password = input('Please input your %s account password:' % Flag).strip()
                    for times in range(0, 3):
                        if [username, password] in userinfo and times < 2:
                            login_status[account_status] = True
                            login_status[account_username] = username
                            ret = f(*args, **kwargs)
                            return ret
                        elif [username, password] not in userinfo and times < 2:
                            times += 1
                            print('Invalid Password, left %d times!' % (3-times))
                            password =input('Please input your password again:').strip()
                        elif [username, password] not in userinfo and times >= 2:
                            print('Invalid Password, tried 3 times, your account has been locked!!')
                elif username not in username_list:
                    print('Invalid username!')
        return inner
    return wrapper

@account('TM')
def func1():
    print(111)

@account('JD')
def func2():
    print(222)
    print(login_status['JD'+'_username'])

@account('TM')
def func3():
    print(333)

func1()
func2()
func3()
'''

# 7、给每个函数写一个记录日志的功能，
# 功能要求：每一次调用函数之前，要将函数名称，时间节点记录到log的日志中。
# 所需模块：
# import time
# struct_time = time.localtime()
# print(time.strftime("%Y‐%m‐%d %H:%M:%S",struct_time))

'''
import time
def logging():
    with open('logging.txt', 'a', encoding='utf8') as f:
        time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        f.write('%s at %s 被执行\n' % (logging.__name__, time_now))
        f.flush()
logging()
'''

# 作业题目：模拟博客园登录
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

'''
import os
import datetime
import json
import sys

is_login = False
login_username = None
log_file = "./log"
user_file = "./register"


def userinfo(method="r",userDict=None):
    """
    用户信息存取
    :param userDict:
    :param method:
    :return:
    """
    if not os.path.exists(user_file):
        with open(user_file, mode="w") as f:
            pass
    if method == "r":
        with open(user_file, mode="r") as f:
            contnet = f.read()
            userDict = json.loads(contnet) if contnet else dict()
            return userDict
    else:
        with open(user_file, mode="w") as f:
            f.write(json.dumps(userDict))
            return True


def logs(fn):
    """
    :param fn: 日志记录装饰器
    :return:
    """
    def wrapper(*args,**kwargs):
        with open(log_file,mode="a+",encoding="utf-8") as f:
            f.write("用户:%s 在%s 执行了 %s 函数\n" % (login_username,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),fn.__name__))
            f.flush()
        return fn(*args,**kwargs)
    return wrapper


def login_required(fn):
    """
    :param fn: 登录检测装饰器
    :return:
    """
    def wrapper(*args,**kwargs):
        if is_login:
            return fn(*args,**kwargs)
        else:
            login_result = login()
            if login_result:
                return fn(*args,**kwargs)
    return wrapper


def register():
    """
    注册并直接登录
    :return:
    """
    global login_username
    global is_login
    username, password = input("请输入注册用户名:  "),input("请输入注册密码:  ")
    userDict = userinfo()
    if userDict.__contains__(username):
        print("用户名 {} 已存在，不允许重复注册.".format(username))
    else:
        userDict.setdefault(username,password)
        result = userinfo(method="w",userDict=userDict)
        if result:
            is_login, login_username = True, username
            print("注册成功, {}  用户已自动登录.".format(username))
        else:
            print("注册失败.")


def login():
    """
    登录验证
    :return:
    """
    global is_login
    global login_username
    init_errors, max_errors,userDict = 0, 3, userinfo()
    while 1 :
        if init_errors >= 3:
            exit(2)
        username, password = input("请输入登录用户名:  "), input("请输入登录密码:  ")
        if userDict.__contains__(username) and password == userDict[username]:
            is_login = True
            login_username = username
            print("用户 {} 登录成功.".format(username))
            return True
        else:
            init_errors += 1
            if init_errors < 3:
                print("用户名或密码输入错误,剩余可操作次数 %s" % (max_errors - init_errors))

def logout():
    """
    注销
    :return:
    """
    global is_login
    global login_username
    if is_login:
        is_login = False
        login_username = None
        print("注销成功.")
    else:
        print("无用户登录信息.")

def exit(code=0):
    """
    退出程序
    :param code:
    :return:
    """
    sys.exit(code)


@login_required
@logs
def articlesPage():
    """
    文章页面
    :return:
    """
    print("欢迎 %s 访问文章页面." % login_username)


@login_required
@logs
def logsPage():
    """
    日志页面
    :return:
    """
    print("欢迎 %s 访问日志页面." % login_username)


@login_required
@logs
def commentPage():
    """
    评论页面
    :return:
    """
    print("欢迎 %s 访问评论页面." % login_username)


@login_required
@logs
def collectionPage():
    """
    收藏页面
    :return:
    """
    print("欢迎 %s 访问收藏页面." % login_username)


def main():
    item_list = {
        "1": {"title": "请登录","func": login},
        "2": {"title": "请注册","func": register},
        "3": {"title": "文章页面","func": articlesPage},
        "4": {"title": "日志页面","func": logsPage},
        "5": {"title": "评论页面","func": commentPage},
        "6": {"title": "收藏页面","func": collectionPage},
        "7": {"title": "注销","func": logout},
        "8": {"title": "退出程序","func": exit},
    }

    print("欢迎来到博客园首页")
    while 1:
        for k,v in item_list.items():
            print("{}. {}".format(k,v.get("title")))
        user_choice = input("请选择需要操作的功能:  ")
        if item_list.__contains__(user_choice):
            fn = item_list.get(user_choice).get("func")
            fn()
if __name__ == "__main__":
    main()
'''