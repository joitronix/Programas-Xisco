import time
import FuncionesPokemon
POKEMON1 = "POKEMON" + "   ||========================================================||"
POKEMON2 = "POKEMON" + "   ||========================================================||"
while True:
    print(POKEMON1)
    print("Bonificacion de ataque: 33")
    print("Bonificacion de velocidad: 43")
    print("Bonificacion de defensa: 23")
    
    print(POKEMON2)
    print("Bonificacion de ataque: 21")
    print("Bonificacion de velocidad: 12")
    print("Bonificacion de defensa: 18")
    
    print("1.Impactrueno: 5pd")
    Ataque = input("Elija el ataque seleccionado: ")
    if Ataque == '1':
        POKEMON1 = FuncionesPokemon.QuitarVida(POKEMON1,5)
        
    if '=' not in POKEMON1 or '=' not in POKEMON2:
        print("Combate Terminado.")
        break 
    