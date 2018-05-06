
frase_usuario = input("Dime una frase:")

vocales = ["a", "e", "i", "o", "u"]

for letras in frase_usuario:
    if letras in vocales:
        print(letras)