#Enunciado:

#Crea una lista con los siguientes números:
#numeros = [3, 8, 15, 6, 2, 10, 7]

#Recorre la lista y:

#Si el número es par, multiplícalo por 2.

#Si el número es impar, súmale 1.

#Guarda los nuevos valores en una nueva lista modificada y muéstrala.

numeros = [3,8,15,6,2,10,7]
numeros_modificados = []

for numero in numeros:
    if numero %2==0:
        nuevo_valor = numero * 2
    else:
        nuevo_valor = numero +1
    numeros_modificados.append(nuevo_valor)
print(numeros_modificados)