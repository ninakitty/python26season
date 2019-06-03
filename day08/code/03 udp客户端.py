import socket
udp_server = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1',8002)

udp_server.sendto(b'yuema',ip_port)

from_server_msg,server_addr = udp_server.recvfrom(1024)
print("来自服务端消息：",from_server_msg)
print(server_addr)