
numeros_usuario = []
suma_numeros_usuario = 0
numeros_lista = 0
parar_pregunta = "F"
pregunta = "N"

while pregunta != parar_pregunta:
    pregunta = input("Dime un numero, pon F si quieres dejar de añadir numeros:")
    if pregunta == parar_pregunta:
        print("El resultado de {} / {} = {}".format(suma_numeros_usuario, numeros_lista, suma_numeros_usuario/numeros_lista ))
    elif pregunta.isdigit():
        suma_numeros_usuario += int(pregunta)
        numeros_usuario.append(pregunta)
        numeros_lista += 1