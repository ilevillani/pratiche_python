import math
from math import pi

def perim_quadrato():
    lato = float(input("Inserisci il lato del quadrato: "))
    print( "Il perimetro del quadrato è = ", lato*4 )

def perim_rettangolo():
    base = float(input("Inserisci la base del rettangolo: "))
    altezza = float(input("Inserisci l'altezza del rettangolo: "))
    print( "Il perimetro del rettangolo è: ", (base*2) + (altezza*2))  

def perim_cerchio():
    raggio = float(input("Inserisci il raggio del cerchio: "))
    print( "Il perimetro del cerchio è", 2*pi*raggio)

def perim_triangolo():
    lato_tr = float(input("Inserisci il lato del triangolo equilatero: "))
    print( "Il perimetro del triangolo equilatero è", 3*lato_tr)

def perim_rombo():
    lato_rombo = float(input("Inserisci il lato del rombo: "))
    print( "Il perimetro del rombo è", 4*lato_rombo)

def esci():
    print("Ciao!")

def cm_invalido():
    print("Opzione invalida. Ritenta.")

menu = """
   1) Quadrato
   2) Rettangolo
   3) Cerchio
   4) Triangolo equilatero
   5) Rombo
   6) Esci dal programma
Seleziona un'opzione (1-6):"""

scelta = ''
while scelta != '7':
   scelta = input(menu)
   {'1': perim_quadrato,
    '2': perim_rettangolo,
    '3': perim_cerchio,
    '4': perim_triangolo,
    '5': perim_rombo,
    '6': esci}.get(scelta, cm_invalido)()