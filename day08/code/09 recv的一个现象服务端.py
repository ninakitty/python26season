
import socket
server = socket.socket()

server.bind(('127.0.0.1',8001))
server.listen(3)  #记着这里


conn,addr = server.accept()

while 1:
    from_client_msg = conn.recv(1024)

    print(from_client_msg)

















