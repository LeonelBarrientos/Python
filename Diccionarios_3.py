estudiante = {
        "nombre":"Mike",
        "edad":90,
        "nacionalidad":"Gringo",
        "nacimiento":2000
    }


def mostrarDatos(): #Creo def mostrarDatos para la opcion 1
    for clave,valor in estudiante.items(): #Le digo al bucle que recorra la clave y su valor en el diccionario y usamos el .items() para que devuelva tanto la clave como el valor
        print(f"{clave}: {valor}") #Lo mostramos por pantalla

def modificar(): #Creo def Modificar para la opcion 2
     clave_a_modificar = input("Ingrese la clave que quiere modificar: ") #Pedimos por pantalla que ingrese una clave que ya este en el diccionario
     if clave_a_modificar in estudiante: #Si la clave se encuentra en el diccionario pasamos a pedirle el valor
          nuevo_valor = input(f"Ingresa un nuevo valor para {clave_a_modificar}") #Pedimos el nuevo valor que se le asignara a la clave ya existente
          estudiante[clave_a_modificar] = nuevo_valor #Decimos en el diccionario si esta la clave que ingreso se le asigna el nuevo valor
          print(f"La {clave_a_modificar} fue actualizada con exito.") #Mostramos por pantalla mensaje de exito
     else: #Sino mostramos un mensaje de que la clave ingresada no se encuentra en nuestro diccionario
          print("La clave que ingresaste no está en el diccionario") #Mostramos por pantalla
def agregarDato(): #Creo def agregarDato para la opción 3
      nueva_clave = input("Ingrese la nueva clave que quiere agregar: ") #Pedimos por pantalla que ingrese una nueva clave para el diccionario
      if nueva_clave in estudiante: #Decimos, si la nueva clave se encuentra en nuestro diccionario, mostraremos un mensaje de que ya existe
           print("La clave ya existe") #Mostramos mensaje por pantalla
      else: #Si el valor que ingresamos no está en el diccionario pasaremos a pedirle el valor que se le asignará
           nuevo_valor = input(f"Ingrese el nuevo valor para {nueva_clave}") #Pedimos el valor
           estudiante[nueva_clave] = nuevo_valor #Decimos, al diccionario se le agrega una nueva clave y a la clave el nuevo valor
           print(f"{nueva_clave} fue agregada correctamente") #Mostramos mensaje de exito
           


def  eliminarDato(): #Crear def eliminar un dato para la opción 4
      dato_a_eliminar = input("Ingrese la clave que quiere elimnar: ") #Solicitamos que ingrese una clave para eliminar (Tiene que existir en el diccionario)
      if dato_a_eliminar in estudiante: #Si la clave a eliminar se encuentra en el diccionario pasamos a eliminarla
           del estudiante[dato_a_eliminar] #Eliminamos la clave con del
           print(f"{dato_a_eliminar} fue eliminada exitosamente") #Mostramos por pantalla mensaje de exito
      else: #Si la clave que ingresamos para eliminar no se encuentra en el diccionario, mostraremos por pantalla un mensaje de que no existe
           print("Esa clave no existe.") #Mostramos mensaje por pantalla
     
     

#Creamos nuestro menu con sus respectivas opciones y el llamado a los def.
while True:
    try: 
        print("""       ***Mini Menu***
                1.Mostrar todos los datos del estudiante.
                2.Modificar un dato existente.
                3.Agregar un nuevo dato (clave y valor).
                4.Eliminar un dato por clave.
                5.Salir.
                """)
        opcion = int(input("Ingrese una opción:"))
        if opcion ==1:
            print("-------------------------------------")
            mostrarDatos()
        elif opcion==2:
            modificar()
        elif opcion==3:
            agregarDato()
        elif opcion==4:
            eliminarDato()
        elif opcion ==5:
                print("Haz salido del programa con exito.")
                break
        else:
            print("La opción que ingresaste no es valida")
    except ValueError:
         print("debes ingresar un número valido")

