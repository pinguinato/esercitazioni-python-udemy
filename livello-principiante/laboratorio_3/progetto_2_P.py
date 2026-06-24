
# doamde e' una lista di dizionari
domande = [
    {
        "testo": "Quale funzione stampa a schermo?",
        "opzioni": ["echo()", "write()", "console.log()", "print()"],
        "corretta": 3
    },
    {
        "testo": "Quale tipo di dato rappresenta 3.14?",
        "opzioni": ["str", "int", "bool", "float"],
        "corretta": 3
    },
    {
        "testo": "Come si crea una lista in Python?",
        "opzioni": ["lista = new List()", "lista = []", "lista = ()", "lista = set()"],
        "corretta": 1
    },
    {
        "testo": "Quale tipo di dato rappresenta True o False?",
        "opzioni": ["str", "int", "bool", "float"],
        "corretta": 2
    },
    {
        "testo": "Come si accede al primo elemento di una lista?",
        "opzioni": ["lista[1]", "lista[0]", "lista.first()", "lista.get(0)"],
        "corretta": 1
    }
]


def crea_domande():
    lista_domande = domande
    return lista_domande


def totale_domande(lista):
    return len(lista)


def mostra_domanda(domanda, numero, totale):
    # TODO: dobbiamo capire come ricavare il numero corretto della domanda
    print(f"Domanda {numero}/{totale}: {domanda["testo"]}")
    # stampa le possibilli risposte alla domanda
    for i, opzione in enumerate(domanda["opzioni"]):
        lettera = chr(i + ord("a"))
        print(f"  {lettera}) {opzione}")


def verifica_risposta(domanda, risposta_utente):
    pass


def main():
    print(50 * "=")
    print("")
    print("   QUIZ DI PYTHON - 5 domande")
    print("")
    print(50 * "=")
    print("")

    # qui dentro ho la lista di dizionari delle 5 domande
    lista_domande = crea_domande()

    # print(lista_domande)

    # stampa a video della domanda
    # mostra_domanda(domanda, 1, totale_domande(lista_domande))
    # mostra_domanda(domanda_2, 2, totale_domande(lista_domande))
    # mostra_domanda(domanda_3, 3, totale_domande(lista_domande))
    # mostra_domanda(domanda_4, 4, totale_domande(lista_domande))
    # mostra_domanda(domanda_5, 5, totale_domande(lista_domande))


main()


"""
Domanda 1/5: Quale funzione stampa a schermo in Python?

      a) echo()

      b) write()

      c) console.log()

      d) print()





FUNZIONI DA IMPLEMENTARE:

    1. crea_domande()
       - Restituisce la lista di dizionari con almeno 5 domande
       - Ogni domanda ha: testo, opzioni (lista di 4 stringhe), corretta (indice)
 
    2. mostra_domanda(domanda, numero, totale)
       - Stampa la domanda formattata con le opzioni (a, b, c, d)
       - numero e totale servono per mostrare "Domanda 2/5"
 
    3. verifica_risposta(domanda, risposta_utente)
       - Converte la lettera (a,b,c,d) in indice (0,1,2,3)
       - Confronta con l'indice della risposta corretta
       - Restituisce True se corretta, False altrimenti
 
    4. calcola_risultati(domande, risposte, punti_per_domanda=10)
       - Calcola il punteggio totale
       - Restituisce un dizionario con: corrette, totale, punteggio, 
         punteggio_max, percentuale, dettaglio (lista di True/False)
 
    5. mostra_risultati(risultati)
       - Stampa il riepilogo finale con punteggio e valutazione
 
    6. valutazione(percentuale)
       - Restituisce una stringa di valutazione basata sulla percentuale
       - >= 90: "Eccellente!", >= 70: "Ottimo!", >= 50: "Sufficiente",
         < 50: "Da ripassare..."
         
         
SUGGERIMENTI:

    - Per convertire "a" -> 0, "b" -> 1, ecc.: usa ord(lettera) - ord("a")

      ord("a") = 97, ord("b") = 98, quindi ord("b") - ord("a") = 1

    - Per convertire 0 -> "a", 1 -> "b", ecc.: usa chr(indice + ord("a"))

    - enumerate() restituisce (indice, elemento) durante l'iterazione

    - Per la percentuale: (corrette / totale) * 10
    
    


OUTPUT ATTESO:

    Il programma deve produrre un output simile a questo:

    ========================================

      QUIZ DI PYTHON - 5 domande

    ========================================

    Domanda 1/5: Quale funzione stampa a schermo in Python?

      a) echo()

      b) write()

      c) console.log()

      d) print()

    Risposta: d

    ✓ Corretto! +10 punti



    Domanda 2/5: Quale tipo di dato rappresenta 3.14?

      a) str

      b) int

      c) bool

      d) float

    Risposta: b

    ✗ Sbagliato! La risposta corretta era: d) float



    ... (altre domande) ...



    ========================================

      RISULTATI FINALI

    ========================================

      Risposte corrette: 4/5

      Punteggio: 40/50

      Percentuale: 80.0%

      Valutazione: Ottimo!




"""
