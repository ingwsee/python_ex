"""#Comparación: operador de igualdad
#Pregunta: ¿Son dos valores iguales?
#Para hacer esta pregunta, se utiliza el == Operador (igual igual).
#No olvides esta importante distinción:
#    = es un operador de asignación, por ejemplo, a = b assigna a la varable a el valor de b.
#    == es una pregunta ¿Son estos valores iguales?; a == b compara a y b.
#Es un operador binario con enlazado a la izquierda. Necesita dos argumentos y verifica si son iguales.
# (Recuerda este par de literales predefinidos, True y False - También son palabras clave de Python).

#igualdad: el operador no es igual a (==)
print ("comparando igualdad")
var = 0 # asignando 0 a var
print(var == 0)

var = 1 # asignando 1 a var
print(var == 0)

#Desigualdad: el operador no es igual a (!=)
print ("comparando desigualdad")
var = 0 # asignando 0 a var
print(var != 0)
var = 1 # asignando 1 a var
print(var != 0)

# Mayor que > True / False
# Mayor o igual que >=

# TABLA DE PRIORIDADES

#Prioridad 	Operador 	
#1 	        +, - 	         unario
#2            	** 	
#3 	        *, /, % 	 
#4 	        +, - 	         binario
#5 	        <, <=, >, >= 	
#6 	        ==, != 	

"""
#3.1.1.5 LABORATORIO
n= int ( input("Ingrese valor n para comparar igualdad:"))
if n < 100:
    print ("n < 100:",n<100)
elif n > 100:
    print ("n > 100:",n>100)

#print ("n < 100:",n<100, "n >= 100:", n>=100 , sep="\n", end="     ")
