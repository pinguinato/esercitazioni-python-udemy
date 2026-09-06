"""
1. Data la lista temperature_c = [0, 20, 37, 100, -40]:
   a) Usa map() con una lambda per convertirle in Fahrenheit (F = C*9/5+32)
   b) Usa filter() per ottenere solo le temperature sopra i 30°C

2. Data la lista nomi = ["alice", "BOB", "Charlie", "diana"]:
   a) Usa map() per capitalizzare ogni nome (.capitalize())
   b) Usa filter() per ottenere solo i nomi con più di 4 lettere

3. Combina map e filter: data una lista di numeri da 1 a 20, filtra
   i numeri pari e poi calcola il quadrato di ognuno.
"""

temperature_c = [0, 20, 37, 100, -40]
nomi = ["alice", "BOB", "Charlie", "diana"]
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


# Usa map() con una lambda per convertirle in Fahrenheit (F = C*9/5+32)
temperature_f = list(map(lambda x : ((x * (9/5)) + 32), temperature_c))
# Usa filter() per ottenere solo le temperature sopra i 30°C
temperature_c_filter = list(filter(lambda y: y > 30, temperature_c))

# Usa map() per capitalizzare ogni nome (.capitalize())
nomi_capitalizzati = list(map(lambda nome: nome.capitalize(), nomi))
# Usa filter() per ottenere solo i nomi con più di 4 lettere
nomi_4_lettere = list(filter(lambda nome: len(nome) > 4, nomi))

# Combina map e filter: data una lista di numeri da 1 a 20, filtra i numeri pari e poi calcola il quadrato di ognuno.
lista_filtrata = list(map(lambda quadrato: quadrato**2, filter(lambda numero: numero % 2 == 0, lista)))

print(50*"=")
print(temperature_f)
print(50*"=")
print(temperature_c_filter)
print(50*"=")
print(nomi_capitalizzati)
print(50*"=")
print(nomi_4_lettere)
print(50*"=")
print(lista_filtrata)
print(50*"=")
