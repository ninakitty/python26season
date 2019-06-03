import socket

server = socket.socket()
ip_port = ('127.0.0.1',8001)
server.bind(ip_port)
server.listen()
#conn 你的客户端和服务端之间建立好的连接通道,addr客户端的地址
conn,addr = server.accept()

print(conn) #<socket.socket fd=496, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8001), raddr=('127.0.0.1', 60055)>
print(addr) #('127.0.0.1', 60055)

from_client_msg = conn.recv(1024) #一次性接受数据的大小1024B
print(from_client_msg) #b'yuema'
conn.send(b'hello')

conn.close()
server.close()

