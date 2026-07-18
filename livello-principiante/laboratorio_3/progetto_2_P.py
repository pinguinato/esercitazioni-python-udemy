
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

risposte_alle_domande = []


def crea_domande():
    lista_domande = domande
    return lista_domande


def totale_domande(lista):
    return len(lista)


def mostra_domanda(domanda, numero, totale):
    print(f"Domanda {numero}/{totale}: {domanda["testo"]}")
    # stampa le possibilli risposte alla domanda
    for i, opzione in enumerate(domanda["opzioni"]):
        lettera = chr(i + ord("a"))
        print("")
        print(f"  {lettera}) {opzione}")


def verifica_risposta(domanda, risposta_utente):
    print(f"Risposta: {risposta_utente}")
    risposte_alle_domande.append(risposta_utente)
    indice_numerico_della_risposta = ord(risposta_utente.lower()) - ord("a")
    lettera_risposta_corretta = chr(domanda["corretta"] + ord("a"))
    if indice_numerico_della_risposta == domanda["corretta"]:
        print("✓ Corretto! +10 punti.")
        return True
    else:
        print(
            f"✗ Sbagliato! La risposta corretta era: {lettera_risposta_corretta}) {domanda["opzioni"][domanda["corretta"]]}")
        return False


def intestazione():
    print(50 * "=")
    print("")
    print("   QUIZ DI PYTHON - 5 domande")
    print("")
    print(50 * "=")
    print("")


def valutazione(percentuale):
    if percentuale >= 90:
        return "Eccellente!"
    elif percentuale < 90 and percentuale >= 70:
        return "Ottimo!"
    elif percentuale < 70 and percentuale >= 50:
        return "Sufficiente"
    else:
        return "Da ripassare..."


def calcola_risultati(lista_domande, risposte_utente, punti_per_domanda=20):
    risultati = {
        "corrette": 0,
        "totale": totale_domande(lista_domande),
        "punteggio": 0,
        "punteggio_max": punti_per_domanda * totale_domande(lista_domande),
        "percentuale": 0
    }
    totale_punteggio_utente = 0
    corrette = 0

    for domanda, risposta in zip(lista_domande, risposte_utente):
        risposta_utente_tradotta = ord(risposta) - ord("a")
        # print(f"Risposta corretta: {domanda["corretta"]}, Risposta utente: {risposta_utente_tradotta}")
        if domanda["corretta"] == risposta_utente_tradotta:
            totale_punteggio_utente = totale_punteggio_utente + punti_per_domanda
            corrette = corrette + 1

    # memorizzo e aggiorno il valore delle risposte corrette
    risultati["corrette"] = corrette
    # memorizzo e aggiorno il punteggio totale ottenuto dall'utente
    risultati["punteggio"] = totale_punteggio_utente
    # memorizzo e aggiorno il valore della percentuale
    risultati["percentuale"] = (corrette / risultati["totale"]) * 100

    return risultati


def mostra_risultati(risultati):
    print(50 * "=")
    print("")
    print("   RISULTATI FINALI")
    print("")
    print(50 * "=")
    print("")
    print(f"Risposte corrette: {risultati["corrette"]}/{risultati["totale"]}")
    print(f"Punteggio: {risultati["punteggio"]}/{risultati["punteggio_max"]}")
    print(f"Percentuale: {risultati["percentuale"]}%")
    print(f"Valutazione: {valutazione(risultati["percentuale"])}")


def main():
    lista_domande = crea_domande()
    risultati = {}
    intestazione()
    # elenco domande
    mostra_domanda(domande[0], 1, totale_domande(lista_domande))
    verifica_risposta(domande[0], "c")
    mostra_domanda(domande[1], 2, totale_domande(lista_domande))
    verifica_risposta(domande[1], "a")
    mostra_domanda(domande[2], 3, totale_domande(lista_domande))
    verifica_risposta(domande[2], "b")
    mostra_domanda(domande[3], 4, totale_domande(lista_domande))
    verifica_risposta(domande[3], "c")
    mostra_domanda(domande[4], 5, totale_domande(lista_domande))
    verifica_risposta(domande[4], "b")
    risultati = calcola_risultati(lista_domande, risposte_alle_domande, 20)
    print("")
    mostra_risultati(risultati)
    print("")


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
