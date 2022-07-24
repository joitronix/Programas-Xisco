import time
import sys
import os
import random
start_time = time.time()
os.system("cls")
#Generamos lista de Numeros:--------------------------------------------------
Numeros = []
Cantidad = int(input("Cantidad de Numeros a ordenar?: "))
for c in range(Cantidad):
    Numeros.append(random.randint(0,10))
#-----------------------------------------------------------------------------
#Buscamos el numero mas grande:-----------------------------------------------
NumMasGrande = 0
for c in Numeros:
    if c > NumMasGrande:
        NumMasGrande = c
#-----------------------------------------------------------------------------
#Generamos lista de posicionamiento de numeros:-------------------------------
candy = []
print(f"El numero mas grande es: {NumMasGrande}")
for a in range(NumMasGrande + 1):
    candy.append(0)
#-----------------------------------------------------------------------------
#Asignamos los numeros a sus respectivas posiciones:--------------------------
for z in Numeros:
    candy[z] = candy[z] + 1
#-----------------------------------------------------------------------------
print(candy)
print("--- %s seconds ---" % (time.time() - start_time))
print(f"El numero mas grande es {NumMasGrande}")