""" 
============================================

    MINI-PROGETTO 1 | LIVELLO: PRINCIPIANTE

    RUBRICA TELEFONICA

============================================

DESCRIZIONE:

        Crea un programma che simula una rubrica telefonica.

        L'utente può aggiungere, cercare, modificare e cancellare contatti.

        Ogni contatto ha: nome, numero di telefono e email (opzionale).

        La rubrica è gestita tramite un menu testuale interattivo


    NOTA: Per rendere il progetto testabile senza input() interattivo, il programma simulerà le operazioni tramite chiamate a funzioni. 

In fondo al file della soluzione trovi anche la versione con input() commentata.

PREREQUISITI (concetti che devi conoscere):

    - Variabili e tipi di dato (str, int, bool)

    - Dizionari: creazione, accesso, modifica, .get(), .pop(), .items()

    - Liste: .append(), iterazione con for

    - Funzioni: def, parametri, return, parametri con default

    - Condizioni: if / elif / else

    - Cicli: while (per il menu), for (per scorrere i contatti)

    - F-string per la formattazione dell'output

    - Operatore 'in' per verificare l'esistenza di una chiave


OUTPUT ATTESO:

    Il programma deve produrre un output simile a questo:


    === RUBRICA TELEFONICA ===


    [1] Contatto 'Mario Rossi' aggiunto con successo!

    [2] Contatto 'Anna Bianchi' aggiunto con successo!

    [3] Contatto 'Luca Verdi' aggiunto con successo!


    --- Rubrica completa (3 contatti) ---

      Mario Rossi    | Tel: 333-1234567 | Email: mario@email.it

      Anna Bianchi   | Tel: 339-7654321 | Email: anna@email.it

      Luca Verdi     | Tel: 347-1112233 | Email: (nessuna)


    --- Ricerca 'anna' ---

      Trovato: Anna Bianchi | Tel: 339-7654321 | Email: anna@email.it


    --- Modifica telefono di 'Mario Rossi' ---

      Telefono aggiornato: 333-9999999


    --- Eliminazione 'Luca Verdi' ---

      Contatto eliminato con successo!


    --- Rubrica finale (2 contatti) ---

      Mario Rossi    | Tel: 333-9999999 | Email: mario@email.it

      Anna Bianchi   | Tel: 339-7654321 | Email: anna@email.it


    Statistiche:

      Contatti totali: 2

      Con email: 2

      Senza email: 0


FUNZIONI DA IMPLEMENTARE:

    1. aggiungi_contatto(rubrica, nome, telefono, email="")

       - Aggiunge un contatto al dizionario rubrica

       - Se il contatto esiste già, stampa un avviso

       - Restituisce True se aggiunto, False se già esistente

  2. cerca_contatto(rubrica, termine)

       - Cerca un contatto per nome (anche parziale, case-insensitive)

       - Restituisce una lista dei contatti trovati

    3. modifica_telefono(rubrica, nome, nuovo_telefono)

       - Modifica il numero di telefono di un contatto esistente

       - Restituisce True se modificato, False se non trovato

    4. elimina_contatto(rubrica, nome)

       - Elimina un contatto dalla rubrica

       - Restituisce True se eliminato, False se non trovato

    5. mostra_rubrica(rubrica)

       - Stampa tutti i contatti in formato tabellare

    6. statistiche(rubrica)

       - Stampa il numero totale di contatti, quanti hanno email e quanti no
       
STRUTTURA DATI:

    La rubrica è un DIZIONARIO dove:

    - Chiave: nome del contatto (stringa)

    - Valore: un altro dizionario con {"telefono": "...", "email": "..."}

    Esempio:

   

    rubrica = {
            "Mario Rossi": {"telefono": "333-1234567", "email": "mario@email.it"},
            "Anna Bianchi": {"telefono": "339-7654321", "email": "anna@email.it"},
        }

SUGGERIMENTI:

    - Per la ricerca case-insensitive, usa .lower() sia sul termine che sul nome

    - Per verificare se un contatto esiste: if nome in rubrica:

    - Per l'email opzionale, usa un valore di default "" (stringa vuota)

    - Per la formattazione tabellare, usa f-string con allineamento: {nome:<15}

Puoi testarlo con:

    rubrica = {}
    aggiungi_contatto(rubrica, "Mario Rossi", "333-1234567", "mario@email.it")
    aggiungi_contatto(rubrica, "Anna Bianchi", "339-7654321", "anna@email.it")
    mostra_rubrica(rubrica)
    # ... ecc..      
"""


from collections import Counter


# funzione per aggiungere un contatto


def aggiungi_contatto(rubrica, nome, telefono, email=""):
    if nome in rubrica:
        print(f"Il contatto: {nome} e' gia' presente nella Rubrica.")
        return False
    else:
        rubrica[nome] = {"telefono": telefono, "email": email}
        return True


# stampa il contenuto della rubrica
def mostra_rubrica(rubrica):
    print(f"--- Rubrica completa ({len(rubrica)} contatti) ---\n")
    for chiave, valore in rubrica.items():
        email = valore.get('email') if valore.get('email') else "(nessuna)"
        print(f"  {chiave:<15} | Tel: {valore.get('telefono'):<15} | Email: {email}\n")


def main():
    print("")
    print("=== RUBRICA TELEFONICA ===")
    print("")
    # la rubrica e' un dizionario, vuoto all'inizio
    rubrica = {}

    # TODO: quando un contatto viene inserito correttamente bisogna visualizzare -> [1] Contatto 'Mario Rossi' aggiunto con successo! ...

    # testing:
    aggiungi_contatto(rubrica, "Roberto Gianotto", "1234", "prova@gmail.com")
    aggiungi_contatto(rubrica, "Stefania Vicentini",
                      "123456", "testa@gmail.com")
    aggiungi_contatto(rubrica, "Sauro Calamari",
                      "111222333", "calamari@gmail.com")

    mostra_rubrica(rubrica)


main()
