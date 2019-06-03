import logging

# filename: ⽂件名
# format: 数据的格式化输出. 最终在⽇志⽂件中的样⼦
# 时间-名称-级别-模块: 错误信息
# datefmt: 时间的格式
# level: 错误的级别权重, 当错误的级别权重⼤于等于leval的时候才会写⼊⽂件
# Root
# logging.basicConfig(filename='x1.txt',
#                     format='%(asctime)s - %(name)s -%(levelname)s -%(module)s: %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     level=10) # 当前配置表示 10以上的分数会被写⼊⽂件
#
#
# logging.critical("报错了") # 最高级别   50
# logging.error("报错了") # 40
# logging.warning("警告") # 30 警告
# logging.info("信息") # 20 正常信息
# logging.debug("调错") # 10
#
# logging.log(9999, "地球炸了")


# 多日志文件
# 创建⼀个操作⽇志的对象logger（依赖FileHandler）
file_handler = logging.FileHandler('l1.log', 'a', encoding='utf-8')
file_handler.setFormatter(logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s: %(message)s"))

logger1 = logging.Logger('德玛西亚', level=logging.ERROR)
logger1.addHandler(file_handler)

# logger1就可以了
logger1.error("错了么? 错了")
logger1.error("错了么? 错了")
logger1.error("错了么? 错了")
logger1.error("错了么? 错了")
logger1.error("错了么? 错了")


# 再创建⼀个操作⽇志的对象logger（依赖FileHandler）
file_handler2 = logging.FileHandler('l2.log', 'a', encoding='utf-8')
file_handler2.setFormatter(logging.Formatter(
    fmt="%(asctime)s - %(name)s -%(levelname)s -%(module)s: %(message)s"))

logger2 = logging.Logger('皮城', level=logging.ERROR)
logger2.addHandler(file_handler2)


logger2.error("没错, 没错")
logger2.error("没错, 没错")
logger2.error("没错, 没错")
logger2.error("没错, 没错")
logger2.error("没错, 没错")
logger2.error("没错, 没错")
logger2.error("没错, 没错")

