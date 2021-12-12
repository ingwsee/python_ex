"""# 4.1.5.1 Creando funciones con dos parámetros
# IMC

def imc(peso, altura):
    return peso / altura ** 2

print(imc(70, 1.70))


####

def imc(peso, altura):
    if altura < 1.0 or altura > 2.5 or \
    peso < 20 or peso > 200:
        return None
    
    return peso / altura ** 2

print(imc(352.5, 1.65))

#  4.1.5.3 Creando funciones con tres parámetros - triangulo

def esUnTriangulo(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(esUnTriangulo (1, 1, 1))
print(esUnTriangulo (1, 1, 3))

def esUnTriangulo(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

print(esUnTriangulo(1, 1, 1))
print(esUnTriangulo(1, 1, 3))


def esUnTriangulo (a, b, c):
    return a + b > c and b + c > a and c + a > b

print(esUnTriangulo (1, 1, 1))
print(esUnTriangulo (1, 1, 3))

4.1.5.4 triángulos y el teorema de Pitágoras


def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input("Ingresa la longitud del primer lado: "))
b = float(input("Ingresa la longitud del segundo lado: "))
c = float(input("Ingresa la longitud del tercer lado: "))

if esUnTriangulo(a, b, c):
    print("Felicidades, puede ser un triángulo.")
else:
    print("Lo siento, no puede ser un triángulo.")

def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b

def esUnTrianguloRectangulo(a, b, c):
    if not esUnTriangulo  (a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2

print(esUnTrianguloRectangulo(5, 3, 4))
print(esUnTrianguloRectangulo(1, 3, 4))

# 4.1.5.5 evaluando el campo de un triángulo rectangulo
def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b

def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def campoTriangulo(a, b, c):
    if not esUnTriangulo(a, b, c):
        return None
    return heron(a, b, c)

print(campoTriangulo(1., 1., 2. ** .5))


#4.1.5.6 Creando funciones: factoriales

def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    producto = 1
    for i in range(2, n + 1):
        producto *= i
    return producto

for n in range(1, 6): # probando
    print(n, factorialFun(n))



# 4.1.5.7 Serie Fibonacci

def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

for n in range(1, 10): # probando
    print(n, "->", fib(n))

#  4.1.5.8 Creando funciones: Recursividad

# fibonacci
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
for n in range(1, 20): # probando
    print(n, "->", fib(n))
#fib(20)

# factorial

def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorialFun(n - 1)
for n in range(1, 10): # probando
    print(n, "->", factorialFun(n))


        #print factorialFun(n)
#factorialFun(5)
"""
#     4.1.5.9 RESUMEN DE SECCIÓN

    List of contents
    Module 0
        Back
        Module 0
        0.0.0 Fundamentos de Programaci&oacute;n en Python - Programa del Curso
            Back
            0.0.0 Fundamentos de Programaci&oacute;n en Python - Programa del Curso
            0.0.0.0 Fundamentos de Programación en Python - Programa del Curso
            0.0.0.1 Fundamentos de Programación en Python - Preguntas Frecuentes
            0.0.0.2 Fundamentos de Programación en Python - PCEP
    Module 1
        Back
        Module 1
        1.1.1 Fundamentos de Programaci&oacute;n en Python: Parte 1
            Back
            1.1.1 Fundamentos de Programaci&oacute;n en Python: Parte 1
            1.1.1.1 Fundamentos de Programación en Python: Parte 1
            1.1.1.2 Fundamentos de Programación en Python: Módulo 1
            1.1.2.1 Programación - Fundamentos básicos
            1.1.2.2 Programación - Fundamentos Básicos
            1.1.2.3 Programación - Fundamentos Básicos
            1.1.2.4 Programación - Fundamentos Básicos | Compilación vs. Interpretación
            1.1.2.5 Programación - Fundamentos Básicos | Compilación vs. Interpretación
            1.1.2.6 Programación - Fundamentos Básicos | Compilación vs. Interpretación
            1.1.3.1 Python - una herramienta, no un reptil
            1.1.3.2 Python - una herramienta, no un reptil
            1.1.3.3 Python - una herramienta, no un reptil | ¿Por qué Python?
            1.1.3.4 Python - una herramienta, no un reptil | ¿Por qué Python?
            1.1.4.1 Python 2 vs. Python 3
            1.1.4.2 Hay más de un Python: CPython y Cython
            1.1.4.3 Hay más de un Python: Jython, PyPy, and RPython
        1.2.1 Comienza tu viaje en Python
            Back
            1.2.1 Comienza tu viaje en Python
            1.2.1.1 Comienza tu viaje en Python
            1.2.1.2 Comienza tu viaje en Python | Descargando e instalando Python
            1.2.1.3 Comienza tu viaje en Python
            1.2.1.4 Comienza tu viaje en Python
            1.2.1.5 Comienza tu viaje en Python
            1.2.1.6 Comienza tu viaje en Python
            1.2.1.7 Comienza tu viaje en Python
            1.2.1.8 Comienza tu viaje en Python
        1.3.1 Interfaces del curso
            Back
            1.3.1 Interfaces del curso
            1.3.1.1 Interfaces del curso
            1.3.1.2 Interfaces del curso
            1.3.1.3 Finalización del Módulo
        1.4.1 Module 1 Quiz Quiz
            Back
            1.4.1 Module 1 Quiz
            1.4.1.1 Module 1 Quiz Quiz
    Module 2
        Back
        Module 2
        2.1.1 Fundamentos de Programaci&oacute;n en Python: M&oacute;dulo 2
            Back
            2.1.1 Fundamentos de Programaci&oacute;n en Python: M&oacute;dulo 2
            2.1.1.1 Fundamentos de Programación en Python: Módulo 2
            2.1.1.2 Tu primer programa
            2.1.1.3 Tu primer programa
            2.1.1.4 Tu primer programa
            2.1.1.5 Tu primer programa
            2.1.1.6 Tu primer programa
            2.1.1.7 LABORATORIO: La función print() Lab
            2.1.1.8 Tu primer programa
            2.1.1.9 Tu primer programa
            2.1.1.10 Tu primer programa
            2.1.1.11 Tu primer programa
            2.1.1.12 Tu primer programa
            2.1.1.13 Tu primer programa
            2.1.1.14 Tu primer programa
            2.1.1.15 Tu primer programa
            2.1.1.16 Tu primer programa
            2.1.1.17 Tu primer programa
            2.1.1.18 Tu primer programa
            2.1.1.19 LABORATORIO: La función print() Lab
            2.1.1.20 LABORATORIO: Dando formato a la salida Lab
            2.1.2.1 Literales de Python
            2.1.2.2 Literales de Python
            2.1.2.3 Literales de Python
            2.1.2.4 Literales de Python
            2.1.2.5 Literales de Python
            2.1.2.6 Literales de Python
            2.1.2.7 Literales de Python
            2.1.2.8 Literales de Python
            2.1.2.9 Literales de Python
            2.1.2.10 Literales de Python
            2.1.2.11 LABORATORIO: Literales de Python - cadenas Lab
            2.1.2.12 RESUMEN DE LA SECCIÓN
            2.1.3.1 Operadores, herramientas para la manipulación de datos
            2.1.3.2 Operadores, herramientas de manipulación de datos
            2.1.3.3 Operadores, herramientas de manipulación de datos
            2.1.3.4 Operadores, herramientas de manipulación de datos
            2.1.3.5 Operadores, herramientas de manipulación de datos
            2.1.3.6 Operadores, herramientas de manipulación de datos
            2.1.3.7 Operadores, herramientas de manipulación de datos
            2.1.3.8 Operadores, herramientas de manipulación de datos
            2.1.3.9 Operadores, herramientas de manipulación de datos
            2.1.3.10 RESUMEN DE LA SECCIÓN
            2.1.4.1 Variables - cajas en forma de datos
            2.1.4.2 Variables - cajas con forma de datos
            2.1.4.3 Variables - cajas con forma de datos
            2.1.4.4 Variables - cajas con forma de datos
            2.1.4.5 Variables - cajas con forma de datos
            2.1.4.6 Variables - cajas con forma de datos
            2.1.4.7 LABORATORIO: Variables Lab
            2.1.4.8 Variables - cajas con forma de datos
            2.1.4.9 LABORATORIO: Variables: un sencillo convertidor Lab
            2.1.4.10 LABORATORIO: Operadores y expresiones Lab
            2.1.4.11 RESUMEN DE LA SECCIÓN
            2.1.5.1 Comentarios
            2.1.5.2 LABORATORIO: Comentarios Lab
            2.1.5.3 RESUMEN DE SECCIÓN
            2.1.6.1 Cómo hablar con una computadora
            2.1.6.2 Cómo hablar con una computadora
            2.1.6.3 Cómo hablar con una computadora
            2.1.6.4 Cómo hablar con una computadora
            2.1.6.5 Cómo hablar con una computadora
            2.1.6.6 Cómo hablar con una computadora: operadores de cadenas
            2.1.6.7 Cómo hablar con una computadora: operadores de cadenas
            2.1.6.8 Cómo hablar con una computadora: operadores de cadenas
            2.1.6.9 LABORATORIO: Entradas y salidas simples Lab
            2.1.6.10 LABORATORIO: Operadores y expresiones Lab
            2.1.6.11 LABORATORIO: Operadores y expresiones Lab
            2.1.6.12 RESUMEN DE SECCIÓN
            2.1.6.13 Módulo Completado
        2.2.1 Module 2 Quiz Quiz
            Back
            2.2.1 Module 2 Quiz
            2.2.1.1 Module 2 Quiz Quiz
        2.3.1 Module 2 Test Test
            Back
            2.3.1 Module 2 Test
            2.3.1.1 Module 2 Test Test
    Module 3
        Back
        Module 3
        3.1.1 Fundamentos de Programaci&oacute;n en Python: M&oacute;dulo 3
            Back
            3.1.1 Fundamentos de Programaci&oacute;n en Python: M&oacute;dulo 3
            3.1.1.1 Fundamentos de Programación en Python: Módulo 3
            3.1.1.2 Tomando decisiones en Python
            3.1.1.3 Tomando decisiones en Python
            3.1.1.4 Tomando decisiones en Python
            3.1.1.5 LABORATORIO: Preguntas y respuestas Lab
            3.1.1.6 Tomando decisiones en Python
            3.1.1.7 Tomando decisiones en Python
            3.1.1.8 Tomando decisiones en Python
            3.1.1.9 Tomando decisiones en Python
            3.1.1.10 Tomando decisiones en Python
            3.1.1.11 LABORATORIO: Operadores de comparación y ejecución condicional Lab
            3.1.1.12 LABORATORIO: Lo fundamental de la instrucción if-else Lab
            3.1.1.13 LABORATORIO: Lo fundamental de la sentencia if-elif-else Lab
            3.1.1.14 RESUMEN DE LA SECCIÓN (1/2)
            3.1.1.15 RESUMEN DE LA SECCIÓN (2/2)
            3.1.2.1 Ciclos en Python | while
            3.1.2.2 Ciclos en Python | while
            3.1.2.3 LABORATORIO: Lo esencial del ciclo while - Adivina el número secreto Lab
            3.1.2.4 Ciclos en Python | for
            3.1.2.5 Ciclos en Python | for
            3.1.2.6 LABORATORIO: Aspectos fundamentales del ciclo for: el conteo Lab
            3.1.2.7 Control de ciclos en Python | break y continue
            3.1.2.8 Control de ciclo en Python | break y continue
            3.1.2.9 LABORATORIO: La declaración break - Atascado en un ciclo Lab
            3.1.2.10 LABORATORIO: La sentencia continue - El Feo Devorador de Vocales Lab
            3.1.2.11 LABORATORIO: La declaración continue - El Bonito Devorador de Vocales Lab
            3.1.2.12 Ciclos en Python | else
            3.1.2.13 Ciclos en Python | else
            3.1.2.14 LABORATORIO: Lo fundamental del ciclo while Lab
            3.1.2.15 LABORATORIO: Hipótesis de Collatz Lab
            3.1.2.16 RESUMEN DE LA SECCIÓN (1/2)
            3.1.2.17 RESUMEN DE LA SECCIÓN (2/2)
            3.1.3.1 Operaciones lógicas y de bits en Python | and, or, not
            3.1.3.2 Operaciones lógicas y de bits en Python | and, or, not
            3.1.3.3 Operaciones lógicas y de bits en Python
            3.1.3.4 Operaciones lógicas y de bits en Python | Operadores bitwise
            3.1.3.5 Operaciones lógicas y de bits en Python | Desplazamiento de bits
            3.1.3.6 RESUMEN DE LA SECCIÓN
            3.1.4.1 Listas - colecciones de datos
            3.1.4.2 Listas - colecciones de datos | Indexación
            3.1.4.3 Listas - colecciones de datos | Indexación
            3.1.4.4 Listas - colecciones de datos | Operaciones en listas
            3.1.4.5 Listas - colecciones de datos | Operaciones en listas
            3.1.4.6 LABORATORIO: Lo básico de las listas Lab
            3.1.4.7 Listas - colecciones de datos | Funciones y métodos
            3.1.4.8 Listas - colecciones de datos | Métodos de listas
            3.1.4.9 Listas - colecciones de datos | Métodos de listas
            3.1.4.10 Listas - colecciones de datos | listas y bucles
            3.1.4.11 Listas - colecciones de datos | listas y bucles
            3.1.4.12 Listas - colecciones de datos | listas y bucles
            3.1.4.13 LABORATORIO: Lo básico de las listas - The Beatles Lab
            3.1.4.14 RESUMEN DE LA SECCIÓN
            3.1.5.1 Ordenando listas simples - el ordenamiento de burbuja
            3.1.5.2 Ordenando listas simples - el ordenamiento de burbuja
            3.1.5.3 Ordenando listas simples - el ordenamiento de burbuja
            3.1.5.4 RESUMEN DE LA SECCIÓN
            3.1.6.1 Operaciones en listas
            3.1.6.2 Operaciones en listas | rodajas
            3.1.6.3 Operaciones en listas | rodajas
            3.1.6.4 Operaciones en listas | rodajas
            3.1.6.5 Operaciones en listas | rodajas y del(eliminar)
            3.1.6.6 Operaciones en listas | in, not in
            3.1.6.7 Listas - más detalles
            3.1.6.8 Listas - más detalles
            3.1.6.9 LABORATORIO: Operando con listas - conceptos básicos Lab
            3.1.6.10 RESUMEN DE LA SECCIÓN
            3.1.7.1 Listas en aplicaciones avanzadas
            3.1.7.2 Listas en aplicaciones avanzadas | Arreglos
            3.1.7.3 Listas en aplicaciones avanzadas | Arreglos
            3.1.7.4 Listas en aplicaciones avanzadas | Arreglos
            3.1.7.5 Listas en aplicaciones avanzadas | Arreglos
            3.1.7.6 RESUMEN DE LA SECCIÓN
            3.1.7.7 Módulo Completado
        3.2.1 Module 3 Quiz Quiz
            Back
            3.2.1 Module 3 Quiz
            3.2.1.1 Module 3 Quiz Quiz
        3.3.1 Module 3 Test Quiz
            Back
            3.3.1 Module 3 Test
            3.3.1.1 Module 3 Test Quiz
    Module 4 Now
        Back
        Module 4
        4.1.1 Fundamentos de Programaci&oacute;n en Python: M&oacute;dulo 4
            Back
            4.1.1 Fundamentos de Programaci&oacute;n en Python: M&oacute;dulo 4
            4.1.1.1 Fundamentos de Programación en Python: Módulo 4
            4.1.1.2 Funciones
            4.1.1.3 Funciones
            4.1.1.4 Escribir Funciones
            4.1.1.5 Escribir funciones
            4.1.1.6 Funciones
            4.1.1.7 RESUMEN DE SECCIÓN
            4.1.2.1 Como las funciones se comunican con su entorno
            4.1.2.2 Como las funciones se comunican con su entorno
            4.1.2.3 Como las funciones se comunican con su entorno
            4.1.2.4 Como las funciones se comunican con su entorno
            4.1.2.5 Como las funciones se comunican con su entorno
            4.1.2.6 Como las funciones se comunican con su entorno
            4.1.2.7 Como las funciones se comunican con su entorno
            4.1.2.8 RESUMEN DE SECCIÓN
            4.1.3.1 Regresando el resultado de una función
            4.1.3.2 Regresando el resultado de una función
            4.1.3.3 Regresando el resultado de una función
            4.1.3.4 Regresando el resultado de una función
            4.1.3.5 Regresando el resultado de una función
            4.1.3.6 LABORATORIO: Un año bisiesto: escribiendo tus propias funciones Lab
            4.1.3.7 LABORATORIO: ¿Cuántos días?: escribiendo y utilizando tus propias funciones Lab
            4.1.3.8 LABORATORIO: Día del año: escribiendo y utilizando tus propias funciones Lab
            4.1.3.9 LABORATORIO: Números primos: ¿Cómo encontrarlos? Lab
            4.1.3.10 LAB: Convirtiendo el consumo de combustible Lab
            4.1.3.11 RESUMEN DE LA SECCIÓN
            4.1.4.1 Los Alcances (Scopes) en Python
            4.1.4.2 Los Alcances (Scopes) en Python
            4.1.4.3 Alcances (Scopes) en Python | La palabra reservada: global
            4.1.4.4 Los Alcances (Scopes) en Python
            4.1.4.5 RESUMEN DE SECCIÓN
            4.1.5.1 Creando funciones con dos parámetros
            4.1.5.2 Creando funciones con dos parámetros
            4.1.5.3 Creando funciones con tres parámetros
            4.1.5.4 Creando funciones: probando triángulos
            4.1.5.5 Creando funciones: triángulos rectángulos
            4.1.5.6 Creando funciones: factoriales
            4.1.5.7 Creando funciones: Fibonacci
            4.1.5.8 Creando funciones: Recursividad
            4.1.5.9 RESUMEN DE SECCIÓN Now
            4.1.6.1 Tuplas y diccionarios
            4.1.6.2 Tuplas y diccionarios
            4.1.6.3 Tuplas y diccionarios
            4.1.6.4 Tuplas y diccionarios
            4.1.6.5 Tuplas y diccionarios
            4.1.6.6 Tuplas y diccionarios | methods
            4.1.6.7 Tuplas y diccionarios | métodos
            4.1.6.8 Tuplas y diccionarios
            4.1.6.9 Tuplas y diccionarios
            4.1.6.10 RESUMEN SECCIÓN (1/3)
            4.1.6.11 RESUMEN SECCIÓN (2/3)
            4.1.6.12 RESUMEN SECCIÓN (3/3)
            4.1.6.13 PROYECTO: TIC-TAC-TOE Lab
            4.1.6.14 Terminación del Módulo
        4.2.1 Module 4 Quiz Quiz
            Back
            4.2.1 Module 4 Quiz
            4.2.1.1 Module 4 Quiz Quiz
        4.3.1 Module 4 Test Quiz
            Back
            4.3.1 Module 4 Test
            4.3.1.1 Module 4 Test Quiz
        4.4.1 Fundamentos de Programaci&oacute;n en Python - Finalizaci&oacute;n
            Back
            4.4.1 Fundamentos de Programaci&oacute;n en Python - Finalizaci&oacute;n
            4.4.1.1 Fundamentos de Programación en Python - Finalización

    Sandbox

