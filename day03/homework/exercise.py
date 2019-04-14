# 1、 文件a1.txt内容
# 序号 部门 人数 平均年龄 备注
# 1 python 30 26 单身狗
# 2 Linux 26 30 没对象
# 3 运营部 20 24 女生多
# .......
# 通过代码，将其构建成这种数据类型：
# [{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'备注':'单身狗'},......]
lst = []  # 定义要求所需列表
with open('a1.txt', mode='r', encoding='utf8') as file:  # 打开文件,只读模式,编码使用utf8
    titleLine = file.readline().strip().split(' ')  # 读取第一行内容做为标题,去除两端空白,将使用空格分割
    for line in file:  # 继续读取剩余内容
        dic = {}  # 定义临时存储字典
        content = line.strip().split(' ')  # 将每行内容去除两端空白,用空格分割
        for index in range(len(content)):  # 按照内容长度,索引循环
            dic[titleLine[index]] = content[index]  # 将每项内容与标题加入字典
        lst.append(dic)  # 将临时存储字典放入列表
print(lst)


# 2、 传入函数的字符串中,[数字]、[字母]、[空格] 以及 [其他]的个数，并返回结果。
def count_input(input_str):  # 定义计算字符串内容函数
    count_num = 0  # 计数数字
    count_alpha = 0  # 计数字母
    count_space = 0  # 计数空白
    count_other = 0  # 计数其他
    for char in input_str:
        if char.isdigit():
            count_num += 1
        elif char.isalpha():
            count_alpha += 1
        elif char.isspace():
            count_space += 1
        else:
            count_other += 1
    return {'num': count_num, 'alpha': count_alpha,
            'space': count_space, 'other': count_other}


print(count_input('12 3 qwe$中文'))


# 3、 写函数，接收两个数字参数，返回比较大的那个数字。
def compare(num1, num2):
    return num1 if num1 > num2 else num2


print(compare(21, 2))


# 4、 写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容
# 返回给调用者。
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# PS:字典中的value只能是字符串或列表

def check_len(in_dic):
    dic = {}
    if isinstance(in_dic, dict):
        for key, value in in_dic.items():
            if isinstance(value, str) or isinstance(value, list):
                dic[key] = value[:2]
            else:
                return '字典中的值不是"字符串"或"列表"'
        return dic
    return '请将参数更改为字典'


print(check_len({1: "12221", 2: [1,2, 3, 4]}))
