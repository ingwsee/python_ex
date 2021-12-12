"""def mensaje(numero):
    print ("Ingresa el número:", numero)
mensaje()

Funciones con parámetros

El potencial completo de una función se revela cuando puede ser equipada con una interface que es capaz de aceptar datos provenientes de la invocación. Dichos datos pueden modificar el comportamiento de la función, haciéndola mas flexible y adaptable a condiciones cambiantes.

Un parámetro es una variable, pero existen dos factores que hacen a un parámetro diferente:

    Los parámetros solo existen dentro de las funciones en donde han sido definidos, y el único lugar donde un parámetro puede ser definido es entre los paréntesis después del nombre de la función, donde se encuentra la palabra reservada def.
    La asignación de un valor a un parámetro de una función se hace en el momento en que la función se manda llamar o se invoca, especificando el argumento correspondiente.

def funcion(parametro):
    ###

Recuerda que:

    Los parámetros solo existen dentro de las funciones (este es su entorno natural).
    Los argumentos existen fuera de las funciones, y son los que pasan los valores a los parámetros correspondientes.

Existe una clara división entre estos dos mundos.

Enriquezcamos la función anterior agregándole un parámetro, se utilizará para mostrar al usuario el valor de un número que la función pide.


Se tendrá que modificar la definición def de la función, así es como se ve ahora:
def mensaje(numero):
    ###

Esta definición especifica que nuestra función opera con un solo parámetro con el nombre de numero. Se puede utilizar como una variable normal, pero solo dentro de la función - no es visible en otro lugar.

Ahora hay que mejorar el cuerpo de la función:
"""
"""
Se ha hecho buen uso del parámetro. Nota: No se le ha asignado al parámetro algún valor. ¿Es correcto?

Si, lo es.

Un valor para el parámetro llegará del entorno de la función.

Recuerda: especificar uno o mas parámetros en la definición de la función es un requerimiento, y se debe de cumplir durante la invocación de la misma. Se debe proveer el mismo numero de argumentos como haya parámetros definidos.

El no hacerlo provocará un error.
# 4.1.2.2 funcinamiento del entorno de las funciones
def mensaje(numero):
    print("Ingresa un número:", numero)
numero = 1234
mensaje(1)
print(numero)
"""

# 4.1.2.3 entorno de las funciones
def mensaje(que, numero):
    print("Ingresa", que, "número", numero)


mensaje("teléfono", 11)
mensaje("precio", 5)
mensaje("número", "número")
"""
def equipo(posicion, nombre):
    print("Ingresa:", posicion, "Nombre:", nombre)
mensaje("Arquero", San)
mensaje("Medio", Tincho)
mensaje("Delantero", "Maxi")
"""

# 4.1.2.4

# Paso de parámetros posicionales --- La técnica que asigna cada argumento al parámetro correspondiente, es llamada paso de parámetros posicionales, los argumentos pasados de esta manera son llamados argumentos posicionales.

def presentar(primerNombre, segundoNombre):
    
    print("Hola, mi nombre es", primerNombre, segundoNombre)

presentar("Luke", "Skywalker")
presentar("Jesse", "Quick")
presentar("Clark", "Kent")


def presentar(nom, ape):
    nom = str(input("Ingrese su nombre:")
    ape = str(input("Ingrese su apellido:")
    print("Hola, mi nombre es", nom, ape)

presentar(nom, ape)
