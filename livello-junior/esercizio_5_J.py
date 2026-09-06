""" 
1. Crea una lambda che calcola il cubo di un numero.
   Testala con i numeri 3 e 5.

2. Crea una lambda che prende due numeri e restituisce il maggiore.

3. Data la lista persone = [("Mario", 30), ("Anna", 25), ("Luca", 35)],
   ordina la lista per età usando sorted() con key=lambda.

4. Data la lista parole = ["Python", "e", "fantastico", "da", "imparare"],
   ordina le parole per lunghezza.
"""

# crea una lambda che calcola il cubo di un numero
funz_lambda_cubo = lambda x: x**3
# crea una lambda che calcola il maggiore tra due numeri
funz_lambda_maggiore = lambda a, b: max(a, b)

persone = [("Mario", 30), ("Anna", 25), ("Luca", 35)]
# ordina sulla base del secondo elemento della lista
funz_sort_lambda_eta = sorted(persone, key=lambda x:x[1])
# risultato: [('Anna', 25), ('Mario', 30), ('Luca', 35)]

parole = ["Python", "e", "fantastico", "da", "imparare"]

# questa lambda ordina le parole per lunghezza
funz_sort_parole_lunghezza = sorted(parole, key=lambda x: len(x))

print(50*"=")
print(funz_lambda_cubo(3))
print(funz_lambda_cubo(5))
print(50*"=")
print(funz_lambda_maggiore(30, 5555))
print(50*"=")
print(funz_sort_lambda_eta)
print(50*"=")
print(funz_sort_parole_lunghezza)
print(50*"=")