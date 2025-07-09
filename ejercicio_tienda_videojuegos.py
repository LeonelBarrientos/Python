videojuegos = {
    'VG001': ['El perfume Axe', 'PS5', 'RPG', '100+', 'Herni'],
    'VG002': ['El carrete del Jona', 'PS5', 'Bohemia', '20+', 'Don Willy'],
    'VG003': ['Minecraft', 'PC', 'Sandbox', '7+', 'Mojang'],
    'VG004': ['The Legend of Zelda: TOTK', 'Switch', 'Aventura', '12+', 'Nintendo'],
    'VG005': ['God of War Ragnarok', 'PS5', 'Acción', '18+', 'Santa Monica Studio'],
    'VG006': ['Mario Kart 8', 'Switch', 'Carreras', '3+', 'Nintendo'],
    'VG007': ['Fortnite', 'PC', 'Battle Royale', '12+', 'Epic Games'],
}

inventario = {
    'VG001': [59990, 5],
    'VG002': [49990, 10],
    'VG003': [29990, 0],
    'VG004': [69990, 3],
    'VG005': [64990, 7],
    'VG006': [39990, 15],
    'VG007': [0, 100],
}

def stock_por_desarrolladora(dev):
    encontrada = False
    for codigo,datos in videojuegos.items():
        if datos [4].lower() == dev:
            stock = inventario[codigo][1]
            print(f"{datos[0]}({codigo}) - Stock: {stock}")
            encontrada = True
    if not encontrada:
        print("No hay videojuegos en esa desarrolladora.")

def busqueda_por_plataforma(plataforma):
    resultados = []  # 1. Crear lista vacía para guardar los juegos que cumplen la condición

    for codigo, datos in videojuegos.items():
        # 2. Verificar condición (plataforma y stock)
        if datos[1].lower() == plataforma and inventario[codigo][1] > 0:
            # 3. Agregar el título y código a la lista resultados
            resultados.append([datos[0], codigo])
    
    # 4. Ordenar la lista resultados por título (que es el índice 0)
    resultados_ordenados = sorted(resultados)

    # 5. Verificar si la lista está vacía para mostrar mensaje
    if len(resultados_ordenados) == 0:
        print("No hay videojuegos con stock para esa plataforma.")
    else:
        # 6. Recorrer la lista ordenada e imprimir resultados
        for titulo, codigo in resultados_ordenados:
            print(f"{titulo} {codigo}")

def actualizar_stock(codigo, nuevo_stock):
    try:
        nuevo_stock = int(nuevo_stock)
    except ValueError:
        print("Debe ingresar un numero entero para el stock.")
        return
    if not codigo in inventario:
        print("El codigo que ingresaste no existe.")
        return
    inventario[codigo][1] = nuevo_stock
    print("El Stock ha sido actualizado.")

def eliminar_videojuego(codigo):
    if codigo in inventario and codigo in videojuegos:
        del inventario[codigo]
        del videojuegos[codigo]
        print("¡El videojuego ha sido eliminado con exito!")
    else:
        print("El codigo ingresado no existe.")

            



while True:
    print("\nMENÚ PRINCIPAL")
    print("1. Stock por desarrolladora")
    print("2. Búsqueda por plataforma")
    print("3. Actualizar stock")
    print("4. Eliminar videojuego por código")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ").strip()

    if opcion == '1':
        dev = input("Ingrese una desarrolladora: ").lower().strip()
        stock_por_desarrolladora(dev)

    elif opcion == '2':
        plataforma = input("Ingrese la plataforma a buscar: ").lower().strip()
        busqueda_por_plataforma(plataforma)
    
    elif opcion == '3':
        codigo = input("Ingresa el código del videojuego: ")
        nuevo_stock = input("Ingrese el nuevo stock: ")
        actualizar_stock(codigo,nuevo_stock)
    
    elif opcion == '4':
        codigo = input("Ingresa el codigo del videojuego que deseas eliminar: ").strip()
        eliminar_videojuego(codigo)
    elif opcion == '5':
        print("Programa finalizado.")
        break

    else:
        print("Debe seleccionar una opción válida!!")