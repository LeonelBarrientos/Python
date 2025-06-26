# Diccionario principal con los datos de los turistas
# Cada clave es un ID y cada valor es una lista con [Nombre, País, Fecha de ingreso]
turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"]
}

# Función que muestra los turistas de un país dado
def turistas_por_pais(pais):
    pais_turistas = []  # Lista para guardar nombres encontrados
    for clave in turistas.values():  # Recorre los valores del diccionario
        if clave[1].strip().lower() == pais:  # Compara el país en minúsculas
            pais_turistas.append(clave[0])  # Guarda el nombre del turista
    if pais_turistas:
        for nombre in pais_turistas:
            print(nombre)  # Muestra cada turista encontrado
    else:
        print("No hay turistas de ese país.")  # Si no se encontró ninguno

# Función que muestra turistas que ingresaron en un mes específico
def turistasPorMes(mes):
    turistas_mes = []  # Lista para guardar nombres encontrados
    for clave in turistas.values():
        if clave[2].split("-")[1] == mes:  # Extrae el mes desde la fecha y compara
            turistas_mes.append(clave[0])  # Guarda el nombre
    if turistas_mes:
        for posicion in turistas_mes:
            print(posicion)  # Muestra cada turista encontrado
    else:
        print("No se encuentra ese mes.")  # Si no se encontró ninguno

# Función que elimina un turista por su ID
def eliminarTurista():
    turista_a_eliminar = input("Ingresa el id del turista a eliminar:").strip().lower()  # Pide el ID
    if turista_a_eliminar in turistas:
        del turistas[turista_a_eliminar]  # Elimina al turista del diccionario
        print("Eliminación exitosa.")
    else:
        print("No se encontró ese turista.")  # Si el ID no existe
    print("***Lista actualizada***")
    print(turistas)  # Muestra el diccionario actualizado

# Bucle principal del programa: muestra el menú y ejecuta las opciones
while True:
    print("***Menú***")
    print("""
        1.- Turistas por país.
        2.- Turista por mes.
        3.- Eliminar turista.
        4.- Salir
    """)
    try:
        opcion = int(input("Ingrese una opción:"))  # Pide al usuario una opción numérica
    except ValueError:
        print("Ingrese una opción válida entre 1-4.")  # Maneja error si no es un número
        continue

    if opcion == 1:
        pais = input("¿De qué país quieres ver turistas?:").strip().lower()  # Pide país
        turistas_por_pais(pais)  # Llama a la función correspondiente
    elif opcion == 2:
        mes = input("Ingrese mes a buscar entre 01-12:").strip()  # Pide el mes
        mes = mes.zfill(2)  # Asegura que tenga dos dígitos (ej: "3" → "03")
        turistasPorMes(mes)
    elif opcion == 3:
        eliminarTurista()  # Llama a la función de eliminación
    elif opcion == 4:
        print("Haz dejado el programa con éxito.")  # Finaliza el programa
        break
    else:
        print("Ingresa una opción dentro del rango de 1-4")  # Si la opción está fuera de rango
