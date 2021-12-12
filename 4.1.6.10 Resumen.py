# 4.1.6.10
"""
    Sandbox

Puntos Clave: Tuplas

1. Las Tuplas son colecciones de datos ordenadas e inmutables. Se puede pensar en ellas como listas inmutables. Se definen con paréntesis:
miTupla = (1, 2, True, "una cadena", (3, 4), [5, 6], None)
print(miTupla)

miLista = [1, 2, True, "una cadena", (3, 4), [5, 6], None]
print(miLista)

Cada elemento de la tupla puede ser de un tipo de dato diferente (por ejemplo, enteros, cadenas, boleanos, etc.). Las tuplas pueden contener otras tuplas o listas (y viceversa).

2. Se puede crear una tupla vacía de la siguiente manera:
tuplaVacia = ()
print(type(tuplaVacia))    # salida: <class 'tuple'>

3. La tupla de un solo elemento se define de la siguiente manera:
tuplaUnElemento = ("uno", )    # paréntesis y coma
tuplaUnElemento2 = "uno",     # sin paréntesis, solo la coma

Si se elimina la coma, Python creará una variable no una tupla:
miTup1 = 1, 
print(type(miTup1))    # salida: <class 'tuple'>

miTup2 = 1
print(type(miTup2))    # salida: <class 'int'>

4. Se pueden acceder los elementos de la tupla al indexarlos:
miTupla = (1, 2.0, "cadena", [3, 4], (5, ), True)
print(miTupla[3])    # salida: [3, 4]

5. Las tuplas son inmutables, lo que significa que no se puede agregar, modificar, cambiar o quitar elementos. El siguiente fragmento de código provocará una excepción:
miTupla = (1, 2.0, "cadena", [3, 4], (5, ), True)
miTupla[2] = "guitarra"    # se levanta una excepción TypeError

Sin embargo, se puede eliminar la tupla completa:

miTupla = 1, 2, 3, 
del miTupla
print(miTupla)    # NameError: name 'miTupla' is not defined




6. Puedes navegar a través de los elementos de una tupla con un bucle (Ejemplo 1), verificar si un elemento o no esta presente en la tupla (Ejemplo 2), emplear la función len() para verificar cuantos elementos existen en la tupla (Ejemplo 3), o incluso unir o multiplicar tuplas (Ejemplo 4):
# Ejemplo 1
t1 = (1, 2, 3)
for elem in t1:
    print(elem)

# Ejemplo 2
t2 = (1, 2, 3, 4)
print(5 in t2)
print(5 not in t2)

# Ejemplo 3
t3 = (1, 2, 3, 5)
print(len(t3))

# Ejemplo 4
t4 = t1 + t2
t5 = t3 * 2

print(t4)
print(t5)

EXTRA

También se puede crear una tupla utilizando la función integrada de Python tuple(). Esto es particularmente útil cuando se desea convertir un iterable (por ejemplo, una lista, rango, cadena, etcétera) en una tupla:
miTup = tuple((1, 2, "cadena"))
print(miTup)

lst = [2, 4, 6]
print(lst)    # salida: [2, 4, 6]
print(type(lst))    # salida: <class 'list'>
tup = tuple(lst)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # salida: <class 'tuple'>

De la misma manera, cuando se desea convertir un iterable en una liste, se puede emplear la función integrada de Python denominada list():
tup = 1, 2, 3, 
lst = list(tup)
print(type(lst))    # outputs: <class 'list'>


Puntos Clave: diccionarios

1. Los diccionarios son *colecciones indexadas de datos, mutables y desordenadas. (*En Python 3.6x los diccionarios están ordenados de manera predeterminada.

Cada diccionario es un par de clave : valor. Se puede crear empleado la siguiente sintaxis:
miDictionario = {
    clave1 : valor1,
    clave2 : valor2,
    clave3 : valor3,
    }

2. Si se desea acceder a un elemento del diccionario, se puede hacer haciendo referencia a su clave colocándola dentro de corchetes (ejemplo 1) o utilizando el método get() (ejemplo 2):
polEspDict = {
    "kwiat" : "flor",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

elemento1 = polEspDict["gleba"]    # ejemplo 1
print(elmento1)    # salida: tierra

elemento2 = polEspDict.get("woda")
print(elemento2)    # salida: agua

3. Si se desea cambiar el valor asociado a una clave especifica, se puede hacer haciendo referencia a la clave del elemento, a continuación se muestra un ejemplo:
polEspDict = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

polEspDict["zamek"] = "cerradura"
item = polEspDict["zamek"]    # salida: cerradura 

4. Para agregar o eliminar una clave (junto con su valor asociado), emplea la siguiente sintaxis:
miDirectorioTelefonico = {}    # un diccionario vacio

miDirectorioTelefonico ["Adan"] = 3456783958    # crear o añadir un par clave-valor
print(miDirectorioTelefonico)    # salida: {'Adan': 3456783958}

del miDirectorioTelefonico ["Adan"]
print(miDirectorioTelefonico)    # salida: {}

Además, se puede insertar un elemento a un diccionario utilizando el método update(), y eliminar el ultimo elemento con el método popitem(), por ejemplo:
polEspDict = {"kwiat" : "flor"}

polEspDict = update("gleba" : "tierra")
print(polEspDict)    # salida: {'kwiat' : 'flor', 'gleba' : 'tierra'}

polEspDict.popitem()
print(polEspDict)    # outputs: {'kwiat' : 'flor'}

5. Se puede emplear el bucle for para iterar a través del diccionario, por ejemplo:
polEspDict = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

for item in polEspDict:
    print(item)    # salida: zamek
                   #          woda
                   #          gleba




6. Si deseas examinar los elementos (claves y valores) del diccionario, puedes emplear el método items() por ejemplo:
polEspDict = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

for clave, valor in polEspDict.items():
    print("Pol/Esp ->", clave, ":", valor)

7. Para comprobar si una clave existe en un diccionario, se puede emplear la palabra reservada in:
polEspDict = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

if "zamek" in polEspDict:
    print("SI")
else:
    print("NO")

8. Se puede emplear la palabra reservada del para eliminar un elemento, o un diccionario entero. Para eliminar todos los elementos de un diccionario se debe emplear el método clear():
polEspDict = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

print(len(polEspDict))    # salida: 3
del polEspDict["zamek"]    # elimina un elemento
print(len(polEspDict))    # salida: 2

polEspDict.clear()   # elimina todos los elementos
print(len(polEspDict))    # salida: 0

del polEspDict    # elimina el diccionario

9. Para copiar un diccionario, emplea el método copy():
polEspDict = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

copyDict = polEspDict.copy()

Puntos Claves: Tuplas y diccionarios

Ejercicio 1

¿Que ocurrirá cuando se intente ejecutar el siguiente código?
miTup = (1, 2, 3)
print(miTup[2])

El programa imprimirá 3 en pantalla.

Ejercicio 2

¿Cuál es la salida del siguiente fragmento de código?
tup = 1, 2, 3
a, b, c = tup

print(a * b * c)

El programa imprimirá 6 en pantalla. Los elementos de la tupla tup han sido "desempaquetados" en las variables a, b, y c.

Ejercicio 3

Completa el código para emplear correctamente el método count() para encontrar la cantidad de 2 duplicados en la tupla siguiente.
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicados = # tu código

print(duplicados)    # salida: 4

tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicado)    # salida: 4

Ejercicio 4

Escribe un programa que "una" los dos diccionarios (d1 y d2) para crear uno nuevo (d3).
d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}

for elemento in (d1, d2):
    # tu código

print(d3)

Solución Muestra:
d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}

for elemento in (d1, d2):
    d3.update(elemento)

print(d3)



Ejercicio 5

Escribe un programa que convierta la lista l en una tupla.
l = ["carro", "Ford", "flor", "Tulipán"]

t = # tu código
print(t)

Solución muestra:
l = ["carro", "Ford", "flor", "Tulipán"]

t = tuple(l)
print(t)

Ejercicio 6

Escribe un programa que convierta la tupla colores en un diccionario.
colores = (("verde", "#008000"), ("azul", "#0000FF"))

# tu código

print(colDict)

Solución Muestra:
colores = (("verde", "#008000"), ("azul", "#0000FF"))

colDict = dict(colores)
print(colDict)

Ejercicio 7

¿Que ocurrirá cuando se ejecute el siguiente código?
miDict = {"A":1, "B":2}
copyMiDict = myDict.copy()
miDict.clear()

print(copyMiDict)


Ejercicio 8

¿Cuál es la salida del siguiente programa?
colores = {
    "blanco" : (255, 255, 255),
    "gris"   : (128, 128, 128),
    "rojo"   : (255, 0, 0),
    "verde"  : (0, 128, 0)
    }

for col, rgb in colores.items():
    print(col, ":", rgb)

