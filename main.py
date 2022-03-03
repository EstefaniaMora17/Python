#menu de opciones

import math


opcion = 1
print("empenadas ")
print("**********")
print("0. salir")
print("1. encontrar multiplo 2")
print("2. encontrar raiz cuadrada")
print("3. sumas + 100")
print("4. elevar a la 2")

while (opcion != 0):
    opcion = int(input("digita una opcion: "))
    if(opcion == 1):
        numero = int(input("digite un numero entero: "))
        if(numero % 2==0):
            print(f"el numero {numero} es multiplo de 2")
        else:
            print(f"el numero {numero} no es multiplo de 2")
    elif(opcion == 2): 
        numero = int(input("digite un numero entero: "))
        print(f"la raiz cuadrada de numero {numero} es: {math.sqrt(numero)}")
    elif(opcion == 3):
          numero = int(input("digite un numero entero: "))
          print(f"la suma de  {numero} es: {numero + 100}")
    elif(opcion == 4):
         numero = int(input("digite un numero entero: "))
         print(f"el cuadrado de {numero} es: {numero * numero}")
    elif(opcion == 0):
        break
    else:
        print("digita una opcion valida")
else:
    print("para ahi")    