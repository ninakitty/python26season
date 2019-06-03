import socket
import subprocess
server = socket.socket()
ip_port = ('127.0.0.1',8001)
server.bind(ip_port)
server.listen()

conn,addr = server.accept()


while 1:
    from_client_msg = conn.recv(1024).decode('gbk')  # 接受客户端的指令
    # cmd = input('请输入指令:')
    sub_conn = subprocess.Popen(
        from_client_msg,
        shell=True,
        stdout=subprocess.PIPE,  # 标准正确输出
        stderr=subprocess.PIPE,  # 标准错误输出
    )
    cmd_result = sub_conn.stdout.read()

    conn.send(cmd_result)



conn.close()
server.close()

