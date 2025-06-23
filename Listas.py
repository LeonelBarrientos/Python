
#Creando lista con list()
lista = list(["hola","leo",10,9,34])

#Devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#Agregando un elemento a la lista
lista.append("JAJA")

agregando_con_append = lista.append("JAJA") #Esto no esta mal pero no es necesario darle el valor porque no es tan impresindible pero es lo mismo de arriba

#Agregando un elemento a la lista en un indice especifico
lista.insert(2,"Que sucede")

#Agregando varios elementos a la lista, aqui para agregar los elementos es necesario pasarlos con los corchetes
lista.extend([False,2030])

#Elimando un elemento de la lista (por su indice)
lista.pop(-1) # -1 para eliminar el ultimo, -2 par eliminar el anteultimo, y asi sucesivamente


#Removiendo un elemento de la lista por su valor
lista.remove("hola")

#Ordenando la lista de forma ascendente (si usamos el parametro reverse=True lo ordena en reversa) (solo funciona con numeros)
lista.sort()

#Invirtiendo los elementos de una lista
lista.reverse()

#Verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(10)

#Elimina todos los elementos de una lista
lista.clear()





print(lista)