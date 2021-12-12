"""
ramones = []

# paso 1
#print("1, 2, 3, 4:", ramones)

for i in range (0,6) :
         ramones.append ("Joey Ramone")
         ramones.append ("Johnny Ramone")
         ramones.append ("Dee Dee Ramone")
         ramones.append ("Tomy Ramone")
         del ramones[4]#("Tomy Ramone")
ramones.insert (1, "Marky Ramone")
ramones.insert (0, "CJ Ramone")

    
print("1, 2, 3, 4:", ramones)

# paso 2
#print("Paso 2:", ramones)

# paso 3
#print("Paso 3:", ramones)

# etapa 4
#print("Paso 4:", ramones)

# paso 5
#print("Paso 5:", ramones)


# probando la longitud de la lista
#print("Los Fab", len(ramones))



Puntos clave

1. La lista es un tipo de dato en Python que se utiliza para almacenar múltiples objetos. Es una colección ordenada y mutable de elementos separados por comas entre corchetes, por ejemplo:
miLista = [1, None, True, "Soy una cadena", 256, 0]

2. Las listas se pueden indexar y actualizar , por ejemplo:
miLista  = [1, 1, None, True, 'Soy una cadena', 256, 0]
print(miLista [3]) # salida: soy una cadena
print(miLista  [-1]) # salida: 0

miLista  [1] = '?'
print (miLista) # salida: [1, '?', True, 'Soy una cadena', 256, 0]

miLista.insert (0, "first")
miLista.append ("last")
print (miLista ) # salida: ['first', 1, '?', True, 'Soy una cadena', 256, 0, 'last'] 

3. Las listas pueden estar anidadas, por ejemplo: miLista = [1, 'a', ["lista", 64, [0, 1], False]].

4. Los elementos de la lista y las listas se pueden eliminar, por ejemplo:
miLista = [1, 2, 3, 4]
del miLista[2]
print(miLista) # salida: [1, 2, 4]

del miLista  # borra toda la lista 

5.Las listas pueden ser iteradas mediante el uso del bucle for, por ejemplo:
miLista = ["blanco", "purpura", "azul", "amarillo", "verde"]

for color in miLista :
    print(color) 

6. La función len() se puede usar para verificar la longitud de la lista, por ejemplo:
miLista = ["blanco", "purpura", "azul", "amarillo", "verde"]
print(len(miLista)) # la salidas es 5

del miLista[2]
print (len(miLista)) # la salidas es 4 

7. Una invocación típica de función tiene el siguiente aspecto: resultado = funcion(argumento), mientras que una invocación típica de un método se ve así: resultado = data.method(arg).



Ejercicio 1

¿Cuál es la salida del siguiente fragmento de código?
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)

print(lst) 

[6, 2, 3, 4, 5, 1]

Ejercicio 2

¿Cuál es la salida del siguiente fragmento de código?

lst = [1, 2, 3, 4, 5]
lst2 = []
agregar = 0

for number in lst:
    agregar += number
    lst2.append (agregar)

print(lst2) 

Ejercicio 3

¿Qué sucede cuando ejecutas el siguiente fragmento de código?

lst = []
del lst
print(lst) 

Ejercicio 4
"""
#¿Cuál es la salida del siguiente fragmento de código?
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst)) 



