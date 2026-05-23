""" 
ESERCIZIO 11 - Dizionari: creazione e accesso

====================================================

1. Crea un dizionario 'studente' con:

   - nome: "Mario"

   - cognome: "Rossi"

   - eta: 22

   - voti: [28, 30, 25, 27, 30]


2. Stampa il nome dello studente

3. Stampa il terzo voto

4. Stampa tutte le chiavi

5. Stampa tutti i valori

6. Stampa tutte le coppie chiave-valore

7. Usa .get() per cercare la chiave "indirizzo" con default "Non specificato"

"""

studente = {
    "nome": "Mario", 
    "cognome": "Rossi",
    "eta": 22,
    "voti": [28, 30, 25, 27, 30]
}

lista_voti = studente["voti"]

print(studente["nome"])
print(lista_voti[2])
print(studente.keys())
print(studente.values())
print(studente.items())
print(studente.get("indirizzo", "Non specificato"))
