import socket as so, platform, os

SRV_ADDR = "192.168.50.100"
SRV_PORT = 12358

s = so.socket(so.AF_INET, so.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)

connection, address = s.accept()

print("Client connected: ", address)

while True:
    try:
        data = connection.recv(1024)
        print(data)
    except: continue
    a = data.decode("utf-8")
    stringa = a.split(sep="\n")

    #print(stringa)

    if(stringa[0] == '1'):
        tosend = platform.platform() + " " + platform.machine()
        connection.sendall(tosend.encode())
    elif(stringa[0] == '2'):
        data = connection.recv(1024)
        try:
            filelist = os.listdir(data.decode("utf-8"))
            tosend = ""
            for x in filelist:
                tosend += "," + x
        except:
            tosend = "Wrong path"
        connection.sendall(tosend.encode)
    elif(stringa[0] == '0'):
        connection.close()
        connection, address = s.accept()
    else:
        print("Errore!")

