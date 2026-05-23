""" 
ESERCIZIO 15 - Ciclo for con range

==================

Usando il ciclo for e range():

1. Stampa i numeri da 1 a 10

2. Stampa i numeri pari da 2 a 20

3. Stampa il conto alla rovescia da 10 a 1

4. Calcola la somma dei numeri da 1 a 100 e stampala

5. Stampa la tavola pitagorica del 7 (da 7x1 a 7x10)

"""

for numero in range(1, 11):
    print(numero)

for numero in range(1, 21):
    if numero % 2 == 0:
        print(numero)

for numero in range(10, 0, -1):
    print(numero)

somma = 0    
for numero in range(1, 101):
    somma += numero
print(f"Somma dei numeri da 1 a 100: {somma}")    

for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

