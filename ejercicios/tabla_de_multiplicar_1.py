
numero_tabla = int(input("¿De que numero quieres hacer la tabla?:"))

for multiplo in range(5, 16):
    print("{} * {} = {}".format(multiplo, numero_tabla, multiplo*numero_tabla))