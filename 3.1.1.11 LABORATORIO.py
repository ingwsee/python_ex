# 3.1.1.11 LABORATORIO: Operadores de comparación y ejecución condicional

# Plantas
"""
entrada = str(input("Ingrese el nombre de la planta:"))
if entrada == "Espatifilo" :
    print ("Si, ¡El Espatifilo es la mejor planta de todos los tiempos!")
elif entrada == "espatifilo" :
    print ("No, ¡quiero un gran Espatifilo!")
else: print ("¡Espatifilo! ¡No" ,entrada) 


# Calculadora de impuestos

ingreso=float(input("Ingrese el ingreso anual:"))
if ingreso <= 85528 and ingreso >3090:
    impuesto = float (ingreso)*0.18-556.2 
    impuesto=round(impuesto, 0)
    print("El impuesto es:", impuesto, "pesos")
          
if ingreso > 85528:
    impuesto=float(14839.2+(0.32*(ingreso-85528)))
    impuesto=round(impuesto, 0)
    print("El impuesto es: ", impuesto, "pesos")

elif ingreso < 3090:
    print ("Usted no paga impuestos")
    

# calculador año bisiesto
  
año = int(input("Introduzca un año:"))

if (año%4!=0):
    print ("el año es comun")    
elif (año%100!=0):
    print ("el año es bisiesto")    
    print ("el año es comun")
else:
    print ("el año es bisiesto")

#-------------------------------------

#Puntos clave

#1. Los operadores de comparación (o también denominados relacionales) se utilizan para comparar valores. La siguiente tabla ilustra cómo funcionan los operadores de comparación, asumiendo que x=0, y=1 y z=0:
#Operador 	Descripción 	Ejemplo
#== 	Devuelve si los valores de los operandos son iguales, y False de lo contrario. 	
#x == y # False
#x == z # True
#!= 	Devuelve True si los valores de los operandos no son iguales, y False de lo contrario. 	
#x != y # True
#x != z # False
#> 	DevuelveTrue si el valor del operando izquierdo es mayor que el valor del operando derecho, y False de lo contrario. 	
#x > y # False
#y > z # True
#< 	Devuelve True si el valor del operando izquierdo es menor que el valor del operando derecho, y False de lo contrario. 	
#x < y # True y < z # False
#≥ 	Devuelve True si el valor del operando izquierdo es mayor o igual al valor del operando derecho, y False de lo contrario. 	
#x >= y # False
#x >= z # True
#y >= z # True
#≤ 	Devuelve True si el valor del operando izquierdo es menor o igual al valor del operando derecho, y False de lo contrario. 	
#x <= y # True x <= z # True
#y <= z # False

#2. Cuando desea ejecutar algún código solo si se cumple una determinada condición, puede usar una declaración condicional:

#    Una única declaración if, por ejemplo:
#    x = 10

#    if x == 10: # condición
#        print("x es igual a 10") # ejecutado si la condición es verdadera
#    Una serie de declaraciones if, por ejemplo:
#    x = 10
#    if x > 5: # condición uno
#        print("x es mayor que 5") # ejecutado si la condición uno es verdadera
#    if x <10: # condición dos
#        print("x es menor que 10") # ejecutado si la condición dos es verdadera
#    if x == 10: # condición tres
#         print("x es igual a 10") # ejecutado si la condición tres es verdadera
#    Cada declaración if se prueba por separado.


#    Una declaración de if-else, por ejemplo:

#    x = 10
#    if x < 10: # condición
#        print ("x es menor que 10") # ejecutado si la condición es Verdadera
#    else:
#        print ("x es mayor o igual a 10") # ejecutado si la condición es False

#    Una serie de declaraciones if seguidas de un else, por ejemplo:
#    x = 10
#    if x > 5: # Verdadero
#        print("x > 5")
#    if x > 8: # Verdadero
#        print("x > 8")
#    if x > 10: # Falso
#        print("x > 10")
#    else:
#        print("Se ejecutará el else")

#    Cada if se prueba por separado. El cuerpo de else se ejecuta si el último if es False.
#    La declaración  if-elif-else, por ejemplo:

#     x = 10

#    if  x == 10: # Verdadero
#        print("x == 10")

 #   if x > 15: # Falso
 #       print("x > 15")

#    elif x > 10: # Falso
#        print("x > 10")

#    elif x > 5: # Verdadero
#        print("x > 5")

#    else:
#        print("No se ejecutará el else")

#    Si la condición para if es False, el programa verifica las condiciones de los bloques elif posteriores: el primer elif que sea True es el que se ejecuta. Si todas las condiciones son False, se ejecutará el bloque else.
#    Declaraciones condicionales anidadas, ejemplo:

#    x = 10

#    if x > 5: # Verdadero
#        if x == 6: # Falso
#            print("anidado: x == 6")
#        elif x == 10: # Verdadero
#            print("anidado: x == 10")
#        else:
#            print("anidado: else")
#    else:
#        print("else")

Puntos Clave: Continuación

Ejercicio 1

¿Cuál es la salida del siguiente fragmento de código?
x = 5
y = 10
z = 8

print(x > y)
print(y > z) 

False
True 

Ejercicio 2

¿Cuál es la salida del siguiente fragmento de código?
x, y, z = 5, 10, 8

print(x > z)
print((y - 5) == x) 

False
True 

Ejercicio 3

¿Cuál es la salida del siguiente fragmento de código?
x, y, z = 5, 10, 8
x, y, z = z, y, x

print(x > z)
print((y - 5) == x) 


Ejercicio 4

¿Cuál es la salida del siguiente fragmento de código?
x = 10

if x == 10:
    print(x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else:
    print("else") 




Ejercicio 5

¿Cuál es la salida del siguiente fragmento de código?
x = "1"

if x == 1:
    print("uno")
elif x == "1":
    if int (x)> 1:
        print("dos")
    elif int (x) < 1:
        print("tres")
    else:
        print("cuatro")
if int (x) == 1:
    print("cinco")
else:
    print("seis") 


Ejercicio 6

¿Cuál es la salida del siguiente fragmento de código?
x = 1
y = 1.0
z = "1"

if x == y:
    print("uno")
if y == int (z):
    print("dos")
elif x == y:
    print("tres")
else:
    print("cuatro") 




"""
