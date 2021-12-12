"""
Puntos clave

1. Hay dos tipos de ciclos en Python: while y for:

    El ciclo while ejecuta una sentencia o un conjunto de declaraciones siempre que una condición booleana especificada sea verdadera, por ejemplo:

    # Ejemplo 1
    while True:
        print("Atascado en un ciclo infinito")

    # Ejemplo 2
    contador = 5
    while contador > 2:
        print(contador)
        contador -= 1

    El ciclo for ejecuta un conjunto de sentencias muchas veces; se usa para iterar sobre una secuencia (por ejemplo, una lista, un diccionario, una tupla o un conjunto; pronto aprenderás sobre ellos) u otros objetos que son iterables (por ejemplo, cadenas). Puedes usar el ciclo for para iterar sobre una secuencia de números usando la función incorporada range. Mira los ejemplos a continuación:

    # Ejemplo 1
palabra = "Python"
for letter in palabra:
    print(letter,"*")

    # Ejemplo 2
for i in range(1, 10):
      if i % 2 != 0:
        print(i)

#2. Puedes usar las sentencias break y continue para cambiar el flujo de un ciclo:

#    Utiliza break para salir de un ciclo, por ejemplo:

texto = "OpenEDG Python Institute"
for letter in texto:
    if letter == "P":
       break
    print(letter, end= "")



#    Utiliza continue para omitir la iteración actual, y continuar con la siguiente iteración, por ejemplo:

text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end= "")

#3. Los ciclos while y for también pueden tener una cláusula else en Python. La cláusula else se ejecuta después de que el ciclo finalice su ejecución siempre y cuando no haya terminado con break, por ejemplo:

n = 0
while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")

#4. La función range() genera una secuencia de números. Acepta enteros y devuelve objetos de rango. La sintaxis de range() tiene el siguiente aspecto: range(start, stop, step), donde:

    start es un parámetro opcional que especifica el número de inicio de la secuencia (0 por defecto).
    stop es un parámetro opcional que especifica el final de la secuencia generada (no está incluido).
    y step es un parámetro opcional que especifica la diferencia entre los números en la secuencia es (1 por defecto).

#Código de ejemplo:
for i in range(3):
    print(i, end=" ") # salidas: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ") # salidas: 6, 4, 2




#-----------------------

Ejercicio 1

Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el esqueleto de abajo:
for i in range(1, 11):
    # línea de código
        # línea de código 

Solución de muestra:
for i in range(0, 11):
    if i % 2 != 0:
        print(i))

Ejercicio 2

#Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el esqueleto de abajo:
x = 1
while x < 11:
    # line of code
        # line of code
    # line of code

Solución de muestra:
x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1

Ejercicio 3

#Crea un programa con un bucle for y una declaración break. El programa debe iterar sobre los caracteres en una dirección de correo electrónico, salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea. Usa el esqueleto de abajo:
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        # línea de código
    # línea de código
Solución de muestra:

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")


Ejercicio 4

Crea un programa con un bucle for y una declaracióncontinue. El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla. Usa el esqueleto de abajo:

for digit in "0165031806510":
    if digit == "0":
        # línea de código
        # línea de código
    # línea de código 

Solución de muestra:

for digit in "0165031806510":
   if digit == "0":
       print("x", end="")
       continue
   print(digit, end="")



Ejercicio 5

¿Cuál es la salida del siguiente código?

n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)

4
3
2
0 

Ejercicio 6

¿Cuál es la salida del siguiente código?

n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)

-1
0
1
2
3 

Ejercicio 7

¿Cuál es la salida del siguiente código?
"""
for i in range(0, 6, 3):
    print(i)
"""
0
3

Prev Next

"""
