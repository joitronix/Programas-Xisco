def Suma(*args):
    return sum(args)
def Multiplicacion(*args):
    Result = ""
    for Index,Numbers in enumerate(args):
        if Index == (len(args) - 1):
            Result += f"{Numbers}"
            continue
        Result += f"{Numbers} * "
            
    return eval(Result)