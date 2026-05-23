"""
ESERCIZIO 12 - Dizionari: metodi e modifica

======================================================

Partendo dal dizionario:

prodotto = {"nome": "Laptop", "prezzo": 999.99, "disponibile": True}


1. Aggiungi la chiave "marca" con valore "Lenovo"

2. Modifica il prezzo a 899.99

3. Rimuovi la chiave "disponibile" e stampa il valore rimosso

4. Crea un secondo dizionario dettagli = {"ram": "16GB", "storage": "512GB"}

5. Unisci 'dettagli' in 'prodotto' usando update()

6. Stampa il dizionario finale

7. Crea una copia del dizionario con .copy()
"""

prodotto = {"nome": "Laptop", "prezzo": 999.99, "disponibile": True}
print(prodotto)

prodotto["marca"] = "Lenovo"
print(prodotto)

prodotto["prezzo"] = 899.99
print(prodotto)

print(prodotto.pop("disponibile"))
print(prodotto)

dettagli = {"ram": "16GB", "storage": "512GB"}

prodotto.update(dettagli)
print(prodotto)

copia_prodotto = prodotto.copy()
print(copia_prodotto)