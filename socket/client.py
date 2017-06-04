import socket, time

HOST = '127.0.0.1'#'localhost' #'0.0.0.0'#'0.0.0.0' #represent default
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
s.connect((HOST, PORT))

while 1:
    send = raw_input("input:")
    s.sendall(send)
    data = s.recv(8192)
    time.sleep(1)
    print "receive message from server", data
s.close()
