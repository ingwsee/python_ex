
# Arreglos tridimensionales

habitaciones = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
habitaciones[1][9][13] = True # reserva en el segundo edificio, en el décimo piso, habitación 14
habitaciones[0][4][1] = False # desocupa el segundo cuarto en el quinto piso ubicado en el primer edificio

#Verifica si hay disponibilidad en el piso 15 del tercer edificio:
vacante = 0

for numeroHabitacion in range(20):
    if not habitaciones[2][14][numeroHabitacion]:
        vacante += 1

print (habitaciones)


### 3.1.7.6 RESUMEN DE LA SECCIÓN

Puntos clave

1. La comprensión de listas te permite crear nuevas listas a partir de las existentes de una manera concisa y elegante. La sintaxis de una lista de comprensión es la siguiente:
[expresión for elemento in lista if condicional]

El cual es un equivalente del siguiente código:
for elemento in lista:
    if condicional:
        expresión

Este es un ejemplo de una lista de comprensión: el código siguiente crea una lista de cinco elementos con los primeros cinco números naturales elevados a la potencia de 3:
cubos = [num ** 3 for num in range (5)]
print(cubos) # salidas: [0, 1, 8, 27, 64]

2. Puedes usar listas anidadas en Python para crear matrices (es decir, listas bidimensionales). Por ejemplo:
Table - a two-dimensional array

# Una tabla de cuatro columnas y cuatro filas: un arreglo bidimensional (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(tabla)
print(tabla [0][0]) # salida: ':('
print(tabla [0][3]) # salida: ':)'



3. Puedes anidar tantas listas en las listas como desee y, por lo tanto, crear listas n-dimensionales, por ejemplo, arreglos de tres, cuatro o incluso sesenta y cuatro dimensiones. Por ejemplo:
Cubo - un arreglo tridimensional

# Cubo - un arreglo tridimensional (3x3x3)

cubo = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cubo)
print(cubo [0][0][0]) # salida: ':('
print(cubo [2][2][0]) # salida: ':)'

