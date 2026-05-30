""" 
ESERCIZIO 20 - Set (insiemi)

==================

Dati:

    classe_a = {"Mario", "Luigi", "Peach", "Toad", "Yoshi"}
    classe_b = {"Luigi", "Daisy", "Toad", "Wario", "Peach"}


1. Stampa gli studenti presenti in ENTRAMBE le classi (intersezione)

2. Stampa TUTTI gli studenti senza duplicati (unione)

3. Stampa gli studenti SOLO nella classe A (differenza)

4. Stampa gli studenti SOLO nella classe B (differenza)

5. Stampa gli studenti in una classe ma NON nell'altra (differenza simmetrica)

6. Aggiungi "Bowser" alla classe A

7. Rimuovi "Wario" dalla classe B
"""

classe_a = {"Mario", "Luigi", "Peach", "Toad", "Yoshi"}
classe_b = {"Luigi", "Daisy", "Toad", "Wario", "Peach"}

print(50 * "=")
print("DATI 2 INSIEMI:")
print(classe_a)
print(classe_b)

print(50 * "=")
print("INTERSEZIONE:")
print(classe_a.intersection(classe_b))

print(50 * "=")
print("UNIONE:")
print(classe_a.union(classe_b))

print(50 * "=")
print("DIFFERENZA INSIEMISTICA:")
print(classe_a.difference(classe_b))
print(classe_b.difference(classe_a))

print(50 * "=")
print("DIFFERENZA SIMMETRICA:")
print(classe_a.symmetric_difference(classe_b))
print(classe_b.symmetric_difference(classe_a))

print(50 * "=")
print("AGGIUNTA DI BOWSER:")
classe_a.add("Bowser")
print(classe_a)

print(50 * "=")
print("RIMOZIONE WARIO:")
classe_b.remove("Wario")
print(classe_b)
