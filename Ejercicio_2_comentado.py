
# Lista vacía donde se almacenarán los datos de los alumnos
alumnos = []

# Función para ingresar datos de 3 alumnos chilenos
def ingresarAlumno():
    for alumno_n in range(3):
        alumno = {}
        alumno["nombre"] = input("Ingrese nombre del alummno: ")
        alumno["rut"] = input("Ingrese rut del alumno: ").strip().lower()
        
        try:
            alumno["edad"] = int(input("Ingrese edad del alumno: "))
        except ValueError:
            print("Edad no valida. Se asigna 0 por defecto.")
            alumno["edad"] = 0
        
        alumno["nacionalidad"] = input("Ingrese nacionalidad del alumno: ").strip().lower()
        alumno["calificaciones"] = []

        if alumno["nacionalidad"] != "chileno":
            print("No puedes matricularte (no eres chileno)")
            continue

        for i in range(3):
            try:
                nota = float(input("Ingrese nota del alumno:"))
                alumno["calificaciones"].append(nota)
            except ValueError:
                print("Nota no valida. Se asigna 0.")
                alumno["calificaciones"].append(0.0)

        alumnos.append(alumno)

# Función que muestra todos los datos de los alumnos ingresados
def mostrarDatos():
    for i, alumno in enumerate(alumnos):
        print(f"{i}: Rut: {alumno['rut']}, Nombre: {alumno['nombre']}, Edad: {alumno['edad']}, Nacionalidad: {alumno['nacionalidad']}, Calificaciones: {alumno['calificaciones']}")

# Función que permite editar los datos de un alumno según su RUT
def editarDatos():
    buscar_rut = input("Ingrese rut: ").strip().lower()
    encontrado = False
    for alumno in alumnos:
        if alumno["rut"] == buscar_rut:
            encontrado = True
            print("***Datos actuales del alumno encontrado***")
            print(f"nombre: {alumno['nombre']}")
            print(f"edad: {alumno['edad']}")
            print(f"nacionalidad: {alumno['nacionalidad']}")
            print(f"calificaciones: {alumno['calificaciones']}")

            print("Ingrese los nuevos datos que quiere cambiar")

            nuevo_nombre = input("Ingresa nuevo nombre:")
            if nuevo_nombre:
                alumno["nombre"] = nuevo_nombre

            try:
                nueva_edad = int(input("Ingresa nueva edad"))
                if nueva_edad:
                    alumno["edad"] = nueva_edad
            except ValueError:
                print("Edad no valida. Se mantiene la anterior")

            nueva_nacionalidad = input("Ingresa nueva nacionalidad:").strip().lower()
            if nueva_nacionalidad:
                if nueva_nacionalidad != "chileno":
                    print("No puedes matricularte, no eres chileno")
                else:
                    alumno["nacionalidad"] = nueva_nacionalidad

            actualizar_notas = input("¿Desea cambiar las notas? Si/No").strip().lower()
            if actualizar_notas == "si":
                nuevas_notas = []
                for i in range(3):
                    try:
                        nueva_nota = float(input("Ingrese nuevas notas:"))
                        nuevas_notas.append(nueva_nota)
                    except ValueError:
                        print("Nota no valida")
                        nuevas_notas.append(0.0)
                if len(nuevas_notas) == 3:
                    alumno["calificaciones"] = nuevas_notas
            print("Notas actualizadas correctamente")
            break
    if not encontrado:
        print("Alumno no encontrado con ese rut")

# Función que permite eliminar un alumno por RUT o todos los datos
def eliminarDatos():
    if not alumnos:
        print("No hay alumnos")
        return
    print("***Elige que quieres eliminar***")
    print("A. Eliminar un alumno por rut")
    print("B. Eliminar todos los datos")
    opcion = input("Ingrese una opción").strip().lower()
    if opcion == "a":
        rut_eliminar = input("Ingrese rut a eliminar:").strip().lower()
        eliminado = False
        for posicion, alumno in enumerate(alumnos):
            if alumno["rut"] == rut_eliminar:
                del alumnos[posicion]
                print(f"Alumno con rut {rut_eliminar} eliminado exitosamente")
                eliminado = True
                break
        if not eliminado:
            print("No se encontró un alumno con ese rut.")
    elif opcion == "b":
        confirmacion = input("¿Está seguro de que desea eliminar TODOS los alumnos? (si/no): ").strip().lower()
        if confirmacion == "si":
            alumnos.clear()
        else:
            print("Eliminación cancelada")
    else:
        print("Opción no válida")

# Función que encuentra al alumno con el mejor promedio
def alumnoMejorPromedio():
    mejor_promedio = -1
    mejor_alumno = None
    for alumno in alumnos:
        promedio = sum(alumno["calificaciones"]) / len(alumno["calificaciones"])
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_alumno = alumno
    if mejor_alumno is not None:
        print("Alumno con mejor promedio")
        print(f"nombre: {mejor_alumno['nombre']}")
        print(f"Rut: {mejor_alumno['rut']}")
        print(f"Promedio: {mejor_promedio:.1f}")
    else:
        print("No hay alumnos registrados")

# Función que muestra qué alumnos aprueban (promedio >= 4.0)
def alumnosAprueban():
    aprobados = 0
    for alumno in alumnos:
        promedio = sum(alumno["calificaciones"]) / len(alumno["calificaciones"])
        if promedio >= 4.0:
            aprobados += 1
            print(f"{alumno['nombre']} aprueba con promedio {promedio:.1f}")
    if aprobados == 0:
        print("Ninguno aprueba")
    else:
        print(f"El total de alumnos aprobados es de {aprobados}")

# Menú principal del programa
while True:
    print("***Menu principal***")
    print("""
        1. Ingresar alumnos
        2. Mostrar datos
        3. Editar datos (según ingreso de rut)
        4. Eliminar por rut o eliminar todos los alumnos
        5. Mejor promedio
        6. Aprueban
        7. Salir
          """)
    
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        ingresarAlumno()
    elif opcion == "2":
        mostrarDatos()
    elif opcion == "3":
        editarDatos()
    elif opcion == "4":
        eliminarDatos()
    elif opcion == "5":
        alumnoMejorPromedio()
    elif opcion == "6":
        alumnosAprueban()
    elif opcion == "7":
        print("El programa ha terminado")
        break
