#f="Hoooolaa"
#print(f.count("o"))
cadenaPalabras = 'Desocupado lector: sin juramento me podrás creer que quisiera este libro '
cadenaPalabras += 'como hijo del entendimiento fuera el más hermoso, el más gallardo y más discreto que pudiera imaginarse'
listaPalabras = cadenaPalabras.split()

frecuenciaPalab = [listaPalabras.count(w) for w in listaPalabras]

print("Cadena\n" + cadenaPalabras +"\n")
print("Lista\n" + str(listaPalabras) + "\n")
print("Frequencias\n" + str(frecuenciaPalab) + "\n")
print("Pares\n" + str(list(zip(listaPalabras, frecuenciaPalab))))