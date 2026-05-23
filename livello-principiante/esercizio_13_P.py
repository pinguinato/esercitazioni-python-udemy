""" 
ESERCIZIO 13 - Condizioni if/elif/else

===============================================

Scrivi un programma che:

1. Assegna un voto numerico (es: voto = 75)

2. Stampa la valutazione secondo questa scala:

   - 90-100: "Eccellente"

   - 80-89: "Ottimo"

   - 70-79: "Buono"

   - 60-69: "Sufficiente"

   - sotto 60: "Insufficiente"

3. Se il voto è superiore a 100 o inferiore a 0, stampa "Voto non valido"


Testa il programma con voti diversi: 95, 82, 75, 55, 105
"""

voti_di_test = [95, 82, 75, 55, 105, -10, 134, 56, 61, 78]
for voto in voti_di_test:
    print(voto)
    if voto > 100 or voto < 0:
        print("Voto non valido")
    elif voto >= 90 and voto <=  100:
        print("Eccellente") 
    elif voto >= 80 and voto <= 89:
        print("Ottimo")
    elif voto >= 70 and voto <= 79:
        print("Buono")
    elif voto >= 60 and voto <= 69:
        print("Sufficiente")
    else:
        print("Insufficiente")