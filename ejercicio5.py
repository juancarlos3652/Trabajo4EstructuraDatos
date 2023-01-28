def cadenadedigitos(cadena):
    if cadena.isdigit()==True:
        lista=cadena.split()
        max=lista[0]
        for x in lista:
            if len(x)>len(max):
                max=x
    else:
        print("no es una cadena de digitos")
    
a="20312312 43213210 55215210"

#print(a.isdigit())
print(cadenadedigitos(a))


