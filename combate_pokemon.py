
combate_pokemon = input("¿Contra quien quieres luchar?  Squirtle/Bulbasur/Charmander:").upper()


vida_enemigo = 0
vida_pikachu = 100
if combate_pokemon == "SQUIRTLE":
    vida_enemigo = 100
elif combate_pokemon == "CHARMANDER":
    vida_enemigo = 80
elif combate_pokemon == "BULBASUR":
    vida_enemigo = 90


while vida_pikachu > 0 or vida_enemigo > 0:
    ataque_elegido = input("¿Elige un ataque?   Voltio/Chispazo:").upper()
    if ataque_elegido == "VOLTIO":
        vida_enemigo -= 10
    elif ataque_elegido == "CHISPAZO":
        vida_enemigo -= 12

    vida_pikachu -= 10
    print("Vida Pikachu:{}".format(vida_pikachu))
    print ("Vida enemigo:{}".format(vida_enemigo))




print("El combate ha terminado")
if vida_pikachu < 0:
    print("Has perdido")
elif vida_enemigo < 0:
        print("Has ganado")