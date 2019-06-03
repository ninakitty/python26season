import socket
client = socket.socket()
server_ip_port = ('127.0.0.1',8001)
client.connect(server_ip_port)

client.send(b'yuema')
import time
time.sleep(0.1)
client.send(b'girl')




# client.close()