Puntos Clave

1. Una función puede invocar otras funciones o incluso a sí misma. Cuando una función se invoca a si misma, se le conoce como recursividad, y la función que se invoca a si misma y contiene una condición de terminación (la cual le dice a la función que ya no siga invocándose a si misma) es llamada una función recursiva.

2. Se pueden emplear funciones recursivas en Python para crear funciones limpias, elegantes, y dividir el código en trozos más pequeños. Sin embargo, se debe tener mucho cuidado ya que es muy fácil cometer un error y crear una función la cual nunca termine. También se debe considerar que las funciones recursivas consumen mucha memoria, y por lo tanto pueden ser en ocasiones ineficientes.

Al emplear la recursividad, se deben de tomar en cuenta tanto sus ventajas como desventajas.

La función factorial es un ejemplo clásico de como se puede implementar el concepto de recursividad:

# Implementación recursiva de la función factorial
def factorial(n):
    if n == 1:    # la condición de terminación
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4)) # 4 * 3 * 2 * 1 = 24




Ejercicio 1

¿Qué ocurrirá al intentar ejecutar el siguiente fragmento de código y porque?
def factorial(n):
    return n * factorial(n - 1)

print(factorial(4))

La función no tiene una condición de terminación, por lo tanto Python arrojara una excepción (RecursionError: maximum recursion depth exceeded)

Ejercicio 2

¿Cuál es la salida del siguiente fragmento de código?
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)

print(fun(25))
