
numeros_usuario = []
numero_del_usuario = ""




while len(numeros_usuario) < 10:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un numero:")
    numeros_usuario.append(numero_del_usuario)
    numero_del_usuario = ""
    print("Número añadido")

print("El numero más pequeño es {}".format(min(numeros_usuario)))