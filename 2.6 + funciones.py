# 2.6 Funcion Input - regresa un valor muy utilizabñe
#La función input() es capaz de leer datos que fueron introducidos por el usuario y pasar esos datos al programa en ejecución.
#El programa entonces puede manipular los datos, haciendo que el código sea verdaderamente interactivo.

# INPUT ()

#print("Dime algo...")
#algo = input() # la funcion se invoca sin argumentos y cuando escribimos y damos enter continua el programa
#print("Mmm...", algo, "...¿en serio?")

#    La función input() al ser invocada con un argumento, contiene una cadena con un mensaje.
#    El mensaje será mostrado en consola antes de que el usuario tenga oportunidad de escribir algo.
#    Después de esto input() hará su trabajo.

#Esta variante de la invocación de la función input() simplifica el código y lo hace más claro.

algo = input("Dime algo...") #La función input() puede hacer algo más: puede mostrar un mensaje al usuario sin la ayuda de la función print().
print("Mmm...", algo, "...¿En serio?")

#Se ha dicho antes, pero hay que decirlo sin ambigüedades una vez más: el resultado de la función input() es una cadena.
#Una cadena que contiene todos los caracteres que el usuario introduce desde el teclado. No es un entero ni un flotante.
#Esto significa que no se debe utilizar como un argumento para operaciones matemáticas, por ejemplo, no se pueden utilizar estos datos para elevarlos al cuadrado, para dividirlos entre algo o por algo.


# Probando mensajes de error

#algo = input("Inserta un número: ")
#resultado = algo ** 2.0
#print(algo, "al cuadrado es ", resultado)

#Traceback (most recent call last):
#File ".main.py", line 4, in <module>
#resultado = algo ** 2.0
#TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'
#La última línea lo explica todo, se intentó aplicar el operador ** a 'str' (una cadena) acompañado por un 'float' (valor flotante).
#Esto está prohibido.
#Esto debe de ser obvio â ¿Puedes predecir el valor de "ser o no ser" elevado a la 2 potencia?
#No podemos. Python tampoco puede.
#¿Habremos llegado a un punto muerto? ¿Existirá alguna solución? Claro que la hay

#"Conversión de datos o casting
#Python ofrece dos simples funciones para especificar un tipo de dato y resolver este problema, aquí están: int() y float().
#Sus nombres indican cual es su función:
#   La función int() toma un argumento (por ejemplo, una cadena: int(string)) e intenta convertirlo a un valor entero; si llegase a fallar, el programa entero fallará también (existe una manera de solucionar esto, se explicará mas adelante).
#   La función float() toma un argumento (por ejemplo, una cadena: float(string)) e intenta convertirlo a flotante (el resto es lo mismo).
#Esto es muy simple y muy efectivo. Sin embargo, estas funciones se pueden invocar directamente pasando el resultado de la función input() directamente. No hay necesidad de emplear variables como almacenamiento intermedio.

algo = float(input("Inserta un número: "))
resultado = algo ** 2.0
print(algo, "al cuadrado es", resultado)


algomas = int (input("Inserta un número: "))
resultado = algomas ** 3
print(algomas, "al cubo es", resultado)


# Calculo de la hipotenusa pasando argumentos con variable 

cateto_a = float(input("Inserta la longitud del primer cateto: "))
cateto_b = float(input("Inserta la longitud del segundo cateto "))
hipo = (cateto_a**2 + cateto_b**2) ** .5
print("La longitud de la hipotenusa es: ", hipo)

#y sin variable (cadena)

cateto_a = float(input("Inserta la longitud del primer cateto: "))
cateto_b = float(input("Inserta la longitud del segundo cateto "))
print("La longitud de la hipotenusa es: ", (cateto_a**2 + cateto_b**2) ** .5)


#Operadores de cadenas - introducción     Es tiempo de regresar a estos dos operadores aritméticos: + y *.
#Concatenación ----  El sigo de + (más), al ser aplicado a dos cadenas, se convierte en un operador de concatenación: string + string

nom = input("¿Me puedes dar tu nombre por favor? ")
ape = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias.")
print("\nTu nombre es " + nom + " " + ape + ".")


#Replicación    ---    El signo de * (asterisco), cuando es aplicado a una cadena y a un número (o a un número y cadena) se convierte en un operador de replicación

# Dibuja un rectangulo

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

#Conversión de tipos de datos: str()

#A estas alturas ya sabes como emplear las funciones int() y float() para convertir una cadena a un número.
#Este tipo de conversión no es en un solo sentido. También se puede convertir un numero a una cadena, lo cual es más fácil y rápido, esta operación es posible hacerla siempre.
#Una función capaz de hacer esto se llama str():

# Calculo de la hipotenusa con función str():

cateto_a = float(input("Ingresa la longitud del primer cateto: "))
cateto_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es: " + str((cateto_a**2 + cateto_b**2) ** .5))


