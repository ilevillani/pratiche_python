import socket

SRV_ADDR = "192.168.50.100"
SRV_PORT = 44444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
print("Server started! Waiting for connection...")
connection, address = s.accept()
print("Client connected with address: ", address)
while 1:
    data = connection.recv(1024)
    if not data:
        break
    #connection.sendall(b'-- Message Received --\n')
    print(data.decode('utf-8'))
connection.close()
