import socket, time

HOST = '127.0.0.1'#'localhost' #'0.0.0.0'#'0.0.0.0' #represent default
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
s.connect((HOST, PORT))

while 1:
    s.sendall("first message from client1")
    data = s.recv(1024)
    time.sleep(1)
    print "receive message from server", repr(data)
s.close()
