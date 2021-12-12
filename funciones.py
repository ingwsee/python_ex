def Equipofut(n):
    Equipo = []
    
    for i in range(0, 10):
        Equipo.insert(0, i)
    
    return Equipo

print(Equipofut(11))

"""def strangeListFunction(n):
    strangeList = []
    
    for i in range(0, n):
        strangeList.insert(0, i)
    
    return strangeList

print(strangeListFunction(5))

def direccion(c, cp, cd):
    print("Tu dirección es:", c, cp, cd)
c = input("Calle: ")
cp = input("Código Postal: ")
cd = input("Ciudad: ")

direccion(c, cp, cd)


def suma(a, c, b=2):
    print(a + b + c)

suma(a=1, c=3)


def suma(numero1,numero2):
    '''función la cual suma dos números'''
    print numero1 + numero2
    print "\n"

def mensaje(que, numero):
    print("Ingresa", que, "número", numero)


mensaje("teléfono", 11)
mensaje("precio", 5)
mensaje("número", "número")

def equipo(posicion, nombre):
     print("Ingresa:", posicion, "Nombre:", nombre)
     



# Paso de parámetros posicionales --- La técnica que asigna cada argumento al parámetro correspondiente, es llamada paso de parámetros posicionales, los argumentos pasados de esta manera son llamados argumentos posicionales.

def presentar(primerNombre, segundoNombre):
    
    print("Hola, mi nombre es", primerNombre, segundoNombre)

presentar("Luke", "Skywalker")
presentar("Jesse", "Quick")
presentar("Clark", "Kent")
"""
"""
def presentar():
    nom = str(input("Ingrese su nombre:"))
    ap = str(input("Ingrese su apellido:"))
    print("Hola, mi nombre es", nom, ap)

presentar()



def suma():
     print ("Este programa calcula la suma de dos numeros")
     a = float (input("Ingrese el 1er numero: "))
     b = float (input("Ingrese el 2do numero: "))
     calculo = float (a + b)
     if a == None or b == None:
         print ("Error, debes enviar dos números a la función")
     return
     print (calculo)
suma()

#print ("Este programa calcula la diferencia entre dos numeros:")
def resta():
     print ("Este programa calcula la diferencia de dos numeros")
     a = float (input("Ingrese el 1er numero: "))
     b = float (input("Ingrese el 2do numero: "))
     calculo = float (a - b)
     if a == None or b == None:
         print ("Error, debes enviar dos números a la función")
     return
     print (calculo)
resta()

## LONGITUD DE LA CIRCUNFERENCIA

print ("Este programa calcula la longitud de la circunferencia")
def lc():
     print("Dime el radio")
     radio = int(input())
     pi = 3.14
     longitud = 2 * pi * radio
     print ("Longitud de la circunferencia:")
     print (longitud)
lc()

def iva():
    #función básica para el calculo del IVA
    iva = 12
    costo = float(input("¿Cual es el monto a calcular?: "))
    calculo = costo * iva / 100
    print ("El calculo de IVA es: " , calculo)
iva()
"""
