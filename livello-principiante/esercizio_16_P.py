""" 
ESERCIZIO 16 - Ciclo for su collezioni

==================

Data la lista nomi = ["Alice", "Bob", "Charlie", "Diana", "Eva"]:


1. Stampa ogni nome con il suo indice usando enumerate()

2. Stampa solo i nomi che hanno più di 4 lettere

3. Crea una nuova lista con tutti i nomi in maiuscolo

4. Crea una nuova lista con la lunghezza di ogni nome

5. Stampa i nomi al contrario (dalla fine all'inizio della lista)
"""

nomi = ["Alice", "Bob", "Charlie", "Diana", "Eva"]

print("============================")
print("Stampa della lista di nomi con il metodo enumerate():")
for indice, valore in enumerate(nomi):
    print(f"{indice}: {valore}")

print("============================")    
print("Nomi con piu' di 4 lettere:")    
for nome in nomi:
    if len(nome) > 4:
        print(nome)
        
print("============================")    
print("Nuova lista con tutti i nomi in maiuscolo:")    
nuova_lista = []
for nome in nomi:
    nuova_lista.append(nome.upper())
print(nuova_lista)

print("============================")    
print("Nuova lista con la lunghezza di tutti i nomi:")    
nuova_lista_2 = []
for nome in nomi:
    nuova_lista_2.append(len(nome))
print(nuova_lista_2)

print("============================")    
print("Stampa dei nomi al contrario dalla fine all'inizio della lista:")    
print(nomi[::-1])



    
        