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



def genera_numero(limite):     
   # ritorna il calcolo della funzione random su interi conpresi da 1 a 20 (limite)
   return r.randint(1, limite)
   




##########
# TESTING
##########

def main():
   print(f"Test: {genera_numero(20)}")
      
   
main()