#3.1.7.1 Listas en aplicaciones avanzadas
#fila = []
#for i in range(8):
#    row.append(PEON_BLANCO)

#fila = [PEON_BLANCO for i in range(8)]

cuadrados = [x ** 2 for x in range(10)]
print (cuadrados)

# lista impar de la lista cuadrados

probabilidades = [x for x in cuadrados if x % 2 != 0]
print (probabilidades)

# potencias de 2

dos = [2 ** i for i in range(8)]
print (dos)

# 3.1.7.2 Listas dentro de listas: arreglos bidimensionales
# tablero ajedrez

#tablero  = []
#for i in range(8):
#    fila = [EMPTY for i in range(8)]
#    tablero.append(fila)
#print (tablero)

EMPTY=0
tablero = [[EMPTY for i in range(8)] for j in range(8)]
print (tablero)

#3.1.7.3

EMPTY = "-"
TORRE = "TORRE"
PEON = "PEON"
CABALLO = "CABALLO"
tablero = []

for i in range(8):
    fila = [EMPTY for i in range(8)]
    tablero.append (fila)

tablero[0][0] = TORRE
tablero[0][7] = TORRE
tablero[7][0] = TORRE
tablero[7][7] = TORRE
tablero[0][1] = CABALLO
tablero[0][6] = CABALLO
tablero[6][1] = PEON
tablero[6][0] = PEON

print(tablero)


#  Arreglos
# REGISTRO DE HORAS POR MES - ESTACION METEOROLOGICA

temps = [[0.0 for h in range (24)] for d in range (31)]
print (temps)

# Promedio de temperatura mensual al mediodia
temps = [[0.0 for h in range(24)] for d in range (31)]
#
# la matriz se actualiza mágicamente aquí
#

suma = 0.0

for day in temps:
    suma += day[11]

promedio= suma / 31

print("Temperatura promedio al mediodía:", promedio)

# Temperatura mas alta durante el mes

temps = [[0.0 for h in range (24)] for d in range (31)]
#
# la matriz se actualiza mágicamente aquí
#

mas_alta = -100.0

for day in temps:
    for temp in day:
        if temp > mas_alta:
            mas_alta = temp

print("La temperatura más alta fue:", mas_alta)

# dias con tempertura a mediodida de al menos 20 grados

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# la matriz se actualiza mágicamente aquí
#

hotDays = 0

for day in temps:
    if day[11] > 20.0:
        hotDays += 1

print(hotDays, " fueron los días calurosos.")


