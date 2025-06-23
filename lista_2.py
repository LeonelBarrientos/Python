#Crear una lista de números del 1 al 10. Mostrar solo los números pares.

#Sumar todos los elementos de una lista de números.

#Eliminar el primer número par de una lista.

#Pedir al usuario 5 números y guardarlos en una lista, luego mostrar el número mayor y menor.

#Revertir el orden de una lista sin usar reverse().

#Multiplicar todos los números de una lista por 2 y guardar el resultado en una nueva lista.

Lista = [1,2,3,4,5,6,7,8,9,10] #Creo la lista del 1 al 10
for numero in Lista: #aqui recorro la lista
    if numero %2==0: #Aquí lo que le digo al programa es que imprima solo los numeros pares con %2==0
        print(f"los numeros pares son :{numero}")
        #continue

total_suma = sum(Lista) #Con el comando sum() sumo todos los elementos dentro de la lista
print(f"la suma de todos los elementos es {total_suma}")
for numero in Lista: #Aquí recorro la lista
    if numero %2==0: #Le digo al programa que recorra los numeros pares
        Lista.remove(numero) #El primer numero par que se encuentre lo borrara
        break #Es importante usar el break aquí o sino irá borrando los numeros pares progresivamente...
print(Lista) #Aquí mostramos la lista actualizada
lista_invertida = Lista[::-1] #La funcion [::-1] sirve para invertir una lista pero sin ocupar el .reverse()
print("Lista invertida:", end=" ") #pongo el end= para que sea mas facil de leer y no acumular tantas lineas
print(lista_invertida) #Muestro la lista invertida actualizada
for i in lista_invertida:
    multi = i * 2
    print(multi)





    

