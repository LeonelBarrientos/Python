
reservas = {}
for i in range(1,21):
    reservas[str(i)] = f"zapatilla{i}"

compradores = []
zapatillas_reservadas = []

def reservarZapatillas():
    nombre = input("Ingrese nombre de comprador:").strip().lower()
    if nombre in compradores:
        print("No puedes reservar.Este nombre ya está en la lista.")
        return
    confirmar = input("Para confirmar la reserva escriba (EstoyEnListaDeReserva)")
    if confirmar != "EstoyEnListaDeReserva":
        print("Esa no es la palabra clave.")
        return
    print("Reserva exitosa.")
    print("Zapatillas disponibles:")

    for clave, nombre_zapatilla in reservas.items():
        print(f"{clave} {nombre_zapatilla}")

    while True:
        opcion = input("Ingrese zapatilla a reservar del 1-20: ").strip().lower()
        if opcion in reservas:
            zapatillas_reservadas.append(reservas[opcion])
            compradores.append(nombre)
            del reservas[opcion]
            print(f"zapatilla {opcion} reservada exitosamente.")
            break
        else:
            print("El numero que ingresaste esta fuera del rango establecido o la zapatilla ya se encuentra reservada.")
            print("Intente nuevamente")

def verZapatillasReservadas():
    if not zapatillas_reservadas:
        print("Nadie ha reservado aún.")
    else:
        print("***Zapatillas reservadas***")
        for zapatilla in zapatillas_reservadas:
            print("-",zapatilla)

def stockReservas():
    print(f"Stock restante: {len(reservas)} zapatillas disponibles.")
    if reservas:
        for clave,nombre_zapatilla in reservas.items():
            print(f"{clave} {nombre_zapatilla}")
        


while True:
    print("***Menú principal")
    print("""
    TOTEM AUTOATENCIÓN RESERVA STRIKE
    1.- Reservar zapatillas
    2.- Ver zapatillas reservadas
    3.- Ver stock disponible
    4.- Salir
    """)
    
    opcion = int(input("Ingrese una opción:"))
    try:
        if opcion == 1:
            reservarZapatillas()
        elif opcion == 2:
            verZapatillasReservadas()
        elif opcion == 3:
            stockReservas()
        elif opcion == 4:
            print("Haz dejado el programa con exito.")
            break
        else:
            print("Ingrese un numero dentro del rango establecido.")
    except ValueError:
        print("Ingresa una opción valida.")



