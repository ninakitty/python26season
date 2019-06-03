import socket
client = socket.socket()

client.connect(('127.0.0.1',8001))

msg = input('客户端说:')
client.send(b'hello')
# while 1:
#     import time
#     time.sleep(0.2)
#     client.send(b'hello')




