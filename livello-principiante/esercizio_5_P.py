frase = "Python e' il linguaggio piu' bello del mondo"

print(f"Lunghezza della stringa: {len(frase)}")
print(f"Stringa tutta in maiuscolo: {frase.upper()}")
print(f"Stringa tutta in minuscolo: {frase.lower()}")
print(f"Quante volte compare la lettera o nella stringa: {frase.count('o')}")
print(f"String replace: {frase.replace('bello', 'potente')}")
print(f"La stringa contiene 'Python'? {"Python" in frase}")
print(f"La stringa termina con mondo? {frase.endswith("mondo")}")
