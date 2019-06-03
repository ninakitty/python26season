import socket

client = socket.socket()  # 建立socket
server_ip_port = ('127.0.0.1', 8001)  # 待连接服务端地址
client.connect(server_ip_port)  # 建立连接
client.send(b"i'm client!")  # 向服务端发送信息
msg = client.recv(1024)  # 接收服务端信息
print(msg)
client.close()
