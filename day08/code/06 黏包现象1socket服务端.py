import socket

server = socket.socket()
ip_port = ('127.0.0.1',8001)
# server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server.bind(ip_port)
server.listen()
conn,addr = server.accept()

# send()  2000B


from_client_msg1 = conn.recv(1024)

from_client_msg2 = conn.recv(1024)

print('from_client_msg1',from_client_msg1)
print('from_client_msg2',from_client_msg2)
conn.close()
server.close()

