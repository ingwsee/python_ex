
# Laboratorio

#a = float (input ("ingresa un valor numerico aquí:   ")) 
#b = float (input ("ingresa un valor numerico aquí:   "))

#print ("suma=",a+b , "\n")# muestra el resultado de la suma aquí 
#print ("resta=",a-b , "\n")# muestra el resultado de la resta aquí
#print ("multiplicación =",a*b , "\n")# muestra el resultado de la multiplicación aquí
#print ("división =",a/b ,"\n")# muestra el resultado de la división aquí
#print("\n¡Eso es todo, amigos!")

# calcula valor expresion y = 1/(x+1/(x+1/(x+1/x))))

#x = float(input("Ingresa el valor para x: "))
# coloca tu código aquí
#y = float (1/(x+1/(x+1/(x+1/x))))
#print("y =", y)



#

#hora = str (input("Hora de inicio (horas): "))
#min = str (input("Minuto de inicio (minutos): "))
#dura = str (("Duración del evento (minutos):  "), hora % min )

# coloca tu código aqui
#print ("tiempo final= ", dura )

# Puntos Clave

#1. La función print() envía datos a la consola, mientras que la función input() obtiene datos de la consola.
#2. La función input() viene con un parámetro inicial: un mensaje de tipo cadena para el usuario. Permite escribir un mensaje antes de la entrada del usuario, por ejemplo:
#nombre = input("Ingresa tu nombre: ")
#print("Hola, " + nombre + ". ¡Un gusto conocerte!")

#3. Cuando la función input() es llamada o invocada, el flujo del programa se detiene, el símbolo del cursor se mantiene parpadeando (le está indicando al usuario que tome acción ya que la consola está en modo de entrada) hasta que el usuario haya ingresado un dato y/o haya presionado la tecla Enter.

#NOTA

#Puedes probar la funcionalidad completa de la función input() localmente en tu máquina. Por razones de optimización, se ha limitado el máximo número de ejecuciones en Edube a solo algunos segundos únicamente. Ve a Sandbox, copia y pega el código que está arriba, ejecuta el programa y espera unos segundos. Tu programa debe detenerse después de unos segundos. Ahora abre IDLE, y ejecuta el mismo programa ahí -¿Puedes notar alguna diferencia?

#Consejo: La característica mencionada anteriormente de la función input() puede ser utilizada para pedirle al usuario que termine o finalice el programa. Observa el siguiente código:
#nombre = input("Ingresa tu nombre: ")
#print("Hola, " + nombre + ". ¡Un gusto conocerte!")

#print("\nPresiona la tecla Enter para finalizar el programa.")
#input()
#print("FIN.")

#3. El resultado de la función input() es una cadena. Se pueden unir cadenas unas con otras a través del operador de concatenación (+). Observa el siguiente código:
#num1 = input("Ingresa el primer número: ") # Ingresa 12
#num2 = input("Ingresa el segundo número: ") # Ingresa 21

#print(num1 + num2) # el programa regresa 1221

#4. También se pueden multiplicar (* - replicación) cadenas, por ejemplo:
#miEntrada = ("Ingresa Algo: ") # Ejemplo: hola
#print(miEntrada * 3) # Salida esperada: holaholahola
