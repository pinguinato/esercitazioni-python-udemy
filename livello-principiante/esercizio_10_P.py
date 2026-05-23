""" 
ESERCIZIO 10 - Tuple

=========================================================

1. Crea una tupla 'coordinate' con i valori (10.5, 20.3, 30.1)

2. Stampa il primo e l'ultimo elemento

3. Prova a modificare il primo elemento e gestisci l'errore con try/except

4. Crea una tupla 'colori' con: rosso, verde, blu, rosso, verde, rosso

5. Conta quante volte appare "rosso"

6. Trova l'indice di "blu"

7. Usa l'unpacking per assegnare i valori di 'coordinate' a x, y, z

"""

tupla = (10.5, 20.3, 30.1)

print(tupla[0],tupla[2])

try:
    tupla[0] = 10.7
except:
    print(f"Non puoi modificare elementi in una tupla, sono immutabili...")
    
colori = ('rosso', 'verde', 'blu', 'rosso', 'verde', 'rosso')

print(colori.count('rosso'))

print(colori.index('blu'))

x, y, z = tupla
print(x)
print(y)
print(z)