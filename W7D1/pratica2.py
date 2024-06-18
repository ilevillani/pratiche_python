'''Scrivi una funzione generatrice di password. La funzione deve generare una stringa alfanumerica di 8 caratteri 
qualora l'utente voglia una password semplice, o di 20 caratteri ascii qualora desideri una password più complicata.'''

import string
#documentazione python suggerisce di preferire il modulo secrets al random per generare password https://docs.python.org/3/library/secrets.html
import secrets

def genera_password(tipo):
    if tipo == 'semplice':
        caratteri = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(caratteri)
        for _ in range(8))
    elif tipo == 'complessa':
        caratteri = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(caratteri)
        for _ in range(20))
    else:
        return None

    return password

def menu():
    while 1:
        print("\t \t \t Menu: ")
        print("\n 1. Genera una password semplice di 8 caratteri alfanumerici: ")
        print("\n 2. Genera una password complessa di 20 caratteri inclusi simboli: ")
        print("\n 3. Esci.")

        #prova ad eseguire il codice se l'utente inserisca solo numeri da 1 a 3 e non lettere o numeri fuori range
        try:
            scelta = int(input("\n Scegli un'opzione: "))
            if scelta in range(1,4):
                if scelta == 1:
                    password = genera_password('semplice')
                    print(f"\n La tua password semplice è: {password}")
                elif scelta == 2:
                    password = genera_password('complessa')
                    print(f"\n La tua password sicura è: {password}")
                else:
                    print("\n Uscita dal programma.")
                    break
            else:
                print("\nScelta non valida. Per favore, inserisci un numero tra 1 e 3.\n")
        #gestisce l'errore se l'utente inserisce lettere
        except ValueError as e:
            print(f"\n Scelta non valida. Inserisci un numero tra 1 e 3.\n\nErrore: {e}\n")
        
menu()


