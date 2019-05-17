# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 22:48
# @Author  : 张杨
# @Email   : 1064586684@qq.com
# @File    : day03_homework.py
# @Software: PyCharm

import os
#变量定义
fil_nam1 = 'C:\\study\\python\\train\\20180902\\employee_info'
lst = ['id', 'name', 'age', 'phone', 'job']
#操作语句
opr_sta1 = input('请输入操作语句：').strip()



#where条件拆分处理
def whr_fun(whr, fld, **dic) :
    if '=' in whr :
        whr_lst = whr.split('=')
        return (dic[fld].strip() == whr_lst[1].strip())
    elif '>' in whr :
        whr_lst = whr.split('>')
        return (int(dic[fld].strip()) > int(whr_lst[1].strip()))
    elif '<' in whr :
        whr_lst = whr.split('<')
        return (int(dic[fld].strip()) < int(whr_lst[1].strip()))
    elif 'like' in whr :
        whr_lst = whr.split('like')
        return ((whr_lst[1].strip()) in (str(dic[fld].strip())))



#文件操作函数
def fil_sel(fil_nam, opr_sta, *lst1) :
    whr_sta = opr_sta.split('where')
    opr_mod = opr_sta.split()[0]
    if '*' in whr_sta[0]:
        sel_fld = lst1
    else :
        sel_fld = whr_sta[0].split(opr_mod)[1].split(',')
    print(sel_fld)


    with open(fil_nam, mode='r', encoding='utf-8') as f1, \
    open(fil_nam + '.bak', mode='w', encoding='utf-8') as f2:
        for line in f1:
            val_lst = line.strip().split(',')
            dic1 =dict(zip(lst1,val_lst))
            #print(dic1)
            for i in lst1 :
                if i in whr_sta[1].strip() :
                    whr_rst1 = whr_fun(whr_sta[1].strip(), str(i), **dic1)
                    print(whr_sta[1].strip(),whr_rst1)
                    if whr_rst1 :
                        if i not in sel_fld :
                            val_lst.remove(dic1[i])
                            print(val_lst)
                    else:
                        continue
            f2.write(','.join(val_lst)+'\n')

fil_sel(fil_nam1, opr_sta1, *lst)