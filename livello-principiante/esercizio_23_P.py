""" 
ESERCIZIO 23 - Operazioni con numeri

==================

1. Scrivi una funzione is_primo(n) che verifica se un numero è primo

   - Ricorda: Un numero primo è divisibile solo per 1 e per se stesso

   - Testa con: 2, 7, 10, 13, 1, 0



2. Scrivi una funzione fattoriale(n) che calcola il fattoriale

   - fattoriale(5) = 5 * 4 * 3 * 2 * 1 = 120

   - Gestisci il caso n = 0 (fattoriale è 1)

   - Testa con: 0, 1, 5, 10

BONUS (punto 3 un po' complicato..):

3. Scrivi una funzione fibonacci(n) che restituisce i primi n numeri della sequenza di Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, ...

   - Testa con n = 10
"""

# funzione per ilcalcolo di un numero primo: 1 non viene considerato un numero primo, un numero primo deve avere 2 divisori


def is_primo(numero):

    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

# funzione per il calcolo del numero fattoriale


def fattoriale(numero):
    if numero < 0:
        print("Il fattoriale di un numero negativo non esiste")
        return None

    if numero == 0 or numero == 1:
        return 1
    else:
        fact = 1
        while numero > 1:
            fact *= numero
            numero -= 1
        return fact

# funzione di Fibonacci


def fibonacci(numero):
    if numero < 0:
        print("Il Fibonacci di un numero negativo non esiste")
        return 0
    elif numero == 0 or numero == 1:
        return numero
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)


print(50 * "=")
print(is_primo(2))
print(is_primo(7))
print(is_primo(10))
print(is_primo(13))
print(is_primo(1))
print(is_primo(0))

print(50 * "=")
print(fattoriale(0))
print(fattoriale(1))
print(fattoriale(5))
print(fattoriale(10))


print(50 * "=")
lista_fibo = []
for i in range(10):
    lista_fibo.append(fibonacci(i))

print(lista_fibo)



""" 
Soluzione migliore per Fibonacci, la ricorsione e' ineficciente

def fibonacci(numero):
    if numero <= 0:
        return [0] if numero == 0 else []
    elif numero == 1:
        return [0, 1]
    fib = [0, 1]
    for i in range(2, numero):
        fib.append(fib[-1] + fib[-2])
    return fib
"""
