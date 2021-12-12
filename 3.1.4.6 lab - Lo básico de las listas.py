"""listaSombrero = [1, 2, 3, 4, 5,] # Esta es una lista existente de números ocultos en el sombrero.

print("Contenido de la lista original:", listaSombrero)
x = int (input("Ingrese un numero para reemplazar al numero central:")) # Paso 1: escribe una línea de código que solicite al usuario

del listaSombrero[2]  # para reemplazar el número de en medio con un número entero ingresado por el usuario.

listaSombrero[2]=x
del listaSombrero[3]  # Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.

print(listaSombrero)  # Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
"""

miLista = [10, 1, 8, 3, 5]
longitud = len(miLista)

for i in range (longitud // 2):
    miLista[i], miLista[longitud-i-1] = miLista[longitud-i-1], miLista[i]

print(miLista) 
