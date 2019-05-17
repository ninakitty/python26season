# 员工信息表
版本 python3.6\
运行python staff_info.py

---
###用户登陆
####一. 该程序用户登录，密码验证
>* 用户名输入
>* 密码输入，且不将密码打印在输入框
>* 判断是否为被锁定用户，如果是则不允许登录
>* 账号和密码验证，同时正确将正常登录
>* 密码错误次数限制，三次密码错误则锁定该用户

####二. user_info文件内容格式
>* 用户文件格式为 用户名:密码（`user:password`）
>* 若没有文件，则会自动生成一个，并创建admin用户，密码123456

####三. user_lock文件
>* 若没有锁定文件则表示无被锁定用户
>* 当有用户密码错误次数超过三次时自动创建

-----

###员工信息查询
#####staff_info存储员工信息,格式如下：
>id,name,age,phone,job\
1,Alex,22,13651054608,IT\
2,Egon,23,13304320533,Teacher\
3,nezha,25,1333235322,IT
#####staff_id存储员工id,格式如下：
>1,2,3....

####一.创建员工记录(insert)
>* insert name=alex,age=25,phone=13833333333,job=BlowingWater

ps: id自增，新增时无需插入

###二.删除员工信息(delete)
>* delete id=1

ps: 匹配条件即删除, 任何字段都可为条件，多条匹配同时删除

###三.修改员工信息(update)
> * update  name=abel where id=1

ps: 语法update 列名=“新的值” where 条件
    匹配条件即更新,多条匹配同时更新

####四.查询员工信息(select)
>* select name,age where age>22
>* select * where job=IT
>* select * where phone like 133

支持: 大于小于等于,模糊查找。\
PS: 大于,小于查找，需要数据与条件为int类型