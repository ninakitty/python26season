import pymysql
import hmac
import os


class Base:  # 基类
    def __init__(self):
        self.key = 'tom'  # 加盐KEY
        self.conn = pymysql.connect(  # 获取连接
            host='localhost',
            port=3306,
            user='root',
            password='root',
            database='host_management',
            charset='utf8')
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def __del__(self):  # 对象销毁,关闭连接
        self.cursor.close()
        self.conn.close()
        # print('连接已关闭')

    def get_md5(self, args):  # MD5工具
        key = self.key.encode('utf8')
        h = hmac.new(key, digestmod='MD5')
        if os.path.isfile(args):
            with open(args, mode='rb') as file:
                while True:
                    block = file.read(1024)  # 每次读取1K
                    if not block:  # 如果文件读取完成跳出循环
                        break
                    h.update(block)  # 更新加密数据
        elif isinstance(args, str):
            args = args.encode('utf8')
            h.update(args)
        return h.hexdigest()


class Admin(Base):
    def login(self):  # 登录
        username = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        sql = 'select aname,passwd from admin where aname=%s and passwd=%s'
        result = self.cursor.execute(sql, args=[username, self.get_md5(password)])
        return result


class Business(Base):  # 业务线
    def add(self):  # 业务线增加
        print('增加业务线'.center(50, '-'))
        bname = input('请输入要添加的业务线名称:').strip()
        if bname != '':
            query_sql = 'select bname from business where bname=%s'
            result = self.cursor.execute(query_sql, args=[bname])
            if result:
                print('业务线已存在', result)
            else:
                add_sql = 'insert into business(bname) values(%s)'
                add_res = self.cursor.execute(add_sql, args=[bname])
                if add_res:
                    self.conn.commit()
                    print(f'添加业务线aa完成,业务名:{bname}')
        else:
            print('输入错误,不能为空!')

    def remove(self):  # 业务线删除
        print('删除业务线'.center(50, '-'))
        self.query()
        bid = input('请输入要删除的业务线Bid:')
        del_sql = 'delete from business where bid=%s'
        res = self.cursor.execute(del_sql, args=[bid])
        if res:
            self.conn.commit()
            print('删除完成!')
        else:
            print('删除失败,输入错误!')

    def modify(self):  # 业务线修改
        print('修改业务线'.center(50, '-'))
        self.query()
        bid = input('请输入修改业务线id:').strip()
        bname = input('请输入修改业务线名称:').strip()
        if bname != "":
            modify_sql = 'update business set bname=%s where bid=%s'
            result = self.cursor.execute(modify_sql, args=[bname, bid])
            if result:
                self.conn.commit()
                print('更新完成!')
            else:
                print('更新失败,原值不变!')
        else:
            print('名称输入错误!')

    def query(self, query=False):  # 业务线查询
        if query:  # 单独调用查询
            print('查询业务线'.center(50, '-'))
        sql = 'select bid,bname from business ordery by bid'
        result = self.cursor.execute(sql)
        obj = self.cursor.fetchall()
        if result:
            tplt = "{0:{2}^10}\t{1:{2}^10}"
            print(tplt.format('id', 'name', ' '))
            for item in obj:
                print(tplt.format(item['bid'], item['bname'], ' '))
        else:
            print('结果为空')
        return obj


