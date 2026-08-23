""" 
============================================

    MINI-PROGETTO 3 | LIVELLO: PRINCIPIANTE

    GIOCO "INDOVINA IL NUMERO"

============================================



DESCRIZIONE:

    Crea un gioco in cui il computer sceglie un numero casuale

    e il giocatore deve indovinarlo. Ad ogni tentativo il programma

    dice se il numero segreto e' PIU' ALTO o PIU' BASSO rispetto

    al tentativo. Il gioco tiene traccia del numero di tentativi

    e alla fine mostra le statistiche delle partite giocate.



    Livelli di difficolta':

    1. Facile:    numero tra 1 e 20  (max 8 tentativi)

    2. Medio:     numero tra 1 e 50  (max 10 tentativi)

    3. Difficile: numero tra 1 e 100 (max 15 tentativi)



    Questo progetto usa solo: random, funzioni, if/elif/else,

    while, input/print, liste, operazioni matematiche.



PREREQUISITI (concetti che devi conoscere):

    - Modulo random: random.randint(a, b)

    - Funzioni: def, parametri, return

    - Condizionali: if / elif / else

    - Ciclo while con contatore

    - Input e output: input(), print(), f-string

    - Conversione di tipo: int()

    - try/except per gestire input non numerici

    - Liste e .append() per le statistiche

    - Operazioni matematiche: somma, divisione, len()



FUNZIONI DA IMPLEMENTARE:

    1. scegli_difficolta() -> tuple (limite, max_tentativi)
       Mostra il menu difficolta' e restituisce i parametri.
 
    2. genera_numero(limite) -> int
       Genera un numero casuale tra 1 e limite.
 
    3. chiedi_tentativo(minimo, massimo) -> int oppure None
       Chiede un numero all'utente e lo valida.
 
    4. dai_suggerimento(tentativo, numero_segreto) -> bool
       Confronta il tentativo col numero segreto.
       Stampa "Troppo alto!" o "Troppo basso!" oppure "Hai indovinato!".
       Restituisce True se indovinato, False altrimenti.
 
    5. gioca_partita() -> int oppure -1
       Gestisce una singola partita completa.
       Restituisce il numero di tentativi usati, oppure -1 se ha perso.
 
    6. mostra_statistiche(risultati) -> None
       Mostra le statistiche di tutte le partite giocate:
       partite giocate, vinte, perse, media tentativi (solo vittorie).
 
    7. main() -> None
       Funzione principale: ciclo che permette di giocare piu' partite
       e alla fine mostra le statistiche.


OUTPUT ATTESO:

    ========================================

      INDOVINA IL NUMERO

    ========================================



    Scegli la difficolta':

      1. Facile    (1-20,  max 8 tentativi)

      2. Medio     (1-50,  max 10 tentativi)

      3. Difficile (1-100, max 15 tentativi)

    Scelta: 1



    --- Partita 1 (Facile: 1-20) ---

    Ho pensato un numero tra 1 e 20. Hai 8 tentativi!



    Tentativo 1/8 - Inserisci un numero: 10

      Troppo alto! Prova piu' basso.

    Tentativo 2/8 - Inserisci un numero: 5

      Troppo basso! Prova piu' alto.

    Tentativo 3/8 - Inserisci un numero: 7

      Hai indovinato in 3 tentativi!



    Vuoi giocare ancora? (s/n): n



    === STATISTICHE ===

    Partite giocate: 1

    Vittorie: 1 | Sconfitte: 0

    Media tentativi (vittorie): 3.0



SUGGERIMENTI:

    - random.randint(1, 20) genera un numero tra 1 e 20 INCLUSI.

    - Usa while tentativi < max_tentativi per limitare i tentativi.

    - Per le statistiche, usa una lista dove aggiungi il risultato

      di ogni partita: il numero di tentativi se vince, -1 se perde.

    - Per la media, filtra solo i valori positivi dalla lista.

    - input().strip().lower() e' utile per normalizzare risposte s/n.

"""

