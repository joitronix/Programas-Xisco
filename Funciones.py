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