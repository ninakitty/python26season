import tools


class User:  # 用户类

    def __init__(self, user, password, home, size):
        self.user = user  # 用户名
        self.password = password  # 密码
        self.home = home  # 家目录
        self.size = size  # 磁盘配额

    @staticmethod
    def sign_in(username, password, user_list):  # 登录
        """
        验证是否登录成功
        :param username: 用户名
        :param password: 密码
        :param user_list: 用户列表
        :return:字典{'success': False, 'msg': '登录失败,请重试!', 'obj': None}
        """
        key = tools.md5_key  # 加密key
        flag = {'success': False, 'msg': '登录失败,请重试!', 'obj': None}
        for user in user_list:
            if user.user == username and tools.my_md5(key, password) == user.password:
                flag['success'] = True
                flag['msg'] = '登录成功!'
                flag['obj'] = user
        return flag

    @staticmethod
    def sign_up(username, password, re_password, user_list, size):  # 注册

        """
        注册用户
        :param username: 用户名
        :param password: 密码
        :param re_password: 再次输入密码
        :param user_list:用户列表
        :return:字典{'success': True, 'msg': '注册成功!', 'obj': None}
        """
        flag = {'success': True, 'msg': '注册成功!', 'obj': None}
        key = tools.md5_key  # 加密key
        if username == '' or password == '' or re_password == '':
            flag['msg'] = '注册失败,帐号或密码不能为空!'
            flag['success'] = False
        if password != re_password:
            flag['msg'] = '注册失败,两次密码输入不一致!'
            flag['success'] = False
        for user in user_list:
            if user.user == username:
                flag['msg'] = '注册失败,用户名重复'
                flag['success'] = False
        if not size.isdigit():
            flag['msg'] = '配置填写错误!'
            flag['success'] = False
        if flag['success']:
            size = int(size)
            new_user = User(username, tools.my_md5(key, password), username, size)
            user_list.append(new_user)
            flag['obj'] = new_user
            flag['user_list'] = user_list
        return flag
