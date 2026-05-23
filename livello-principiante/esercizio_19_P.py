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
    return f"{saluto}, mi chiamo {nome}"


def statistiche(numeri):
    pass

# test delle funzioni
print(presentati("Roberto"))
print(presentati("Roberto", "Buonasera"))
