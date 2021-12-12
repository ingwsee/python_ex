miLista = [0, 3, 12, 8, 2]

print(5 in miLista)
print(5 not in miLista)
print(12 in miLista)


# el mayor de la lista

miLista = [18, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista[0]

for i in range(0, len(miLista)):
   if miLista [i]> mayor:
        mayor = miLista[i]

print(mayor)


# Ahora encontremos la ubicación de un elemento dado dentro de una lista:

miLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Encontrar = int (input("Ingrese el numero que desea encontrar:"))
Encontrado = False

for i in range(len(miLista)):
    Encontrado = miLista[i] == Encontrar
    if Encontrado:
        break

if Encontrado:
    print("Numero encontrado en el índice", i)
else:
    print("El numero ingresado no esta en la lista")



# Loteria

sorteados = [5, 11, 9, 42, 3, 49]
seleccionados = [3, 7, 11, 42, 34, 49]
aciertos = 0

for i in seleccionados:
    if i in sorteados:
        aciertos += 1

print(aciertos)
