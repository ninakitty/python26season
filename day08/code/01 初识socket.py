import socket
from threading import Thread
server = socket.socket()
server.bind(('192.168.16.1',8001))
server.listen()

def f1(conn):
    from_client_msg = conn.recv(1024)
    print(from_client_msg)

    with open('test.html','rb') as f:
        data = f.read()
        conn.send(data)
    conn.close()

while 1:
    conn,addr = server.accept()
    t = Thread(target=f1,args=(conn,))
    t.start()















