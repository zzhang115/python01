import socket

HOST = '0.0.0.0'#'0.0.0.0' #represent default
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
s.bind((HOST, PORT))
s.listen(2)
conn, addr = s.accept()

print 'GOT connection from:', addr

while 1:
    data = conn.recv(4096)#receive 4kb character once
    if not data:
        break
    conn.sendall(data)
    print data
conn.close()