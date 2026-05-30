"""
ESERCIZIO 21 - Conversione tra collezioni

==================

Data la lista numeri = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]:


1. Converti in set per ottenere solo i valori unici, poi riconverti in lista

2. Crea un dizionario che conta le occorrenze di ogni numero

   (senza usare Counter - usa un ciclo for)

3. Crea una lista di tuple dove ogni tupla è (numero, occorrenze)

4. Ordina la lista di tuple per occorrenze (crescente)

5. Crea una stringa con i numeri unici separati da virgola    
"""

numeri = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]

# 1. Converti in set per ottenere solo i valori unici, poi riconverti in lista
numeri_set = set(numeri)
numeri_lista_unici = list(numeri_set)

print(50 * "=")
print("LISTA ORIGINALE:")
print(numeri)
print("\nSET (valori unici):")
print(numeri_set)
print("\nLISTA RICREATA DA SET:")
print(numeri_lista_unici)

# 2. Crea un dizionario che conta le occorrenze di ogni numero (senza usare Counter - usa un ciclo for)
print(50 * "=")
print("DIZIONARIO OCCORRENZE:")
numeri_dict = {}
for numero in numeri:
    if numero in numeri_dict:
        numeri_dict[numero] += 1
    else:
        numeri_dict[numero] = 1

print(numeri_dict)

# 3. Crea una lista di tuple dove ogni tupla è (numero, occorrenze)
print(50 * "=")
print("LISTA DI TUPLE (numero, occorrenze):")
lista_tuple = list(numeri_dict.items())
print(lista_tuple)

# 4. Ordina la lista di tuple per occorrenze (crescente)
print(50 * "=")
print("LISTA ORDINATA PER OCCORRENZE (crescente):")
lista_ordinata = sorted(lista_tuple, key=lambda x: x[1])
print(lista_ordinata)

# 5. Crea una stringa con i numeri unici separati da virgola
print(50 * "=")
print("STRINGA CON NUMERI UNICI SEPARATI DA VIRGOLA:")
stringa_numeri = ", ".join(str(num) for num in numeri_lista_unici)
print(stringa_numeri)
