import os.path
import os
from tkinter import SE

def CrearTabla(Nombre,Columnas):
    try:
        with open(f'{Nombre}.txt', 'x') as f:
            f.write('º'.join(str(x) for x in Columnas) + "\n")
        print("Tabla creada correctamente")
    except:
        print("La tabla ya existe")
        
def SelectColumnasTabla(Tabla):
    if os.path.exists(f'{Tabla}.txt'):
        with open(f"{Tabla}.txt", "r") as file:
            return file.readline().strip().split("º")
        
def ImprimirTabla(Tabla):
    if os.path.exists(f'{Tabla}.txt'):
        with open(f"{Tabla}.txt", "r") as file:
            for a in file.readlines():
                print(a.strip().split("º"))
    else:
        print(f"La tabla {Tabla} no existe")
def InserTabla(Tabla,ListaInsert):
    try:
        if os.path.exists(f'{Tabla}.txt'):
            if len(SelectColumnasTabla(Tabla)) == len(ListaInsert):
                with open(f'{Tabla}.txt', 'a+') as f:
                    f.write( 'º'.join(str(x) for x in ListaInsert) + "\n")
                print("Elemento insertado correctamente")
            else:
                print("Numero de argumentos no valido")
        else:
            print(f"La tabla {Tabla} no existe.")
    except:
        print("Error Insertando.")
        
for a in range(1,1000000):
    print(a)
    InserTabla("Nombre",["perro","Candy"])