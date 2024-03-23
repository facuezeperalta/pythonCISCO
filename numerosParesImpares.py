numerosPares = 0
numeroImpares= 0

number = int(input("Ingresa un número, ingresá 0 para terminar."))

while number != 0:
    if number % 2 == 1:
        numeroImpares+= 1
    else:
        numerosPares += 1
    
    number = int(input("Ingresa un número, ingresá 0 para terminar."))

print("Cantidad de numeros paraes: ", numerosPares)
print("Cantidad de numeros impares: ", numeroImpares)