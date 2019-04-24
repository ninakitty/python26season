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
from functools import wraps

user = ''  # 帐号
user_is_login = False  # 是否已登录
filename = 'register'  # 帐号密码文件
logfile = 'log'  # 日志文件名


def log_wrapper(fn):  # 定义日志装饰器
    @wraps(fn)
    def inner(*args, **kwargs):  # 内部函数
        fun_name = fn.__name__
        if user_is_login:
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # 当时时间
            with open(logfile, mode='a', encoding='utf8') as file:  # 打开文件管道
                line_content = f'用户:{user} {timestamp} 执行了 {fun_name}函数\n'  # 拼接字符
                file.write(line_content)  # 写入文件
            result = fn(*args, **kwargs)  # 执行被装饰函数
            return result  # 返回函数结果

        else:
            do_login()

    return inner  # 返回被装饰过的函数


def login():  # 1.登录程序
    print('进入登录页面'.center(50, '-'))
    count = 3  # 重试机会
    while count:  # 根据剩余机会循环
        count -= 1  # 每次循环减1
        uname = input('请输入帐号:').strip()  # 要求输入帐号
        upwd = input('请输入密码:').strip()  # 要求输入密码
        with open(filename, mode='r', encoding='utf8') as file:  # 打开文件管道
            for line in file:  # 迭代每行文件
                username, password = line.strip().split(',')  # 获取每行帐号密码
                if uname == username and upwd == password:  # 匹配帐号密码
                    return {'suc': True, 'user': uname}  # 返回成功登录
        if count:  # 剩余机会大于0,打开次数
            print(f'您的重试机会还有{count}次,请重试!')
        else:  # 剩余等于0,打开已用尽!
            print('您的重试机会已用尽!')
    return {'suc': False}  # 返回登录错误


def do_login():  # 执行登录
    result = login()
    if result['suc']:
        global user, user_is_login  # 引入全局变量
        user = result['user']  # 更改变量
        user_is_login = True
        print('登录成功!', user)
    else:
        print('登录失败!')
        close()  # 关闭程序


def login_wrapper(fn):  # 登录装饰器
    @wraps(fn)
    def login_inner(*args, **kwargs):  # 内部函数
        global user_is_login  # 引入全局变量
        if user_is_login:  # 如果已登录
            result = fn(*args, **kwargs)  # 执行原函数
            return result  # 返回结果和函数名称
        else:  # 如果未登录
            do_login()  # 登录

    return login_inner


def register():  # 2.注册

    uname = input('请输入注册帐号:')
    upwd = input('请输入密码:')
    confirm_upwd = input('请再次输入密码:')
    if uname == '' or upwd == '':  # 如果帐号或密码为空
        return {'msg': '用户名或密码不能为空!', 'suc': False}
    elif upwd != confirm_upwd:  # 如果两次密码输入不同
        return {'msg': '两次密码输入不相同!', 'suc': False}
    with open(filename, mode='r', encoding='utf8') as read_file:
        for line in read_file:  # 迭代每行内容
            username, password = line.strip().split(',')  # 分割每行内容
            if uname == username:  # 如果帐号已存在
                return {'msg': '用户名重复!', 'suc': False}
    with open(filename, mode='a', encoding='utf8') as file:  # 打开文件管道
        user_content = uname + ',' + upwd + '\n'  # 拼接写入内容
        file.write(user_content)  # 写入
    return {'msg': '注册成功', 'suc': True, 'user': uname}


def do_register():  # 执行注册
    print('欢迎进入注册页面')
    result = register()
    if result['suc']:
        global user, user_is_login  # 引入全局变量
        user = result['user']  # 更改内容
        user_is_login = True
        print(result['msg'], user)
    else:
        print(result['msg'])


@log_wrapper
@login_wrapper
def article():  # 3.文章页面
    print(f'欢迎{user}用户访问文章页面'.center(100, '-'))


@log_wrapper
@login_wrapper
def diary():  # 4.日记页面
    print(f'欢迎{user}用户访问日记页面'.center(100, '-'))


@log_wrapper
@login_wrapper
def comment():  # 5.评论页面
    print(f'欢迎{user}用户访问评论页面'.center(100, '-'))


@log_wrapper
@login_wrapper
def favorite():  # 6.收藏
    print(f'欢迎{user}用户访问收藏页面'.center(100, '-'))


def logout():  # 7.注销
    global user, user_is_login  # 引入全局变量
    user = ""  # 修改内容
    user_is_login = False
    print('注销成功')


def close():  # 退出
    print('再见!')
    exit()


if __name__ == '__main__':
    serial = [i for i in range(1, 9)]  # 序号范围
    while 1:  # 循环
        print('''
            欢迎来到博客园首页
        1:请登录
        2:请注册
        3:文章页面
        4:日记页面
        5:评论页面
        6:收藏页面
        7:注销
        8:退出程序    
        ''')
        input_num = input('请输入序号进入程序:')
        if input_num.isdigit():  # 判断输入内容为数字
            input_num = int(input_num)  # 输入内容转换为数字
            if input_num in serial:  # 判断是否在序号范围
                if input_num == 1:  # 登录
                    do_login()
                elif input_num == 2:  # 注册
                    do_register()
                elif input_num == 3:  # 文章
                    article()
                elif input_num == 4:  # 日记
                    diary()
                elif input_num == 5:  # 评论
                    comment()
                elif input_num == 6:  # 收藏
                    favorite()
                elif input_num == 7:  # 登出
                    logout()
                elif input_num == 8:  # 退出
                    close()
            else:
                print('请输入数字序号!')
        else:
            print('请输入数字序号!')
