def presentacion():
    print("Programa que permite cargar dos valores por teclado")
    print("Efectúa la suma de los valores")
    print("Muestra el resultado de la suma")
    print("*********************************")

def cargar_suma():
    valor1=int(input("Ingrese el primer valor..."))
    valor2=int(input("Ingrese el segundo valor..."))
    suma=valor1+valor2
    print("La suma de los dos valores es ", suma)

def finalizar():
    print("***********************")
    print("Gracias por utilizar el programa ...!")

presentacion()
cargar_suma()
finalizar()