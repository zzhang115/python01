import socket

HOST = '127.0.0.1'#'localhost' #'0.0.0.0'#'0.0.0.0' #represent default
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
s.connect((HOST, PORT))

s.sendall("first message from client2")
data = s.recv(1024)
s.close()
print "receive message from server", repr(data)
