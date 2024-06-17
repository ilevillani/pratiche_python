import math
from math import pi

def perim_area_quadrato(lato):
    perimetro = lato * 4
    area = lato ** 2
    return perimetro, area

def perim_area_rettangolo(lato):
    base = lato
    altezza = lato / 2
    perimetro = 2 * (base + altezza)
    area = base * altezza
    return perimetro, area

def perim_area_cerchio(lato):
    raggio = lato
    perimetro = 2 * pi * raggio
    area = pi * raggio ** 2
    return perimetro, area

def perim_area_triangolo(lato):
    perimetro = 3 * lato
    area = (math.sqrt(3) / 4) * lato ** 2
    return perimetro, area

def perim_area_rombo(lato):
    perimetro = 4 * lato
    area = lato ** 2
    return perimetro, area

def esci():
    print("\nCiao!")
    exit()

def cm_invalido():
    print("Opzione invalida. Inserisci un numero tra 1 e 6.")

funzioni_figure = {
    '1': ("Quadrato", perim_area_quadrato),
    '2': ("Rettangolo", perim_area_rettangolo),
    '3': ("Cerchio", perim_area_cerchio),
    '4': ("Triangolo equilatero", perim_area_triangolo),
    '5': ("Rombo", perim_area_rombo)
}

def mostra_menu(funzioni_figure):
    print("\nScegli un'opzione: \n")
    for key, value in funzioni_figure.items():
        print(f"   {key}) {value[0]}")
    print("   6) Esci dal programma")

# Richiedi l'input iniziale una sola volta dopo che l'utente seleziona la prima figura
lato_iniziale = None

# Loop per calcolare 5 figure
for _ in range(5):
    mostra_menu(funzioni_figure)
    scelta = input("\nSeleziona un'opzione: \n\n")
    
    if scelta == '6':
        esci()

    if scelta in funzioni_figure:
        if lato_iniziale is None:
            lato_iniziale = float(input("\nInserisci il valore del lato della prima figura. Questo valore verrà utilizzato per calcolare le aree di tutte le altre figure: \n\n"))
        
        figura, func = funzioni_figure.pop(scelta)
        perimetro, area = func(lato_iniziale)
        print(f"\n{figura}:")
        print(f"Perimetro = {perimetro:.2f}")
        print(f"Area = {area:.2f}")
        lato_iniziale = area
    else:
        cm_invalido()

print("\nLe opzioni sono finite! Grazie per aver usato il programma!")
