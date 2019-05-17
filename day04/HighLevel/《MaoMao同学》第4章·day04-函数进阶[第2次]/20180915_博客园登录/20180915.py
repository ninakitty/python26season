# -*- coding: utf-8 -*-
# @Time    : 2018/9/15 12:11
# @Author  : 张杨
# @Email   : 1064586684@qq.com
# @File    : 20180915.py
# @Software: PyCharm

import os
import time

#变量定义
logged = False
fil_nam = 'C:\\study\\python\\train\\20180915\\register'
log_nam = 'C:\\study\\python\\train\\20180915\\log'
fil_siz = os.path.getsize(fil_nam)


def rgt_fun(usr_nam) :
    rgt_flg = False
    if fil_siz == 0 :
        print('注册文件为空，请初始化一份用户登陆信息！')
    else:
        with open(fil_nam, mode = 'r', encoding = 'utf-8') as f1 :
            for line in f1 :
                usr_pwd_lst = line.split(',')
                if usr_nam == usr_pwd_lst[0].strip() :
                    rgt_flg = True
                    return usr_pwd_lst[1].strip()
                    break
                else:
                    continue
            if rgt_flg == False :
                print('该账号不存在，请确认账号是否正确。如没有账号请注册！')

def wrt_log(log_inf) :
    with open(log_nam, mode = 'a', encoding = 'utf-8') as f2 :
        print(log_inf)
        f2.write(log_inf)

def logon_fun() :
    logged = False
    if not logged:
        cnt = 3
        for i in range(cnt):
            usr = input('请输入用户名：').strip()
            pwd = input('请输入密码：').strip()
            rgt_pwd = rgt_fun(usr)
            if rgt_pwd == pwd:
                logged = True
                return usr
                break
            else:
                cnt -= 1
                print('密码不正确，请重新输入，您还有%s次重试机会！'%cnt)
                continue

def wrapper(fun) :

    def inner(*args, **kwargs) :
        print ('欢迎登陆博客园')
        usr1 = logon_fun()
        log_rcd = '欢迎%s用户在%s执行了%s函数' % (usr1, time.strftime('%Y-%m-%d %H:%M:%S'), fun.__name__)
        wrt_log(log_rcd+'\n')
        ret = fun(usr1, *args, **kwargs)
        return ret
    return inner()

@wrapper#fun1=wrapper(fun1)
def fun1(usr2) :
    log_ctt = int(input('请选择需要登录的页面(3:文章页面，4:日记页面，5:评论页面，6:收藏页面):'))
    if log_ctt == 3 :
        print('欢迎%s用户访问文章页面'%usr2)
    elif log_ctt == 4 :
        print('欢迎%s用户访问日志页面'%usr2)
    elif log_ctt == 5:
        print('欢迎%s用户访问评论页面' % usr2)
    elif log_ctt == 6:
        print('欢迎%s用户访问收藏页面' % usr2)


