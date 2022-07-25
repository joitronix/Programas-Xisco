import time
import os
import random
from itertools import repeat
start_time = time.time()
os.system("cls")
#Generamos lista de Numeros:--------------------------------------------------
Numeros = []
Resultado = []
Cantidad = int(input("Cantidad de Numeros a ordenar?: "))
for c in range(Cantidad):
    Numeros.append(random.randint(0,999999999))
#-----------------------------------------------------------------------------
#Buscamos el numero mas grande:-----------------------------------------------
NumMasGrande = 0
for c in Numeros:
    if c > NumMasGrande:
        NumMasGrande = c
#-----------------------------------------------------------------------------
#Generamos lista de posicionamiento de numeros:-------------------------------
Candy = []
print(f"El numero mas grande es: {NumMasGrande}")
Candy.extend(repeat(0,NumMasGrande + 1))
print("Lista Finalizada.")
#-----------------------------------------------------------------------------
#Asignamos los numeros a sus respectivas posiciones:--------------------------
for a in Numeros:
    Candy[a] += 1
#-----------------------------------------------------------------------------
print("HolaCandy")
#Generamos lista Ordenada:----------------------------------------------------
for i,a in enumerate(Candy):
    if a != 0: Resultado.extend(repeat(i,a))
#-----------------------------------------------------------------------------
print(int(time.time() - start_time) / 60)