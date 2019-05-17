'''
博客园需求
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

import logging.config,time,os       #导入日志配置
LOG_PATH="access.log"       #定义日志路径
stand_format="[%(name)s][%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d][%(levelname)s][%(message)s]"        #定日日志格式
LOGGING_DIC={
    "version":1,
    "disable_existing_loggers": False,
    "formatters":{
        "stand":{
            "format":stand_format,
        },
    },
    "filters":{},
    "handlers":{
        "default":{
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'stand',
            'filename': LOG_PATH,
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'encoding': 'utf-8',
        },
    },
    "loggers":{
        "":{
            "handlers":["default"],
            "level":"DEBUG",
            "propagate":False,
        }
    }
}           #定日logging.config配置
DB_PATH="register"          #定义用户配置
login_tag=False             #定义用户登陆的属性
usercheck=[]                #用户tocken
userregister=[]             #用户注册记录
text_dic={
    "1": {"文章1":"文章1的内容"},
    "2": {"文章2": "文章2的内容"},
    "3": {"文章3": "文章3的内容"},
    "4": {"文章4": "文章4的内容"},
    "5": {"文章5": "文章5的内容"},
}               #文章字典
diary_dic={
    "1": {"日记1":"日记1的内容"},
    "2": {"日记2": "日记2的内容"},
    "3": {"日记3": "日记3的内容"},
    "4": {"日记4": "日记4的内容"},
    "5": {"日记5": "日记5的内容"},
}               #日记字典
text_comment=[]             #文章内容评论
diary_comment=[]            #日记内容评论
desktop={
    "1": "登录",
    "2": "注册",
    "3": "文章页面",
    "4": "日记页面",
    "5": "评论页面",
    "6": "收藏页面",
    "7": "注销",
    "8": "退出程序",
}               #首页字典
favorite_list=[]             #用户收藏字典

def get_logger(name):
    '''
    定义日志logger获取
    :param name:
    :return:
    '''
    logging.config.dictConfig(LOGGING_DIC)      #生效logging字典配置
    log=logging.getLogger(name)                 #初始化logger
    return log                                 #返回初始化的logger

def history_log(func):                                      #定义日志记录装饰器
    def inner(*args,**kwargs):
        logname = get_logger(func.__name__)                 # 将函数名称传入之logger，作为Logger的名字
        name=func.__name__                                  #获取记录日志的函数名称
        if name == "login":                                 #定义login函数的登陆记录，login函数登陆前是收集不到用户的，所以先运行函数在记录日志，如果登陆失败则记录为游客登陆
            ret = func(*args, **kwargs)
            if len(usercheck) != 0:
                logname.info(f"{usercheck[0]} 使用了函数{name}")
            else:
                logname.info(f"游客记录")
        elif name == "register":                            #定义register函数的日志记录，register函数登陆前是收集不到用户的，所以先运行函数在记录日志，如果注册失败则记录为游客登陆
            ret = func(*args, **kwargs)
            if len(userregister) != 0:
                logname.info(f"{userregister[0]} 使用了函数{func.__name__}")
                userregister.clear()                           #用户注册的使用在注册成功后就清空掉临时的用户注册记录列表，该列表主要用来记录日志时那个用户进行了注册
            else:
                logname.info(f"游客记录")
        elif name == "cancel_login":                        #定义cancel_login注销函数记录，如果未登陆该函数回报错，用户无法获取，纪录为游客登陆，如果用户存在则正常记录日志
            if len(usercheck) != 0:
                logname.info(f'{usercheck[0]} 使用了函数{name}')
            else:
                logname.info(f"游客记录")
            ret=func(*args,**kwargs)
        else:
            logname.info(f'{usercheck[0]} 使用了函数{name}')     #其他函数的日志记录
            ret = func(*args, **kwargs)
        return ret                                           #返回函数的返回值
    return inner

def show_top(dic=desktop):                                  #定义博客首页，返回用户的选择
    '''
    博客首页打印
    :param dic:
    :return:
    '''
    print("欢迎进入博客".center(20,"="))
    for k,v in desktop.items():
        print(k,v)
    choice=input("请选择>>:").strip()
    print()
    return choice

@history_log
def login():                    #定义用户登陆
    '''
    用户登陆
    :return:
    '''
    global login_tag            #用户登陆状态变量
    if login_tag:               #当用户登陆状态未True时禁止登陆
        print("请勿重复登陆")
        return False
    print("用户登陆".center(20,"="))
    for count in range(3):
        user=input("user>>:").strip()
        upwd=input("passwd>>:").strip()
        if os.path.isfile(DB_PATH) == False:
            db=open(DB_PATH,"wt")
            db.close()
        with open(DB_PATH, "rt", encoding="utf-8") as f1:
            for line in f1:
                data = line.strip().split(",")
                if data[0] == user and data[1] == upwd:
                    login_tag=True
                    print(f"\n\n恭喜用户{user}登陆成功")
                    usercheck.append(user)
                    return True         #登陆成功返回True，交由login_verify接收判断
            else:
                print("用户名或密码错误\n\n")
                login_tag=False         #如果登陆失败则返回假
    print("登陆超出限制，退出后重试")
    return False                        #如果登陆失败则返回假

def login_verify(func):                 #定义登陆装饰器
    '''
    登陆验证
    :return:
    '''
    def inner(*args,**kwargs):
        while True:
            if login_tag:               #如果登陆状态为真则正常运行函数
                ret=func(*args,**kwargs)
                return ret
            else:
                print("请先登陆商城")
                if login():continue     #该while循环实则就只有两个循环，当用户未登陆时，这里进行登陆，登陆函数返回值为True时，进行第二次循环正常运行函数，如果登陆函数返回false则直接退出
                break
    return inner

@history_log
def register():                          #定义用户注册函数
    if login_tag:                           #用户登陆后禁止注册
        print("已登陆，请注销后重试")
        return False
    print("用户注册".center(20,"="))
    for count in range(3):
        print("新用户注册")
        user=input("user>>:").strip()
        upwd=input("passwd>>:").strip()
        if user.isalnum() and upwd.isalnum():
            with open(DB_PATH,"rt",encoding="utf-8") as f1,open(DB_PATH,"at",encoding="utf-8") as f2:
                for line in f1:
                    data=line.strip().split(",")
                    if data[0] == user:
                        print("用户已存在\n")
                        break
                else:
                    print(f"恭喜用户注册成功：{user}，登陆密码：{upwd}")
                    f2.write(f"{user},{upwd}\n")
                    userregister.append(user)                               #用户注册成功，将用户注册名记录导用户注册列表中，在日志中记录
                    break
        else:
            print("用户名或密码格式错误，只能由字母数字组成\n")
    else:
        print("注册次数过多，请退出后再试\n")

@login_verify
@history_log
def text(dic=text_dic):                     #定义文章功能
    '''
    文章页面
    :return:
    '''
    print(f"欢迎用户{usercheck[0]}进入博客文章页面".center(20,"="))
    while True:
        for k in dic:
            for n,v in dic[k].items():
                print(k,n)
        choice=input("请输入查看的文章[q:退出]").strip()
        if choice in dic:
            for k,v in dic[choice].items():
                print(k.center(10,"="))
                print(v)
                print("\n")
                choice2=input("收藏(y)>>:").strip()
                if choice2 == "y" or choice2 == "Y":                    #同时定义收藏功能,不支持取消收藏，重复收藏会提示
                    if dic[choice] not in favorite_list:
                        favorite_list.append(dic[choice])
                        print(f"成功收藏文章{k}")
                    else:
                        print("该文章已收藏，勿重复添加")
        if choice == "q":
            print("退出文章页面...")
            break

@login_verify
@history_log
def diary(dic=diary_dic):                   #日志定义，与文章函数相同
    '''f
    日记页面
    :return:
    '''
    print(f"欢迎用户{usercheck[0]}进入博客日记页面".center(20,"="))
    while True:
        for k in dic:
            for n,v in dic[k].items():
                print(k,n)
        choice=input("请输入查看的日记[q:退出]").strip()
        if choice in dic:
            for k,v in dic[choice].items():
                print(k.center(10,"="))
                print(v)
                print("\n\n")
                choice2=input("收藏(y)>>:").strip()
                if choice2 == "y" or choice2 == "Y":
                    if dic[choice] not in favorite_list:
                        favorite_list.append(dic[choice])
                        print(f"成功收藏日记{k}")
                    else:
                        print("该日记已收藏，勿重复添加")
        if choice == "q":
            print("退出日记页面...")
            break


@login_verify
@history_log
def commen():                       #定义评论功能
    '''
    评论页面
    :return:
    '''
    tag=True
    print(f"欢迎用户{usercheck[0]}进入文章评论页面".center(20,"="))
    while tag:
        print("1、选择文章评论\n2、选择日记评论")
        choice=input("请选择评论内容[q:退出]>>:").strip()        #选择评论文章还是日志
        if choice == "1":
            while tag:
                for k in text_dic:                      #读文章字典并打印
                    for n, v in text_dic[k].items():
                        print(k, n)
                choice = input("选择要评论的文章[q:上一层,b:退出评论]").strip()        #接收要评论的文章
                if choice in text_dic:
                    for k, v in text_dic[choice].items():                       #打印文章内容
                        print(k.center(10, "="))
                        print(v)
                        print()
                        for text_ct in text_comment:                    #text_comment是文章评论的列表，text_ct是列表中的元素（字典）
                            for coment_user in text_ct:                 #text_ct是一个字典，key是用户名称
                                for text_index,comment_content in text_ct[coment_user].items():     #获取字典中用户对应的文章号和评论内容
                                    if choice == text_index:                #如果用户的选择==当前循环到的文章号则打印评论内容
                                        print(f"用户：{coment_user}\t\t评论：{comment_content}\t\t时间：{time.strftime('%Y-%m-%d %H:%M:%S')}")
                        print()
                        content=input("评论内容>>:").strip()        #获取用户评论内容
                        if content.isalnum():                       #评论必须又字符或数字组成
                            print("文章评论成功")
                            text_comment.append({usercheck[0]:{choice:content}})        #添加到文章评论列表中
                        else:
                            print("输入非法,评论只能包含字符和数字")
                elif choice == "q":
                    print("退出文章评论...")
                    break
                elif choice == "b":
                    print("退出评论")
                    tag=False
        elif choice == "2":                         #日记的评论与文章评论逻辑一致
            while tag:
                for k in diary_dic:
                    for n, v in diary_dic[k].items():
                        print(k, n)
                choice = input("选择要评论的日记[q:上一层,b:退出评论]").strip()
                if choice in diary_dic:
                    for k, v in diary_dic[choice].items():
                        print(k.center(10, "="))
                        print(v)
                        print()
                        for  diary_ct in diary_comment:
                            for coment_user in diary_ct:
                                for diary_index,comment_content in diary_ct[coment_user].items():
                                    if choice == diary_index:
                                        print(f"用户：{coment_user}\t\t评论：{comment_content}\t\t时间：{time.strftime('%Y-%m-%d %H:%M:%S')}")
                        print()
                        content=input("评论内容[q:上一层]>>:").strip()
                        if content.isalnum():
                            print("日记评论成功")
                            diary_comment.append({usercheck[0]:{choice:content}})
                        else:
                            print("输入非法,评论只能包含字符和数字")
                elif choice == "q":
                    print("退出日记评论...")
                    break
                elif choice == "b":
                    print("退出评论")
                    tag=False
        elif choice == "q":
            print("退出评论")
            break



@login_verify
@history_log
def favorite(f_list=favorite_list):             #打印收藏列表中的内容
    '''
    收藏文章
    :return:
    '''
    print(f"欢迎用户{usercheck[0]}进入收藏页面".center(20,"="))
    if len(f_list) < 1:
        print("收藏列表为空，请添加后查看")
        return False
    for i,dic in enumerate(f_list):
        for k,v in dic.items():
            print(str(i+1),k,v)
    print("\n\n")




@history_log
def cancel_login():             #注销函数，通过对用户登陆状态改为False来模拟注销，未登录不可以注销
    '''
    取消登陆
    :return:
    '''
    global login_tag
    if login_tag:
        usercheck.clear()
        login_tag=False
    else:
        print("账号未登录")

def main():         #整合函数
    '''
    函数整理
    :return:
    '''
    while True:
        user_choice=show_top()
        if user_choice in desktop:
            if user_choice == "1":
                login()
            elif user_choice == "2":
                register()
            elif user_choice == "3":
                text()
            elif user_choice == "4":
                diary()
            elif user_choice == "5":
                commen()
            elif user_choice == "6":
                favorite()
            elif user_choice == "7":
                cancel_login()
            else:
                print("退出博客.")
                exit()


main()

