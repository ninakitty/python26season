# ---------给装饰器传递参数
# def wrapper_out(flag):
#     def wrapper(fn):
#         def inner(*args, **kwargs):
#             if flag:
#                 print('function front')
#                 result = fn(*args, **kwargs)
#                 print('function after')
#             else:
#                 result = fn(*args, **kwargs)
#             return result
#
#         return inner
#
#     return wrapper
# @wrapper_out(1)
# def fun1():
#     print('fun1')
# @wrapper_out(0)
# def fun2():
#     print('fun2')
#
# fun1()
# fun2()

# -------分别放置日志
# def wrapper_out(filename):
#     def log(fn):
#         def inner(*args, **kwargs):
#             ret = fn(*args, **kwargs)
#             with open(filename, mode='a', encoding='utf8') as file:
#                 file.write(filename + ',' )
#             return ret
#
#         return inner
#
#     return log
#
#
# @wrapper_out('func1')
# def func1():  # 日志放在func1.txt
#     print("我是func1")
#
#
# @wrapper_out('func2')
# def func2():  # 日志放在func2.txt
#     print("我是func2")
#
#
# func1()
# func2()

# -------统计列表中"周杰伦出现的次数"----counter计数器
# import collections
#
# #
# # lst = ['周杰伦', '周杰伦', '周杰伦', '周杰伦', 1, 2, 3]
# # c = collections.Counter(lst)
# # print(c.get('周杰伦'))
#
# # ------默认值-----defaultdict(函数或None)
# d = collections.defaultdict(lambda :10)
# d['aa'] = 10
# print(d)
# print(d['bb'])
# print(d)

# 时间转换 strftime \strftime
# import time

# time_stamp = time.time()  # 时间戳
# struct_time = time.localtime()  # 结构化时间
# # 时间戳-->结构化时间-->字符串时间
# str_time = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
# print(time_stamp)
# print(struct_time)
# print(str_time)
#
# #字符串时间-->结构化时间-->时间戳
# str='2018-12-21 15:20:14'#字符串时间
# struct_time2=time.strptime(str,'%Y-%m-%d %H:%M:%S')#结构化时间
# time_stamp2=time.mktime(struct_time2)
# print(str)
# print(struct_time2)
# print(time_stamp2)
# # 时间相差
# def strtime_to_timestamp(strtime):
#     strtime = time.strptime(strtime, '%Y-%m-%d %H:%M:%S')
#     strtime = time.mktime(strtime)
#     return strtime
#
#
# def timestamp_to_strtime(timestamp):
#     timestamp = time.localtime(timestamp)
#     timestamp=time.strftime('%Y-%m-%d %H:%M:%S',timestamp)
#
#     return timestamp
#
#
# s1 = "1989-01-01 12:00:00"
# s2 = "1989-01-02 14:35:00"
#
# result = strtime_to_timestamp(s2) - strtime_to_timestamp(s1)
# minute=result//60
# display_hour=minute//60
# display_min=minute%60
# print(display_hour,display_min)

# 26小时35分钟

# pickle
# import pickle
#
# lst = ['tea', 'juice', 'coffee']
# bs = pickle.dumps(lst)  # list转换为字节码
# print(bs)
# bs2 = b'\x80\x03]q\x00(X\x03\x00\x00\x00teaq\x01X\x05\x00\x00\x00juiceq\x02X\x06\x00\x00\x00coffeeq\x03e.'
# lst1 = pickle.loads(bs2)  # 字符码转换回list
# print(lst1)


# json
# import json
#
# dic = {'name': 'tome', 'age': 20, 'gender': 'female'}
# dic1 = {'name': 'tome1', 'age': 201, 'gender': 'female1'}
# json_str = json.dumps(dic)  # dic to json_str
# print(json_str)
# print(type(json_str))
#
# json_str1 = '{"name": "tome", "age": 20, "gender": "female"}'
# dic1 = json.loads(json_str1)  # json_str to dic
# print(dic1)
# print(type(dic1))

