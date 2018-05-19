
frase_usuario = input("Dime una frase:")
vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
numero = 0

for letra in frase_usuario:
    if letra in vocales:
        numero += 1
        frase_usuario = frase_usuario.replace(letra, str(numero))
    else:
        numero += 1

print(frase_usuario)

