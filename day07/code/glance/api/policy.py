
# 用一下cmd里面的功能
# 包的绝对路径:
# sys.path  -> 启动文件
# 我们用这个多
# from glance.cmd import manage

# 相对导入 , 第三方开源框架
# 不允许离开这个包
#  attempted relative import beyond top-level package
from ..cmd import manage

def func():
    print("我是policy")
    manage.func()
func()
