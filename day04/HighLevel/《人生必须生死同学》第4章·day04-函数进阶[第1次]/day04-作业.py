#!/usr/bin/env python

import time

user_info_file = 'registry.txt'
log_file = 'log'

# 存储已登录的用户名
user_is_login = ''

# 控制while循环
flag = True


def wrapper_login(func):
    '''装饰器-用户访问页面前的认证'''
    def inner(*args, **kwargs):
        if user_is_login:
            ret = func(*args, **kwargs)
        else:
            print('访问该页面需要先登录')

            login()
            if user_is_login:
                ret = func(*args, **kwargs)
                return ret
            else:
                global flag
                flag = False
    return inner



def wrapper_log(func):
    '''装饰器-用户访问页面前的日志'''

    def inner(*args, **kwargs):
        add_log(user_is_login, func.__name__)
        ret = func(*args, **kwargs)
        return ret
    return inner


def welecom():
    msg = '''\
    欢迎来到博客园首页
    1:请登录
    2:请注册
    3:文章页面
    4:日记页面
    5:评论页面
    6:收藏页面
    7:注销
    8:退出程序
    '''
    print(msg)


def add_log(user_name, func_name):
    '''写入用户操作日志'''

    year,month,day = get_date()
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write('用户:%s 在%s年%s月%s日 执行了 %s函数\n' % (user_name, year,month,day, func_name))


def get_date():
    '''获取年月日'''

    year,month,day = time.strftime('%Y %m %d').split()
    return year,month,day


def get_user_input():
    '''获取用户在首页的输入'''

    user_input = input('请输入序号进行选择: ')
    return user_input


def get_user_input_account():
    '''获取用户输入的账号密码'''

    user_name = input('请输入用户名: ').strip()
    user_password = input('请输入密码: ').strip()

    return user_name,user_password


def check_user_info(user_name, user_password):
    '''验证用户账号密码'''

    with open(user_info_file, 'r', encoding='utf-8') as f:
        for line in f:
            # 将用户的账号密码 转换为一个列表
            line = line.split()

            # 如果如果列表为空，则
            if len(line) < 2:
                continue
            if user_name == line[0] and user_password == line[1]:
                return True
    return False


def check_user_exist(user_name):
    '''检测用户是否存在文件内'''

    with open(user_info_file, 'r', encoding='utf-8') as f:
        for line in f:
            # 将用户的账号密码 转换为一个列表
            line = line.split()

            if user_name in line :
                return True

            else:
                return False


def write_new_user(user_name, user_password):
    '''向文件写入注册的新用户'''

    with open(user_info_file, 'a', encoding='utf-8') as f:
        f.write('%s %s\n' % (user_name, user_password))


def login():
    '''用户登录'''
    global user_is_login
    error_count = 0
    while error_count <= 2:
        user_name,user_password = get_user_input_account()

        # 验证用户账号密码
        check_user_info_result = check_user_info(user_name, user_password)

        if check_user_info_result:
            user_is_login = user_name
            return user_name
        else:
            error_count += 1
            if error_count > 2:
                continue
            print('用户名或密码错误，请重新输入!')
    else:
        print('错误次数过多，请重新启动程序!')
        return False


def logout():
    global user_is_login
    if user_is_login:
        user_is_login = ''
        print('用户已注销')
    else:
        print('用户未登录，无法注销!')


def registry():
    '''用户注册函数'''

    global user_is_login

    user_name,user_password = get_user_input_account()

    check_user_exist_resutl = check_user_exist(user_name)


    if check_user_exist_resutl:
        return False
    else:
        write_new_user(user_name, user_password)
        user_is_login = user_name
        return True


@wrapper_login
@wrapper_log
def doc_page():
    print('''\
    
    ---欢迎%s用户访问文章页面---
    
    ''' % user_is_login)

@wrapper_login
@wrapper_log
def note_page():
    print('''\
    
    ---欢迎%s用户访问日记页面---
    
    ''' % user_is_login)

@wrapper_login
@wrapper_log
def comment_page():
    print('''\

    ---欢迎%s用户访问评论页面---

    ''' % user_is_login)

@wrapper_login
@wrapper_log
def collect_page():
    print('''\
    
    ---欢迎%s用户访问收藏页面---
    
    ''' % user_is_login)




while flag:
    welecom()

    user_input = get_user_input()


    if user_input == '1':
        login_result = login()
        if login_result:
            print('登录成功')
        else:
            flag = False

    elif user_input == '2':

        if user_is_login:
            print('用户已登录，无法再注册')
            continue

        resgistry_result = registry()

        if resgistry_result:
            print('注册成功')
        else:
            print('注册失败，该用户已存在!')

    elif user_input == '3':
        doc_page()


    elif user_input == '4':
        note_page()


    elif user_input == '5':
        comment_page()


    elif user_input == '6':
        collect_page()


    elif user_input == '7':
        logout()


    elif user_input == '8':
        print('程序退出中...')
        break

    else:
        print('输出错误，请重新输入!')
