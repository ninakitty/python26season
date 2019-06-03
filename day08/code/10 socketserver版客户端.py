import socket

client = socket.socket()
server_ip_port = ('127.0.0.1',8001)
client.connect(server_ip_port)

while 1:
    msg = input('客户端1号>>>')

    client.send(msg.encode('utf-8'))
    from_server_msg = client.recv(1024)
    print(from_server_msg.decode('utf-8'))



