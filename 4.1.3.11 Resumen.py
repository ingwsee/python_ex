
Puntos clave

1. Puedes emplear la palabra clave return para decirle a una función que devuelva algún valor. La instrucción return termina la función, por ejemplo:
def multiply(a, b):
    return a * b

print(multiply(3, 4))    # salida: 12

def multiply(a, b):
    return

print(multiply(3, 4))    # salida: None 

2. El resultado de una función se puede asignar fácilmente a una variable, por ejemplo:
 def deseos():
    return "¡Felíz Cumpleaños!"

d = deseos()

print(d)    # salida: ¡Felíz Cumpleaños!

Observa la diferencia en la salida en los siguientes dos ejemplos:
# Ejemplo 1
def deseos():
    print("Mis deseos")
    return "¡Felíz Cumpleaños!"

deseos()    # salida: Mis deseos


# Ejemplo 2
def deseos():
    print("Mis Deseos")
    return "¡Feliz Cumpleaños!"

print(deseos())    # salidas: Mis Deseos
                   #          ¡Feliz Cumpleaños!

3. Puedes usar una lista como argumento de una función, por ejemplo:
def HolaaTodos(myList):
    for nombre in myList:
        print("Hola,", nombre)

HolaaTodos(["Adam", "John", "Lucy"])

4. Una lista también puede ser un resultado de función, por ejemplo:
def createList(n):
    myList = []
    for i in range(n):
        myList.append(i)
    return myList

print(createList(5))




Ejercicio 1

¿Cuál es la salida del siguiente fragmento de código?
def hola():
    return
    print("¡Hola!")

hola()


Ejercicio 2

¿Cuál es la salida del siguiente fragmento de código?
 def isInt(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False 
    
print(isInt(5))
print(isInt(5.0))
print(isInt("5"))


Ejercicio 3

¿Cuál es la salida del siguiente fragmento de código?
 def evenNumLst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst

print(evenNumLst(11))


Ejercicio 4

¿Cuál es la salida del siguiente fragmento de código?
 def listUpdater(lst):
    updList = []
    for elem in lst:
        elem **= 2
        updList.append(elem)
    return updList

l = [1, 2, 3, 4, 5]
print(listUpdater(l))


