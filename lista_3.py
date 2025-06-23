#Eliminar los elementos repetidos de una lista sin usar set().

#Contar cuántas veces aparece un número específico en una lista.

#Intercambiar el primer y el último elemento de una lista.

#Separar los números pares e impares de una lista en dos listas diferentes.

#Ordenar una lista de números sin usar sort() (algoritmo de burbuja simple).

#Buscar si un número ingresado por el usuario está en la lista y mostrar su posición

lista = [10,20,10,69] #"leo","rocket","rocket"
lista_sin_repetidos = []
for elemento in lista:
    if elemento not in lista_sin_repetidos: #Si este número aún no está en la lista lista_sin_repetidos, agrégalo
        lista_sin_repetidos.append(elemento)#Aquí se agregan
print(lista_sin_repetidos) #Muestro la lista sin numeros repetidos por pantalla

numero_especifico = (input("Ingrese el elemento especifico a encontrar: "))
try: #Envuelvo todo en un try
    if "." in numero_especifico: #Si aparece un punto en la entrada lo convierte a float
        numero_especifico = float(numero_especifico) #Convierte la entrada a float
    else: #Si la entrada no tiene un punto pasa a tomarlo como numero entero
        numero_especifico = int(numero_especifico) #Lo convierte a numero entero
except ValueError: #Si hay un error con el valor ingresa te tirara un mensaje por pantalla
    print("el valor ingresado no es valido") #Mensaje por pantalla
cantidad = lista.count(numero_especifico) #Te muestra cuantas veces aparece un numero especifico en la lista
print(f"Aparece {cantidad} veces") #Mensaje por pantalla
lista [0],lista[-1] = lista[-1],lista[0] #Intercambiamos el primer elemento al ultimo lugar y el ultimo lugar al primer lugar
print(f"la nueva lista con intercambios es:{lista}") #Mostramos por pantalla
lista.sort() #Ordenamos la lista de menor a mayor con sort(), si queremos de mayor a menor agregar el reverse=True
print(f"La lista ordenada de sería así:{lista}") #Mostramos por pantalla
try: #Envolvemos todo dentro de un try
    buscar_numero = int(input("Ingrese un numero a buscar para saber su posición:")) #Pedimos que ingrese el numero a buscar
    if buscar_numero in lista: #Si el numero que ingresamos esta en la lista
        posicion_num = lista.index(buscar_numero) #Buscara el numero y mostrara en que posición está
        print(f"El elemento que ingresaste esta en la posición:{posicion_num}") #Mostramos por pantalla
    else: #Sino le mostraremos un mensaje de que el numero no está en la lista
        print("El numero no esta en la lista") #Mostramos mensaje
except ValueError: #Si ingresamos un cualquier otro valor que no sea un numero entero arrojaremos un mensaje
    print("algo estas haciendo mal") #Mostramos por pantalla el mensaje

