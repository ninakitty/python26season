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

login_status = {'flag': 0}#记录用户的登录状态

nav = {'1' : '请登陆', '2' : '请注册', '3' : '文章页面', '4' : '日记页面',
       '5' : '评论页面', '6' : '收藏页面', '7' : '注销', '8' : '退出程序'}

#定义文件提取和转换函数
def txt_switch(txt):#文件提取文本后，转换成列表
    f = open(txt,mode='r',encoding='utf-8')
    f_list = []#将文本都每一行存储此列表中
    for line in f:
        f_list.append(line.strip().split(','))
    list_name = f_list.pop(0)#取出列名，将列名和明细进行分离
    return list_name, f_list
    f.close()

#执行登录操作
def login_action(max_login = 3):#默认最大登录次数为3
        login_times = 0
        while login_times <= max_login:
            username = input('请输入用户名(liusl)：')
            password = input('请输入密码(123456)：')
            if login(username, password):
                break
            else:
                login_times += 1
        else:
            exit()

#登录函数
def login(username, password):
    list_name, list_item = txt_switch('register')#将文本文件中的用户名和密码渠道内存中
    for i in list_item:
        if username == i[1] and password == i[2]:
            login_status['flag'] = 1  # 更新登录状态信息
            login_status['username'] = username  # 更新登录状态信息，存储当前登录用户名
            print('登录成功！')
            return True
            break
    else:
        print('登陆失败！')
        return False

#判断登录状态函数
def login_state(page_content):
    def inner(*args, **kwargs):
        if login_status['flag'] == 0:
            login_action()
        ret = page_content(*args, **kwargs)
        return ret
    return inner

#注销函数
def logout():
    login_status['flag'] = 0

#注册函数
def register():
    list_name, list_item = txt_switch('register')#将文本文件中的用户名和密码渠道内存中
    username_list = []
    for i in list_item:
        username_list.append(i[1])
    while True:
        username = input('请输入用户名：')
        if username in username_list:
            print('用户名已存在，请重新输入！')
            continue
        else:
            password = input('请输入密码：')
            break
    with open('register', 'a', encoding='utf-8') as register:
        register.write('\n' + str(int(list_item[-1][0])+1) + ',' + username  + ',' + password)
    return username, password

#日志函数
import time
def log(page_content):
    def inner(*args, **kwargs):
        ret = page_content(*args, **kwargs)
        with open('log', 'a', encoding='utf-8') as logging:
            logging.write(login_status['username'] + ' 在 ' + time.strftime('%Y %m %d %H:%M:%S') + ' 执行了 ' + '%s函数'% page_content.__name__ + '\n')
        return ret
    return inner

#页面显示内容函数
@login_state
@log
def page_content(page_num):
    print('欢迎%s访问评论%s'% (login_status['username'],nav[page_num]))

#首页
print('欢迎登录博客园首页')
for key, value in nav.items():
    print(key + ':' + value)

while True:
    page_num = input('请输入访问的页面序号:')
    if page_num.isdigit():
        if int(page_num) in range(1,9):
            if page_num == '1':
                login_action()
                continue
            elif page_num == '2':
                username, password = register()
                login(username, password)
                continue
            elif page_num == '7':
                logout()
                continue
            elif page_num == '8':
                break
            else:
                page_content(page_num)
        else:
            print('输入页面序号错误请重新输入')
            continue
    else:
        print('输入页面序号错误请重新输入')
        continue














