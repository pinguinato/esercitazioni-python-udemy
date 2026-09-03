""" 
1. Crea un dizionario che mappa i numeri da 1 a 10 al loro quadrato:
   {1: 1, 2: 4, 3: 9, ...}

2. Data la lista frutti = ["mela", "banana", "kiwi", "arancia"], crea
   un dizionario che mappa ogni frutto alla sua lunghezza.

3. Dato il dizionario prezzi = {"mela": 1.5, "banana": 0.8, "kiwi": 2.0,
   "arancia": 1.2, "mango": 3.5}, crea un nuovo dizionario con solo
   i frutti che costano meno di 2.0 euro.
"""

frutti = ["mela", "banana", "kiwi", "arancia"]

prezzi = {
   "mela": 1.5, "banana": 0.8, "kiwi": 2.0, "arancia": 1.2, "mango": 3.5}

# creare un dizionario che mappa i numeri da 1 a 10 al loro quadrato in dict comprehension
dizionario_al_quadrato = {x:x**2 for x in range(1,10)}
# mappaggio di ogni frutto alla sua lunghezza in stringa
dizionario_frutta = {frutto:len(frutto) for frutto in frutti}
# solo i frutti che costano meno di 2.0 euro
frutti_economici = {frutto:prezzo for frutto,prezzo in prezzi.items() if prezzo < 2.0}

print(50*"=")
print(dizionario_al_quadrato)
print(dizionario_frutta)
print(frutti_economici)
print(50*"=")