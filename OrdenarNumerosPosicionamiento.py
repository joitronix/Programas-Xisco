import time
import sys
import os
import random
start_time = time.time()

#Generamos lista de Numeros:
Numeros = []
Cantidad = int(input("Cantidad de Numeros a ordenar?: "))
for c in range(Cantidad):
    Numeros.append(random.randint(0,10))
#---------------------------------------------------------------------
#Buscamos el numero mas grande:
NumMasGrande = 0
for c in Numeros:
    if c > NumMasGrande:
        NumMasGrande = c
#-----------------------------------------------------------------------------
candy = []
for a in range(NumMasGrande):
    candy.append(0)

print("--- %s seconds ---" % (time.time() - start_time))
print(f"El numero mas grande es {NumMasGrande}")