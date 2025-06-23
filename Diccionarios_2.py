

estudiante = {
    "nombre": "Matias",
    "edad": 20,
    "carrera": "ingeniería",
    "promedio": 6.2
}
for clave in estudiante:
    print(clave,":",estudiante[clave])
#Le pida al usuario el nombre de la clave que quiere modificar (por ejemplo: edad)

#Si esa clave existe, que le pida el nuevo valor y la modifique.

#Si no existe, que muestre un mensaje diciendo que esa clave no está en el diccionario.
clave_a_modificar= input("ingrese una clave que quiere modificar:") #Le digo que del diccionario elija una clave para modificar
if clave_a_modificar in estudiante: #Si la clave que ingreso está en el diccionario le pediremos que valor le asignara
    nuevo_valor = input(f"Ingrese el nuevo valor para {clave_a_modificar}") #Creamos el nuevo valor y se lo pedimos como imput
    estudiante[clave_a_modificar] = nuevo_valor #Aquí decimos que del diccionario la clave que ingresamos pasa a ser reemplazada por el nuevo valor que ingresamos
    print(f"{clave_a_modificar} fue actualizada") #Mostramos por pantalla el mensaje de exito
else:
    print("La clave que ingresaste no esta en el diccionario.")
print(estudiante)#Mostramos el diccionario


