""" 
ESERCIZIO 18 - Funzioni base

==================

Crea le seguenti funzioni:


1. saluta(nome) - restituisce "Ciao, [nome]!"

2. area_rettangolo(base, altezza) - restituisce l'area

3. is_pari(numero) - restituisce True se il numero è pari

4. valore_assoluto(numero) - restituisce il valore assoluto senza usare abs()

5. celsius_to_fahrenheit(celsius) - converte da Celsius a Fahrenheit

   (formula: F = C * 9/5 + 32)


Testa ogni funzione con almeno 2 valori diversi.
"""

def saluta(nome):
    print(f"Ciao, {nome}!")


def area_rettangolo(base, altezza):
    return base * altezza


def is_pari(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

    
def valore_assoluto(numero):
    if numero >= 0:
        return numero
    else:
        return numero * -1
    

def celsius_to_fahrenheit(celsius):
    # formula: F = C * 9/5 + 32
    return celsius * 9/5 + 32    


# test delle funzioni con almeno 2 valori...
saluta("Roberto")
saluta("Stefania")

print("=======================")
print(f"Area del rettangolo è: {area_rettangolo(5,4)}")
print(f"Area del rettangolo è: {area_rettangolo(10,6)}")

print("=======================")
print(f"Test is_pari(11): {is_pari(11)}")
print(f"Test is_pari(10): {is_pari(10)}")

print("=======================")
print(f"Valore assoluto di -100: {valore_assoluto(-100)}")
print(f"Valore assoluto di 10: {valore_assoluto(10)}")

print("=======================")
print(f"Test 30 gradi celsius sono {celsius_to_fahrenheit(30)} F°")
print(f"Test 35 gradi celsius sono {celsius_to_fahrenheit(35)} F°")