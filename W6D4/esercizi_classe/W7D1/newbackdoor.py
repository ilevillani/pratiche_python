#leggi documentazione di socket in doc.python.org
import socket as so

import os #importo il sistema operativo

SRV_ADDR = "127.0.0.1" #cosi fa bind su tutte le porte
SRV_PORT = 44446 #scelgo porta alta cosi non devo dare permessi di root

c = so.socket(so.AF_INET, so.SOCK_STREAM)#la connessione è ipv4 (AF_INET), poi faccio una connessione di tipo stream che è tcp
#da non confondere con la datagram che è udp
#faccio la richiesta al sistema operativo per il bin

#dico al so cosa deve fare, dico al socket che deve mettersi in ascolto
#gli dico quante connessioni massimo può accettare, per ora va bene 1
c.connect((SRV_ADDR, SRV_PORT))
#s.listen(1)

#quando mi sono messo in ascolto, scrivo che sono in ascolto
print(f"Sono connesso al server: {SRV_ADDR}")

def send_file(filename):
    try:
        with open(filename, 'rb') as file:
            file_data = file.read()
            c.sendall(f"FILE {filename} {len(file_data)}".encode("utf-8"))  # Invio del comando e della dimensione del file
            ack = c.recv(1024).decode()
            if ack == 'READY':
                c.sendall(file_data)  # Invio del contenuto del file
                print(f"File {filename} inviato con successo.")
            else:
                print("Errore durante la sincronizzazione con il server.")
    except FileNotFoundError:
        print(f"File {filename} non trovato.")
    except Exception as e:
        print(f"Errore durante l'invio del file: {e}")
while True:
    # Lettura del comando o del messaggio da inviare al server
    command = input("Enter command (send <filename> / message / bye): ").strip()

    if command.lower() == "bye":
        break

    if command.startswith("send "):
        filename = command[5:].strip()
        send_file(filename)
    else:
        c.sendall(command.encode("utf-8"))
        data = c.recv(1024).decode("utf-8")
        print("Received from server: " + data)

# Chiusura della connessione
c.close()
print("Connessione chiusa")