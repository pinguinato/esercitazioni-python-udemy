

domanda = {
    "testo": "Quale funzione stampa a schermo?",
    "opzioni": ["echo()", "write()", "console.log()", "print()"],
    "corretta": 3
}

domanda_2 = {
    "testo": "Quale tipo di dato rappresenta 3.14?",
    "opzioni": ["str", "int", "bool", "float"],
    "corretta": 3
}

domanda_3 = {
    "testo": "Come si crea una lista in Python?",
    "opzioni": ["lista = new List()", "lista = []", "lista = ()", "lista = set()"],
    "corretta": 1
}

domanda_4 = {
    "testo": "Quale tipo di dato rappresenta True o False?",
    "opzioni": ["str", "int", "bool", "float"],
    "corretta": 2
}

domanda_5 = {
    "testo": "Come si accede al primo elemento di una lista?",
    "opzioni": ["lista[1]", "lista[0]", "lista.first()", "lista.get(0)"],
    "corretta": 1
}


def crea_domande():
    lista_domande = []
    lista_domande.append(domanda)
    lista_domande.append(domanda_2)
    lista_domande.append(domanda_3)
    lista_domande.append(domanda_4)
    lista_domande.append(domanda_5)

    return lista_domande


def totale_domande(lista):
    return len(lista)


def mostra_domanda(domanda, numero, totale):
    # TODO: dobbiamo capire come ricavare il numero corretto della domanda
    print(f"Domanda {numero}/{totale}: {domanda["testo"]}")
    for i, opzione in enumerate(domanda["opzioni"]):
        lettera = chr(i + ord("a"))
        print(f"  {lettera}) {opzione}")


def main():
    print(50 * "=")
    print("")
    print("   QUIZ DI PYTHON - 5 domande")
    print("")
    print(50 * "=")

    # qui dentro ho la lista delle 5 domande
    lista_domande = crea_domande()

    print(lista_domande)

    print(mostra_domanda(domanda_2, 2, totale_domande(lista_domande)))


main()


"""
Domanda 1/5: Quale funzione stampa a schermo in Python?

      a) echo()

      b) write()

      c) console.log()

      d) print()



for i, opzione in enumerate(domanda["opzioni"]):
    lettera = chr(i + ord("a"))    # 0→'a', 1→'b', 2→'c', 3→'d'
    print(f"  {lettera}) {opzione}")


"""
