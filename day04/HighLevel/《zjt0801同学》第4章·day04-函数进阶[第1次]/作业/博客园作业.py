'''
1)，启动程序，首页面应该显示成如下格式：
    欢迎来到博客园首页
    1:请登录
    2:请注册
    3:文章页面
    4:日记页面
    5:评论页面
    6:收藏页面
    7:注销
    8:退出程序
2)，用户输入选项，3~6选项必须在用户登录成功之后，才能访问成功。
3)，用户选择登录，用户名密码从register文件中读取验证，三次机会，
        没成功则结束整个程序运行，成功之后，可以选择访问3~6项，访问页面之前，
        必须要在log文件中打印日志，日志格式为-->用户:xx 在xx年xx月xx日 执行了 %s函数，
        访问页面时，页面内容为：欢迎xx用户访问评论（文章，日记，收藏）页面
4)，如果用户没有注册，则可以选择注册，注册成功之后，可以自动完成登录，然后进入首页选择。
5)，注销用户是指注销用户的登录状态，使其在访问任何页面时，必须重新登录。
'''


import time
file_path = 'register'
log_path = 'log.out'
logined = False # 标志位，只有登陆后才能购物
guser = ''

msg = '''
1:请登录
2:请注册
3:文章页面
4:日记页面
5:评论页面
6:收藏页面
7:注销
8:退出程序
'''

#登陆验证装饰器
def login(func):
    def inner(*args, **kwargs):
        '''登陆装饰器'''
        global logined
        global guser
        count = 0
        if not logined:
            print('请先登录')
            with open(file_path, mode='r', encoding='utf-8') as f:
                lst = []
                lst2 = []
                for i in f:
                    if i:
                        lst.append(i.split('|')[0])
                        lst2.append(i.split('|')[1].strip())
                while count < 4:
                    user = input('enter user: ').strip()
                    if user not in lst:
                        print('用户不存在，请先注册')
                        register()

                    pwd = input('enter password: ').strip()
                    if pwd not in lst2:
                        print('账户密码错误,请重新输入，还有 %d 次机会' % (3 - count))
                        if count == 3:
                            print('输入次数过多，账号已锁定')
                            q()

                    if user in lst and pwd in lst2:
                        print('登录成功')
                        logined = True
                        guser = user
                        m = {'1':logining, '2': register , '3':articleoage,'4':logpage , '5':commpage , '6':collectionpage , '7':cancellation, '8': q}
                        print(msg)
                        while 1:
                            cmd = input('输入你的选项: ')
                            if cmd in m:
                                m[cmd]()
                            else:
                                print('error repeat enter')

                    count += 1
                    continue
        if logined:
            ret = func(*args, **kwargs)  # 被装饰的函数
            return ret

    return inner


# 日志记录
def log(func):
    def inner(*args,**kwargs):
        ret = func(*args,**kwargs)
        m = '用户:%s 在%s 执行了%s函数' % (guser, time.strftime('%Y-%m-%d %H:%M:%S'),func.__name__)
        print(m)
        with open(log_path,mode='a',encoding='utf-8') as f:
            f.write(m+'\n')


        return ret
    return inner


def q():
    ''' 退出 '''
    quit()

def cancellation():
    '''注销'''
    global logined
    logined = False
    print('注销成功，回到首页')
    main()

def register():
    '''注册'''
    global logined
    global guser
    while 1:
        username = input('输入用户名：')
        with open(file_path,mode='r',encoding='utf-8') as f:
            for line in f:
                if username == line.split('|')[0].strip():
                    print('用户名已存在')
                    break
            else:
                password = input('enter password: ')
                password_r = input('repeat password: ')
                if password == password_r:
                    with open(file_path, mode='a' , encoding='utf-8') as f:
                        f.write(username + '|' + password + '\n')
                        f.flush()  # 强制写入硬盘
                        print('注册成功')
                        logined = True
                        guser = username
                        main()

def logining():
    ''' 登录 '''
    global logined
    global guser
    count = 0

    with open(file_path, mode='r' , encoding='utf-8') as f:
        lst = []
        lst2 = []
        for i in f:
            if i:
                lst.append(i.split('|')[0])
                lst2.append(i.split('|')[1].strip())
        while count < 4:
                user = input('enter user: ').strip()
                if user not in lst:
                    print('用户不存在，请注册')
                    register()

                pwd = input('enter password: ').strip()
                if pwd not in lst2:
                    print('账户密码错误,请重新输入，还有 %d 次机会' % (3-count))
                    if count == 3:
                        print('输入次数过多，账号已锁定')
                        q()

                if user in lst and pwd in lst2:
                    print('登录成功')
                    logined = True
                    guser = user
                    main()
                count += 1
                continue


@login
@log
def articleoage():
    print('欢迎%s用户访问文章页面' %guser)

@login
@log
def logpage():
    print('欢迎%s用户访问日志页面' % guser)


@login
@log
def commpage():
    print('欢迎%s用户访问评论页面' % guser)


@login
@log
def collectionpage():
    print('欢迎%s用户访问收藏页面' % guser)



def main():
    ''' 程序交互入口 '''
    print(msg)
    d = {'1':logining, '2': register , '3':articleoage,'4':logpage , '5':commpage , '6':collectionpage , '7':cancellation, '8': q}
    # for k in d:
    #     print(k)
    while 1:
        cmd = input('输入你的选项: ')
        if cmd in d:
            d[cmd]()

        else:
            print('error repeat enter')


if __name__ == '__main__':
    main()