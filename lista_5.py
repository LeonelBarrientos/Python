
numeros = [12, 5, 8, 19, 33, 4, 18, 7, 25, 2]# Creo una lista
mayor_10 = [] #Creo una lista vacía para asignarle valores más adelante y la lista vacía siempre tiene que ir antes de los bucles
for numero in numeros: #Creo el bucle para recorrer la lista
    if numero > 10: #Si el numero en la lista es mayor a 10 se guardara en la lista vacía que cree
        mayor_10.append(numero) #Aquí lo que decimos es que agregamos a la lista vacia cuyos numeros sean mayores a 10
print(f"los numeros mayores a 10 son :{mayor_10}") #Mostramos por pantalla
print("La cantidad de numeros que tiene la nueva lista es de:", end=" ") #Mostramos por pantalla
print(len(mayor_10)) #Con esto contamos los elementos que están dentro de nuestra nueva lista.
