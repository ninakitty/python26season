只写了员工信息表查询作业，支持以下三种查询语句
select name,age where age > 22
select * where job = IT
select * where phone like 133

bug:
执行这条语句时：select name,age where age > 22
打印结果不能一行同时显示name和age，如下所示，很不美观
Egon
23
nezha
25
nezha
25