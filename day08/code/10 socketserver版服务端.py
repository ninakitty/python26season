import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while 1:
            from_client_msg = self.request.recv(1024)  # conn
            print(from_client_msg.decode('utf-8'))
            msg = input('to_client_msg>>>')
            self.request.send(msg.encode('utf-8'))

if __name__ == '__main__':
    ip_port = ('127.0.0.1',8001)
    server = socketserver.ThreadingTCPServer(ip_port,MyServer)
    server.serve_forever()







