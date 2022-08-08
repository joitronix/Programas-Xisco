import time
import FuncionesPokemon
POKEMON1 = "POKEMON" + "   ||========================================================||"
POKEMON2 = "POKEMON" + "   ||========================================================||"
while True:
    
    print(POKEMON1)
    print(f"Bonificacion de ataque: 33")
    print(f"Bonificacion de velocidad: 43")
    print(f"Bonificacion de defensa: 23")
    
    print(POKEMON2)
    print(f"Bonificacion de ataque: 21")
    print(f"Bonificacion de velocidad: 12")
    print(f"Bonificacion de defensa: 18")
    
    
    Ataque = input("Elija el ataque seleccionado: ")
    if Ataque == '1':
        POKEMON1 = FuncionesPokemon.QuitarVida(POKEMON1,5)
        
    if '=' not in POKEMON1 or '=' not in POKEMON2:
        FuncionesPokemon.TextoImpresoLento("Combate Finalizado.",0.03)
        break 
    