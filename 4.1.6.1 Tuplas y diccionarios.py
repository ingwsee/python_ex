"""# 4.1.6.1 Tuplas y diccionarios
# Tipos de secuencias y mutabilidad

#Debido a que el bucle for es una herramienta especialmente diseñada para iterar a través de las secuencias, podemos definirlas de la siguiente manera: una secuencia es un tipo de dato que puede ser escaneado por el bucle for.

# la mutabilidad - es una propiedad de cualquier tipo de dato en Python que describe su disponibilidad para poder cambiar libremente durante la ejecución de un programa. Existen dos tipos de datos en Python: mutables e inmutables.

#Los datos mutables pueden ser actualizados libremente en cualquier momento, a esta operación se le denomina "in situ".
list.append(1)

# Tupla Los datos inmutables no pueden ser modificados de esta manera. El tipo de datos que se desea tratar ahora se llama tupla. Una tupla es una secuencia inmutable. Se puede comportar como una lista pero no puede ser modificada en el momento.

tuplaVacia = () # ¿Cómo crear una tupla? ¿Es posible crear una tupla vacía? Si, solo se necesitan unos paréntesis:
tuplaUnElemento1 = (1, )
tuplaUnElemento2 = 1., # tupla con coma al final



miTupla = (1, 10, 100, 1000)

print(miTupla[0])
print(miTupla[-1])
print(miTupla[1:])
print(miTupla[:-2])

for elem in miTupla:
    print(elem)

miTupla = (1, 10, 100)

t1 = miTupla + (1000, 10000)
t2 = miTupla * 3

print(len(t2))
print(t1)
print(t2)
print(10 in miTupla)
print(-10 not in miTupla)
"""

var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)
