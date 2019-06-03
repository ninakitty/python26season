import socket
client = socket.socket()
server_ip_port = ('127.0.0.1',8001)
client.connect(server_ip_port)

client.send(b'yuema')
from_server_msg = client.recv(1024)
print(from_server_msg)


# client.close()





