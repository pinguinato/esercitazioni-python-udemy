""" 
ESERCIZIO 9 - Liste: modifica

===================================================

Partendo dalla lista numeri = [10, 20, 30, 40, 50]:


1. Aggiungi 60 alla fine

2. Inserisci 15 nella posizione 1 (tra 10 e 20)

3. Rimuovi il valore 30

4. Rimuovi e stampa l'ultimo elemento (pop)

5. Ordina la lista in ordine decrescente

6. Stampa la lista risultante

7. Crea una copia della lista e svuota l'originale

8. Stampa sia la copia che la lista originale (vuota)

"""

# stampa della lista cosi come e'
numeri = [10, 20, 30, 40, 50]
print(numeri)

# Aggiungi 60 alla fine
numeri.append(60)
print(numeri)

# Inserisci 15 nella posizione 1 (tra 10 e 20)
numeri.insert(1, 15)
print(numeri)

# Rimuovi il valore 30
numeri.remove(30)
print(numeri)

# Rimuovi e stampa l'ultimo elemento (pop)
print(numeri.pop())
print(numeri)

# Ordina la lista in ordine decrescente e stampa la risultante
numeri.sort(reverse=True)
print(numeri)

# Crea una copia della lista e svuota l'originale e stampa entrambe
numeri_copia = numeri.copy()
numeri.clear()
print(numeri)
print(numeri_copia)



