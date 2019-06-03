import socket
udp_server = socket.socket(type=socket.SOCK_DGRAM)  #udp的socket了,datagram
ip_port = ('127.0.0.1',8002)
udp_server.bind(ip_port)
print(11111)
msg,addr = udp_server.recvfrom(1024) #1024B ,这里会阻塞
print(22222)
print(msg,addr) #('127.0.0.1', 51384)

udp_server.sendto(b'gunduzi',addr)
udp_server.close()





