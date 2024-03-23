secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

number = int(input("Adivina El número secreto... "))

while number != secret_number:
    print("Ups! Fallaste, no es el numero secreto.\nIntentá de nuevo: ")
    number = int(input("Adivina El número secreto... "))

print("felicidades! Acertaste el numero secreto! era ", secret_number)
    
    