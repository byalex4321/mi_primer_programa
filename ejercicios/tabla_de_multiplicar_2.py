numero_tabla = int(input("¿De que numero quieres hacer la tabla?:"))


for multiplo in range(1, 20):
    if (numero_tabla * multiplo)%2:
        multiplo += 1
    else:
        print("{} * {} = {}".format(multiplo, numero_tabla, multiplo*numero_tabla))