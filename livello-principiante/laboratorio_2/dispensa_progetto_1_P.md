# Dispensa — Progetto 1 Principiante
## Rubrica Telefonica

> **Obiettivo della dispensa**: fornirti gli strumenti necessari per completare
> il progetto. In alcuni casi faremo riferimenti espliciti al codice che verra'
> usato direttamente nella soluzione.

---

## Indice

1. [Variabili e tipi di dato (`str`, `int`, `bool`)](#1-variabili-e-tipi-di-dato-str-int-bool)
2. [Dizionari: il cuore del progetto](#2-dizionari-il-cuore-del-progetto)
3. [Dizionari annidati (dizionario di dizionari)](#3-dizionari-annidati-dizionario-di-dizionari)
4. [Liste e `.append()`](#4-liste-e-append)
5. [Funzioni: `def`, parametri, `return`, valori di default](#5-funzioni-def-parametri-return-valori-di-default)
6. [Condizionali: `if` / `elif` / `else`](#6-condizionali-if--elif--else)
7. [Cicli: `while` e `for`](#7-cicli-while-e-for)
8. [F-string e formattazione tabellare](#8-f-string-e-formattazione-tabellare)
9. [Operatore `in` e metodi dei dizionari](#9-operatore-in-e-metodi-dei-dizionari)
10. [Metodi delle stringhe: `.lower()`](#10-metodi-delle-stringhe-lower)
11. [Riepilogo e consigli](#11-riepilogo-e-consigli)

---

## 1. Variabili e tipi di dato (`str`, `int`, `bool`)

Una **variabile** è un nome che si riferisce a un valore in memoria.

```python
nome = "Mario"       # str  (stringa — testo)
eta = 25             # int  (intero — numero senza decimali)
attivo = True        # bool (booleano — vero o falso)
```

### I 3 tipi usati nel progetto

| Tipo | Descrizione | Esempi |
|---|---|---|
| `str` | Testo tra virgolette | `"Mario"`, `"333-123"`, `""` (vuota) |
| `int` | Numero intero | `0`, `3`, `-1` |
| `bool` | Valore logico | `True`, `False` |

### Verità e falsità (truthy e falsy)

In Python, ogni valore può essere valutato come "vero" o "falso" in un contesto booleano (es: dentro un `if`):

| Valore | Valutazione |
|---|---|
| `""` (stringa vuota) | **Falsy** → `bool("") = False` |
| `"ciao"` (qualsiasi stringa non vuota) | **Truthy** → `bool("ciao") = True` |
| `0` | **Falsy** |
| `42` (qualsiasi numero diverso da 0) | **Truthy** |
| `{}` (dizionario vuoto) | **Falsy** |
| `{"a": 1}` (dizionario con dati) | **Truthy** |
| `[]` (lista vuota) | **Falsy** |
| `None` | **Falsy** |

Questo è fondamentale nel progetto. Ad esempio, per verificare se un'email è stata fornita:

```python
email = ""
if email:        # email è "" → falsy → False
    print("Ha email")
else:
    print("Nessuna email")
```

---

## 2. Dizionari: il cuore del progetto

Un **dizionario** (`dict`) è una collezione di coppie **chiave: valore**.
È la struttura dati principale del progetto: la rubrica stessa è un dizionario.

### Creazione

```python
# Dizionario vuoto
rubrica = {}

# Dizionario con dati
studente = {"nome": "Mario", "eta": 25, "citta": "Roma"}
```

### Accesso ai valori

```python
studente = {"nome": "Mario", "eta": 25}

# Accesso con parentesi quadre
print(studente["nome"])    # "Mario"
print(studente["eta"])     # 25

# ATTENZIONE: se la chiave non esiste → KeyError!
# print(studente["email"])  # KeyError: 'email'
```

### Aggiunta e modifica

```python
studente = {"nome": "Mario"}

# Aggiungere una nuova chiave
studente["eta"] = 25           # {"nome": "Mario", "eta": 25}

# Modificare un valore esistente
studente["eta"] = 26           # {"nome": "Mario", "eta": 26}

# La sintassi è la STESSA! Se la chiave esiste, sovrascrive.
# Se non esiste, la crea.
```

### Rimozione

```python
studente = {"nome": "Mario", "eta": 25, "citta": "Roma"}

# Metodo 1: del (lancia KeyError se la chiave non esiste)
del studente["citta"]

# Metodo 2: .pop(chiave, default) — più sicuro!
valore = studente.pop("eta", None)     # Restituisce 25 e rimuove la chiave
valore = studente.pop("xyz", None)     # Restituisce None (nessun errore!)
```

### `.pop()` con valore di default

```python
dizionario.pop(chiave, valore_default)
```

- Se `chiave` esiste → la rimuove e restituisce il suo valore.
- Se `chiave` NON esiste → restituisce `valore_default` (nessun errore).

Questo è **molto più sicuro** di `del` perché non causa `KeyError`.

### Metodi principali

| Metodo | Descrizione | Esempio |
|---|---|---|
| `d[chiave]` | Accede al valore | `d["nome"]` → `"Mario"` |
| `d[chiave] = valore` | Aggiunge/modifica | `d["eta"] = 25` |
| `d.get(chiave, default)` | Accede senza errore | `d.get("email", "N/A")` |
| `d.pop(chiave, default)` | Rimuove e restituisce | `d.pop("nome", None)` |
| `d.items()` | Coppie (chiave, valore) | `for k, v in d.items()` |
| `d.keys()` | Solo le chiavi | `list(d.keys())` |
| `d.values()` | Solo i valori | `list(d.values())` |
| `len(d)` | Numero di chiavi | `len({"a": 1, "b": 2})` → `2` |

### `.get()` vs accesso diretto

```python
d = {"nome": "Mario"}

# Accesso diretto: ERRORE se la chiave non esiste
# d["email"]  # KeyError!

# .get() con default: nessun errore
d.get("email", "Non specificato")   # "Non specificato"
d.get("nome", "Non specificato")    # "Mario" (la chiave esiste)
```

> **Riferimento**: [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

---

## 3. Dizionari annidati (dizionario di dizionari)

Nel progetto, la rubrica è un **dizionario che contiene altri dizionari**.
Ogni contatto è una chiave il cui valore è un altro dizionario con i dettagli.

### Struttura

```python
rubrica = {
    "Mario Rossi": {
        "telefono": "333-1234567",
        "email": "mario@email.it"
    },
    "Anna Bianchi": {
        "telefono": "339-7654321",
        "email": "anna@email.it"
    }
}
```

### Accesso a due livelli

```python
# Livello 1: ottieni il dizionario del contatto
contatto = rubrica["Mario Rossi"]
# contatto = {"telefono": "333-1234567", "email": "mario@email.it"}

# Livello 2: ottieni un dato specifico
telefono = rubrica["Mario Rossi"]["telefono"]
# telefono = "333-1234567"

email = rubrica["Mario Rossi"]["email"]
# email = "mario@email.it"
```

### Aggiungere un contatto

```python
# Creiamo il dizionario interno e lo assegniamo come valore
rubrica["Luca Verdi"] = {
    "telefono": "347-1112233",
    "email": ""
}
```

### Modificare un dato

```python
# Modifichiamo il telefono di Mario Rossi
rubrica["Mario Rossi"]["telefono"] = "333-9999999"
```

### Iterare sui contatti

```python
for nome, dati in rubrica.items():
    print(f"{nome}: {dati['telefono']}")
```

Output:
```
Mario Rossi: 333-1234567
Anna Bianchi: 339-7654321
```

---

## 4. Liste e `.append()`

Una **lista** è una collezione ordinata di elementi, indicizzati da 0.

```python
frutti = ["mela", "banana", "arancia"]
print(frutti[0])    # "mela"
print(frutti[-1])   # "arancia" (ultimo elemento)
```

### `.append()` — aggiungere un elemento alla fine

```python
risultati = []              # lista vuota
risultati.append("Mario")   # ["Mario"]
risultati.append("Anna")    # ["Mario", "Anna"]
```

### Nel progetto

La funzione `cerca_contatto` raccoglie i risultati in una lista:

```python
risultati = []
for nome, dati in rubrica.items():
    if termine in nome.lower():
        risultati.append((nome, dati))   # aggiunge una TUPLA
```

### Tuple: mini-liste immutabili

Una **tupla** è come una lista, ma non modificabile. Si crea con le parentesi tonde `()`:

```python
coppia = ("Mario Rossi", {"telefono": "333-123"})
print(coppia[0])    # "Mario Rossi"
print(coppia[1])    # {"telefono": "333-123"}
```

Nel progetto, `risultati.append((nome, dati))` aggiunge una tupla `(nome, dati)`
alla lista dei risultati. Le doppie parentesi sono intenzionali:
- Le esterne sono di `.append(...)`
- Le interne creano la tupla `(nome, dati)`

---

## 5. Funzioni: `def`, parametri, `return`, valori di default

### Ripasso base

```python
def nome_funzione(parametro1, parametro2):
    # corpo
    return risultato
```

### Parametri con valore di default

Un parametro può avere un **valore di default**: se il chiamante non lo specifica,
viene usato il default.

```python
def aggiungi_contatto(rubrica, nome, telefono, email=""):
    #                                             ^^^^^^
    #                                  valore di default: stringa vuota
    rubrica[nome] = {"telefono": telefono, "email": email}
```

Uso:

```python
# Con email (4 argomenti)
aggiungi_contatto(rubrica, "Mario", "333-123", "mario@email.it")

# Senza email (3 argomenti) → email sarà ""
aggiungi_contatto(rubrica, "Luca", "347-111")
```

### Regola: i parametri con default DEVONO essere alla fine

```python
# CORRETTO: prima quelli obbligatori, poi quelli con default
def f(a, b, c="default"):
    pass

# ERRORE: parametro con default prima di uno senza default
# def f(a, b="default", c):  # SyntaxError!
```

### `return True` / `return False`

Le funzioni del progetto restituiscono `True` o `False` per indicare il successo:

```python
def elimina_contatto(rubrica, nome):
    if nome not in rubrica:
        return False    # operazione fallita
    rubrica.pop(nome)
    return True         # operazione riuscita
```

---

## 6. Condizionali: `if` / `elif` / `else`

### Sintassi

```python
if condizione:
    # blocco True
elif altra_condizione:
    # blocco alternativo
else:
    # se nessuna condizione è vera
```

### Operatore ternario (una riga)

Una forma compatta per assegnare un valore in base a una condizione:

```python
# Forma estesa
if dati["email"]:
    email_display = dati["email"]
else:
    email_display = "(nessuna)"

# Forma compatta (operatore ternario)
email_display = dati["email"] if dati["email"] else "(nessuna)"
#               ^^^^^^^^^^^^    ^^^^^^^^^^^^^^^       ^^^^^^^^^^^
#               valore_se_True  condizione            valore_se_False
```

La sintassi è: `valore_true if condizione else valore_false`

> **Riferimento**: [Conditional Expressions](https://docs.python.org/3/reference/expressions.html#conditional-expressions)

---

## 7. Cicli: `while` e `for`

### `for` — iterare su una collezione

```python
# Su una lista
for frutto in ["mela", "banana", "kiwi"]:
    print(frutto)

# Su un dizionario (itera sulle CHIAVI)
for nome in rubrica:
    print(nome)

# Su coppie chiave-valore
for nome, dati in rubrica.items():
    print(f"{nome}: {dati['telefono']}")
```

### `while True` con `break` — menu interattivo

```python
while True:
    print("1. Aggiungi")
    print("2. Cerca")
    print("0. Esci")
    scelta = input("Scelta: ")
    
    if scelta == "0":
        break           # esce dal ciclo
    elif scelta == "1":
        # ... aggiungi
        pass
```

### Iterare e cercare contemporaneamente

Nel progetto, la ricerca itera sui contatti e raccoglie quelli che corrispondono:

```python
for nome, dati in rubrica.items():
    if termine_lower in nome.lower():
        risultati.append((nome, dati))
```

---

## 8. F-string e formattazione tabellare

Per stampare i contatti in modo allineato e leggibile, le f-string offrono
specifiche di **allineamento**:

### Allineamento

```python
nome = "Mario Rossi"

f"{nome:<18}"    # "Mario Rossi       "   ← allineato a sinistra, 18 car.
f"{nome:>18}"    # "       Mario Rossi"   ← allineato a destra
f"{nome:^18}"    # "   Mario Rossi    "   ← centrato
```

### Applicazione: tabella dei contatti

```python
for nome, dati in rubrica.items():
    email = dati["email"] if dati["email"] else "(nessuna)"
    print(f"  {nome:<18} | Tel: {dati['telefono']:<14} | Email: {email}")
```

Output:
```
  Mario Rossi        | Tel: 333-1234567   | Email: mario@email.it
  Anna Bianchi       | Tel: 339-7654321   | Email: anna@email.it
  Luca Verdi         | Tel: 347-1112233   | Email: (nessuna)
```

### Centrare un titolo

```python
print(f"{'RUBRICA TELEFONICA':^50}")
# "                RUBRICA TELEFONICA                "
```

> **Riferimento**: [Format Specification](https://docs.python.org/3/library/string.html#formatspec)

---

## 9. Operatore `in` e metodi dei dizionari

### `in` con i dizionari

L'operatore `in` su un dizionario controlla se un valore è **tra le chiavi** (non i valori!):

```python
rubrica = {"Mario": {...}, "Anna": {...}}

"Mario" in rubrica    # True  (è una chiave)
"Luca" in rubrica     # False (non è una chiave)

# Per controllare l'assenza:
"Luca" not in rubrica  # True
```

### `in` con le stringhe

L'operatore `in` sulle stringhe verifica se una sotto-stringa è **contenuta**:

```python
"anna" in "Anna Bianchi".lower()    # True
"xyz" in "Anna Bianchi".lower()     # False
```

Questo è il meccanismo usato per la **ricerca parziale** dei contatti.

### `.items()` — iterare su chiavi e valori

```python
for chiave, valore in dizionario.items():
    print(f"{chiave}: {valore}")
```

`.items()` restituisce coppie `(chiave, valore)` che possiamo **spacchettare** (unpacking)
direttamente nelle variabili del `for`.

---

## 10. Metodi delle stringhe: `.lower()`

### `.lower()` — tutto minuscolo

```python
"CIAO".lower()          # "ciao"
"Anna Bianchi".lower()  # "anna bianchi"
"ciao".lower()          # "ciao" (già minuscolo, nessun effetto)
```

### Importante: le stringhe sono **immutabili**

`.lower()` **non modifica** la stringa originale. Restituisce una **nuova** stringa:

```python
nome = "MARIO"
nome.lower()        # restituisce "mario" MA non cambia 'nome'!
print(nome)         # "MARIO" (invariato)

nome_lower = nome.lower()   # salva il risultato in una nuova variabile
print(nome_lower)   # "mario"
```

### Ricerca case-insensitive

Per cercare ignorando maiuscole/minuscole, converti **entrambi** in minuscolo:

```python
termine = "ANNA"
nome = "Anna Bianchi"

# Senza .lower(): "ANNA" in "Anna Bianchi" → False!
# Con .lower():   "anna" in "anna bianchi" → True!

if termine.lower() in nome.lower():
    print("Trovato!")
```

### `.strip()` — rimuovere spazi iniziali e finali

```python
"  ciao  ".strip()    # "ciao"
"ciao".strip()        # "ciao" (nessun effetto)
```

Utile per pulire l'input dell'utente: `scelta = input("Scelta: ").strip()`

> **Riferimento**: [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

---

## 11. Riepilogo e consigli

### Mappa concetti → dove li usi nel progetto

| Concetto | Dove lo usi |
|---|---|
| Dizionario vuoto `{}` | Creazione della rubrica |
| Dizionario annidato | Ogni contatto: `rubrica[nome] = {"telefono": ..., "email": ...}` |
| `in` su dizionario | Controllare se un contatto esiste |
| `.pop(chiave, None)` | `elimina_contatto()` — rimozione sicura |
| `.items()` | Iterare sui contatti in `mostra_rubrica()` e `cerca_contatto()` |
| `.get(chiave, default)` | Accesso sicuro a chiavi opzionali |
| `.lower()` | Ricerca case-insensitive in `cerca_contatto()` |
| `in` su stringhe | Ricerca parziale: `"ann" in "anna bianchi"` |
| `def` con default | `aggiungi_contatto(..., email="")` |
| `return True/False` | Indicare successo/fallimento di ogni operazione |
| f-string con `:<N` | Allineamento tabellare in `mostra_rubrica()` |
| Operatore ternario | `email if email else "(nessuna)"` |
| `while True` + `break` | Menu interattivo (versione bonus) |
| Lista + `.append()` | Raccogliere i risultati della ricerca |

### Ordine consigliato di implementazione

1. **`aggiungi_contatto()`** — la più semplice, crea la struttura dati
2. **`mostra_rubrica()`** — così puoi *vedere* cosa hai aggiunto
3. **`cerca_contatto()`** — ricerca con `.lower()` e `in`
4. **`modifica_telefono()`** — accesso a due livelli del dizionario
5. **`elimina_contatto()`** — usa `.pop()`
6. **`statistiche()`** — conta con un ciclo `for`
7. **Testa tutto** con i dati di esempio

### Errori comuni da evitare

- **KeyError**: accedere a una chiave che non esiste → usa sempre `if nome in rubrica` prima.
- **Dimenticare `.lower()`**: la ricerca "anna" non trova "Anna" senza convertire.
- **Modificare il dizionario mentre lo iteri**: non fare `del rubrica[nome]` dentro un `for nome in rubrica`.
- **Default mutabile**: non scrivere `def f(lista=[])`, ma `def f(lista=None)`.

---

### Riferimenti ufficiali

- [Dizionari](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Metodi stringhe](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [F-string](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)
- [`input()`](https://docs.python.org/3/library/functions.html#input)
- [Formattazione](https://docs.python.org/3/library/string.html#formatspec)
- [Operatore ternario](https://docs.python.org/3/reference/expressions.html#conditional-expressions)
