#Crea una lista llamada numeros con los siguientes valores:
#numeros = [11, 4, 9, 16, 7, 2, 13, 20, 5, 8]

#Recorre la lista y:

#Guarda los números pares en una lista llamada pares.

#Guarda los números impares en una lista llamada impares.

#Muestra:

#La lista de pares.

#La lista de impares.

#Cuántos hay de cada uno.

numeros = [11, 4, 9, 16, 7, 2, 13, 20, 5, 8] #Creo la lista con los valores asignados
numeros_pares = [] #Creo la lista vacía donde iran los pares
numeros_impares = [] #Creo la lista vacía donde iran los inpares
print(f"La lista inicial es: {numeros}") #Muestro por pantalla la lista inicial
for numero in numeros: #Recorro la lista
    if numero %2==0: #Si el numero es par se agrega a  la lista vacia de pares
        numeros_pares.append(numero) #Agregamos a la lista vacía de pares con .append()
    else:
        numeros_impares.append(numero) #Agregamos a la lista vacía de inpares con .append()
print(f"Los numeros pares son:{numeros_pares}") #Mostramos por pantalla los pares
print(f"Los numeros impares son:{numeros_impares}") #Mostramos por pantalla los inpares
print("En la lista de pares hay:",end=" ") #Printeamos y al final pongo el end= para que se junte con la linea que sigue
print(len(numeros_pares))
print("En la lista de inpares hay:", end=" ") #Printeamos y al final pongo el end= para que se junte con la linea que sigue
print(len(numeros_impares))
