import hmac
import os
import sys
import pickle
import struct

md5_key = 'helloworld'  # md5加密键
db_file = os.path.join(os.getcwd(), 'userlist.db')  # 用户列表
path = os.path.join(os.getcwd(), 'home')  # 用户上传路径


def my_md5(key, args):  # md5工具
    """
    md5加密文件或字符
    :param key:加密的键
    :param args:加密的文件或字符
    :return:返回md5值
    """
    key = key.encode('utf8')  # 加密键
    h = hmac.new(key, digestmod='MD5')  # 加密方法
    if os.path.isfile(args):  # 是否为文件
        with open(args, mode='rb') as file:
            while True:
                block = file.read(1024)  # 每次读取1K
                if not block:  # 如果为空退出
                    break
                h.update(block)  # 追加信息
    elif isinstance(args, str):  # 是否为字符
        args = args.encode('utf8')
        h.update(args)
    return h.hexdigest()


def get_pickle_obj(file):  # 获取pickle对象
    obj = []
    if os.path.isfile(file):
        with open(file, mode='rb') as fp:
            obj = pickle.load(fp)
    else:
        with open(file, mode='wb') as fp:
            pickle.dump(obj, fp)
    return obj


def set_pickle_obj(file, obj):  # 保存pickle文件
    with open(file, mode='wb') as fp:
        pickle.dump(obj, fp)


def pack_char(conn, char):  # 打包并发送
    pickle_char = pickle.dumps(char)
    len_pack = struct.pack('i', len(pickle_char))
    conn.send(len_pack)
    conn.send(pickle_char)


def unpack_char(conn):  # 解包获取内容
    len_pack = conn.recv(4)
    size = struct.unpack('i', len_pack)
    obj = conn.recv(size[0])
    return pickle.loads(obj)


def ftp_client(conn, filename, file_size, have_size):  # 上传文件端
    is_exists = unpack_char(conn)
    md5_same = unpack_char(conn)
    msg = ''
    if is_exists:
        if md5_same:
            msg = '文件已存在,MD5值相同!'
            return msg

    with open(filename, mode='rb') as fp:
        fp.seek(have_size)
        while True:
            block = fp.read(1024)
            if not block:
                break
            pack_char(conn, block)  # 发送文件
            new_file_size = unpack_char(conn)
            per_cent = round(new_file_size / file_size, 2)
            sys.stdout.write('>')
            sys.stdout.flush()
            print('\r' + '%s%%' % (int(per_cent * 100)) + '*' * (int(per_cent * 100)), end='')

    return msg


def ftp_server(conn, filename, md5_value, file_size, have_size):  # 接收文件端
    new_file_size = 0  # 新文件大小
    new_filename = filename  # + '_' + str(time.time())  # 新文件名
    msg = ''
    is_exists = False  # 文件是否存在
    md5_same = False  # md5一致
    if os.path.isfile(filename):
        is_exists = True
        pack_char(conn, is_exists)
        if my_md5(md5_key, filename) == md5_value:
            md5_same = True
            pack_char(conn, md5_same)
            msg = '文件已存在,MD5值相同!'
        else:
            pack_char(conn, md5_same)
            new_file_size = have_size  # 改变已存在文件大小
            with open(new_filename, mode='ab')as fp:
                while new_file_size < file_size:
                    block = unpack_char(conn)
                    fp.write(block)
                    new_file_size += len(block)
                    pack_char(conn, new_file_size)
                    per_cent = round(new_file_size / file_size, 2)
                    sys.stdout.write('>')
                    sys.stdout.flush()
                    print('\r' + '%s%%' % (int(per_cent * 100)) + '*' * (int(per_cent * 100)), end='')
            new_md5_value = my_md5(md5_key, new_filename)
            if md5_value == new_md5_value:
                msg = '文件继传完成,MD5值相同'
            else:
                msg = '文件继传完成,MD5值不相同'
    else:
        pack_char(conn, is_exists)
        pack_char(conn, md5_same)
        with open(new_filename, mode='wb')as fp:
            while new_file_size < file_size:
                block = unpack_char(conn)
                fp.write(block)
                new_file_size += len(block)
                pack_char(conn, new_file_size)
                per_cent = round(new_file_size / file_size, 2)
                sys.stdout.write('>')
                sys.stdout.flush()
                print('\r' + '%s%%' % (int(per_cent * 100)) + '*' * (int(per_cent * 100)), end='')
        new_md5_value = my_md5(md5_key, new_filename)
        if md5_value == new_md5_value:
            msg = 'MD5值相同'
        else:
            msg = 'MD5值不相同'

    return msg


def get_dir_size(dir_obj):  # 获取文件夹大小
    size = 0
    for root, dirs, files in os.walk(dir_obj):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size


if __name__ == '__main__':
    # 测试字符
    res = my_md5('1', 'helloworld')
    print(res)
    # 测试文件
    res = my_md5('1', 'user.py')
    print(res)
    # 比较文件是否一致
    with open('user.py', 'rb') as fp:
        print(hmac.new('1'.encode('utf8'), fp.read()).hexdigest())
    str = '中国'
    r1 = pickle.dumps(str)
    print(r1)
    r2 = pickle.loads(r1)
    print(r2)
    s3 = b'\x80\x03X\x07\x00\x00\x00'
    r3 = pickle.loads(s3)
    print(r3)
