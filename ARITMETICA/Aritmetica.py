class Aritmetica:
    list = []
    def __init__(self,hola):
        self.hola = hola
        Aritmetica.list.append(self)

for a in range(0,4):
    Aritmetica(a)

for a in Aritmetica.list:
    print(a.hola)


