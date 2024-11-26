#funcion con parámetros arbitrarios

def promedio(*numeros):#recibe n cantidad de números en una sola instruccion
    return sum(numeros)/len(numeros)

print(f'El promedio es {promedio(10,20,30)}')

print(f'El promedio es {promedio(10,20)}')

print(f'El promedio es {promedio(6)}')