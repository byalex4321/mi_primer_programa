
frase = input("Dime una frase:")
vocales = ["a", "e", "o", "u", "A", "E", "I", "O", "U"]
sus = "i"

for letra in vocales:
    frase = frase.replace(letra, sus)


print(frase)