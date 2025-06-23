

diccionario = {1:"uno",2:"dos",3:"tres"} #Creamos nuestro diccionario y separamos cada elemento y su key con una ","
diccionario[3] = input("ingresa algo") #Con esto lo que podemos hacer es reemplazar un elemento por uno que escribamos por teclado
#print(diccionario) #Mostramos el diccionario 
for clave in diccionario:
    print(clave,":",diccionario[clave])