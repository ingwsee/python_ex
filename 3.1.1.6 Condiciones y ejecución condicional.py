"""#Condiciones y ejecución condicional

#Para tomar tales decisiones, Python ofrece una instrucción especial. Debido a su naturaleza y su aplicación, se denomina instrucción condicional (o declaración condicional).
#Ejecución condicional: La declaración if

#inducciónalsueño = contadordeOvejas
#if contadordeOvejas >= 120: #evalúa una expresión de prueba.
#    dormirSoñar (print ("Me quede dormido")) #se ejecuta si la expresión de prueba es Verdadera. 

#Ejecución condicional: la declaración if-else

#    if condición_true_or_false:
#       ejecuta_si_condición_true
#     else:                          # else es una pa.abra reservada
#       ejecuta_si_condición_false

# La declaración if-else: más de ejecución condicional

#Si el clima es bueno, saldremos a caminar. De lo contrario, iremos al cine. No importa si el clima es bueno o malo, almorzaremos después (después de la caminata o después de ir al cine). 
#    if climaEsBueno:
#       irACaminar()
#    else:
#       irAlCine()
#       almorzar()

# if climaEsBueno:
#    irACaminar()
#    Diviertirse()
# else:
#    irAlCine()
#    disfrutaLaPelicula()
# almorzar()

#Declaraciones if-else anidadas

#if climaEsBueno:
#    if encontramosBuenRestaurante:
#        almorzar()
#    else:
#        comerSandwich() 
#else:
#    if hayBoletosDisponibles:
#        irAlCine()
#    else:
#        irDeCompras()


# Este uso de la declaración if se conoce como anidamiento; recuerda que cada else se refiere al if que se encuentra en el mismo nivel de sangría; se necesita saber esto para determinar cómo se relacionan los ifs y los elses.
# Considera como la sangría mejora la legibilidad y hace que el código sea más fácil de entender y rastrear.

# La declaración elif - presenta otra nueva palabra clave de Python: elif. Como probablemente sospechas, es una forma más corta de else-if.
# elif se usa para verificar más de una condición, y para detener cuando se encuentra la primera declaración verdadera.

#if climaBueno:
#    iraCaminar()
#elif hayBoletosDisponibles:   # elif - de lo contrario
#    IralCine()
#elif mesasLibres:
#    almorzar()
#else:
#    jugarAjedrezEnCasa() 

# La forma de ensamblar las siguientes declaraciones if-elif-else a veces se denomina cascada.

# Ejemplos de codigo
#----------------------------------------------------

#1
#lee dos números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))

#elegir el número más grande
if numero1> numero2:
    nmasGrande = numero1
else:
    nmasGrande = numero2

#imprimir el resultado
print("El número más grande es:", nmasGrande)

"""
#2
#lee dos números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))

# elegir el número más grande
if numero1 > numero2: nmasGrande = numero1
else: nmasGrande = numero2

#imprimir el resultado
print("El número más grande es: ", nmasGrande)

"""
#3

#lee tres números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))
numero3 = int (input("Ingresa el tercer número:"))

#asumimos temporalmente que el primer número
#es el más grande
#lo verificaremos pronto
nmasGrande = numero1

#comprobamos si el segundo número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if   numero2 > nmasGrande:
     nmasGrande = numero2
#comprobamos si el tercer número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero3 > nmasGrande:
    nmasGrande = numero3

#imprimir el resultado
print("El número más grande es:", nmasGrande)


# Pseudocódigo e introducción a los ciclos o bucles -- el pseudocodigo no se puee ejecutar sirve para leer
# La ejecución de una determinada parte del código más de una vez se denomina bucle. El significado de este término es probablemente obvio para ti.

print (" lee tres números y calcula el mayor")
numero1 = int(input("Ingresa el primer número:"))
numero2 = int(input("Ingresa el segundo número:"))
numero3 = int(input("Ingresa el tercer número:"))

# verifica cuál de los números es el mayor
# y pásalo a la variable de mayor número

numeroMayor = max(numero1,numero2,numero3)   # max() funcion de Python

# imprimir el resultado
print("El número más grande es:", numeroMayor) 

#--------------------------------------------
print (" lee tres números y calcula el menor")
numero1 = int(input("Ingresa el primer número:"))
numero2 = int(input("Ingresa el segundo número:"))
numero3 = int(input("Ingresa el tercer número:"))

# verifica cuál de los números es el menor
# y pásalo a la variable de menor número

numeromenor = min(numero1,numero2,numero3)   # min() funcion de Python"""

# imprimir el resultado
print("El número menor es:", numeromenor) 
