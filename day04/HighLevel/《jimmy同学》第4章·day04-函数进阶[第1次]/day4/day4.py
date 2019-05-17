

import os

user_info_list = []  # 用户信息
with open(r'F:\python\作业讲解\register.txt', 'r+', encoding='utf-8') as f:
    if len(f.read()) == 0:
        f.write('%s \t%s\n' % ('用户名', '密码'))

def user_name_info():
    '''验证用户名是否已被注册'''
    while True:  # 验证用户名是否已被注册
        user_info = input('请输入用户名：').strip().lower()
        with open(r'F:\python\作业讲解\register.txt', 'r', encoding='utf-8') as f:
            for lines in f:
                name = lines.strip().split(' ')
                if user_info == name[0]:
                    print('用户已存在')
                    break
            else:
                print('用户名可使用')
                return user_info

def write_user_info(newuser_name, newuser_pwd):
    '''将新用户的用户名,密码,初始购物卡金额写入文件'''
    with open(r'F:\python\作业讲解\register.txt', 'a', encoding='utf-8') as f:
        f.write('%s \t%s\n' % (newuser_name, newuser_pwd))
        return

def user_pwd_info():
    '''验证密码是否一致'''
    while True:  # 验证密码是否一致
        user_pwd = input('请输入密码：').strip()
        user_pwd_again = input('请确认密码：').strip()
        if user_pwd == user_pwd_again:
            print('注册成功')
            return user_pwd
        print('密码不一致')

def log_in():
    '''注册'''
    new_name = user_name_info()  # 检查新用户注册的名字是否可以使用
    new_pwd = user_pwd_info()  # 检查用户注册的密码是否一致
    write_user_info(new_name, new_pwd)  # 将新用户的用户名,密码,初始购物卡金额写入文件
    return

auth_status = False
def wrapper(func):
    def auth(*args,**kwargs):
        '''登陆'''
        count = 0
        global auth_status
        while True:
            if count == 3:
                print('错误次数过多...')
                exit()
            user = input('请输入账户名:').strip().lower()
            pwd = input('请输入登陆密码:').strip()
            with open(r'F:\python\作业讲解\register.txt', 'r', encoding='utf-8') as f:
                for line in f:
                     data = line.strip().split(' \t')
            if user == data[0] and pwd == data[1]:
                print('登陆成功!')
                auth_status =True
                ret = func(*args,**kwargs)
                return ret
            else:
                print('用户名或密码不正确！')
                count += 1
    return auth

@wrapper
def article():
    print('欢迎xx用户访问评论（文章，日记，收藏）页面')

@wrapper
def diary():
    print('欢迎xx用户访问评论（文章，日记，收藏）页面')

@wrapper
def point():
    print('欢迎xx用户访问评论（文章，日记，收藏）页面')

@wrapper
def collect():
    print('欢迎xx用户访问评论（文章，日记，收藏）页面')

@wrapper
def cancel():
    print('欢迎xx用户访问评论（文章，日记，收藏）页面')

def quit():
    print('再见！')
    exit()

# 主体代码
dic = {
    '1': log_in,
    '2': wrapper,
    '3': article,
    '4': diary,
    '5': point,
    '6': collect,
    '7': cancel,
    '8': quit
}

def register():
    while True:
        print('''
        1.请注册
        2.请登陆
        3.文章页面
        4.日记页面
        5.评论页面
        6.收藏页面
        7.注销
        8.退出程序
        ''')
        choice1 = input('---->').strip()
        if choice1 in dic:
            dic[choice1]()
        else:
            print('非法输入')

register()
