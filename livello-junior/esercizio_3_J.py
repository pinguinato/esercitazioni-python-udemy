""" 
1. Crea una funzione somma_tutto(*args) che accetta un numero qualsiasi
   di argomenti numerici e restituisce la loro somma.

2. Crea una funzione stampa_info(titolo, *args) che stampa un titolo
   e poi elenca tutti gli argomenti con un numero progressivo.
   
   Esempio: stampa_info("Frutti", "mela", "banana", "kiwi")
   Output:
   --- Frutti ---
   1. mela
   2. banana
   3. kiwi
"""

def somma_tutto(*args):
   try:
      somma = sum(args) 
      return somma
   except TypeError:
      print("Si possono sommare soltanto numeri interi positivi e negativi!") 
      return None


def stampa_info(titolo, *args):
   if len(args) == 0:
      print("Non hai inserito argomenti in input!")
      return False
   else: 
      print(f"--- {titolo} ---")
      counter_args = 1
      i = 0
      while counter_args <= len(args) and i < counter_args:
         print(f"{counter_args}. {args[i]}")
         i = i + 1
         counter_args = counter_args + 1
   


print(50*"=")
print(somma_tutto(12.5,12,23,45,-1000,1234,-102.4567))
print(50*"=")
stampa_info("Frutti", "mela", "banana", "kiwi")



