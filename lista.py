numbers = [10,5,7,2,1]
print("Contenido de la lista: ",numbers)

numbers[0]= 30

print("Lista actualizada: ",numbers)
print("--------")
numbers[1] = numbers[3]
print("Lista con valores copiados: ", numbers)

print("--------")
print("Tamaño de la lista: ", len(numbers))

print("---Eliminando elementos de una lista---")
del numbers[1]
print("Longuitud actualizada: ",len(numbers) )
print(numbers)

print("---AGREGAR ELEMENTOTS---")
numbers.append(20)
print("Lista Actualizada: ",numbers)

print("---INSERT---")
numbers.insert(3,450)
print("Lista con insert: ",numbers)

print("---LISTAS CON FOR---")
my_lista = []

for i in range(5):
    my_lista.append(i+1)
print(my_lista)

print("---LISTA CON FOR E INSERT---")
miLista2 = []
for i in range(10):
    miLista2.insert(0,i+1)
print(miLista2)

print("---Sumar elementos de una Lista ---")
listaParaSuma = [10, 1, 8, 3, 5]
total = 0
for i in range(len(listaParaSuma)):
    total+=listaParaSuma[i]

print(total)

print("---For in, listas---")
total2 = 0
for i in listaParaSuma:
    total2+=i

print(total2)

print("---Listas intercambiadas---")
length = len(miLista2)
for i in range(length//2):
    miLista2[i],miLista2[length-i-1] =  miLista2[length-i-1],miLista2[i]

print(miLista2)
