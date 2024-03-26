hat_list = [1, 2, 3, 4, 5]

# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
numeroIngresado = int(input("Ingrese un numero para reemplazar el numero del medio: "))
hat_list[2] = numeroIngresado
print("Sombrero actulizado: ", hat_list)
# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[-1]
print("Se eliminó el último elemento del sombrero: ", hat_list)
# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("Tamaño del sombrero: ",len(hat_list))

print("------")