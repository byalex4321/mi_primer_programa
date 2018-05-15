
numeros_usuario = []
contador = 0
parar_pregunta = "F"
pregunta = "N"

while pregunta != parar_pregunta:
    pregunta = input("Dime un numero, pon F si quieres dejar de añadir numeros:")
    if pregunta == parar_pregunta:
        print(contador)

    elif pregunta.isdigit():
        contador += 1
        numeros_usuario.append(pregunta)
