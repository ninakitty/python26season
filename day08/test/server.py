import socket

server = socket.socket()  # 获取socket
ip_port = ('127.0.0.1', 8001)  # 待绑定IP和端口
server.bind(ip_port)  # 绑定
server.listen()  # 监听
conn, addr = server.accept()  # 接收,conn连接管道,addr客户端地址
print(conn)
print(addr)
msg = conn.recv(1024)  # 接收客户端信息
print(msg)
conn.send(b"i'm server!")  # 发送信息给客户端
conn.close()
server.close()
