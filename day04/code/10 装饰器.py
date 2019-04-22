#
# def yue():
#     print("我要约个人出来吃饭")
#
# def wen(fn): # fn => yue
#     def inner():
#         print("问问alex....") # 执行目标函数之前
#         fn()  #  yue()  # 执行目标函数
#     return inner
#
# #yue => inner
# yue = wen(yue)
# yue() # => inner()
#
# yue()
# yue()
# yue()





#
# def kaiGua(fn): # 记录一下你要开挂的游戏 -> 目标函数
#     def inner():
#         print("开外挂")
#         fn()  # 正常玩游戏
#         print("关闭外挂")
#     return inner
#
# @kaiGua  #语法糖  => dnf = kaigua(dnf)
# def dnf():
#     print("我要打DNF")
#
# @kaiGua # lol = kaiGua(lol)
# def lol():
#     print("我要玩儿LOL")
#
# dnf()
# lol() #  inner






def kaiGua(fn): # 记录一下你要开挂的游戏 -> 目标函数
    def inner(*args, **kwargs): # 为了给目标函数传递参数  *,**  聚合
        print("开外挂")
        ret = fn(*args, **kwargs)  # *,** 打散
        print("关闭外挂")
        return ret
    return inner

# @kaiGua  #语法糖  => dnf = kaigua(dnf)

@kaiGua
def dnf(uname, upwd):
    print("我要打DNF", uname, upwd)
    return "流光星陨刀"


# inner() takes 0 positional arguments but 2 were given
ret = dnf("alex", "10086") # inner()
print(ret)


















