#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/15 2:39
# @Author  : Abel
# @File    : op_logs.py
# @Software: PyCharm
import time
# 当前日期 年-月-日
now_time = time.strftime("%Y-%m-%d")


def log_write_to_file(msg):
    """
    日志写入文件内.
    :param msg: 一个字符串格式的数据
    :return:
    """
    with open("cn_blog_log", "a", encoding="utf-8") as user_file:
        user_file.write("%s\n" % msg)
        user_file.close()
    return True


def log_record(func):
    def inner(*args, **kwargs):
        # 获取函数名，在ret = func(*args, **kwargs)之前，否则获取到的函数名为inner
        func_name = func.__name__  # func.__name__所调用的函数的函数名
        # 获取已登陆用户的用户名
        name = args[0]["name"]
        ret = func(*args, **kwargs)
        # 如果调用的注册函数则在函数执行后重新获取用户名，否则用户注册后自动登陆登陆的日志内用户将获取为空
        if func_name == "cn_blog_register":
            name = args[0]["name"]
        msg = "用户:【{name}】\t【{datetime}】\t执行了【{func_name}】函数".format(name=name,
                                                                     datetime=now_time,
                                                                     func_name=func_name)
        if ret:
            # 函数执行成功(True)，才将操作写入日志文件,比如未登陆用户退出程序，不记录日志，已登陆用户退出则记录日志
            log_write_to_file(msg)
        return ret
    return inner
