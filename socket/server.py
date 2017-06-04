import socket, time, os

HOST = 'localhost'#'0.0.0.0'#'0.0.0.0' #represent default
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
s.bind((HOST, PORT))
s.listen(2)
# conn, addr = s.accept()
# print 'GOT connection from:', addr

while 1:
    conn, addr = s.accept()
    print 'GOT connection from:', addr
    while 1:
        #if connection has not been closed, conn.recv will waiting until get message from client
        data = conn.recv(1024)#receive 4kb character once
        send = os.popen(data)
        result = send.read()
        if not data:
            break
        conn.sendall(result)
        print result
        time.sleep(1)
conn.close()