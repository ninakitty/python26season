# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 22:48
# @Author  : 张杨
# @Email   : 1064586684@qq.com
# @File    : day03_homework.py
# @Software: PyCharm

import os
#变量定义
#需要增删改查的数据文件
fil_nam = 'C:\\study\\python\\train\\20180902\\employee_info'
bak_fil = 'C:\\study\\python\\train\\20180902\\employee_info.bak'
fil_siz = os.path.getsize(fil_nam)
#数据文件字段信息
lst = ['id', 'name', 'age', 'phone', 'job']
#操作语句，返回操作方式及where条件
opr_dic = {}
opr_sta = input('请输入操作语句：').strip()
opr_mod = opr_sta.split()[0].strip().lower()
whr_sta = opr_sta.split('where')
opr_dic[opr_mod] = whr_sta

#解析插入的字段，例如：
#插入：insert 5,maomao,22,13651054608,IT
def ist_fun(*lst1, **opr_dic1):
    ret_dic = {}
    if len(lst1) != opr_dic1['insert'][0].count(',') + 1:
        print('输入的insert语句字段值个数与文件字段个数不一致！例如:insert 5,maomao,22,13651054608,IT')
    ist_sta = opr_dic1['insert'][0].split('insert')
    ist_fld = ist_sta[1].split(',')
    ret_dic = dict(zip(lst1, ist_fld))
    print(ret_dic)
    return ret_dic

#解析查询的字段，例如：
#查询：select name, age where age>22
def sel_fun(*lst1, **opr_dic1):
    ret_dic = {}
    sel_dic = {}
    if '*' in opr_dic1['select'][0]:
        sel_fld = lst
    else :
        sel_fld = opr_dic1['select'][0].split('select')[1].split(',')
    ret_dic[opr_dic1['select'][1]] = sel_fld
    return ret_dic

#解析删除的字段，例如：
#删除：delete * where id = 5
def dlt_fun(*lst1, **opr_dic1):
    ret_dic = {}
    dlt_dic = {}
    if '*' not in opr_dic1.values()[0]:
        print('部分字段无法删除，只能删除整条记录！例如：delete * where id = 5')
    else:
        dlt_lst = opr_dic1.values()[1].strip().split('=')
        dlt_dic[dlt_lst[0]] = dlt_lst[1]
    ret_dic['delete'] = dlt_dic
    print(ret_dic)
    return ret_dic

#解析更新的字段，例如：
#更新：set name=MM where age>22
def set_fun(*lst1, **opr_dic1):
    ret_dic = {}
    upd_dic = {}
    if '=' not in opr_dic1['set'][0]:
        print('需要设置字段变更后的新值！例如：set 列名=新的值 where 条件')
    upd_lst = opr_dic1['set'][0].strip().split('set')[1].strip().split('=')
    ret_dic[upd_lst[0]] = upd_lst[1]
    print(ret_dic)
    return ret_dic


#where条件拆分处理
def whr_fun(whr, **dic) :
    if '=' in whr :
        whr_lst = whr.split('=')
        return (dic[whr_lst[0].strip()] == whr_lst[1].strip())
    elif '>' in whr :
        whr_lst = whr.split('>')
        return (int(dic[whr_lst[0].strip()]) > int(whr_lst[1].strip()))
    elif '<' in whr :
        whr_lst = whr.split('<')
        return (int(dic[whr_lst[0].strip()]) < int(whr_lst[1].strip()))
    elif 'like' in whr :
        whr_lst = whr.split('like')
        return (str(whr_lst[1].strip()) in (str(dic[whr_lst[0].strip()])))

#查询操作函数
def fil_opr(fil_nam1, *lst2, **opr_dic2) :
    ret_dic1 = {}
    #插入新纪录
    if 'insert' in opr_dic2.keys() :
        with open(fil_nam1, mode='a', encoding='utf-8') as f1:
            ret_dic1 = ist_fun(*lst2, **opr_dic2)
            if fil_siz == 0 :
                ret_dic1.values()[0] = 1
                new_lin = ','.join(ret_dic1.values()).strip()
                f1.write(new_lin)
            else:
                new_lin = ','.join(ret_dic1.values()).strip()
                f1.write('\n' + new_lin)
    #查询满足where条件的语句
    elif 'select' in opr_dic2.keys() :
        if fil_siz == 0 :
            print('没有内容可供查询!')
        else:
            ret_dic1 = sel_fun(*lst2, **opr_dic2)
            val_lst1 = []
            with open(fil_nam1, mode='r', encoding='utf-8') as f2:
                for line in f2 :
                    val_lst = line.strip().split(',')
                    lin_dic1 = dict(zip(lst2, val_lst))
                    whr_rst = whr_fun(opr_dic2['select'][1], **lin_dic1)
                    if whr_rst :
                        for fld in ret_dic1[opr_dic2['select'][1]]:
                            val_lst1.append(lin_dic1[fld.strip()])
                    else:
                        continue
                print(val_lst1)
    #删除满足where条件的记录
    elif 'delete' in opr_dic2.keys() :
        if fil_siz == 0 :
            print('无内容可删除!')
        else:
            with open(fil_nam1, mode = 'r', encoding='utf-8') as f3,\
                    open(bak_fil, mode='w', encoding='utf-8') as f4 :
                for line in f3 :
                    val_lst2 = line.strip().split(',')
                    lin_dic2 = dict(zip(lst2, val_lst2))
                    whr_rst2 = whr_fun(opr_dic2['delete'][1], **lin_dic2)
                    if not whr_rst2 :
                        f4.write(line)
                        print(line)
            os.remove(fil_nam1)
            os.rename(bak_fil, fil_nam1)
    #更新满足条件的记录
    elif 'set' in opr_dic2.keys() :
        ret_dic3 = set_fun(*lst2, **opr_dic2)
        if fil_siz == 0 :
            print('无内容可更新!')
        else:
            with open(fil_nam1, mode = 'r', encoding='utf-8') as f5,\
                    open(bak_fil, mode='w', encoding='utf-8') as f6 :
                for line in f5 :
                    val_lst3= line.strip().split(',')
                    lin_dic3 = dict(zip(lst2, val_lst3))
                    whr_rst3 = whr_fun(opr_dic2['set'][1].strip(), **lin_dic3)
                    print(ret_dic3.keys())
                    if not whr_rst3 :
                        f6.write(line)
                    else:
                        for fld in lst2 :
                            if fld in ret_dic3.keys() :
                                lin_dic3[fld] = ret_dic3[fld]
                            else:
                                continue
                        line1 = ','.join(lin_dic3.values())
                        f6.write(line1)
                        print(line1)
            os.remove(fil_nam1)
            os.rename(bak_fil, fil_nam1)




fil_opr(fil_nam, *lst, **opr_dic)