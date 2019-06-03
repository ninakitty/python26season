
# try:
# #     # print(1/0) # ZeroDivisionError
# #     # dic = {}
# #     # print(dic["jay"]) # KeyError
# #     # lst = []
# #     # print(lst[10086]) # IndexError
# #     # for i in 123:
# #         print("哈哈哈")
# # except ZeroDivisionError:
# #     print("1/0")
# # except KeyError:
# #     print("键错了")
# # except IndexError:
# #     print("索引错误")
# # except Exception:  # 放在最后, 收尾
# #     print("我是全能的")
# # finally: # 最后的
# #     print("最后都要执行者个代码")


# import traceback  # 可以看见堆栈信息
#
# try:
#     print(1/0)
# except Exception:
#     print("报错了")
#     print(traceback.format_exc()) # 错误信息
#     # 程序员更希望直到哪里错了错误




# # 自定义异常
# class JackException(Exception):
#     pass
#
#
# def func(a, b):
#     """
#     计算a+b的结果
#     :param a: 必须是数字
#     :param b: 必须是数字
#     :return:  和
#     """
#     if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
#         return a + b
#     else:
#         # 报错
#         raise JackException('a和b的数据类型不对')
#
# func("a", 12)
