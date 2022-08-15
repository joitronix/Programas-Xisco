class Rectangulo:
    def __init__(self,altura,anchura) -> None:
        self.anchura = anchura
        self.altura = altura
    
    def CalcularArea(self):
        return int(self.altura) * int(self.anchura)
    
anchura = input("Proporciona la base: ")
altura = input("Proporciona la altura: ")
print(f"El area del rectangulo es: {Rectangulo(anchura,altura).CalcularArea()}")


