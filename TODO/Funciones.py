import time
#=====================================================================================================
def Suma(*args):
    return sum(args)
#-----------------------------------------------------------------------------------------------------
#=====================================================================================================
def Multiplicacion(*args):
    Result = ""
    #Range le quitamos uno para que no muestre el ultimo digito(por defecto ya quita el extra de len)
    for IndexNumber in range(0,len(args) - 1):
        Result += f"{args[IndexNumber]} * "
    #Mostramos el ultimo valor que queriamos sin el *.
    Result += str(args[len(args) - 1])
            
    return eval(Result)
#-----------------------------------------------------------------------------------------------------
#=====================================================================================================
def Locura(Numero):
    if not Numero < 1:
        if Numero == 1:
            print(1)
        else:
            print(Numero)
            Numero -= 1
            Locura(Numero)
#-----------------------------------------------------------------------------------------------------
#=====================================================================================================
def impuesto(ConImpuesto,SinImpuesto):
    return SinImpuesto + SinImpuesto * (ConImpuesto/100)
#-----------------------------------------------------------------------------------------------------
#=====================================================================================================
def Temperatura(UnidadMedida,Temperatura):
    if UnidadMedida in ("C","c"):
        return f"La temperatura {Temperatura} ºC = {round((Temperatura*1.8) + 32 , 2)} ºF"
    else:
        return f"La temperatura {Temperatura} ºF = {round((Temperatura - 32) / 1.8 , 2)} ºC"
#-----------------------------------------------------------------------------------------------------