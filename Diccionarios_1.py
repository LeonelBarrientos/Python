#Crea un diccionario llamado estudiante con los siguientes datos:

#nombre: "Matías"

#edad: 20

#carrera: "Ingeniería"

#promedio: 6.2

#Luego, recorre el diccionario e imprime cada clave y valor con el formato:


estudiante = {"nombre":"Matias","edad":20,"carrera":"ingeniería","promedio":6.2} #Creo el diccionario
estudiante["edad"] = int(input("Ingrese la edad de matias:")) #Con este parametro podemos modifcar su edad
estudiante["correo"] = input("Ingrese su correo: ") #De esta manera podemos agregar una nueva clave y valor en este caso un correo
clave_a_borrar = input("ingrese que desea borrar:") #Creamos este input para que ingrese una clave que este en el diccionario para borrar
if clave_a_borrar in estudiante: #Aquí decimos si la clave a borrar esta en el diccionario, pasará a borrar esa clave
    del estudiante[clave_a_borrar] #La borramos con del
    print(f"La clave {clave_a_borrar} fue eliminada con exito.") #Si ingresaste una clave existente mostrara este print por pantalla
else: #Sino te arrojará un mensaje de que la clave que ingresaste no se encuentra en el diccionario
    print(f"La clave {clave_a_borrar} no se encuentra en el diccionario") #Mostramos el mensaje
for clave in estudiante: #Recorro cada clave en mi diccionario de estudiante
    print(clave,":",estudiante[clave]) #Imprimo cada clave y su valor correspondiente
