
"""si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal).
    si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos.
    Tu tarea es escribir una calculadora de impuestos
    Debe aceptar un valor de punto flotante: el ingreso.
    A continuación, debe imprimir el impuesto calculado, redondeado a pesos totales. Hay una función llamada round() que hará el redondeo por ti - la encontrarás en el código de esqueleto del editor.
Nota: este país feliz nunca devuelve dinero a sus ciudadanos. Si el impuesto calculado es menor que cero, solo significa que no hay impuesto (el impuesto es igual a cero). Ten esto en cuenta durante tus cálculos.
Observa el código en el editor - solo lee un valor de entrada y genera un resultado, por lo que debes completarlo con algunos cálculos inteligentes.
 """

ingreso = float(input("Ingrese el salario del cuidadano: "))

montoImponible = 85.528
recargoPorExcedente = 14.839

if ingreso < montoImponible:
    impuesto = ingreso * 0.18 - 556.02
else:
    impuesto = (ingreso - montoImponible) * 0.32 + recargoPorExcedente


if impuesto < 0.0:
    impuesto = 0.0

impuesto = round(impuesto,0)

print("El impuesto es: ", impuesto, "pesos")


