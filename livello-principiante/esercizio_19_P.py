""" 
ESERCIZIO 19 - Funzioni con valori di default e return multipli

==================

1. Crea una funzione presentati(nome, saluto="Ciao") che stampa "[saluto], mi chiamo [nome]!"

   - Chiamala con e senza il parametro saluto


2. Crea una funzione statistiche(numeri) che riceve una lista di numeri e restituisce una tupla con:

(minimo, massimo, somma, media)

   - Non usare le funzioni min(), max(), sum() - calcolali manualmente

   - Testa con la lista [10, 25, 3, 47, 12, 8]
"""


def presentati(nome, saluto="Ciao"):
    print(f"{saluto}, mi chiamo {nome}")


def statistiche(numeri):
    somma = 0
    minimo = numeri[0]
    massimo = numeri[0]

    for numero in numeri:
        somma += numero
        if numero <= minimo:
            minimo = numero
        if numero >= massimo:
            massimo = numero

    media = somma / len(numeri)
    # costituisci un tupla
    tupla = (minimo, massimo, somma, media)

    return tupla


# test delle funzioni
presentati("Roberto")
presentati("Roberto", "Buonasera")

print("================================")
lista_numeri = [10, 25, 3, 47, 12, 8]
print(statistiche(lista_numeri))
