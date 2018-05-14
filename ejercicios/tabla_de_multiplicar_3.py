numero_tabla = int(input("¿De que numero quieres hacer la tabla?:"))
contador = 10


while contador > 0:
    print("{} * {} = {}".format(numero_tabla, contador, numero_tabla * contador))
    contador -= 1
