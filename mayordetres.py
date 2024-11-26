#programa que muestra el mayor de tres números

def mayor(v1,v2,v3):
    print("El mayor valor de los tres números es ...")

    if v1>v2 and v1>v3:
        print("El mayor es el ",v1)
    elif v2>v1 and v2>v3:
        print("El mayor es el ",v2)
    else:
        print("El mayor es el ",v3)

def cargar():
    valor1=int(input("Ingresa el primer valor"))
    valor2=int(input("Ingresa el segundo valor"))
    valor3=int(input("Ingresa el tercer valor"))
    mayor(valor1,valor2,valor3)


cargar()#esta seria la funcion pricipal a cargar


    
