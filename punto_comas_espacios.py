
frase_usuario = input("Dime una frase:")

comas = ","
puntos = "."
espacios =" "

n_espacios = 0
n_puntos = 0
n_comas = 0



for letra in frase_usuario:
    if letra in espacios:
        n_espacios += 1
    if letra in puntos:
        n_puntos += 1
    if letra in comas:
        n_comas += 1


print("Hay {} espacios".format(n_espacios))
print("Hay {} puntos".format(n_puntos))
print("Hay {} comas".format(n_comas))