# 练习1: 匹配一个邮箱 homexue@126.com   448910663@qq.com
# 练习2: <span><div>fdsafasdfasdfsda</div></span>
actors = "西尔维斯特&middot;史泰龙 Sylvester Stallone <br />\u3000\u3000\u3000\u3000\u3000\u3000黄晓明 Xiaoming Huang <br />\u3000\u3000\u3000\u3000\u3000\u3000戴夫&middot;巴蒂斯塔 Dave Bautista <br />\u3000\u3000\u3000\u3000\u3000\u3000杰西&middot;麦特卡尔菲 Jesse Metcalfe <br />\u3000\u3000\u3000\u3000\u3000\u300050分 50 Cent <br />\u3000\u3000\u3000\u3000\u3000\u3000约翰&middot;威斯利&middot;查特曼 John Wesley Chatham <br />\u3000\u3000\u3000\u3000\u3000\u3000唐辰瀛 Chen Tang <br />\u3000\u3000\u3000\u3000\u3000\u3000泰伦&middot;伍德利 Tyron Woodley <br />\u3000\u3000\u3000\u3000\u3000\u3000泰勒&middot;乔恩&middot;奥尔森 Tyler Jon Olson <br />\u3000\u3000\u3000\u3000\u3000\u3000提图斯&middot;维里沃 Titus Welliver <br />\u3000\u3000\u3000\u3000\u3000\u3000谢伊&middot;巴克纳 Shea Buckner <br />\u3000\u3000\u3000\u3000\u3000\u3000杰米&middot;金 Jaime King <br />\u3000\u3000\u3000\u3000\u3000\u3000丽迪雅&middot;赫尔 Lydia Hull <br />\u3000\u3000\u3000\u3000\u3000\u3000阿什利&middot;库萨托 Ashley Cusato <br />\u3000\u3000\u3000\u3000\u3000\u3000罗旖凡 Yifan Luo <br />\u3000\u3000\u3000\u3000\u3000\u3000罗温&middot;布赛义德 Rowan Bousaid <br />\u3000\u3000\u3000\u3000\u3000\u3000贝莉&middot;柯伦 Baylee Curran <br />\u3000\u3000\u3000\u3000\u3000\u3000泽科&middot;扎基 Zeeko Zaki <br />\u3000\u3000\u3000\u3000\u3000\u3000文森特&middot;杨 Vincent Young <br />\u3000\u3000\u3000\u3000\u3000\u3000埃里克&middot;纽纳姆 Eric Newnham <br />\u3000\u3000\u3000\u3000\u3000\u3000马克&middot;希克斯 Mark Hicks <br />\u3000\u3000\u3000\u3000\u3000\u3000彼特&middot;温兹 Peter Wentz <br />\u3000\u3000\u3000\u3000\u3000\u3000奚梦瑶 Ming Xi <br />\u3000\u3000\u3000\u3000\u3000\u3000罗曼&middot;米蒂齐扬 Roman Mitichyan <br />\u3000\u3000\u3000\u3000\u3000\u3000戈登&middot;迈克尔斯 Gordon Michaels <br />\u3000\u3000\u3000\u3000\u3000\u3000婕咪&middot;埃迪 Jamie Eddy <br />\u3000\u3000\u3000\u3000\u3000\u3000约瑟夫&middot;布莱克&middot;门泽尔 Joseph Blake Menzel <br />\u3000\u3000\u3000\u3000\u3000\u3000乔&middot;吉尔希翁 Joe Gelchion <br />\u3000\u3000\u3000\u3000\u3000\u3000阿方索&middot;A&middot;杰克逊 Alphonso A'Qen-Aten Jackson <br />\u3000\u3000\u3000\u3000\u3000\u3000奥罗拉&middot;卡琳 Aurora Karine <br />\u3000\u3000\u3000\u3000\u3000\u3000德方塔&middot;弗里曼 Devonta Freeman <br />\u3000\u3000\u3000\u3000\u3000\u3000科里&middot;温斯顿 Corey Winston <br />\u3000\u3000\u3000\u3000\u3000\u3000佩里&middot;约翰逊 Perry Johnson <br />\u3000\u3000\u3000\u3000\u3000\u3000麦克&middot;里德 Mike Leeder <br />\u3000\u3000\u3000\u3000\u3000\u3000瑞恩&middot;牛顿 Ryan Newton <br />\u3000\u3000\u3000\u3000\u3000\u3000蒂莫西&middot;米勒 Timothy Miller <br />\u3000\u3000\u3000\u3000\u3000\u3000埃里克&middot;本德罗斯 Eric Bendross <br />\u3000\u3000\u3000\u3000\u3000\u3000德里克&middot;瑞安&middot;杜克 Derek Ryan Duke <br />\u3000\u3000\u3000\u3000\u3000\u3000大卫&middot;邓斯顿 David Dunston <br />\u3000\u3000\u3000\u3000\u3000\u3000J&middot;麦克罗伊 J. Mcleroy"
temp=actors.split('\u3000\u3000\u3000\u3000\u3000\u3000')
print(temp)