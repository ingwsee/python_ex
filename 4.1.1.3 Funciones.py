#  4.1.1.3 Funciones
# 4.1.1.4 Escribir Funciones
"""print("Ingresa un valor: ")
a = int(input())
print("Ingresa un valor: ")
b = int(input())
print("Ingresa un valor: ")
c = int(input())
print ("Usted ha ingresado:", a , b , c)"""


########

"""print("Se comienza aquí.")

def mensaje():
    print("Ingresa un valor por favor: ")
mensaje()
a = int (input())
mensaje()
b = int (input())
mensaje()
c = int (input())
print ("Usted ha ingresado:", a, b, c)

print("Se termina aquí.")
"""

##########
    def hola(nombre):    # definiendo una función
        print("Hola,", nombre)    # cuerpo de la función

nombre = input("Ingresa tu nombre: ")
hola(nombre)    # invocación de la función

"""
    Sandbox

Puntos Clave

1. Una función es un bloque de código que realiza una tarea especifica cuando la función es llamada (invocada). Las funciones son útiles para hacer que el código sea reutilizable, que este mejor organizado y más legible. Las funciones contienen parámetros y pueden regresar valores.

2. Existen al menos cuatro tipos de funciones básicas en Python:

    Funciones integradas las cuales son partes importantes de Python (como lo es la función print()). Puedes ver una lista completa de las funciones integradas de Python en la siguiente liga: https://docs.python.org/3/library/functions.html.
    También están las que se encuentran en módulos pre-instalados (se hablará acerca de ellas en el Módulo 5 de este curso).
    Funciones definidas por el usuario las cuales son escritas por los programadores para los programadores, puedes escribir tus propias funciones y utilizarlas libremente en tu código.
    Las funciones lambda (aprenderás acerca de ellas en el Módulo 6 del curso).

3. Las funciones propias se pueden definir utilizando la palabra reservada def y con la siguiente sintaxis:
def tuFuncion (parámetros opcionales):
    # el cuerpo de la función

Se puede definir una función sin que haga uso de argumentos, por ejemplo:
def mensaje():    # definiendo una función
    print("Hola")    # cuerpo de la función

mensaje()    # invocación de la función 

También es posible definir funciones con argumentos, como la siguiente que contiene un solo parámetro:
def hola(nombre):    # definiendo una función
    print("Hola,", nombre)    # cuerpo de la función


nombre = input("Ingresa tu nombre: ")

hola(nombre)    # invocación de la función

Se hablará mas acerca de funciones con parámetros en la siguiente sección.



Ejercicio 1

La función input() es un ejemplo de:

a) una función definida por el usuario
b) una función integrada

b - es una función integrada

Ejercicio 2

¿Qué es lo que ocurre cuando se invoca una función antes de ser definida? Ejemplo:
hola()

def hola():
    print("hola!")

Se genera una excepción (la excepción NameError)

Ejercicio 3

¿Qué es lo que ocurrirá cuando se ejecute el siguiente código?
def hola():
    print("hola")

hola(5)

Se genera una excepción (la excepción TypeError) - la función hola() no toma argumentos.

"""
