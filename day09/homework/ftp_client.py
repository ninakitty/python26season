import socket
import time
import sys
import tools
import os


class FtpClient:
    def __init__(self, server_ip_port):
        self.client = socket.socket()  # 连接conn
        self.server_ip_port = server_ip_port  # ip和port
        self.client.connect(server_ip_port)  # 连接

    def close_connection(self):  # 关闭连接
        self.client.close()

    def sign_in(self):  # 登录
        tools.pack_char(self.client, 'sign_in')
        username = input('请输入用户名:')
        password = input('请输入密码:')
        tools.pack_char(self.client, username)
        tools.pack_char(self.client, password)
        obj = tools.unpack_char(self.client)
        return obj

    def sign_up(self):  # 注册
        tools.pack_char(self.client, 'sign_up')
        username = input('请输入用户名:')
        password = input('请输入密码:')
        re_password = input('请再次输入密码:')
        size = input('请输入磁盘配额(字节,1k=1024字节):')
        tools.pack_char(self.client, username)
        tools.pack_char(self.client, password)
        tools.pack_char(self.client, re_password)
        tools.pack_char(self.client, size)
        obj = tools.unpack_char(self.client)
        return obj

    def get_back(self, user):  # 返回上一级
        tools.pack_char(self.client, 'get_back')
        tools.pack_char(self.client, user)
        print(tools.unpack_char(self.client))

    def enter_into(self):  # 进入下一级
        tools.pack_char(self.client, 'enter_into')
        folder_list = tools.unpack_char(self.client)
        choose_folder = ''
        if folder_list:
            for index, folder in enumerate(folder_list, 1):
                print(index, folder)
            choose_folder = input('请输入文件夹序号:')
        tools.pack_char(self.client, choose_folder)
        flag = tools.unpack_char(self.client)
        print(flag['msg'])

    def display(self):  # 查看文件和文件夹
        tools.pack_char(self.client, 'display')
        file_list = tools.unpack_char(self.client)
        print('文件列表'.center(50, '-'))
        if file_list:
            for index, item in enumerate(file_list, 1):
                for key, value in item.items():
                    print(index, key, value)
        else:
            print('文件夹为空!')

    def new_folder(self):  # 新建文件夹
        tools.pack_char(self.client, 'new_folder')
        input_folder = input('请输入文件夹名称:')
        tools.pack_char(self.client, input_folder)
        print(tools.unpack_char(self.client))

    def upload(self, user):  # 上传
        tools.pack_char(self.client, 'upload')  # 标志位
        tools.pack_char(self.client, user)
        filename = input('请输入文件名称:')
        if os.path.isfile(filename):
            tools.pack_char(self.client, filename)  # 传送文件名
            md5_value = tools.my_md5(tools.md5_key, filename)
            tools.pack_char(self.client, md5_value)  # md5值
            file_size = os.stat(filename).st_size  # 文件大小
            tools.pack_char(self.client, file_size)  # 传送文件大小
            have_size = tools.unpack_char(self.client)  # 服务器上的文件大小
            suc = tools.unpack_char(self.client)
            if suc:
                tools.ftp_client(self.client, filename, file_size, have_size)
                flag = tools.unpack_char(self.client)
                print(flag['msg'])
            else:
                flag = tools.unpack_char(self.client)
                print(f'文件过大无法上传!您的磁盘配额为:{flag["user.size"]},'
                      f'当前已用{flag["current_size"]},'
                      f'上传的文件大小:{flag["file_size"]}')
        else:
            tools.pack_char(self.client, '')  # 传送空文件名
            print('文件名填写错误!')

    def download(self):  # 下载
        tools.pack_char(self.client, 'download')  # 标志位
        file_list = tools.unpack_char(self.client)  # 获取文件列表
        if file_list:
            for index, file in enumerate(file_list, 1):
                print(index, file)
            file_index = input('请输入下载文件序号:')
            tools.pack_char(self.client, file_index)
            file_name = tools.unpack_char(self.client)
            file_md5 = tools.unpack_char(self.client)
            file_size = tools.unpack_char(self.client)
            have_size = 0
            if os.path.isfile(file_name):
                have_size = os.stat(file_name).st_size  # 服务器上的文件大小
            tools.pack_char(self.client, have_size)
            if file_name == '':
                print('序号输入错误!')
            else:
                msg = tools.ftp_server(self.client, file_name, file_md5, file_size, have_size)
                print(msg)
        else:
            print('文件夹为空!')

    def remove(self):  # 删除文件或空文件夹
        tools.pack_char(self.client, 'remove')  # 标志位
        listdir = tools.unpack_char(self.client)  # 文件和文件夹列表
        if listdir:
            for index, item in enumerate(listdir, 1):
                print(index, item)
            file_index = input('请输入要删除文件的序号:')
            tools.pack_char(self.client, file_index)
        flag = tools.unpack_char(self.client)
        print(flag['msg'])


if __name__ == '__main__':
    ip_port = ('127.0.0.1', 8001)  # ip端口
    client = FtpClient(ip_port)
    switch = True  # 总开关
    is_login = False  # 是否登录
    user = None
    while switch:
        print('''
        欢迎使用FTP系统
        ''')
        if not is_login:  # 未登录
            print('''
            输入1登录,输入2注册,输入3退出.
            ''')
            input_num = input('请输入序号:')
            if input_num.isdigit():  # 是否为数字
                input_num = int(input_num)
                if input_num == 1:  # 输入1登录
                    result = client.sign_in()
                    if result['success']:
                        is_login = True
                        user = result['obj']
                    print(result['msg'])
                elif input_num == 2:  # 输入2注册
                    result = client.sign_up()
                    if result['success']:
                        is_login = True
                        user = result['obj']
                    print(result['msg'])
                elif input_num == 3:  # 输入3退出
                    switch = False
                else:
                    print('输入错误!')
            else:
                print('输入错误!')
        else:  # 已登录
            print('''
                1.返回上一级菜单
                2.进入下一级菜单
                3.新建文件夹
                4.查看目录下的文件和文件夹
                5.上传文件
                6.下载文件
                7.删除文件或文件夹
                8.退出                
                        ''')
            input_num = input('请输入序号:')
            if input_num.isdigit():  # 是否为数字
                input_num = int(input_num)
                if input_num == 1:  # 输入1返回上一级
                    client.get_back(user)
                elif input_num == 2:  # 输入2进入下一级
                    client.enter_into()
                elif input_num == 3:  # 输入3新建文件夹
                    client.new_folder()
                elif input_num == 4:  # 输入4查看目录下的文件
                    client.display()
                elif input_num == 5:  # 输入5上传文件
                    client.upload(user)
                elif input_num == 6:  # 输入6下载文件
                    client.download()
                elif input_num == 7:  # 输入7删除文件或空文件夹
                    client.remove()
                elif input_num == 8:  # 登出
                    is_login = False
                else:
                    print('输入错误!')
            else:
                print('输入错误!')
    client.close_connection()
