'''Scrivi una funzione che data in ingresso una lista A contenente n parole, restituisca in output una lista B di interi 
che rappresentano la lunghezza delle parole contenute in A. '''

def lunghezza_parole(lista_parole):
    #crea una lista vuota per contenere la lunghezza delle parole
    lunghezza = []
    #itera lungo ogni parola della lista
    for parola in lista_parole:
        #aggiunge con append la lunghezza della parola alla lista delle lunghezze delle parole creata prima
        lunghezza.append(len(parola))
    return lunghezza


#funzione per raccogliere parole da input utente
def main():
    #crea una lista vuota per contenere le parole inserite dall'utente
    parole = []
    #chiede all'utente di inserire le parole
    print("\nInserisci le parole una alla volta. Scrivi 'stop' per terminare.")
    while 1:
        #replace(" ") sostituisce gli spazi bianchi di modo che non vengano conteggiati
        parola = input("\nInserisci una parola: \n\n").replace(" ","")
        if parola.lower() == 'stop':
            print("\nOk, contiamo la lunghezza delle parole!")
            break
        else:
            #aggiunge con append la parola alla lista parole create prima
            parole.append(parola)
    
    #calcola lunghezza parole
    lunghezza = lunghezza_parole(parole)

    print(f"\nLe parole che hai inserito hanno una lunghezza di {lunghezza} caratteri")


main()

