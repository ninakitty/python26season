import socket
import subprocess
import struct
client = socket.socket()
server_ip_port = ('127.0.0.1',8001)
client.connect(server_ip_port)

while 1:
    cmd = input('请输入指令:')
    client.send(cmd.encode('gbk'))
    from_server_msg = client.recv(4)
    a = struct.unpack('i',from_server_msg)[0]
    from_server_msg = client.recv(a)
    print(from_server_msg.decode('gbk'))



# client.close()





