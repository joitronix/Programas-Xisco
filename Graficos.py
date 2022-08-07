import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random
#Definimos una lista con paises como string
paises = ['Jonny', 'Marta', 'Xavier', 'Pedritto','Mamaxisco']
#Definimos una lista con ventas como entero
ventas = [random.randrange(-100,100,1) for a in range(5)]
fig, ax = plt.subplots()
#Colocamos una etiqueta en el eje Y
ax.set_ylabel('Insults cap en xisco / hora')
#Colocamos una etiqueta en el eje X
ax.set_title('Cantidad de insultos emitidos hacia xisco por persona por hora.')
#Creamos la grafica de barras utilizando 'paises' como eje X y 'ventas' como eje y.
for i, v in enumerate(ventas):
    ax.text(i-.25, 
              v/ventas[i]+100, 
              ventas[i], 
              fontsize=18)
plt.bar(paises, ventas)
plt.savefig('barras_simple.png')
#Finalmente mostramos la grafica con el metodo show()
plt.savefig('c:\\users\\yo\\desktop\\xd.png')
plt.show()