
flag = False # 没登录
def login():
    global flag
    uname = input("请输入用户名:")
    upwd = input("请输入密码:")
    if uname == "alex" and upwd =="123":
        print("登录成功")
        flag = True
    else:
        print("登录失败")
        flag = False


def login_verify(fn):
    def inner(*args, **kwargs):
        while 1:
            if flag:  # 如果登录成功
                ret = fn(*args, **kwargs)
                return ret
            else:
                # 没登录
                login()

    return inner


def munu():
    print("我是菜单")

def read():
    print("读tiezi")

@login_verify
def fatie():
    print("发帖")

@login_verify
def shou():
    print("收藏")