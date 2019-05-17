#!/usr/bin/env python
#_*_conding:utf-8_*_
#
import time

username = ''
file_path = 'register.txt'
flag = 0
def login():
    ''' 登录 '''
    global flag
    count = 0

    with open(file_path, encoding='utf8') as f:
        while count < 4:
                global username
                username = input('输入用户名: ').strip()
                pwd = input('请输入密码: ').strip()
                for i in f.readlines():
                    if username in i.split('|')[0] and pwd in i.split('|')[1].strip('\n'):
                        print('登录成功，开始畅游博客园吧!!!')
                        flag = 1
                        operat()
                else:
                    if count != 3:
                        print('\033[31m用户不存在,还有 %s 次机会\033[0m' % (3 - count))
                    else:
                        print('\033[31m账号被锁定,请24小时后再登录吧!!!\033[0m')
                        q()
                    count += 1
                    continue

def register():
    ''' 注册 '''
    global flag
    while True:
        global username
        username = input('输入用户名：')
        with open(file_path, 'r', encoding='UTF-8') as f:
            info = f.readlines()
        for i in info:
            if username == i.split('|')[0].strip():
                print('用户名已存在')
                break
        else:
            password = input('enter password: ')
            password_r = input('repeat password: ')
            if password == password_r:
                with open(file_path, 'a', ) as f:
                    f.write(username + '|' + password + '\n')
                    f.flush()  # 强制写入硬盘
                    print('注册成功，开始畅游博客园吧!!!')
                    flag = 1
                    print('欢迎 %s 来到博客园' %username)
                    operat()

def q():
    ''' 退出 '''
    quit()

def page_context():
    print('欢迎 %s 访问文章页面' %username)
    log()
def log_context():
    print('欢迎 %s 访问日志页面' %username)
    log()
def pinglun():
    print('欢迎 %s 访问评论区页面' %username)
    log()
def shouchang():
    print('欢迎 %s 访问收藏页面' %username)
    log()
def log():
    with open('log.txt', 'a', encoding='utf-8') as f:
        info = '用户:' + str(username) + time.strftime('%Y%m-%d %H:%M:%S') + '执行了' +'%s函数'
        f.write(info + '\n')
        f.flush()
def operat():
    ''' 操作程序入口 '''
    if flag:
        dic = {'3': '文章页面', '4': '日志页面', '5': '评论区', '6': '收藏页面', '7': '注销', '8': '退出程序'}
        for k, v in dic.items():
            print(k, v)
    while True:
        context = int(input('\033[32m请输入你的选项\033[0m'))
        if context == 3:
            page_context()
        elif context == 4:
            log_context()
        elif context == 5:
            pinglun()
        elif context == 6:
            shouchang()
        elif context == 7:
            main()
        elif context == 8:
            quit()
        else:
            print('您输入的选项有误，请重新输入: ')
    else:
        print('前请先登录或注册')
        main()
        log()

def main():
    ''' 程序交互入口 '''
    dic = {'1': '请登录', '2': '请注册', '3': '文章页面', '4': '日志页面', '5': '评论区', '6': '收藏页面', '7': '注销', '8': '退出程序'}
    print('欢迎来到博客园首页')
    for k, v in dic.items():
        print(k, v)
    while True:
        context = int(input('\033[32m请输入你的选项:\033[0m'))
        if context == 1:
            login()
        elif context == 2:
            register()
        elif context == 3:
            print('\033[31m请登录或者注册后访问\033[0m')
            continue
        elif context == 4:
            print('\033[31m请登录或者注册后访问\033[0m')
            continue
        elif context == 5:
            print('\033[31m请登录或者注册后访问\033[0m')
            continue
        elif context == 6:
            print('\033[31m请登录或者注册后访问\033[0m')
            continue
        elif context == 7:
            print('\033[31m请登录或者注册后访问\033[0m')
            continue
        elif context == 8:
            quit()
        else:
            print('您输入的选项有误，请重新输入: ')

if __name__ == '__main__':
    main()