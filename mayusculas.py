
frase_usuario = input("Dime una frase:")

mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "V", "U", "W", "Y", "X", "Z"]
n_mayusculas = 0


for letras in frase_usuario:
    if letras in mayusculas:
        n_mayusculas += 1

print("Hay {} letras en mayuscula".format(n_mayusculas))