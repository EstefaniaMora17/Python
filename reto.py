contador = 1
sumatoria = 0

while(contador <= 19):
   numero = int(input('ingrese un numero: '))
   if(numero < 0):
        sumatoria +=1
contador +=1

print(f'la cantidad de numeros negativos ingresados fue: {sumatoria}')
