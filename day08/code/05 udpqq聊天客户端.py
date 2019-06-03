import socket
BUFSIZE=1024
udp_client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_ip_port=('127.0.0.1',8081)
while True:
    msg=input('客户端说: ').strip()
    udp_client_socket.sendto(msg.encode('utf-8'),server_ip_port)

    server_msg,server_addr = udp_client_socket.recvfrom(1024)
    print(server_msg.decode('utf-8'),server_addr)