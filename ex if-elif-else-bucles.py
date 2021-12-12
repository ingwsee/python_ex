# calcula si el numero ingresado es >0

#numero = float (input("Ingrese un número:"))
#print ("El numero ingresado es:" , numero)
#if numero >0:
#    print ("El número es positivo")
#    print ("Gracias por utilizar la calculadora para identificar numeros")

#if numero == 0:
#    print ("El número es neutro")
#    print ("Gracias por utilizar la calculadora para identificar numeros")
#elif numero <0:
#    print ("El número es negativo")
#    print ("Gracias por utilizar la calculadora para identificar numeros")


#edad = int(input("¿Cuántos años tiene? "))
#if edad < 18:
#    print("Es usted menor de edad")
#    print("Recuerde que está en la edad de aprender")
#else:
#    print("Es usted mayor de edad")
#    print("Recuerde que debe seguir aprendiendo")
#print("¡Hasta la próxima!")

print("Este programa mezcla dos colores.")
print("  r. Rojo      a. Azul")
primera = input("  Elija un color (r o a): ")
if primera == "r":
    print("  a. Azul      v. Verde")
    segunda = input("  Elija otro color (a o v): ")
    if segunda == "a":
        print("La mezcla de Rojo y Azul produce Magenta.")
    else:
        print("La mezcla Rojo y Verde produce Amarillo.")
else:
    print("  v. Verde    r. Rojo")
    segunda = input("  Elija otro color (v o r): ")
    if segunda == "v":
        print("La mezcla de Azul y Verde produce Cian.")
    else:
        print("La mezcla Azul y Rojo produce Magenta.")
print("¡Hasta la próxima!")

#--------------------------------------

edad = int(input("¿Cuántos años tiene? "))
if edad < 0:
    print("No se puede tener una edad negativa")
elif edad >= 0 and edad < 18:
    print("Es usted menor de edad")
else:
    print("Es usted mayor de edad")

    # multiplos de 4 y 2
numero = int(input("Escriba un número: "))
if numero % 2 == 0 and numero % 4 != 0:
    print(f"{numero} es múltiplo de dos")

elif numero % 4 == 0:
        print(f"{numero} es múltiplo de cuatro y de dos")

else:
    print(f"{numero} no es múltiplo de dos")
