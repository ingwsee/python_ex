#¿Qué es un diccionario? El diccionario es otro tipo de estructura de datos de Python. No es una secuencia (pero puede adaptarse fácilmente a un procesamiento secuencial) y además es mutable
"""
En el mundo de Python, la palabra que se esta buscando se denomina clave(key). La palabra que se obtiene del diccionario es denominada valor.

Esto significa que un diccionario es un conjunto de pares de claves y valores. Nota:

    Cada clave debe de ser única. No es posible tener una clave duplicada.
    Una clave puede ser un tipo de dato de cualquier tipo: puede ser un número (entero o flotante), o incluso una cadena.
    Un diccionario no es una lista. Una lista contiene un conjunto de valores numerados, mientras que un diccionario almacena pares de valores.
    La función len() aplica también para los diccionarios, regresa la cantidad de pares (clave-valor) en el diccionario.
    Un diccionario es una herramienta de un solo sentido. Si fuese un diccionario español-francés, podríamos buscar en español para encontrar su contraparte en francés mas no viceversa. 

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
numerosTelefono = {'jefe' : 5551234567, 'Suzy' : 22657854310}
diccionarioVacio = {}

print(dict)
print(numerosTelefono)
print(diccionarioVacio)


dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
words = ['gato', 'leon', 'caballo']

for word in words:
    if word in dict:
        print(word, "->", dict[word])
    else:
        print(word, "no está en el diccionario")





#4.1.6.6 ¿Cómo utilizar un diccionario? El método keys() El método retorna o regresa una lista de todas las claves dentro del diccionario.

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for key in dict.keys():
    print(key, "->", dict[key])


# La función sorted()
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for key in sorted(dict.keys()):
    print(key, "->", dict[key])

# ¿Cómo utilizar un diccionario? Los métodos item() y values()

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for spanish, french in dict.items():
    print(spanish, "->", french)

# values
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for french in dict.values():
    print(french)


dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dict['gato'] = 'minou'
print(dict)


dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dict['cisne'] = 'cygne'
print(dict)

#También es posible insertar un elemento al diccionario utilizando el método update(), por ejemplo:
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dict.update({"pato" : "canard"})
print(dict)


# Eliminado claves

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
del dict['perro']
print(dict)

#Para eliminar el ultimo elemento de la lista, se puede emplear el método popitem():
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dict.popitem()
print(dict)    # outputs: {'gato' : 'chat', 'perro' : 'chien'}
"""
# estudiantes promedios

grupo = {}

while True:
    nombre = input("Ingresa el nombre del estudiante (o exit para detenerse): ")
    if nombre == 'exit':
        break
    
    calif = int(input("Ingresa la calificación del alumno (0-10): "))
    
    if nombre in grupo:
        grupo[nombre] += (calif,)
    else:
        grupo[nombre] = (calif,)
        
for nombre in sorted(grupo.keys()):
    sum = 0
    contador = 0
    for calif in grupo[nombre]:
        sum += calif
        contador += 1
    print(nombre, ":", sum / contador)
