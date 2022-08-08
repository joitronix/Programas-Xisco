import time
#=====================================================================================================
def TextoImpresoLento(Texto,velocidad):
    for g in Texto:
        print( g , end='' , flush=True )
        time.sleep(velocidad)
#-----------------------------------------------------------------------------------------------------
#=====================================================================================================
def QuitarVida(Vida,Cantidad):
    Vida = list(Vida)
    for z,a in enumerate(Vida[::-1]):
        if a == '=':
            Vida[len(Vida) - 1 - z] = " "
            Cantidad -= 1
        if(Cantidad == 0):
            break
    return str(''.join(Vida))
#-----------------------------------------------------------------------------------------------------
#=====================================================================================================
def QuitarVida(Vida,Cantidad):
    Vida = list(Vida)
    for z,a in enumerate(Vida[::-1]):
        if a == '=':
            Vida[len(Vida) - 1 - z] = " "
            Cantidad -= 1
        if(Cantidad == 0):
            break
    return str(''.join(Vida))
#-----------------------------------------------------------------------------------------------------