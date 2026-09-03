""" 
1. Data la lista numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crea con
   una list comprehension:
   a) Una lista con i quadrati di ogni numero
   b) Una lista con solo i numeri pari
   c) Una lista con i numeri pari elevati al cubo

2. Data la stringa frase = "python e il linguaggio del futuro", crea
   con una list comprehension:
   a) Una lista con la lunghezza di ogni parola
   b) Una lista con ogni parola capitalizzata (prima lettera maiuscola)
"""

numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
frase = "python e il linguaggio del futuro"

# come mettere tutti i numeri al quadrato
numeri_al_quadrato = [x**2 for x in numeri]
# come estrarre soltanto i numeri pari
numeri_solo_pari = [x for x in numeri if x % 2 == 0]
# come ottenere i numeri al cubo del gruppo dei numeri pari
numeri_solo_pari_a_cubo = [x**3 for x in numeri_solo_pari]

# come calcolare la lunghezza di ogni parola di una frase
lunghezza_di_ogni_parola = [len(parola) for parola in frase.split()]
# come creare una lista capitalizzata
lista_capitalizzata = [parola.capitalize() for parola in frase.split()]

print(50*"=")
print(numeri)
print(numeri_al_quadrato)
print(numeri_solo_pari)
print(numeri_solo_pari_a_cubo)
print(50*"=")
print(frase)
print(lunghezza_di_ogni_parola)
print(lista_capitalizzata)
print(50*"=")