""" 
1. Crea una funzione crea_profilo(**kwargs) che riceve dati di un utente
   come keyword arguments e restituisce un dizionario.
   
   Esempio: crea_profilo(nome="Mario", eta=30, citta="Roma")
   Output: {"nome": "Mario", "eta": 30, "citta": "Roma"}

2. Crea una funzione stampa_configurazione(**kwargs) che stampa ogni
   chiave-valore formattato. Se non ci sono argomenti, stampa
   "Configurazione vuota".
"""

def crea_profilo(**kwargs):
   if not kwargs:
      print("Non ci sono argomenti in ingresso.")
      return None
   else:
      return kwargs


def stampa_configurazione(**kwargs):
   if not kwargs:
      print("Configurazione vuota")
      return None
   else:
      for k,v in kwargs.items():
         print(f"{k}: {v}")
 
 
print(50*"=")
print(crea_profilo(argomento1="test1", argomento2="test2"))
print(50*"=")
stampa_configurazione(argomento1="test1", argomento2="test2")
print(50*"=")