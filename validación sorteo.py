'''Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos 
(utilizando una función que realice dicha suma).'''
def sumaDigitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//100
    return suma

 
num=int(input("Ingresse un caracter entero del 0 al 10, obtendras la sumatoria pero hay un numero prohibido, Adivina cual es: "))
while num!=0:
    print("Suma:",sumaDigitos(num))
    num=int(input("Número a procesar: "))        
