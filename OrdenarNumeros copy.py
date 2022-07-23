import random
#Generamos lista de Numeros:

Cantidad = int(input("Cantidad de Numeros a ordenar?: "))
Numeros = []
for c in range(Cantidad):
    Numeros.append(random.randint(0,999999999))
    
a = sorted(Numeros)

print(a)