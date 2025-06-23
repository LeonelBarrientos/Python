
diccionario = {
    "nombre" : "leonel",
    "apellido" : "barrientos",
    "subs" : 1000000
}
#Nos devuelve un objeto dict_item
claves = diccionario.keys()

#Obteniendo un elemento con get() (no me lanza una excepcion y si no encuentra nada el programa continua)
vañpr_de_quesucede= diccionario.get("que sucede")
print("el programa continua")

#Eliminando todo del diccionario
#diccionario.clear()

#Eliminando un elemento del diccionario
#diccionario.pop("subs")

#Obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()





print(diccionario_iterable)
