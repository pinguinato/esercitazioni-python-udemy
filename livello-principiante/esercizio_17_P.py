""" 
ESERCIZIO 17 - Ciclo while

==================

1. Scrivi un ciclo while che stampa i numeri da 1 a 10

2. Scrivi un ciclo while che dimezza un numero (partendo da 1000)

   fino a quando è minore di 1. Stampa ogni passaggio.

3. Scrivi un ciclo while che simula un conto alla rovescia:

   - Parti da 5

   - Stampa il numero corrente

   - Quando arrivi a 0, stampa "PARTENZA!"
"""

print("========================")
x = 1
while x <= 10:
   print(x)
   x+=1

print("========================")

numero = 1000
while numero > 1:
   numero = numero / 2
   print(numero) 
   
print("========================")
conto_alla_rovescia = 5
while conto_alla_rovescia > 0:
   print(f"Conto alla rovescia: {conto_alla_rovescia}")
   conto_alla_rovescia = conto_alla_rovescia - 1
   if conto_alla_rovescia == 0:
      print("PARTENZA!")
 
