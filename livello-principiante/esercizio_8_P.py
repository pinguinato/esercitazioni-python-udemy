"""
ESERCIZIO 8 - Liste: creazione e accesso

=====================================

1. Crea una lista 'frutti' con: mela, banana, arancia, kiwi, mango

2. Stampa il secondo elemento

3. Stampa l'ultimo elemento usando indice negativo

4. Stampa i primi 3 elementi (slicing)

5. Stampa la lunghezza della lista

6. Verifica se "banana" è nella lista (operatore 'in')

7. Verifica se "pera" è nella lista

8. Stampa l'indice di "arancia" nella lista

"""

frutti = ['mela', 'banana', 'arancia', 'kiwi', 'mango']

print(frutti[1])
print(frutti[-1])
print(frutti[0:3])
print(len(frutti))
print('banana' in frutti)
print('pera' in frutti)
print(frutti.index('arancia'))
