# 2.4 Variables

#Python ofrece "cajas" (contenedores) especiales para este propósito, estas cajas son llamadas variables - el nombre mismo sugiere que el contenido de estos contenedores puede variar en casi cualquier forma.

#¿Cuáles son los componentes o elementos de una variable en Python?

 #   Un nombre.
 #   Un valor (el contenido del contenedor).
# El nombre de la variable debe de estar compuesto por MAYUSCULAS, minúsculas, dígitos, y el carácter _ (guion bajo).

#Palabras Clave

#Observa las palabras que juegan un papel muy importante en cada programa de Python.
#['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#Son llamadas palabras clave o (mejor dicho) palabras reservadas. Son reservadas porque no se deben utilizar como nombres: ni para variables, ni para funciones, ni para cualquier otra cosa que se desee crear.

# Creando variables

var = 1
print(var)

var = 1
balance_cuenta = 1000.0
nombreCliente = 'John Doe'
print(var, balance_cuenta, nombreCliente)
print(var)

#var = 1
#print(Var) #var <> Var en Python

#Se puede utilizar print() para combinar texto con variables utilizando el operador + para mostrar cadenas con variables, por ejemplo:
var = "3.7.1"
print("Versión de Python: " + var)

#2.1.4.5

var = 1
print(var)
var = var + 1
print(var)

var = 100
var = 200 + 300
print(var)

#2.1.4.6 Teorema de Pitagoras - variables con forma de datos
print ("Teorema de Pitagoras")
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2)
print ("c=", c)


# manzanas

j=3
m=5
a=6
totalManzanas=j+m+a
print ((j, m, a), sep="\,") 
print ("Total de manzanas=", totalManzanas)


# Operadores Abreviados

x=2
x = x * 2
print (x)

x *= 2


# convertidor de km a millas

kilometros = 12.25
millas = 7.38

millas_a_kilometros = (millas * 1.61)
kilometros_a_millas = (kilometros / 1.61)

print(millas, " millas son ", round(millas_a_kilometros, 2), " kilómetros ")
print(kilometros, " kilómetros son ", round(kilometros_a_millas, 2), " millas ")


# Ecuación 3x3 - 2x2 + 3x - 1 

x=1
x = float(x)
y=(3*x**3-2*x**2+3*x-1)
print("y =", y)

# este programa fue escrito ahora mismos

print ("Este programa calcula los segundos en cierto número de horas determinadas") 

a = 2 # numero de horas
segundos = 3600 # número de segundos en una hora

print("Horas: ", a) #imprime el numero de horas
print("Segundos en horas: ", a * segundos) # se imprime el numero de segundos en determinado numero de horas
print("Adios" )#aquí también se debe de imprimir un "Adiós", pero el programador no tuvo tiempo de escribirlo
#este el es fin del programa que calcula el numero de segundos en 2 horas

# 2.1.5.3
# Esto es
#un comentario
#en varias líneas #

print("Hola!")
