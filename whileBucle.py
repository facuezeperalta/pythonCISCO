largerNumber = -999999999

inputNumber = int(input("Ingresa un numero o ingresa -1 para salir de la carga de números: "))
cantIngresos =0

while inputNumber != -1:
    if inputNumber > largerNumber:
        largerNumber = inputNumber
    cantIngresos+=1
    inputNumber = int(input("Ingresa un numero o ingresa -1 para salir de la carga de números: "))
    


print("El numbero mas grande ingresado fue: ",largerNumber, "de: ",cantIngresos,"numberos ingresados.")