import time
import sys
import os
import random
start_time = time.time()
os.system("cls")
#Generamos lista de Numeros:--------------------------------------------------
Numeros = []
Resultado = []
Cantidad = int(input("Cantidad de Numeros a ordenar?: "))
for c in range(Cantidad):
    Numeros.append(random.randint(0,100000))
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
#Generamos lista Ordenada:----------------------------------------------------
for i,a in enumerate(candy):
    for b in range(a):
        Resultado.append(i)
#-----------------------------------------------------------------------------
print(Resultado)
print("--- %s seconds ---" % (time.time() - start_time))