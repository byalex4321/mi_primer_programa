
operacion_matematica = input("¿Que operación quieres hacer?   Suma/Resta/Multiplicacion/Division:".upper()).upper()
primer_numero = int(input("Dime un numero:"))
segundo_numero = int(input("Dime otro numero:"))





if  operacion_matematica == "DIVISION":
    print(primer_numero / segundo_numero)
elif operacion_matematica == "SUMA":
    print(primer_numero + segundo_numero)
elif operacion_matematica == "RESTA":
    print(primer_numero - segundo_numero)
elif operacion_matematica == "MULTIPLICACION":
    print(primer_numero * segundo_numero)


