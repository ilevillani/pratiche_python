import socket as so

target = input("Inserisci l'IP da scansionare: ")

portrange = input("Inserisci un range di porte (es: 0-200): ")

low_port = 0
high_port = 200

#cosi se l'utente ha inserito la porta fa cosi altrimenti va in default e non da errore
if portrange.find("-") == 1:
    low_port = int(portrange.split("-")[0])
    high_port = int(portrange.split("-")[1])

print(f"Verranno scansite le porte da {low_port} a {high_port}")
closePort = []

#si puo fare anche with range as..., stessa cosa di for port in 

with range(low_port, high_port +1) as port:
    s = so.socket(so.AF_INET, so.SOCK_STREAM)
    #faccio la connessione, ex sta per express ha bisogno di una tupla
    status = s.connect_ex((target, port))
    if (status == 0):
        print("**** Porta {port} Aperta ****")
    #per avere un report alla fine
    else:
        closePort.append(port)
        s.close()
print("Porte chiuse", {closePort})

