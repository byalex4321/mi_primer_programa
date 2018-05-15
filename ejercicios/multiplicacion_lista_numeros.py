
lista_numeros = [423, 23423, 4235.423, 432, 234234, 2]
contador = 1
cantidad = len(lista_numeros)
resultado = lista_numeros[0]

while contador != cantidad:
    resultado = resultado * lista_numeros[contador]
    contador += 1
print(resultado)




