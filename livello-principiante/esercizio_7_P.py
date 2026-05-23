messaggio = "   Ciao, come stai? Io sto BENE!   "
# rimozione degli spazi iniziali e finali della stringa -> Ciao, come stai? Io sto BENE!
print(messaggio.strip()) 
# dividi la stringa in parole usando la funziona split -> ['Ciao,', 'come', 'stai?', 'Io', 'sto', 'BENE!']
print(messaggio.split())
# conta quante parole ci sono 
print(len(messaggio.split())) 
# trova la posizione della parola 'come'
print(messaggio.find('come'))
# verifica se la stringa dopo strip contiene solo lettere
messaggio_1 = messaggio.strip() 
print(messaggio_1.isalpha())
# capitalizza soltanto la prima lettera di ogni parola
print(messaggio.title())
# centra la stringa in un campo di 50 caratteri rimepito con il carattere '-'
print(messaggio.strip().center(50, '-'))

