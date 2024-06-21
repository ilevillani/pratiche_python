#leggi documentazione di socket in doc.python.org
import socket as so

import os #importo il sistema operativo

SRV_ADDR = "" #cosi fa bind su tutte le porte
SRV_PORT = 44446 #scelgo porta alta cosi non devo dare permessi di root

s = so.socket(so.AF_INET, so.SOCK_STREAM)#la connessione è ipv4 (AF_INET), poi faccio una connessione di tipo stream che è tcp
#da non confondere con la datagram che è udp
#faccio la richiesta al sistema operativo per il bind
s.bind((SRV_ADDR, SRV_PORT))#guardare bind cosa fa nei python docs.

#dico al so cosa deve fare, dico al socket che deve mettersi in ascolto
#gli dico quante connessioni massimo può accettare, per ora va bene 1
s.connect((SRV_ADDR, SRV_PORT))
#s.listen(1)

#quando mi sono messo in ascolto, scrivo che sono in ascolto
print(f"Sono in ascolto su {SRV_PORT}")

#devo istruirlo ad accettare le connessioni, si mette in blocco da ora in avanti
#python estrapola gli indirizzi
connection, address = s.accept()
print(f"Si è collegato: {SRV_ADDR}")
#cmd = sys.exc_info("ls")
#print(cmd)
while True:
    output = os.popen("pwd").read().rstrip() + "$"
    connection.sendall(output.encode("utf-8"))
    #gli chiedo di ricevere dati da questo servizio
    #il pacchetto tcp viene ricevuto finche non viene dato invio
    #la comunicazione tcp deve sapere quanti pacchetti deve aspettare dopo
    #in python possiamo dire quanti byte massimi deve ricevere anche se lui non ha dato invio
    #data contiene il grezzo che arriva dall'altro lato
    #1024 = quando sta ricevendo lo stream dei dati o si interrompe e manda avanti quando l'altro preme invio, oppure quando arriva a 1024 byte
    data = connection.recv(1024)

    #il dato ci arriva in formato binario
    #con if not data verifico = Se non arriva nessun dato vuol dire che l'altro ha interrotto la conn. in modo formato con ctrl c, quindi non deve continuare
    if not data:
        break
    cmd = data.decode("utf-8").rstrip()
    if cmd == "help":
        #b è uguale a scrivere encode uft8 ma questo è meno intuitivo
        connection.sendall(b"Ci hai provato.")
    elif cmd == "ciao":
        connection.sendall(b"Come stai?")
    else:
        #uno legge l'esec. del comando e lo manda su output, l'altro legge

        output = os.popen(cmd.read()) + "\n"
        #con qualsiasi altro comando manda tutte le informazioni (prova ls-l) e creare file (fai una prova con "touch prova.txt")
        connection.sendall(output.encode("utf-8") + "\n")

    #sendall non significa invia a tutti qui, questo invia tutto il messaggio, non il messaggio a tutti
    #le connessioni con il b davanti lo trasformano in binario, quindi posso scrivere messaggio ricevuto
    #connection.sendall(b'Messaggio ricevuto\n')

    #decodifico dal binario all'utf8, altrimenti escono gli esadecimali
    print(data.decode('utf-8'))
#se esce dalla connessione la deve chiudere per poi farne ripartire un'altra
connection.close()