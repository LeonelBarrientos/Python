#Crear un menu en base a la lista y diccionarios dados.

# Diccionario de patines
patines = {
    '1234PT': ['Rollerblade', 38, 'bota rígida', 80, 'aluminio', 'intermedio', 'negro con rojo', 1.6, 'trasero', 'fitness'],
    '4321PT': ['Powerslide', 37, 'bota blanda', 76, 'plástico reforzado', 'principiante', 'azul marino', 1.4, 'trasero', 'fitness'],
    '1111PT': ['FR Skates', 39, 'bota rígida', 90, 'aluminio', 'avanzado', 'negro mate', 1.9, 'sin freno', 'urbano'],
    '1212PT': ['Oxelo', 40, 'bota blanda', 72, 'plástico', 'principiante', 'gris con verde', 1.3, 'trasero', 'fitness'],
    '2121PT': ['Rollerblade', 42, 'bota rígida', 84, 'aluminio', 'intermedio', 'negro con azul', 1.7, 'intercambiable', 'urbano'],
    '2222PT': ['Fila', 36, 'bota blanda', 76, 'plástico reforzado', 'principiante', 'rosa con blanco', 1.2, 'trasero', 'fitness'],
    '3131PT': ['Oxelo', 41, 'bota semirrígida', 80, 'aluminio', 'intermedio', 'gris con rojo', 1.5, 'trasero', 'fitness'],
    '1313PT': ['Oxelo', 40, 'bota rígida', 100, 'aluminio', 'avanzado', 'negro con dorado', 2.0, 'sin freno', 'freestyle']
}

# Diccionario de inventario
inventario = {
    '1234PT': [89990, 10],
    '4321PT': [79990, 4],
    '1111PT': [139990, 1],
    '1212PT': [59990, 13],
    '2121PT': [49990, 22],
    '2222PT': [99990, 7],
    '3131PT': [119990, 4],
    '1313PT': [109990, 5]
}


def modelos_por_marca(marca):
    cantidad = 0
    for codigo,datos in patines.items():
        if datos[0].lower() == marca.lower():
            print(f"{datos[0]} {codigo}")
            cantidad +=1
    if cantidad >0:
        print(f"Total de modelos de la marca {marca}: {cantidad}")
    else:
        print("No hay modelos de esa marca.")

def patines_disponibles_por_marca():
    conteo = {}
    for codigo,datos in patines.items():
        marca = datos[0]
        cantidad = inventario[codigo][1]
        conteo[marca] = conteo.get(marca,0) + cantidad
    for marca,total in conteo.items():
        print(f"{marca}: {total} unidades disponibles.")

def cantidad_patines_por_talla():
    try:
        talla = int(input("Ingresa la talla para buscar: "))
    except ValueError:
        print("Invalido.Ingresa un numero entero.")
        return
    cantidad = 0
    for codigo,datos in patines.items():
        if datos[1] == talla:
            cantidad += inventario[codigo][1]
    if cantidad > 0:
        print(f"Tenemos {cantidad} disponibles en la talla que buscas.")
    else:
        print("No tenemos pares disponibles en esa talla :(")

def busqueda_por_rango_precio():
    try:
        valor_minimo = int(input("Ingrese valor minimo: "))
        valor_maximo = int(input("Ingrese valor maximo: "))
    except ValueError:
        print("Ingresa un numero entero.")
        return
    encontrados = False
    for codigo,datos in inventario.items():
        precio = datos[0]
        if valor_minimo <= precio <= valor_maximo:
            marca = patines[codigo][0]
            stock = datos[1]
            print(f"Codigo: {codigo}, Marca: {marca}, precio: ${precio}, stock: {stock}")
            encontrados = True
    if not encontrados:
        print("No se encontraron patines en ese rango de precio.")

def busqueda_por_tamanio_rueda():
    try:
        tamanio_rueda = int(input("Ingresa un tamaño de rueda: "))
    except ValueError:
        print("Ingresa un numero entero.")
        return
    encontrados = False
    for codigo,datos in patines.items():
        if datos[3] == tamanio_rueda:
            marca = patines[codigo][0]
            stock = inventario[codigo][1]
            print(f"codigo: {codigo}, marca: {marca}, stock: {stock}")
            encontrados = True
    if not encontrados:
        print("No se encontraron patines con ese tamaño de rueda.")

def actualizar_precio():
    codigo_patines = input("Ingrese el codigo a actualizar: ").upper().strip()
    if codigo_patines not in inventario:
        print("El codigo que ingresaste no esta en nuestro inventario.")
        return
    print("¿Qué deseas actualizar?")
    print('1.Precio')
    print('2.Cantidad')
    opcion_actualizar = input("Ingrese la opción: ")
    if opcion_actualizar == '1':
        try:
            nuevo_precio = int(input("Ingrese el nuevo precio: "))
            inventario[codigo_patines][0] = nuevo_precio
            print("¡Precio actualizado!")
        except ValueError:
            print("Debes ingresar un numero entero.")
    elif opcion_actualizar == '2':
        try:
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            inventario[codigo_patines][1] = nueva_cantidad
            print("¡Cantidad actualizada!")
        except ValueError:
            print("Debes ingresar un numero entero.")
    else:
        print("Opción invalida.")

while True:
    print("\nMenú principal")
    print("1. Cantidad de modelos por marca")
    print("2. Cantidad de patines disponibles por marca")
    print("3. Cantidad de patines disponibles por talla")
    print("4. Búsqueda por rango de precio")
    print("5. Búsqueda de patines por tamaño de rueda")
    print("6. Actualizar precio y/o cantidad")
    print("7. Salir")
    try:
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            marca = input("Ingrese una marca: ").strip().lower()
            modelos_por_marca(marca)
        elif opcion == 2:
            patines_disponibles_por_marca()
        elif opcion == 3:
            cantidad_patines_por_talla()
        elif opcion == 4:
            busqueda_por_rango_precio()
        elif opcion == 5:
            busqueda_por_tamanio_rueda()
        elif opcion == 6:
            actualizar_precio()
        elif opcion == 7:
            print("Haz salido del programa.")
            break
        else:
            print("Ingrese una opción entre 1-7.")
    except ValueError:
        print("Ingrese una opción valida.")









