"""
ESERCIZIO 25 - Mini-progetto: Registro voti

==================

Crea un programma che gestisce un registro di voti studenti:



1. Crea un dizionario 'registro' dove:

   - Le chiavi sono i nomi degli studenti

   - I valori sono liste di voti



2. Popola il registro con almeno 4 studenti e 3-5 voti ciascuno



3. Crea le seguenti funzioni:

   - media_studente(registro, nome): calcola la media di uno studente

   - migliore_studente(registro): trova lo studente con la media più alta

   - stampa_registro(registro): stampa una tabella formattata con nome, voti e media di ogni studente

   - aggiungi_voto(registro, nome, voto): aggiunge un voto a uno studente  (crea lo studente se non esiste)



4. Testa tutte le funzioni e stampa il registro completo
"""

registro = {
    "Olindo Romano": [27, 18, 19, 21, 25],
    "Alberto Stasi": [27, 30, 30, 22],
    "Pietro Maso": [18, 18, 21],
    "Sabrina Misseri": [27, 28, 29, 21, 25],
    "Rudi Guede": [27, 18, 19, 21, 25],
}

# stampa del contenuto del dizionario registro
print(registro)


# funzione per il calcolo della media voti dello studente
def media_studente(registro, nome):
    media_voti_studente = 0.0
    if nome in registro.keys():
        totale_numero_voti_studente = 0
        for nome_studente, voti in registro.items():
            if nome_studente == nome:
                totale_numero_voti_studente = len(voti)
                totale_punteggio_voti = 0
                for voto in voti:
                    totale_punteggio_voti += voto
                media_voti_studente = totale_punteggio_voti / totale_numero_voti_studente
        return media_voti_studente
    else:
        print(f"Lo studente: {nome} non e' presente nel registro...")
        return None


# Versione piu' semplice della funzione
# def media_studente(registro, nome):
#     if nome in registro:
#         voti = registro[nome]
#         return sum(voti) / len(voti)
#     else:
#         print(f"Lo studente: {nome} non è presente nel registro...")
#         return None


# funzione che individua lo studente con la media piu' alta
def migliore_studente(registro):
    media_migliore = 0.0
    studente_migliore = ''
    for studente in registro:
        # ottengo la media dello studente
        media = media_studente(registro, studente)
        if media_migliore <= media:
            media_migliore = media
            studente_migliore = studente

    return studente_migliore


# funzione per la stampa del registro
def stampa_registro(registro):
    print(60 * "-")
    print(f"{'Nome':<20} {'Voti':<30} {'Media':<10}")
    print(60 * "-")

    for nome, voti in registro.items():
        stringa_voti = ", ".join(str(v) for v in voti)
        media = media_studente(registro, nome)
        print(f"{nome:<20} {stringa_voti:<30} {media:<10.2f}")

    print(60 * "-")


# funzione per l'aggiunta di un voto
def aggiungi_voto(registro, nome, voto):
    if nome in registro:
        registro[nome].append(voto)
    else:
        registro[nome] = [voto]


# testing
print(50 * "=")
media_studente(registro, "Pippo")
print(
    f"La media voti dello studente Olindo Romano e': {media_studente(registro, "Olindo Romano")}")
print(
    f"La media voti dello studente Rudi Guede e': {media_studente(registro, "Rudi Guede")}")
print(
    f"La media voti dello studente Alberto Stasi e': {media_studente(registro, "Alberto Stasi")}")
print(
    f"La media voti dello studente Sabrina Misseri e': {media_studente(registro, "Sabrina Misseri")}")

print(50 * "=")
print(f"Lo studente migliore: {migliore_studente(registro)}")

print(50 * "=")
stampa_registro(registro)

print(50 * "=")
aggiungi_voto(registro, "Olindo Romano", 23)
aggiungi_voto(registro, "Alberto Stasi", 26)
aggiungi_voto(registro, "Roberto Gianotto", 24)
print(registro)

