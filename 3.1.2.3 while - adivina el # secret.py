# Escenario

# Un mago junior ha elegido un número secreto. Lo ha escondido en una variable
# llamada númeroSecreto. Quiere que todos los que ejecutan su programa jueguen
# el juego Adivina el número secreto, y adivina qué número ha elegido para ellos.
#¡Quienes no adivinen el número quedarán atrapados en un ciclo sin fin para siempre!
# Desafortunadamente, él no sabe cómo completar el código.

#Tu tarea es ayudar al mago a completar el código en el editor de tal manera
#que el código:

#    Pedirá al usuario que ingrese un número entero.
#    Utilizará un ciclo while.
#    Comprobará si el número ingresado por el usuario es el mismo que el número
# escogido por el mago. Si el número elegido por el usuario es diferente al
# número secreto del mago, el usuario debería ver el mensaje "¡Ja, ja!
#¡Estás atrapado en mi ciclo!" y se le solicitará que ingrese un número nuevamente.
# Si el número ingresado por el usuario coincide con el número escogido por el mago, el número debe
# imprimirse en la pantalla, y el mago debe decir las siguientes palabras: "¡Bien hecho, muggle! Eres libre ahora".

#¡El mago está contando contigo! No lo decepciones.

#INFO EXTRA

# Por cierto, mira la función print(). La forma en que lo hemos utilizado aquí se llama impresión
#multilínea . Puede utilizar comillas triples para imprimir cadenas en varias líneas para
#facilitar la lectura del texto o crear un diseño especial basado en texto. Experimenta con ello.

print(
"""
+===================================+
| Bienvenido a mi juego, magico!    |
| Introduce un número entre 0 y 100 |
| y adivina qué número he           |
| elegido para ti.                  |
| Entonces,                         |
| ¿Cuál es el número secreto?       |
+===================================+
""")
numerosecreto = 69
numero = input ("Ingresa el numero:")
while numero != 69:
    if numero == numerosecreto:
        numero = numerosecreto
        print ("La puerta se abrio magicamente, eres libre!!")
    #     numero = int (input ("Ingresa otro numero o seguiras encanado")
     
print("fuera guachin, eres libre!!!")
#print ("Aun estas en cana, intenta con otro numero para abrir la puerta de la celda")
    
