numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista:", numeros) # imprimiendo contenido de la lista original.
numeros[0] = 111 
print("Nuevo contenido de la lista:", numeros) # contenido de la lista actual.
numeros[1] = numeros[4]
numeros[4] = numeros[1]  # copiando el valor del quinto elemento al segundo
print("Nuevo contenido de la lista:", numeros) # imprimiendo el contenido de la lista actual.
