#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/14 22:48
# @Author  : Abel
# @File    : cn_blog.py
# @Software: PyCharm
# 用户登陆相关函数
import user_login
# 操作日志相关函数
import op_logs


def cn_blog_home_page(func_dict):
    """
    1. 打印cnblog可以提供的所有功能
    2. 根据用户用户输入的选择，返回该功能名
    :param func_dict: 一个字典格式的数据:内容为{"功能名", 功能所在方法的内存地址}
    :return: 功能的名字, 即func_dict的一个key 或者 False
    """
    print("欢迎来到博客园首页".center(80, "="))
    func_list_tmp = []
    # 将字典的key转换为元祖,格式为 (数字,"dict的key")
    for i in enumerate(func_dict):
        # 因为python数据为0开始， 所以i[0]+1示器显示为1开始
        print("%d: %s" % (i[0]+1, i[1]))
        # 将元祖加入到方法列表，获得所有的数字与方法名的对应关系，[(1,"dict的key"),(2,"dict的key")....]
        func_list_tmp.append(i)
    print("".center(89, "="))
    user_input = input("请输入[1-%d]选择功能:" % (len(func_list_tmp)))
    # 判断输入是否为纯数字
    if not user_input.isdigit():
        return False
    # 因之前i[0]+1， 所以现在需要将用户输入int(user_input)-1,才能匹配到正确的数据
    user_input = int(user_input)-1
    if user_input < len(func_list_tmp):
        # 根据用户输入,返回功能名,
        return func_list_tmp[user_input][1]
    else:
        return False


@user_login.login_index
@op_logs.log_record
def cn_blog_login(user_status):
    """
    登陆函数，用户用户登陆使用
    :param user_status: 用户登陆状态, 格式为:{"name": "user_name"},未登陆为{"name": ""}
    :return: True / False
    """
    # 判断是否已经登陆
    if user_status["name"]:
        print("".center(89, "="))
        return True
    else:
        print("".center(89, "="))
        return False


@user_login.login_index
@op_logs.log_record
def cn_blog_article(user_info):
    """
    文章页面
    :param user_info: 已登陆用户的信息格式为:{"name": "user_name"},未登陆为{"name": ""}
    :return:True
    """
    print("欢迎【{name}用户】访问【文章页面】".format(name=user_info["name"]))
    print("".center(89, "="))
    return True


@user_login.login_index
@op_logs.log_record
def cn_blog_diary(user_info):
    """
    日记页面
    :param user_info: 已登陆用户的信息格式为:{"name": "user_name"},未登陆为{"name": ""}
    :return: True
    """
    print("欢迎【{name}用户】访问【日记页面】".format(name=user_info["name"]))
    print("".center(89, "="))
    return True


@user_login.login_index
@op_logs.log_record
def cn_blog_comment(user_info):
    """
    评论页面
    :param user_info: 已登陆用户的信息格式为:{"name": "user_name"},未登陆为{"name": ""}
    :return: True
    """
    print("欢迎【{name}用户】访问【评论页面】".format(name=user_info["name"]))
    print("".center(89, "="))
    return True


@user_login.login_index
@op_logs.log_record
def cn_blog_collection(user_info):
    """
    收藏页面
    :param user_info: 已登陆用户的信息格式为:{"name": "user_name"},未登陆为{"name": ""}
    :return: True
    """
    print("欢迎【{name}用户】访问【收藏页面】".format(name=user_info["name"]))
    print("".center(89, "="))
    return True


# 用户注册不需要先登陆，所以不加载登陆使用的装饰器
@op_logs.log_record
def cn_blog_register(user_info):
    """
    用户注册页面
    :param user_info: 已登陆用户的信息格式为:{"name": "user_name"},未登陆为{"name": ""}
    :return: True
    """
    # 调用专用的注册函数
    return user_login.user_register(user_info)


@user_login.login_index
@op_logs.log_record
def cn_blog_logout(user_info):
    """
    用户注销页面
    :param user_info: 已登陆用户的信息格式为:{"name": "user_name"},未登陆为{"name": ""}
    :return: True
    """
    # 将全局的{"name": "user_name"}设置为{"name": ""}表示注销
    user_info["name"] = ""
    print("用户注销成功")
    return True


# 程序退出，不需要登陆就可以退出程序，所以不加载登陆装饰器
@op_logs.log_record
def cn_blog_exit(user_info):
    """
    用户退出页面, 添加上该函数，可以调用装饰器，记录用户退出时的操作
    :param user_info: 已登陆用户的信息格式为:{"name": "user_name"},未登陆为{"name": ""}
    :return: False
    """
    return False


if __name__ == '__main__':
    # 用户登陆状态
    login_status = {"name": ""}
    # 所有可用的方法,与方法的函数名
    cn_blog_func = {"登录": cn_blog_login,
                    "注册": cn_blog_register,
                    "文章页面": cn_blog_article,
                    "日记页面": cn_blog_diary,
                    "评论页面": cn_blog_comment,
                    "收藏页面": cn_blog_collection,
                    "注销": cn_blog_logout,
                    "退出程序": cn_blog_exit}

    # 程序运行状态
    running_state = True

    while running_state:
        func = cn_blog_home_page(cn_blog_func)
        if func == "退出程序":
            # 将运行状态 running_state修改为False,退出循环
            running_state = cn_blog_func[func](login_status)
            print("退出成功")
        elif func:
            # func有值的话，说明用户输入没有问题,所以调用相应函数
            cn_blog_func[func](login_status)
        else:
            # 用户输入有误, 可能输入的不是数字，或者输入的数字没有对应的功能
            print("没有这个选项")
