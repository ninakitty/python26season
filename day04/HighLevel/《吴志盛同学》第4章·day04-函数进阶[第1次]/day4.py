''''''
'''
作业题目: 模拟博客园登录
作业需求:
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
##  登录状态
user_status = {'username': None,
               'status': False,}  #定义一个字典 status ： False 为了改变函数执行的方向。

dic1 = {
    1: '登录',
    2: '注册',
    3: '文章',
    4: '日记',
    5: '评论',
    6: '收藏',
    8: '退出程序'
}

dic2 = {
    3: 'artecle',
    4: 'diary',
    5: 'comment',
    6: 'collection',
    7: 'logout',
    8: 'exited',
}

Flag = True
def wrapper(f1): #装饰器 选择页面前判断是否登录，如果未登录 跳转至登录页面
    def inner(*args, **kwargs):
        if user_status.get('status'):
            ret = f1(*args, **kwargs)
            time.sleep(1)
            print('...\n\n请选择其他操作：\n')
            choice2()
            # return inner
        else:
            print('您还未登录，请登录您的账号')
            login() #跳转到登录界面
    return inner

def login(): ##等登录接口
    cot = 2
    while cot >= 0: #三次确认登录机会
        print('请登录')
        Usernm = input('Username:').strip() #.strip()去除字符串左右两边空格
        Passwd = input('Password:').strip()
        with open('register', encoding='utf-8') as f1: #查找register文件是否该用户/密码
            for line in f1:
                if Usernm == line.split()[0] and Passwd == line.split()[1]: #.split()将字符串转换为list,以空格为分隔符
                    print('welcome,', Usernm)
                    cot = -1 #登录成功，则直接下一步不用再登录
                    global user_status #global修改user_status全局变量
                    user_status = {'username': Usernm, 'status': True, } #登录成功，则将status改为True
                    return choice2()
            else:
                print("账户/密码错误，您还有%s次机会" % (cot))
                cot-=1

def register(): # 注册用户，已存在用户直接跳转至登录接口
    print('请注册用户')
    new_user = input('用户名： ').strip()
    with open('register', encoding='utf-8', mode='r+') as f1: #r+ 对文件进行读写
        for line in f1:
            if new_user == line.split()[0]:
                print('该用户已注册，请直接登录')
                return login()
        else:
            new_pass = input('请输入密码： ').strip()
            f1.write('\n')
            f1.write(new_user)
            f1.write('\t')
            f1.write(new_pass)
            global user_status
            user_status = {'username': new_user, 'status': True, }
            choice2()

@wrapper #artecle  = wraaper(article)
def article():
    print('欢迎%s来到文章页面'%(user_status.get('username')))

@wrapper
def diary():
    print('欢迎来到日记本页面')

@wrapper
def comment():
    print('欢迎来到评论页面')

@wrapper
def collection():
    print('欢迎来到收藏页')

@wrapper
def logout():
    print('退出登录')
    global user_status
    user_status = {'username':None, 'status': False, }


def exited():  #退出程序
    print('退出程序')
    global Flag
    Flag = False  ## Flag为False直接退出程序


def choice2(): ## 登录后操作选项
    global user_status
    if user_status.get('status'): #若状态为True即登录状态，直接显示3-8选项
        print('欢迎登陆,请按序号选择登录页面:')
        for k, v in dic2.items(): #直接打印登录后选项
            print(k, v)
        choice = input('请按序号选择页面： ').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice == 3:
                article()
            elif choice == 4:
                diary()
            elif choice == 5:
                comment()
            elif choice == 6:
                collection()
            elif choice == 7:
                logout()
            elif choice == 8:
                exited()
        else:
            print('请输入正确序号')


def main():
    while Flag: # 主函数
        print('请输入序号选择操作：')
        for k, v in dic1.items():
            print(k, v)
        choice = input('请选择操作项目：').strip()
        if  choice.isdigit():
            choice = int(choice)
            if choice == 1:
                login()
            elif choice == 2:
                register()
            elif choice == 3:
                article()
            elif choice == 4:
                diary()
            elif choice == 5:
                comment()
            elif choice == 6:
                collection()
            # elif choice == 7: #没有7，是未登录则没有注销功能
            #     pass
            elif choice == 8:
                exited()
            else:
                print('请按提示输入:')
        else:
            print('请按提示输入')
            return main()

main()

'''
1、整理装饰器的形成过程，背诵装饰器的固定格式
'''
#固定格式
def wrapper(func):
    def inner(*args,**kwargs):
        print('''在执行被装饰函数之前要做的事儿''')
        ret = func(*args,**kwargs)   # 执行被装饰的函数 得到返回值ret
        print('''在执行被装饰函数之后要做的事儿''')
        return ret                   # 将被装饰函数的返回值返回
    return inner

#装饰器的形成过程
import time
def timer(func):
    def inner():
        start = time.time()
        func()
        print(time.time() - start)
    return inner
@timer #==> func1 = timer(func1)
def func1():
    print('in func1')
func1()
'''
这里我们先定义了一个装饰器timer()，而timer函数里面的inner函数就是一个闭包。当我们在函数
func1定义前加上@timer时，这个语句相当于：func1 = timer(func1)。也就是说，我们在进行不带参数的装
饰器的调用时，相当于把下面的函数名当做参数传给了@后面的函数，@timer也就相当于执行了timer(func1)。
后面就好理解了：timer()函数返回了inner函数的内存地址，下面的func1()其实就调用了“闭包”inner()，进行
了inner()函数里面的操作
'''


'''
2、编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需
求添加代码’
'''
def wrapper(func):
    def inner():
        print("每次执行被装饰函数之前都得先经过这里")
        func()
    return inner
@wrapper
def game():
    print("漫画")
game()


'''
3、编写装饰器,在每次执行被装饰函数之后打印一句’每次执行完被装饰函数之后都得先经过这里,这里根据
需求添加代码’
'''
def wrapper(func):
    def inner():
        func()
        print("每次执行完被装饰函数之后都得先经过这里")
    return inner

@wrapper
def game():
    print("动漫")
game()
'''
4、编写装饰器,在每次执行被装饰函数之前让用户输入用户名,密码,给用户三次机会,登录成功之后,才能访
问该函数.
'''
def auth():
    def wrapper(func):
        def inner(*args,**kwargs):
            count=2
            while count >= 0:
                name=input('账户:')
                passwd=input('密码:')
                if name == 'wzs' and passwd == '123':
                    print('登录成功')
                    ret=func(*args,**kwargs)
                    return ret
                else:
                    print('账户或密码错误，您还有%s次机会'%(count))
                    count-=1
                    continue
        return inner
    return wrapper

@auth()
def game():
    print("您可以购物")
game()
# user_login={'username':None,'status':False}
# def auth():
#     def wrapper(func):
#         def inner(*args,**kwargs):
#             if user_login['username'] and user_login['status']:
#                 ret=func(*args,**kwargs)
#                 return ret
#             else:
#                 count=2
#                 while count >= 0:
#                     name=input('账户:')
#                     passwd=input('密码:')
#                     if name == 'wzs' and passwd == '123':
#                         print('登录成功')
#                         ret=func(*args,**kwargs)
#                         return ret
#                     else:
#                         print('账户或密码错误，您还有%s次机会'%(count))
#                         count-=1
#                         continue
#         return inner
#     return wrapper
#
# @auth()
# def game():
#     print("您可以购物")
# game()

'''
5、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,只支持单用户的账号密码,给用
户三次机会），要求登录成功一次，后续的函数都无需再输入用户名和密码
'''
def auth(type='file'):
    def wrapper(func):
        def inner(*args,**kwargs):
            if type == 'file':
                with open('file',mode='r',encoding="utf-8") as f:
                    dic=eval(f.read())
                    count=2
                    while count >= 0:
                        name=input('账户:')
                        passwd=input('密码:')
                        if name in dic and passwd == dic[name]:
                            print('登录成功')
                            ret=func(*args,**kwargs)
                            return ret
                        else:
                            print('账户或密码错误,您还有%s次机会' % (count))
                            count-=1
        return inner
    return wrapper

@auth()
def game():
    print("您可以购物")
game()



'''
7、给每个函数写一个记录日志的功能，
    功能要求：每一次调用函数之前，要将函数名称，时间节点记录到log的日志中。
    所需模块：
    import time
    struct_time = time.localtime()
    print(time.strftime("%Y‐%m‐%d %H:%M:%S",struct_time))
'''
import time
def log(log):
    def wrap(func):
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            aa = time.strftime('%Y-%m-%d %X')
            with open(log, 'a') as wrt:
                info = aa + '--' + func.__name__ + '--' + 'run' + '\n'
                wrt.write(info)
        return inner
    return wrap

@log(log='logs')
def excute():
    print("look up")

@log(log='logs')
def cat():
    print("dog dog")

excute()
cat()











