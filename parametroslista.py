#funcion con parametros tipo lista
def suma(lista):
    suma=0
    for x in range(len(lista)):
        suma=suma + lista[x]
    return suma
###################################
def mayor(otralista):
    may=otralista[0]
    for x in range(1,len(otralista)):
        if otralista[x]>may:
            may=otralista[x]
    return may
#programa principal desde donde llamos las funciones

listadevalores=[12,3,4,56,78,100]
print("La lista completa es ",listadevalores)

print("La suma de todos los elementos de la lista es ",suma(listadevalores))

print("El número mayor encontrado en la lista es ",mayor(listadevalores))