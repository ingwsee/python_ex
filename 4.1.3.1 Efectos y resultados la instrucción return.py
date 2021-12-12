"""
# return sin una expresión
# Feliz año nuevo

def felizAñoNuevo(deseos = True):
    print("Tres ...")
    print("Dos ...")
    print("Uno ...")
    if not deseos:
        return
    
    print("¡Feliz año nuevo!") 
felizAñoNuevo()

# return con una expresión

def funcion_aburrida():
    return 123

x = funcion_aburrida()

print ("La funcion_aburrida ha devuelto su resultado. Es: ", x)

def funcion_aburrida():
    print("'Modo aburrimiento' ON.")
    return 123
    print("¡Esta lección es interesante!")
funcion_aburrida()
print("Esta lección es aburrida ...")

#4.1.3.2 acerca de None

valor = None
if valor == None:
    print("Lo siento, no tienes ningún valor") 

#4.1.3.4 Se puede enviar una lista a una función como un argumento?

def sumaDeLista(lst):
    sum = 0
    
    for elem in lst:
        sum += elem
    
    return sum
print(sumaDeLista([5, 4, 3]))

# ¿Puede una lista ser el resultado de una función?
"""
def strangeListFunction(n):
    strangeList = []
    
    for i in range(0, n):
        strangeList.insert(0, i)
    
    return strangeList

print(strangeListFunction(5))
