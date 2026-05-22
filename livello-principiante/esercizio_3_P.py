prezzo_str = "49.99"
prezzo_float = float(prezzo_str)
prezzo_iva = (prezzo_float * 0.22) + prezzo_float
prezzo_intero = int(prezzo_iva)

print(f"Prezzo stringa: {prezzo_str} - tipo: {type(prezzo_str)}")
print(f"Prezzo float: {prezzo_float} - tipo: {type(prezzo_float)}")
print(f"Prezzo con IVA: {prezzo_iva} - tipo: {type(prezzo_iva)}")
print(f"Prezzo intero: {prezzo_intero} - tipo: {type(prezzo_intero)}")