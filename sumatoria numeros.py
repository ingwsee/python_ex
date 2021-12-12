'''Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al finalizar,
 mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. 
Reutilizar la misma función realizada en el ejercicio 2.'''
def sumaDigitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        numero=numero//10
        suma=suma+digito
    return suma

sumatoria=0
num=int (input("Ingrese un caracter de 0 a 10"))
while num!=0:
    print ("Suma =",sumaDigitos(num))
    sumatoria=sumatoria+num
    num=int(input("Número a procesar: "))
    print("Sumatoria:", sumatoria)
    print("Dígitos:", sumaDigitos(sumatoria))
