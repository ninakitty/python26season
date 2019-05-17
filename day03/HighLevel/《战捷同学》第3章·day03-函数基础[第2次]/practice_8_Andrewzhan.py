#!/usr/bin/env python
# -*- encoding:utf-8 -*-
# Author: Andrew.zhan
# Create by 2019 Apr 15

import shutil


def practice_8():
    '''
    写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作。
    读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
    a = 10
    b = 20
    def test5(a,b):
        print(a,b)
    c = test5(b,a)
    print(c)

    ---------------------
    答:
    代码会输出
    20 10
    None
    全局名称空间的a=10, b=20 传递给test5这个函数(b,a). test5内的局部名称空间中a获得的是外部传进来的20, b获得的是外部传进来的10.
    print(a,b)时,调用的是局部空间内的变量.所以输出为20,10
    由于函数没有返回值,所以print(c)的值为None
    '''
    # 这里补一下函数. 上一个文件写完简答忘了写这个函数了.
    # 快速写一下了. 主要是把知识点过一下.
    file_name = input("请输入文件名: ").strip()
    print("请输入要替换的内容.")
    source = input("原: ")
    replaced = input("替换为: ")
    tmp_file_name = ".%s.tmp" % file_name
    with open(file_name, 'r', encoding="utf-8") as fp, open(tmp_file_name, "w", encoding="utf-8") as tmp_fp:
        for line in fp:
            tmp_fp.write(line.replace(source, replaced))
    # 也可以用os的remove再rename. 但是需要两行代码了.
    shutil.move(tmp_file_name, file_name)


if __name__ == "__main__":
    '''
    先创建了个文件8.txt 里面的内容为
    这里都是小写字母
    这里都是小写字母
    这里都是小写字母
    ....
    然后使用该方法可以进行替换.例如把小替换成大.
    '''
    practice_8()
