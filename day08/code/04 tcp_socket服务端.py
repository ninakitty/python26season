import socket

server = socket.socket()
ip_port = ('127.0.0.1',8001)

server.bind(ip_port)
server.listen()
size = server.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
print('size',size) #65536 64k
#conn 你的客户端和服务端之间建立好的连接通道,addr客户端的地址
# print(1111)
conn,addr = server.accept()  #阻塞程序,等待建立连接
# print(2222)
while 1:
    # print(3333)
    from_client_msg = conn.recv(1024) #一次性接受数据的大小1024B,阻塞,等待接收信息
    # print(44444)
    print(from_client_msg.decode('utf-8'))  # b'yuema'
    server_msg = input('服务端说:')

    conn.send(server_msg.encode('utf-8'))

conn.close()
server.close()

