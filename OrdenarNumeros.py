import random
import os
#Generamos lista de Numeros:
Numeros = []
Cantidad = int(input("Cantidad de Numeros a ordenar?: "))
for c in range(Cantidad):
    Numeros.append(random.randint(0,999999999))
#---------------------------------------------------------------------

Movidos = 0
Iteraciones = 0
Movimientos = 0
Iteraciones1 = 0
SaltosIteracion = 0

for i,h in enumerate(Numeros):
    os.system("cls")
    print(i)
    print(f"Cantidad de Iteraciones: {Iteraciones} : {Iteraciones1} con {SaltosIteracion} saltos de iteracion y se han movido {Movimientos}")
    if Movidos > 0:
        SaltosIteracion += 1
        Movidos -= 1
        continue
    
    for f in range(i+1,len(Numeros)):
        Iteraciones += 1
        if Numeros[i] > Numeros[f]:
            Num1 = Numeros[i]
            Numeros[i] = Numeros[f]
            Numeros[f] = Num1

    for z in range(i+1,len(Numeros)):
        Iteraciones1 += 1
        if Numeros[i] == Numeros[z]:
            Numeros.pop(z)
            Numeros.insert(i,Numeros[i])
            Movidos += 1
            Movimientos +=1
            
print(f"Cantidad de Iteraciones: {Iteraciones} : {Iteraciones1} con {SaltosIteracion} saltos de iteracion y se han movido {Movimientos}")