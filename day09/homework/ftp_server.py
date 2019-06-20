# 1. 多用户同时登陆
# 2. 用户登陆，加密认证
# 3. 上传/下载文件，保证文件一致性
# 4. 传输过程中现实进度条
# 5. 不同用户家目录不同，且只能访问自己的家目录
# 6. 对用户进行磁盘配额、不同用户配额可不同
# 7. 用户登陆server后，可在家目录权限下切换子目录
# 8. 查看当前目录下文件，新建文件夹
# 9. 删除文件和空文件夹
# 10. 充分使用面向对象知识
# 11. 支持断点续传
#
# 练习题：20
# 基本实现：70
#     1.实现文件的上传、下载功能
#     2.实现c/s端 密文登陆功能
#     3.有效处理大文件
#     4.md5进行文件已执行校验
#     5.实现进度条功能
#     6.充分使用面向对象的知识
#     7.目录结构、流程如和readme
# 代码写的清晰、健壮、可扩展：10
# 相关链接:https://www.cnblogs.com/clschao/articles/9593164.html#part_13
import os
import socketserver
import traceback
import struct
import tools
import user


class FtpServer(socketserver.BaseRequestHandler):
    def handle(self):  # 主入口
        while 1:
            try:
                menu = tools.unpack_char(self.request)
                if menu == 'sign_in':
                    self.sign_in()
                elif menu == 'sign_up':
                    self.sign_up()
                elif menu == 'upload':
                    self.upload()
                elif menu == 'download':
                    self.download()
                elif menu == 'get_back':
                    self.get_back()
                elif menu == 'display':
                    self.display()
                elif menu == 'new_folder':
                    self.new_folder()
                elif menu == 'enter_into':
                    self.enter_into()
                elif menu == 'remove':
                    self.remove()
                else:
                    print('输入错误')
                    continue
            except (struct.error, ConnectionResetError):
                print('用户断开连接!')
                break

    def sign_in(self):  # 登录
        print('sign_in')
        username = tools.unpack_char(self.request)
        password = tools.unpack_char(self.request)
        user_list = tools.get_pickle_obj(tools.db_file)  # 获取用户列表
        result = user.User.sign_in(username, password, user_list)
        if result['success']:
            os.chdir(os.path.join(tools.path, result['obj'].home))
        tools.pack_char(self.request, result)

    def sign_up(self):  # 注册
        print('sign_up')
        username = tools.unpack_char(self.request)
        password = tools.unpack_char(self.request)
        re_password = tools.unpack_char(self.request)
        size = tools.unpack_char(self.request)
        user_list = tools.get_pickle_obj(tools.db_file)  # 获取用户列表
        result = user.User.sign_up(username, password, re_password, user_list, size)
        if result['success']:
            tools.set_pickle_obj(tools.db_file, result['user_list'])
            os.mkdir(os.path.join(tools.path, result['obj'].home))
            os.chdir(os.path.join(tools.path, result['obj'].home))
        tools.pack_char(self.request, result)

    def upload(self):  # 上传
        print('upload')
        user = tools.unpack_char(self.request)  # 用户
        filename = tools.unpack_char(self.request)  # 文件名
        if not filename == '':
            md5_value = tools.unpack_char(self.request)  # md5值
            file_size = tools.unpack_char(self.request)  # 文件大小
            have_size = 0
            if os.path.isfile(filename):
                have_size = os.stat(filename).st_size  # 服务器上的文件大小
            tools.pack_char(self.request, have_size)
            current_size = tools.get_dir_size(os.path.join(tools.path, user.home))
            print('current_size', current_size, 'file_size', file_size, 'user.size', user.size)
            flag = {'success': False, 'file_size': file_size, 'current_size': current_size, 'user.size': user.size,
                    'msg': ''}
            if (current_size + file_size) < user.size:
                flag['success'] = True
                tools.pack_char(self.request, True)
                res = tools.ftp_server(self.request, filename, md5_value, file_size, have_size)
                flag['msg'] = res
                tools.pack_char(self.request, flag)
            else:
                tools.pack_char(self.request, False)
                tools.pack_char(self.request, flag)

    def download(self):  # 下载
        print('download')
        file_list = []  # 文件列表
        for file in os.listdir():  # 当前目录文件
            if os.path.isfile(file):
                file_list.append(file)
        tools.pack_char(self.request, file_list)  # 列表发送给对端
        if file_list:
            file_index = tools.unpack_char(self.request)  # 文件索引
            if file_index.isdigit():
                file_index = int(file_index)
                if 0 < file_index <= len(file_list):  # 文件在列表中
                    file_name = file_list[file_index - 1]  # 文件名
                    file_size = os.stat(file_name).st_size  # 文件大小
                    tools.pack_char(self.request, file_name)  # 发送给对端
                    tools.pack_char(self.request, tools.my_md5(tools.md5_key, file_name))
                    tools.pack_char(self.request, file_size)
                    have_size = tools.unpack_char(self.request)  # 获取已存文件大小
                    tools.ftp_client(self.request, file_name, file_size, have_size)  # 执行文件传输
                else:
                    for _ in range(3):
                        tools.pack_char(self.request, '')
            else:
                for _ in range(3):
                    tools.pack_char(self.request, '')

    def get_back(self):  # 返回上一级
        current_path = os.getcwd()  # 当前路径
        user = tools.unpack_char(self.request)
        user_path = os.path.join(tools.path, user.home)  # 用户家目录
        if not current_path == user_path:  # 非家目录则切换
            os.chdir(os.path.pardir)
            tools.pack_char(self.request, '切换完成!')
        else:
            tools.pack_char(self.request, '已达到最高路径,不能再返回!')

    def display(self):  # 显示文件
        file_list = []
        for item in os.listdir():
            if os.path.isfile(item):
                file_list.append({'文件:': item})
            elif os.path.isdir(item):
                file_list.append({'目录:': item})
        tools.pack_char(self.request, file_list)

    def new_folder(self):  # 新建文件夹
        input_folder = tools.unpack_char(self.request)
        flag = True
        for item in os.listdir():
            if os.path.isdir(item) and input_folder == item:
                tools.pack_char(self.request, '文件夹已存在!')
                flag = False
        if flag:
            os.mkdir(input_folder)
            tools.pack_char(self.request, '文件夹建立成功!')

    def enter_into(self):  # 进入目录
        folder_list = []
        flag = {'success': False, 'msg': ''}  # 标记
        for folder in os.listdir():
            if os.path.isdir(folder):
                folder_list.append(folder)
        tools.pack_char(self.request, folder_list)
        if folder_list:
            choose_folder = tools.unpack_char(self.request)
            if choose_folder.isdigit():
                choose_folder = int(choose_folder)
                if 0 < choose_folder <= len(folder_list):
                    os.chdir(folder_list[choose_folder - 1])
                    flag['success'] = True
                    flag['msg'] = '切换成功'
        else:
            flag['msg'] = '无下一级目录'
        tools.pack_char(self.request, flag)

    def remove(self):  # 删除文件或空目录
        flag = {'success': False, 'msg': ''}
        listdir = os.listdir()
        tools.pack_char(self.request, listdir)
        if not listdir:
            flag['msg'] = '无文件!'
        else:
            file_index = tools.unpack_char(self.request)
            if file_index.isdigit():
                file_index = int(file_index)
                if 0 < file_index <= len(listdir):
                    file_name = listdir[file_index - 1]
                    if os.path.isfile(file_name):
                        os.remove(file_name)
                        flag['success'] = True
                        flag['msg'] = '删除文件成功'
                    elif os.path.isdir(file_name):
                        try:
                            os.rmdir(file_name)
                            flag['success'] = True
                            flag['msg'] = '删除文件夹成功'
                        except Exception:
                            flag['msg'] = '文件夹非空,不能删除'
                else:
                    flag['msg'] = '序号输入错误!'
            else:
                flag['msg'] = '序号输入错误!'
        tools.pack_char(self.request, flag)


if __name__ == '__main__':

    ip_port = ('127.0.0.1', 8001)
    server = socketserver.ThreadingTCPServer(ip_port, FtpServer)
    try:
        server.serve_forever()
    except Exception:
        print(traceback.format_exc())
    finally:
        server.server_close()
