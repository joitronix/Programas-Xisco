import time
import FuncionesPokemon
import ClasePokemon

POKEMONSTATS1 = ClasePokemon.Pokemon("MetalGreymon",1,2,3)
POKEMONSTATS2 = ClasePokemon.Pokemon("Rayquaza",123,23,12)

VIDAPOKEMON1 = f"POKEMON" + f"   ||========================================================||"
VIDAPOKEMON2 = f"POKEMON" + f"   ||========================================================||"

while True:
    
    print(VIDAPOKEMON1)
    print(f"Bonificacion de ataque: {POKEMONSTATS1.AtaqueBase}")
    print(f"Bonificacion de velocidad: {POKEMONSTATS1.DefensaBase}")
    print(f"Bonificacion de defensa: {POKEMONSTATS1.VelocidadBase}")
    
    print(VIDAPOKEMON2)
    print(f"Bonificacion de ataque: {POKEMONSTATS2.AtaqueBase}")
    print(f"Bonificacion de velocidad: {POKEMONSTATS2.DefensaBase}")
    print(f"Bonificacion de defensa: {POKEMONSTATS2.VelocidadBase}")
    
    
    Ataque = input("Elija el ataque seleccionado: ")
    if Ataque == '1':
        VIDAPOKEMON1 = FuncionesPokemon.QuitarVida(VIDAPOKEMON1,5)
        
    if '=' not in VIDAPOKEMON1 or '=' not in VIDAPOKEMON2:
        FuncionesPokemon.TextoImpresoLento("Combate Finalizado.",0.03)
        break 
    