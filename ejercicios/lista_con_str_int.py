
lista_cosas = ["das", 123, 456, "fsdskhg", 796, "36464230a", "sfsd", 723746245]
lista_numeros = []
lista_str = []



for dato in lista_cosas:
    if type(dato) == str:
        lista_str.append(dato)
    elif type(dato) == int:
        lista_numeros.append(dato)


print(lista_str)
print(lista_numeros)