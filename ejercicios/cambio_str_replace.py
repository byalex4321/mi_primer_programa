
frase_usuario = input("Dime una frase:")
se_sustituye = ["a", "A"]
sutituir_valor = "VACA"
for letra in se_sustituye:
    frase_usuario = frase_usuario.replace(letra, sutituir_valor)


print(frase_usuario)