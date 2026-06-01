"""
============================================

    MINI-PROGETTO 0 | LIVELLO: PRINCIPIANTE

    CONVERTITORE DI UNITA' DI MISURA

============================================

DESCRIZIONE:

    Crea un programma che converte unita' di misura tra diversi sistemi.

    Il programma deve:

    mostrare un menu

    accettare l'input dell'utente

    stampare il risultato della conversione.


    Categorie di conversione supportate:

    1. Lunghezza:   metri <-> piedi, km <-> miglia

    2. Peso:        kg <-> libbre, grammi <-> once

    3. Temperatura: Celsius <-> Fahrenheit

    Questo progetto usa solo: funzioni, if/elif/else, input/print, ciclo while, operazioni matematiche.

PREREQUISITI (concetti che devi conoscere):

    - Funzioni: def, parametri, return

    - Condizionali: if / elif / else

    - Input e output: input(), print(), f-string

    - Operazioni matematiche: +, -, *, /

    - Ciclo while (solo per il menu principale)

    - Conversione di tipo: float(), int()

FUNZIONI DA IMPLEMENTARE:

        1. metri_a_piedi(metri) -> float
        2. piedi_a_metri(piedi) -> float
        3. km_a_miglia(km) -> float
        4. miglia_a_km(miglia) -> float
        5. kg_a_libbre(kg) -> float
        6. libbre_a_kg(libbre) -> float
        7. grammi_a_once(grammi) -> float
        8. once_a_grammi(once) -> float
        9. celsius_a_fahrenheit(celsius) -> float
        10. fahrenheit_a_celsius(fahrenheit) -> float
        11. mostra_menu() -> stampa il menu delle opzioni
        12. chiedi_valore(messaggio) -> float (chiede un numero all'utente)
        13. main() -> funzione principale con il ciclo del programma


FORMULE DI CONVERSIONE:

    - 1 metro  = 3.28084 piedi

    - 1 km     = 0.621371 miglia

    - 1 kg     = 2.20462 libbre

    - 1 grammo = 0.035274 once

    - Celsius -> Fahrenheit: (C * 9/5) + 32

    - Fahrenheit -> Celsius: (F - 32) * 5/9


OUTPUT ATTESO:

    ========================================

      CONVERTITORE DI UNITA' DI MISURA

    ========================================


    Categorie:

      1. Lunghezza

      2. Peso

      3. Temperatura

      0. Esci


    Scelta: 1


    --- Lunghezza ---

      1. Metri -> Piedi

      2. Piedi -> Metri

      3. Km -> Miglia

      4. Miglia -> Km

    Scelta: 1


    Inserisci il valore in Metri: 10

    Risultato: 10.00 Metri = 32.81 Piedi


    ---

    Categorie:

      1. Lunghezza

      ...


SUGGERIMENTI:

    - Ogni funzione di conversione fa UNA sola operazione. Tienile semplici, una riga di codice ciascuna.

    - Per chiedi_valore(), usa try/except per gestire input non numerici.

    - Il ciclo while nel main continua finche' l'utente non sceglie "0".

    - Usa f-string con :.2f per formattare i numeri con 2 decimali.    
"""


def mostra_menu():
    """ 
        Funzione che stampa il menu' iniziale del programma
    """
    print(40 * "=")
    print("")
    print(f"{"   CONVERTITORE UNITA' DI MISURA":>10}")
    print("")
    print(40 * "=")
    print("")
    print("")
    print("Categorie:")
    print("")
    print(" 1. Lunghezza")
    print("")
    print(" 2. Peso")
    print("")
    print(" 3. Temperature")
    print("")
    print(" 0. Esci")
    print("")


def chiedi_valore(messaggio):
    """ 
        Funzione per chiedere un valore, permette di settare un messaggio in input  
    """
    while True:
        try:
            scelta = float(input(messaggio))
            return scelta
        except:
            print("Valore non corretto, riprova!")


# ------------------------------
# 10 funzioni per le conversioni
# ------------------------------
def metri_a_piedi(metri):
    """ 
        1 metro  = 3.28084 piedi
    """
    return metri * 3.28084


def piedi_a_metri(piedi):
    return piedi / 3.28084


def km_a_miglia(km):
    """ 
        1 km     = 0.621371 miglia
    """
    return km * 0.621371


def miglia_a_km(miglia):
    return miglia / 0.621371


def kg_a_libbre(kg):
    """ 
        1 kg     = 2.20462 libbre
    """
    return kg * 2.20462


def libbre_a_kg(libbre):
    return libbre / 2.20462
    

def grammi_a_once(grammi):
    """ 
        1 grammo = 0.035274 once
    """
    return grammi * 0.035274
    

def once_a_grammi(once):
    return once / 0.035274
    
  
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# ------------------------------


def main():
    """
        Funzione che avvia il programma
    """
    while True:
        mostra_menu()

        scelta = chiedi_valore("Scelta: ")

        if scelta == 1:
            print("")
            print("--- Lunghezza ---")
            print("")
            print("1. Metri -> Piedi")
            print("")
            print("2. Piedi -> Metri")
            print("")
            print("3. Km -> Miglia")
            print("")
            print("4. Miglia -> Km")
            print("")

            scelta_lunghezza = chiedi_valore("Scelta: ")

        elif scelta == 2:
            print("")
            print("--- Peso ---")
            print("")
            print("1. Kg -> Libbre")
            print("")
            print("2. Libbre -> Kg")
            print("")
            print("3. Grammi -> Once")
            print("")
            print("4. Once -> Grammi")
            print("")

            scelta_peso = chiedi_valore("Scelta: ")

        elif scelta == 3:
            print("")
            print("--- Temperature ---")
            print("")
            print("1. Celsius -> Fahrenheit")
            print("")
            print("2. Fahrenheit -> Celsius")
            print("")

            scelta_temperature = chiedi_valore("Scelta: ")

        elif scelta == 0:
            print("")
            print("--- Fine del programma ---")
            print("")
            exit()


# testing progetto
main()
