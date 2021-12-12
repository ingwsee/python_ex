"""Paso de argumentos con palabras clave

Python ofrece otra manera de pasar argumentos, donde el significado del argumento esta definido por su nombre, no su posición, a esto se le denomina paso de argumentos con palabras clave.



def presentar (Nombre, Apellido ):
    #presentar(primerNombre = str(input("Ingrese su Nombre:", Nombre, "Ahora su Apellido:", Apellido))
    presentar(Nombre = "Luke", Apellido = "Skywalker")
    print("Hola, mi nombre es", Nombre, Apellido)
presentar (Nombre, Apellido)    

def presentar (primerNombre, segundoNombre):
    print("Hola, mi nombre es", primerNombre, segundoNombre)
    presentar(str = primerNombre = input("Nombre:", str segundoNombre = input("Apellido")))
#presentar(segundoNombre = "Skywalker", primerNombre = "Luke")


##4.1.2.6 combinar argumentos posicionales y de palabras clave

Es posible combinar ambos tipos si se desea, solo hay una regla inquebrantable: se deben colocar primero los argumentos posicionales y después los de palabras clave.

Piénsalo por un momento y entenderás el porque.

Para mostrarte como funciona, se utilizara la siguiente función de tres parámetros:
def suma(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

Su propósito es el de evaluar y presentar la suma de todos sus argumentos.

La función, al ser invocada de la siguiente manera:
suma(1, 2, 3)

suma(3, c = 1, b = 2)

     4.1.2.8 RESUMEN DE SECCIÓN

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
            4.1.2.8 RESUMEN DE SECCIÓN Now
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
            4.1.5.9 RESUMEN DE SECCIÓN
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

1. Se puede pasar información a las funciones utilizando parámetros. Las funciones pueden tener tantos parámetros como sean necesarios.

Un ejemplo de una función con un parámetro:
def hola(nombre):
    print("Hola,", nombre)

hola("Greg")

Un ejemplo de una función de dos parámetros:
def holaTodos(nombre1, nombre2):
    print("Hola,", nombre2)
    print("Hola,", nombre1)

holaTodos("Sebastián", "Felipe")

Un ejemplo de una función de tres parámetros:
def direccion(calle, ciudad, codigoPostal):
    print("Tu dirección es:", calle, ciudad, codigoPostal)

c = input("Calle: ")
cp = input("Código Postal: ")
cd = input("Ciudad: ")

address(c, cd, cp)

2. Puedes pasar argumentos a una función utilizando las siguientes técnicas:

    Paso de argumentos posicionales en la cual el orden de los parámetros es relevante (Ejemplo 1).
    Paso de argumentos con palabras clave en la cual el orden de los argumentos es irrelevante (Ejemplo 2).
    Una mezcla de argumentos posicionales y con palabras clave (Ejemplo 3).

Ejemplo 1
def resta(a, b):
    print(a - b)

resta(5, 2)    # salida: 3
resta(2, 5)    # salida: -3


Ejemplo 2
def resta(a, b):
    print(a - b)

resta(a=5, b=2)    # salida: 3
resta(b=2, a=5)    # salida: 3

Ex. 3
def resta(a, b):
    print(a - b)

resta(5, b=2)    # salida: 3
resta(5, 2)    # salida: 3

Es importante recordar que primero se especifican los argumentos posicionales y después los de palabras clave. Es por esa razón que si se intenta ejecutar el siguiente código:
def resta(a, b):
    print(a - b)

resta(5, b=2)    # salida: 3
resta(a=5, 2)    # Syntax Error

Python no lo ejecutará y marcará un error de sintaxis SyntaxError.



3. Se puede utilizar la técnica de argumentos con palabras clave para asignar valores predefinidos a los argumentos:
def nombre(nombre, apellido="Pérez"):
    print(nombre, apellido)

nombre("Andy")    # salida: Andy Pérez
nombre("Bety", "Rodríguez")    # salida: Bety Johnson (el argumento de palabra clave es reemplazado por " Rodríguez ")



Ejercicio 1

¿Cuál es la salida del siguiente código?
def intro(a="James Bond", b="Bond"):
    print("Mi nombre es", b + ".", a + ".")

intro()


Ejercicio 2

¿Cuál es la salida del siguiente código?
def intro(a="James Bond", b="Bond"):
    print("Mi nombre es", b + ".", a + ".")

intro(b="Sergio López")


Ejercicio 3

¿Cuál es la salida del siguiente fragmento de código?
def intro(a, b="Bond"):
    print("Mi nombre es", b + ".", a + ".")

intro("Susan")


Ejercicio 4

¿Cuál es la salida del siguiente código?
def suma(a, b=2, c):
    print(a + b + c)

suma(a=1, c=3)

SyntaxError - a non-default argument (c) follows a default argument (b=2)

"""
