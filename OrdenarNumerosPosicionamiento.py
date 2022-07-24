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
for a in range(NumMasGrande + 1):
    Candy.append(0)
print("Lista Finalizada.")
#-----------------------------------------------------------------------------
#Asignamos los numeros a sus respectivas posiciones:--------------------------
while Numeros != []:
    Candy[Numeros[0]] += 1
    Numeros.pop(0)
#-----------------------------------------------------------------------------
print("HolaCandy")
#Generamos lista Ordenada:----------------------------------------------------
for i,a in enumerate(Candy):
    for b in range(a):
        Resultado.append(i)
"""
Contador = 0
while Candy != []:
    for a in range(Candy[0]):
        Resultado.append(Contador)
    Candy.pop(0)
    Contador += 1
"""
#-----------------------------------------------------------------------------
print(int(time.time() - start_time) / 60)