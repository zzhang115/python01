#!/usr/bin/env python
import SocketServer, socket
class myTCPHandler():
    def handle(self):
        self.data = self.request.recv(4096)
        print self.data
        format_data = "\033[32,1m%s \033[0m" %self.data
        self.request.sendall(self.data.upper())

host, port = '', 9999
server = SocketServer.TCPServer((host, port), myTCPHandler)
server.serve_forever()
