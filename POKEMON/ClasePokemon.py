import FuncionesPokemon
class Pokemon:
    #=====================================================================================================
    def __init__(self, Nombre,AtaqueBase,DefensaBase,VelocidadBase,Ataques,Vida):
        self.Vida = Vida
        self.Nombre =  Nombre
        self.AtaqueBase = AtaqueBase
        self.DefensaBase = DefensaBase
        self.VelocidadBase = VelocidadBase
        self.Ataques = Ataques
    #-----------------------------------------------------------------------------------------------------
    #=====================================================================================================
    def ImprimirAtaques(self):
        print("")
        for Index,NombreAtaque in enumerate(self.Ataques):
            Index += 1
            FuncionesPokemon.TextoImpresoLento(f"{Index}.{NombreAtaque}",0.01)
            print(" ",end=" ")
            if Index % 2 == 0:
                print("\n")
    #-----------------------------------------------------------------------------------------------------