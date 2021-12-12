# Rodajas [:]

# Copiando toda la lista
lista1 = [1]
lista2 = lista1[:]
lista1[0] = 2
print(lista2)

# Copiando parte de la lista
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista[1:3]
print(nuevaLista)


#  Rodajas - índices negativos

miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista [1:-1]
print(nuevaLista)

miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista [-1:1]
print(nuevaLista)

#

miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista [:3]
print(nuevaLista)


#

miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista[3:]
print(nuevaLista)

#

miLista = [10, 8, 6, 4, 2]
del miLista[1:3] 
print(miLista)

miLista = [10, 8, 6, 4, 2]
del miLista[:] 
print(miLista)

miLista = [10, 8, 6, 4, 2]
del miLista 
print(miLista)