class Host(Base):  # 主机
    def __init__(self):
        super(Host, self).__init__()

    @staticmethod
    def get_business_id_list():
        """
        获取业务线id列表
        :return: 返回业务线列表
        """
        business = Business()
        obj = business.query()
        bid_list = []
        for item in obj:
            bid_list.append(item['bid'])
        return bid_list

    def add(self):  # 增加
        print('增加主机'.center(50, '-'))
        hname = input('1.请输入主机名:').strip()
        hpasswd = input('2.请输入密码:').strip()
        bid_list = self.get_business_id_list()  # 获取业务线ID列表
        bid = input('3.请输入业务线ID:').strip()
        if bid.isdigit() and hname != '' and hpasswd != '':  # 输入是否为数值,非空
            bid = int(bid)
            if bid in bid_list:
                query_sql = 'select hid from host where hname=%s'
                query_res = self.cursor.execute(query_sql, args=[hname])
                if not query_res:
                    add_sql = 'insert into host(hname,hpasswd,bid) values(%s,%s,%s)'
                    add_res = self.cursor.execute(add_sql, args=[hname, self.get_md5(hpasswd), bid])
                    if add_res:
                        self.conn.commit()
                        print('添加主机完成')
                    else:
                        print('添加失败')
                else:
                    print('主机名已存在')
            else:
                print('业务线ID错误!')
        else:
            print('输入不能为空')

    def remove(self):  # 删除
        print('删除主机'.center(50, '-'))
        self.query()
        hid = input('请输入主机ID:').strip()
        del_sql = 'delete from host where hid=%s'
        del_res = self.cursor.execute(del_sql, args=[hid])
        if del_res:
            self.conn.commit()
            print('主机删除完成')
        else:
            print('删除失败,请确认id')

    def modify(self):  # 修改
        print('修改主机'.center(50, '-'))
        self.query()
        hid = input('请输入主机ID:')
        if hid.isdigit():
            hid = int(hid)
            hname = input('请输入主机名:')
            hpasswd = input('请输入密码:')
            bid_list = self.get_business_id_list()
            bid = input('请输入业务线ID:')
            if bid.isdigit():
                bid = int(bid)
                if bid in bid_list:
                    modify_sql = 'update host set hname=%s,hpasswd=%s,bid=%s where hid=%s'
                    modify_res = self.cursor.execute(modify_sql, args=[hname, self.get_md5(hpasswd), bid, hid])
                    if modify_res:
                        self.conn.commit()
                        print('修改成功')
                    else:
                        print('修改失败.')
                else:
                    print('序号输入错误!')
        else:
            print('id输入错误')

    def query(self, query=False):  # 查询
        if query:  # 直接调用查询,打印信息
            print('查询主机'.center(50, '-'))
        sql = 'select hid,hname,bname from host inner join business on host.bid=business.bid order by hid'
        result = self.cursor.execute(sql)
        if result:
            obj = self.cursor.fetchall()
            tplt = "{0:{3}^10}\t{1:{3}^10}\t{2:{3}^10}"
            print(tplt.format('ID', 'host-name', 'business', ' '))
            for item in obj:
                print(tplt.format(item['hid'], item['hname'], item['bname'], ' '))
        else:
            print('结果为空')


def func_list_operate(fun_list):  # 方法列表操作
    """
    操作方法列表
    :param fun_list:接收方法列表
    :return: 方法名称
    """
    for index_num, obj in enumerate(fun_list, 1):
        print(index_num, obj[1])
    fun_num = input('请输入功能序号:').strip()
    fun_name = ''
    if fun_num.isdigit():
        fun_num = int(fun_num)
        if 0 < fun_num <= len(fun_list):
            fun_name = fun_list[fun_num - 1][0]
        else:
            print('序号输入错误')
    else:
        print('序号输入错误')
    return fun_name


def do_method(_class, method_name):
    """
    反射执行方法
    :param _class:方法所在类
    :param method_name: 方法名称
    :return: 无返回
    """
    if hasattr(_class, method_name):
        fun = getattr(_class(), method_name)
        if method_name == 'query':
            fun(query=True)
        else:
            fun()


if __name__ == '__main__':
    admin = Admin()
    is_login = False  # 判断是否登录
    retry_count = 3  # 登录尝试次数
    switch = True  # 总开关
    while switch:
        if not is_login:
            while retry_count:
                retry_count -= 1
                if admin.login():
                    is_login = True
                    print('登录成功!')
                    break
                if retry_count == 0:  # 最后一次失败,关闭程序
                    switch = False
                    print('登录失败,剩余次数已用尽!')
                    break
                print('登录失败,剩余尝试次数', retry_count)
        else:
            function_list = [('Host', '主机管理'), ('Business', '业务线管理'), ('Exit', '退出')]
            function_name = func_list_operate(function_list)
            if function_name == 'Host':  # 主机管理
                host_method_list = [('add', '增加主机'), ('remove', '删除主机'), ('modify', '修改主机'), ('query', '查询主机')]
                host_method_name = func_list_operate(host_method_list)  # 操作功能列表
                do_method(Host, host_method_name)  # 执行功能

            elif function_name == 'Business':  # 业务线管理
                business_method_list = [('add', '增加业务'), ('remove', '删除业务'), ('modify', '修改业务'), ('query', '查询业务')]
                business_method_name = func_list_operate(business_method_list)
                do_method(Business, business_method_name)
            elif function_name == 'Exit':  # 退出
                switch = False
                print('再见!')