import random as r

FACILE = 1
MEDIO = 2
DIFFICILE = 3

def titolo_gioco():
   # titolo iniziale del gioco
   print(50 * "=")
   print("")
   print("  INDOVINA IL NUMERO")
   print("")
   print(50 * "=")
   print("")
   print("")
   # scegli la difficolta'
   print("Scegli la difficolta':\n")
   print("\t1. Facile    (1-20,  max 8 tentativi)")
   print("\t2. Medio     (1-50,  max 10 tentativi)")
   print("\t3. Difficile (1-100, max 15 tentativi)\n")


def scegli_difficolta():
   try:
      scelta = int(input("Scelta: "))
      if scelta == FACILE:
         return (20,8)
      elif scelta == MEDIO:
         return (50,10)
      elif scelta == DIFFICILE:
         return (100,15)
      else:
         print("Valore numerico non ammesso.")
         return None
   except ValueError:
      print("Non puoi inserire valori letterali, solo numeri interi da 1 a 3")
      return None
   
      


def genera_numero(limite):     
   # ritorna il calcolo della funzione random su interi conpresi da 1 a 20 (limite)
   if limite <= 0 or limite > 100:
      print("Non posso generare un numero randon con valori <= 0.")
      return None
   else:
      return r.randint(1, limite)
   


def chiedi_tentativo(minimo, massimo): 
   while True:
      try:
         numero_utente = int(input("Inserisci un numero: "))
         if minimo <= numero_utente <= massimo:
            return numero_utente; # il numero inserito dall'utente va bene ed è valido
         else:
            print(f"Deve essere un valore tra {minimo} e {massimo}!")
      except ValueError:
         print("Inserisci un numero intero!")


def gioca_partita():
   pass




def dai_suggerimento(tentativo, numero_segreto):
   # numero_segreto sarebbe numero_pensato dal computer
   if tentativo == numero_segreto:
      print("Hai indovinato!")
      return True
   elif tentativo > numero_segreto:
      print("Troppo alto!")
      return False
   elif tentativo < numero_segreto:
      print("Troppo basso!")
      return False
       
   



##########
# TESTING
##########

def main():
   #print(f"Test: {genera_numero(20)}")
   titolo_gioco()
   tupla_scelta = scegli_difficolta()
   
   # dentro tupla_scelta arriva una tupla (massimo intero da indovinare, numero massimo dei tentativi)
   
   massimo_numero_input = tupla_scelta[0] # può essere anche il limite
   massimo_numero_tentativi = tupla_scelta[1] 
   numero_partita = 1
   
   
   # caso partita facile
   if (massimo_numero_input == 20 and massimo_numero_tentativi == 8):
      print(f"--- Partita {numero_partita} (Facile: 1-20) ---")
      numero_pensato_computer = genera_numero(massimo_numero_input)
      print(f"Numero pensato dal computer: {numero_pensato_computer}")
      print("Ho pensato un numero tra 1 e 20. Hai 8 tentativi!")
      print(f"Il numero pensato dal computer: {numero_pensato_computer}")
      print(f"Tentativo {numero_partita}/8 - ")
      # validazione del tentativo
      tentativo = chiedi_tentativo(1,20)
      dai_suggerimento(tentativo, numero_pensato_computer) 
      
      
      
      
      
      # TODO: implementare il meccanismo dei tentativi
      
      
      
   elif (massimo_numero_input == 50 and massimo_numero_tentativi == 10):
      print(f"--- Partita {numero_partita} (Medio: 1-50) ---")
      print("Ho pensato un numero tra 1 e 50. Hai 10 tentativi!")
   elif (massimo_numero_input == 100 and massimo_numero_tentativi == 15):
      print(f"--- Partita {numero_partita} (Difficile: 1-100) ---")
      print("Ho pensato un numero tra 1 e 100. Hai 15 tentativi!")
   
   
   
   
   #print(f"Hai scelto {tupla_scelta}")   
   
main()