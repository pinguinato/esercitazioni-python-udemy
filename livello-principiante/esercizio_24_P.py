""" 
ESERCIZIO 24 - Manipolazione avanzata di liste

==================

1. Data la lista numeri = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]:

   - Rimuovi tutti i duplicati mantenendo l'ordine originale

   - Trova il secondo valore più grande

   - Inverti la lista senza usare reverse() o [::-1]

   - Appiattisci la lista annidata: [[1, 2], [3, 4], [5, 6]] in [1, 2, 3, 4, 5, 6]



2. Date due liste:

   

lista_a = [1, 2, 3, 4, 5]
lista_b = [4, 5, 6, 7, 8]
   - Trova gli elementi comuni

   - Trova gli elementi che sono in lista_a ma non in lista_b

   - Unisci le due liste senza duplicati
"""


numeri = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]


def cerca_secondo_massimo(lista):
    massimo_1 = 0
    massimo_2 = 0
    lista_massimi = []

    for numero in lista:
        if massimo_1 <= numero:
            massimo_1 = numero
            if massimo_1 <= massimo_2:
                massimo_1 = massimo_2

    # mi aggiungo il valore del primo massimo in modo da ricordarmelo da qualche parte
    lista_massimi.append(massimo_1)

    # calcolo il secondo massimo
    for numero in lista:
        if numero not in lista_massimi and massimo_2 <= numero:
            massimo_2 = numero

    return massimo_2


def inverti_lista(lista):
    temp_lista = []
    lunghezza_lista = len(lista) - 1

    while lunghezza_lista >= 0:
        temp_lista.append(lista[lunghezza_lista])
        lunghezza_lista -= 1

    return temp_lista


def rimozione_duplicati(lista):
    lista_set = set()
    temp_lista = []
    
    for numero in lista:
        if numero not in lista_set:
            lista_set.add(numero)
            temp_lista.append(numero)
            
    return temp_lista        
    


print(f"Lista di numeri: {numeri}")

# rimozione dei duplicati mantenendo l'ordine originale
print(50 * "=")
print(f"Lista senza duplicati e con conservazione dell'ordine: {rimozione_duplicati(numeri)}")

# estrai il secondo valore piu' grande
print(50 * "=")
print(f"Il secondo valore piu' grande nella lista di numeri e': {cerca_secondo_massimo(numeri)}")

# reverse della lista di numeri
print(50 * "=")
print(f"Stampa della lista invertita: {inverti_lista(numeri)}")
