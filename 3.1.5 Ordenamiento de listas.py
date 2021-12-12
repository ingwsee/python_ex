"""
miLista = [8, 10, 6, 2, 4] # lista para ordenar

for i in range(len(miLista) - 1): # necesitamos (5 - 1) comparaciones
    if miLista[i] > miLista[i + 1]: # compara elementos adyacentes
        miLista[i], miLista [i + 1] = miLista[i + 1], miLista[i] # si terminamos aquí significa que tenemos que intercambiar los elementos.
print (miLista)


##########################
"""
miLista = [8, 10, 6, 2, 4] # lista para ordenar
swapped = True # lo necesitamos verdadero (True) para ingresar al bucle while

while swapped:
    swapped = False # no hay swaps hasta ahora
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped= True # ocurrió el intercambio!
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print(miLista)

"""

###############################

miLista = [8, 10, 6, 2, 4]
miLista.sort() 
print(miLista) 


################

miLista = []
swapped = True
num = int (input("¿Cuántos elementos deseas ordenar?:"))

for i in range(num):
    val = float(input("Introduce un elemento de la lista:"))
    miLista.append(val)


#while swapped:
#    swapped = False
#    for i in range(len(miLista) - 1):
#        if miLista[i] > miLista[i + 1]:
#            swapped = True
#            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]
miLista.sort()
print("\nOrdenado:")
print(miLista)


##################


Puntos clave

1. Puedes usar el método sort() para ordenar los elementos de una lista, por ejemplo:
lst = [5, 3, 1, 2, 4]
print(lst)

lst.sort ()
print(lst) # salida: [1, 2, 3, 4, 5]

2.También hay un método de lista llamado reverse(), que puedes usar para invertir la lista, por ejemplo:
lst = [5, 3, 1, 2, 4]
print(lst)
    
lst.reverse()
print (lst) # salida: [4, 2, 1, 3, 5]




Ejercicio 1

¿Cuál es la salida del siguiente fragmento de código?

lst = ["D", "F", "A", "Z"]
lst.sort ()

print(lst)

ercicio 2

¿Cuál es la salida del siguiente fragmento de código?

a = 3
b = 1
c = 2

lst = [a, c, b]
lst.sort ()

print(lst)


Ejercicio 3

¿Cuál es la salida del siguiente fragmento de código?
"""
a = "A"
b = "B"
c = "C"
d = ""

lst = [a, b, c, d]
lst.reverse ()

print(lst)



