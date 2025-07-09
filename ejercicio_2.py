
reservas = {}
#for i in range(1,21):
    #reservas[str(i)] = f"zapatilla{i}"
def reservar_zapatillas():
    nombre_comprador = input("Ingresa un nombre: ")
    if nombre_comprador in reservas:
        print("Comprador ya tiene reserva.")
        return
    palabra_secreta = input("Para confirmar la reserva escriba 'EstoyEnListaDeReserva': ")
    if palabra_secreta != 'EstoyEnListaDeReserva':
        print("Palabra clave incorrecta.Reserva no realizada")
        return
    
    pares_reservados = sum(reservas.values())
    if pares_reservados >= 20:
        print("No hay stock disponible para reservar.")
        return
    else:
        reservas[nombre_comprador] = 1
        print(f"Reserva exitosa para {nombre_comprador}")

def buscar_zapatillas_reservadas():
    nombre_reserva = input("Ingrese un nombre: ")
    if nombre_reserva not in reservas:
        print("No se encontro ninguna reserva con ese nombre.")
        return
    
    pares = reservas[nombre_reserva]
    tipo = 'VIP' if pares == 2 else 'Estándar'
    print(f"Reserva encontrada: {nombre_reserva} - {pares} par(es) ({tipo})")

    if pares == 1:
        respuesta = input("¿Desea pagar adicional para VIP y reservar 2 pares? si/no: ").strip().lower()
        if respuesta == 'si':
            if sum(reservas.values()) + 1 <=20:
                reservas[nombre_reserva] = 2
                print(f"Reserva actualizada a vip.Ahora {nombre_reserva} tiene 2 pares reservados.")
            else:
                print("No fue posible actualizar a VIP.Stock insuficiente.")
        else:
            print("Manteniendo reserva actual.")
    else:
        print("Manteniendo reserva actual.")

def ver_stock_de_reservas():
    print("\n**** Stock de reservas***")
    pares_reservados = sum(reservas.values())
    pares_disponibles = 20 - pares_reservados
    print(f"Los pares reservados actualmente son {pares_reservados}")
    print(f"Los pares disponibles actualmente son {pares_disponibles}")

while True:
    print("TOTEM AUTOATENCIÓN RESERVA STRIKE")
    print("1.- Reservar zapatillas")
    print("2.- Buscar zapatillas reservadas.")
    print("3.- Ver stock de reservas.")
    print("4.- Salir.")

    try:
        opcion = int(input("Ingresa una opción: "))
        if opcion == 1:
            reservar_zapatillas()
        elif opcion == 2:
            buscar_zapatillas_reservadas()
        elif opcion == 3:
            ver_stock_de_reservas()
        elif opcion == 4:
            print("Haz dejado el programa.")
            break
        else:
            print("Opción invalida")
    except ValueError:
        print("Debes ingresar un numero entero entre 1-4")

        
