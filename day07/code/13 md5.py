import hashlib

# md5 一般用来验证文件或者密码的一致性

# username = "alex"
# password = "123456"
#
# obj = hashlib.md5(b'fklasjflkdasfjadsklfjadslkfjdsalkfjdsalkfjadsklfjdaskfj')
# obj.update(password.encode("utf-8"))   # 必须是字节
# s = obj.hexdigest()
#
# # e10adc3949ba59abbe56e057f20f883e
# # 61f21a8301307988cbfdd5b438e59c01
# # 4d5e92b1eb2f24ea93c4b410d2af3af3
# print(s)


username = "alex"
password = "6f6c4a8c7e2f69017da5756a8bc2310b"

def my_md5(s):
    obj = hashlib.md5(b'abdefglkfjsdaklfjklasdjfkldas')
    obj.update(s.encode("utf-8"))
    return obj.hexdigest()

def reg():
    uname = input("请输入用户名")
    upwd = input("请输入密码")
    global username
    username = uname
    global password
    password = my_md5(upwd)
    print(password)

def login():
    uname = input("请输入用户名")
    upwd = input("请输入密码")
    if uname == username and my_md5(upwd) == password:
        print("登录成功")
    else:
        print("登录失败")
# reg()

login()

#  logging 记录日志的
