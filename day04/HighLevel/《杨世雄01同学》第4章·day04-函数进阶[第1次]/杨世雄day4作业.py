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
status =True#定义一个全局状态
def log(func):#日志模块
    def inner(*args):
        struct_time = time.localtime()
        format_time = time.strftime('%Y-%m-%d %H:%M:%S',struct_time)#格式化时间
        res = func(*args)
        with open('log','a',encoding='utf-8') as f:
            f.write('用户:%s 在%s 执行了 %s函数\n'%(args,format_time,func.__name__))#记录日志
        return res
    return inner

    pass
def login(func):#登陆模块
    def inner(*args,**kwargs):
        global status,username#将状态与用户名定义全局以便使用
        count = 3#定义失误次数
        with open('register','r',encoding='utf-8') as f:#读取账号密码
            content = f.read()
        while status and count !=0:
            username = input('请输入账号：').strip()
            password = input('请输入密码：').strip()
            if username + password in content:#验证
                status =False
                print('登录成功，欢迎来到博客园！')
                break
            else:
                count -=1
                print('账号密码输入有误，请重新输入，你还有%s次机会'%count)
        if not status:#验证登陆状态
            res = func(username)
            return res
    return inner

@login#登陆装饰器
@log#日志装饰器
def artical(*args):#文章
    print('欢迎%s访问文章页面'%args)

@login
@log
def logger(*args):#日记
    print('欢迎%s访问日记页面'%args)


@login
@log
def comment(*args):#评论
    print('欢迎%s访问评论页面'%args)


@login
@log
def save(*args):#收藏
    print('欢迎%s访问收藏页面'%args)
@log
def cancellation(*args):#注销
    global status
    status = True
    print('注销成功')
def interactive():#用户交互
    msg ={
        1:login,
        2:enroll,
        3:artical,
        4:logger,
        5:comment,
        6:save,
        7:cancellation,
        8:quit,
        9:pp
    }#将函数地址保存为字典的值，以便调用
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
    9:打印日志
    ''')
    list = [1,2,3,4,5,6,7,9]
    while True:#选择功能
        choice = input('请你选择功能：').strip()
        if int(choice) in list:
            msg[int(choice)](0)
        elif int(choice) == 8:
            break
        else:
            print('无输入功能，请重新选择！')
@login
@log
def pp(*args):#打印日志函数
    with open('log','r',encoding='utf-8') as f:
        for line in f:
            print(line)
def enroll(*args,**kwargs):#注册函数
    global status,username#将状态，用户名定义全局，以便调用
    sure = True
    while sure:
        username = input('请输入要注册的用户名：').strip()
        password = input('请输入要注册的密码：').strip()
        print(username,password)
        choice = input('请确认是否创建上述账号,y/n').strip()#让用户确认是否创建
        if choice == 'y': sure = False
    st = username + password
    with open('register','a',encoding='utf-8') as f:#写入账号密码
        f.write(st)
    status = False
if __name__ == '__main__':#主函数调用
    interactive()
