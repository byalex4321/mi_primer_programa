
numero_a_adivinar = 5

primer_numer = int(input("Di un numero del 1 al 10:"))
if primer_numer == numero_a_adivinar:
    print("has ganado")
else:
    print("Vuelve a intentarlo")
    segundo_numero = int(input("Di un numero del 1 al 10:"))
    if segundo_numero == numero_a_adivinar:
      print("Bien hecho")
    else:
      print("Vuelve a probar")
      tercer_numero = int(input("Di un numero del 1 al 10:"))
      if tercer_numero == numero_a_adivinar:
          print("Has acertado")
      else:
          print("Sigue intentandolo")
          cuarto_numero = int(input("Di un numero del 1 al 10:"))
          if cuarto_numero == numero_a_adivinar:
              print("Lo has conseguido")
          else:
              print("No te rindas")
              ultimo_numero = int(input("Di un numero del 1 al 10:"))
              if ultimo_numero == numero_a_adivinar:
                  print("Lo lograste")
              else:
                  print("No lo conseguite")