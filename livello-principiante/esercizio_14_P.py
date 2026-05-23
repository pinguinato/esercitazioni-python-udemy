""" 
ESERCIZIO 14 - Operatori logici

==================

Dati:

    eta = 25
    reddito = 30000
    ha_garanzia = True


Verifica e stampa se la persona può ottenere un prestito secondo queste regole:

1. Deve avere almeno 18 anni E un reddito superiore a 20000

2. OPPURE deve avere una garanzia

3. Ma NON può avere più di 65 anni

Testa con diversi valori e stampa il risultato di ogni condizione intermedia.
"""

persona_di_test = {
    "eta": 70, 
    "reddito": 30000,
    "ha_garanzia": True
}

if ((persona_di_test["eta"] >= 18 and persona_di_test["reddito"] > 20000) or persona_di_test["ha_garanzia"]) and persona_di_test["eta"] <= 65:
    print("Puo' ottenere un prestito.")
else:
    print("Non puo' ottenere un prestito.")
    
cond1 = persona_di_test["eta"] >= 18 and persona_di_test["reddito"] > 20000
cond2 = persona_di_test["ha_garanzia"]
cond3 = persona_di_test["eta"] <= 65

print(f"Condizione 1 (eta >= 18 AND reddito > 20000): {cond1}")
print(f"Condizione 2 (ha_garanzia): {cond2}")
print(f"Condizione 3 (eta <= 65): {cond3}")
print(f"Risultato: {(cond1 or cond2) and cond3}")
    

