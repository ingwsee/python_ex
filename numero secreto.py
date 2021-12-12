# Lab 3.1.2.3 adivina # secreto

print(
"""
+==================================+
| Bienvenido a mi juego, hobbit!   |
| Introduce un número entero del   |
| 1 al 100 y adivina qué número he |         |
| elegido para ti.                 |
| Si adivinas se abrira la puerta  |
| de la celda, de lo contrario     |
| seguiras encanado en Mordor      |         |
| Entonces,                        |
| ¿Cuál es el número secreto?      | 
| UTILIZA EL PODER DEL PRECIOSO!!! |
+==================================+
""")
numeroSecreto = 69
numero = int (input ("Ingresa el húmero secreto para abrir la celda:"))
while numero != numeroSecreto:
    if (numero != numeroSecreto):
        print ("NUMERO INCORRECTO, SEGUIRAS EN PRISION HASTA ADIVINAR EL NUERO DEL ANILLO MAGICO,INGRESA OTRO NUMERO ")
        numero = int (input ("Ingresa el húmero secreto para abrir la celda:"))
else:
   print ("HAS ABIERTO LA CELDA HOBBIT, PUEDES CONTINUAR TU BUSQUEDA DEL ANILLO...")
     #   numeroSecreto = numero
        
