解题思路；

文件读取函数
1、定义一个文件读取函数，可以将文件中的文本，转换成列表读取到内存中


用户登陆
1、调用文件读取函数，将用户账号密码文件，读取到内存中；
2、定义用户名和密码验证函数，匹配读取到内存中的账号和密码信息


查询语句解析
1、定义一个函数，将指定的查询语句转换成python编程语言中的查询条件；
2、查询条件分两部分，一部分是条件，另一部分查询范围的字段，分两部分存储在列表中，有函数返回此列表


查询语句执行
1、调用文件读取函数，将员工信息表读取到内存中；
2、调用查询语句解析函数，将查询条件和返回字段存储在列表中；
3、根据查询语句解析后的列表，在内存中的员工信息表列表中去查询符合条件的内容
