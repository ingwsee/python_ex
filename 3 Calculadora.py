# MOdulo 3 - Calculadora

print(2*2.5)


# Operadores Basicos (+, -, *, /, //, %, **) - uando los datos y operadores se unen, forman juntos expresiones. La expresión más sencilla es el literal.

# exponenciacion **

print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

# multiplicacion

print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

# division

print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)


# division entera //

print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

# division flotante

print(6 // 4)   # el resultado siempre se redondea hacia el valor entero mas bajo
print(6. // 4)

print(-6 // 4)
print(6. // -4)

# Operadores: residuo (módulo - en otros lenguajes) sin equivalente en operadores arit tradicionales - Python % - El resultado de la operación es el residuo que queda de la división entera.

print(14 % 4)
print(12 % 4.5)

# suma

print(-4 + 4)
print(-4. + 8)

# El operador de resta, operadores unarios y binarios

print(-4 - 4)
print(4. - 8)
print(-1.1)

print(+2)

#  2.1.3.7 Operadores, herramientas de manipulación de datos

print (2 + 3 * 5) # la multiplicacion tiene mas jerarquia que la suma

#Operadores y sus enlaces - la mayoria de los operadores de Python tienen enlazado los operadores de izq a der

print(9 % 6 % 2)

# Operadores y sus enlaces: exponenciación

print(2 ** 2 ** 3) # el operador de exponenciación utiliza enlazado hacia la derecha.

# Lista de prioridades operadores

#Prioridad 	Operador 	
#1 	+, - 	unario
#2 	** 	
#3 	*, /, % 	
#4 	+, - 	binario 

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

#Puntos Clave

#1. Una expresión es una combinación de valores (o variables, operadores, llamadas a funciones, aprenderás de ello pronto) las cuales son evaluadas y dan como resultado un valor, por ejemplo, 1+2.

#2. Los operadores son símbolos especiales o palabras clave que son capaces de operar en los valores y realizar operaciones matemáticas, por ejemplo, el * multiplica dos valores: x*y.

#3. Los operadores aritméticos en Python: + (suma), - (resta), * (multiplicación), / (división clásica: regresan un flotante si uno de los valores es de este tipo), % (módulo: divide el operando izquierdo entre el operando derecho y regresa el residuo de la operación, por ejemplo, 5%2=1), ** (exponenciación: el operando izquierdo se eleva a la potencia del operando derecho, por ejemplo, 2**3=2*2*2=8), // (división entera: retorna el numero resultado de la división, pero redondeado al numero entero inferior más cercano, por ejemplo, 3//2.0=1.0).

#4. Un operador unario es un operador con solo un operando, por ejemplo, -1, o +3.

#5. Un operador binario es un operador con dos operados, por ejemplo, 4+5, o 12%5.

#6. Algunos operadores actúan antes que otros, a esto se le llama - jerarquía de prioridades:

 #   Unario + y - tienen la prioridad más alta.
  #  Después: **, después: *, /, y %, y después la prioridad más baja: binaria + y -.

#7. Las sub-expresiones dentro de paréntesis siempre se calculan primero, por ejemplo, 15-1*(5*(1+2))=0.

#8. Los operadores de exponenciación utilizan enlazado hacia la derecha, por ejemplo, 2**2**3=256.






