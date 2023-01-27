
def listaPalabrasDicFrec(listaPalabras):
    frecuenciaPalab = [listaPalabras.count(p) for p in listaPalabras]
    return dict(list(zip(listaPalabras,frecuenciaPalab)))
f="Gokuuuu eeres "
z=listaPalabrasDicFrec(f)
print(z)