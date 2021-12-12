c0 = int (input ("Ingrese un numero mayor que 0 o 1 para salir:"))
pasos = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2
        print (c0)
        pasos += 1
        
    if c0 % 2 != 0:
        c0 == 3 * c0 + 1
        print (c0)
        pasos += 1

    print ("Usted ha salido del juego, Se han ejecutado", pasos , "pasos" )
    
else:
    print ("Usted ha salido del juego, No se han ejecutado pasos, ha ingresado 1" )

    #elif print ("Usted ha salido del juego, Se han ejecutado", pasos , "pasos" )
    
#else:
 
