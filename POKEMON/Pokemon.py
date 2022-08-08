import time
import FuncionesPokemon
import ClasePokemon
import random

POKEMONSTATS1 = ClasePokemon.Pokemon("MetalGreymon",1,2,3,{"IMPACTRUENO":2,"ONDA VOLTIO":1,"PSICORRAYO":3,"RAYO HIELO":1},60)
POKEMONSTATS2 = ClasePokemon.Pokemon("Rayquaza",123,23,1,{"IMPACTRUENO":3,"ONDA VOLTIO":1,"PSICORRAYO":10,"RAYO HIELO":1},50)

VIDAPOKEMON1 = POKEMONSTATS1.Nombre + f"  ||{'='*POKEMONSTATS1.Vida}||"
VIDAPOKEMON2 = POKEMONSTATS2.Nombre + f"  ||{'='*POKEMONSTATS2.Vida}||"
#-------------------------------------------------------------------------------------
while True:
    print("")
    print(VIDAPOKEMON1)
    print("")
    print(f"Bonificacion de ataque: {POKEMONSTATS1.AtaqueBase}")
    print(f"Bonificacion de velocidad: {POKEMONSTATS1.DefensaBase}")
    print(f"Bonificacion de defensa: {POKEMONSTATS1.VelocidadBase}")
    
    print("")
    print(VIDAPOKEMON2)
    print("")
    print(f"Bonificacion de ataque: {POKEMONSTATS2.AtaqueBase}")
    print(f"Bonificacion de velocidad: {POKEMONSTATS2.DefensaBase}")
    print(f"Bonificacion de defensa: {POKEMONSTATS2.VelocidadBase}")
#BASTARIA QUE FOS UNA FUNCIO AMB SA VARIABLE POKEMONSTATS------------------------------
    if (POKEMONSTATS1.VelocidadBase > POKEMONSTATS2.VelocidadBase):
        POKEMONSTATS1.ImprimirAtaques()
        Ataque = int(input("Elija el ataque seleccionado: ")) - 1
        VIDAPOKEMON2 = FuncionesPokemon.QuitarVida(VIDAPOKEMON2,list(POKEMONSTATS1.Ataques.values())[Ataque])
        VIDAPOKEMON1 = FuncionesPokemon.QuitarVida(VIDAPOKEMON1,list(POKEMONSTATS2.Ataques.values())[random.randint(0, 3)])

    else:
        POKEMONSTATS2.ImprimirAtaques()
        POKEMONSTATS1.ImprimirAtaques()
        Ataque = int(input("Elija el ataque seleccionado: ")) - 1
        VIDAPOKEMON1 = FuncionesPokemon.QuitarVida(VIDAPOKEMON1,list(POKEMONSTATS1.Ataques.values())[Ataque])
        
        
    if '=' not in VIDAPOKEMON1 or '=' not in VIDAPOKEMON2:
        VIDAPOKEMON1 = FuncionesPokemon.TextoImpresoLento("Combate Finalizado.",0.03)
        break 