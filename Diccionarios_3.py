estudiante = {
        "nombre":"Mike",
        "edad":90,
        "nacionalidad":"Gringo",
        "nacimiento":2000
    }


def mostrarDatos():
    for clave,valor in estudiante.items():
        print(f"{clave}: {valor}")

def modificar():
     clave_a_modificar = input("Ingrese la clave que quiere modificar: ")
     if clave_a_modificar in estudiante:
          nuevo_valor = input(f"Ingresa un nuevo valor para {clave_a_modificar}")
          estudiante[clave_a_modificar] = nuevo_valor
          print(f"La {clave_a_modificar} fue actualizada con exito.")
     else:
          print("La clave que ingresaste no está en el diccionario")
def agregarDato():
      nueva_clave = input("Ingrese la nueva clave que quiere agregar: ")
      if nueva_clave in estudiante:
           print("La clave ya existe")
      else:
           nuevo_valor = input(f"Ingrese el nuevo valor para {nueva_clave}")
           estudiante[nueva_clave] = nuevo_valor
           print(f"{nueva_clave} fue agregada correctamente")
           


def  eliminarDato():
      dato_a_eliminar = input("Ingrese la clave que quiere elimnar: ")
      if dato_a_eliminar in estudiante:
           del estudiante[dato_a_eliminar]
           print(f"{dato_a_eliminar} fue eliminda exitosamente")
      else:
           print("Esa clave no existe.")
     
     

          
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

