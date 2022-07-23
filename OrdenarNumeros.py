import random
#Generamos lista de Numeros:

Cantidad = int(input("Cantidad de Numeros a ordenar?: "))
Numeros = []
ResultadoOrdenado = []
for c in range(999999999):
    ResultadoOrdenado.append(0)
for a in range(Cantidad):
    NumeroAleatorio = random.randint(0,999999999)
    Numeros.append(NumeroAleatorio)
for b in Numeros:
    ResultadoOrdenado.insert(b,ResultadoOrdenado[b] + 1)

print(len(ResultadoOrdenado))
print(Numeros)
for z,f in enumerate(ResultadoOrdenado):
    if f != 0:
        print(f"Numero: {z} apareció: {f} veces.")