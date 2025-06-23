#Crear una lista de 5 frutas y mostrarla por pantalla.

#Agregar una fruta al final de la lista.

#Insertar una fruta en la segunda posición.

#Eliminar la última fruta de la lista.

#Contar cuántas frutas hay en la lista.

#Mostrar el primer y el último elemento de la lista.

frutas = ["pera","manzana","platano","durazno","frutilla"] #creo la lista con 5 frutas
print(frutas) #muestro la lista en pantalla
frutas.append(input("ingrese una fruta: ")) #agrego una nueva fruta al final con append
print(frutas) #muestro la lista actualizada
frutas.insert(2,input("ingrese una fruta para la posición 2: ")) #agrego una nueva fruta en lo posición indicada en este caso en la posición 2
print(frutas) #Muestro la lista actualizada
frutas.pop(-1) #Aquí elimino el ultimo elemento en mi lista con el pop y -1
print(frutas) #Muestro mi lista actualizada
cantidad = len(frutas) #Con len cuento cuantos elementos hay en mi lista
print(f"en la lista hay {cantidad} frutas") #Muestro por pantalla cuantos elementos hay
print("el primer y el ultimo elemento en la lista son:",end=" ") #Uso end para que se junten las lineas de codigo siguientes y sea más intuitivo de leer
print(frutas[0], end=",") #Muestro el primer elemento de mi lista por pantalla
print(frutas[-1]) #Muestro el ultimo elemento de mi lista por pantalla


