""" 
ESERCIZIO 22 - F-string avanzate

==================

1. Dato nome = "Python" e versione = 3.12, stampa:

   "Linguaggio: Python, Versione: 3.12"


2. Dato prezzo = 1234.5678, stampa:

   - Con 2 decimali: "1234.57"

   - Con separatore migliaia: "1,234.57"

   - Allineato a destra in un campo di 15 caratteri


3. Data una lista voti = [28, 30, 25, 27], stampa la media con 1 decimale


4. Stampa una tabella formattata con queste colonne (nome, età, città):

   Mario      25    Roma

   Giulia     30    Milano

   Marco      22    Napoli
"""

# Dati iniziali
nome = "Python"
versione = 3.12
prezzo = 1234.5678
voti = [28, 30, 25, 27]
tabella = [
    ('Mario', 25, 'Roma'),
    ('Giulia', 30, 'Milano'),
    ('Marco', 22, 'Napoli')
]


def calcola_media_voti(voti):
    media_da_ritornare = 0.0
    for voto in voti:
        media_da_ritornare += voto

    return (media_da_ritornare / len(voti))


def stampa_tabella(tabella):
    for nome, eta, citta in tabella:
        print(f"\n{nome:<10} {eta:>5} {citta:>10}")


# Stampa -> "Linguaggio: Python, Versione: 3.12"
print(50 * "=")
print(f"Linguaggio: {nome}, Versione: {versione}")

print(50 * "=")
# stampa il prezzo con sole 2 cifre dopo la virgola
print(f"Prezzo con 2 sole cifre decimali: {prezzo:.2f}")
# stampa con separatore di migliaia
print(f"Prezzo con virgola come separatore di migliaia: {prezzo:,.2f}")
# stampa il prezzo con un allineamento a destra in un campo di 15 caratteri
print(f"Prezzo con 2 sole cifre decimali: {prezzo:>15,.2f}")

# stampa la media dei voti con una 1 cifra decimale
print(50 * "=")
media_voti = calcola_media_voti(voti)
print(f"Media dei voti: {media_voti:.1f}")

# stampa di una tabella formattata con lf string
print(50 * "=")
print(32 * "-")
print(f"{'Nome':<10} {'Eta':>5} {'Citta':>10}")
stampa_tabella(tabella)
print(32 * "-")
