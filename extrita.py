libros = {
    'LB001': ['Cien años de soledad', 'Gabriel García Márquez', 'Realismo mágico', '16+', 'Sudamericana'],
    'LB002': ['1984', 'George Orwell', 'Distopía', '14+', 'Secker & Warburg'],
    'LB003': ['Harry Potter y la piedra filosofal', 'J.K. Rowling', 'Fantasía', '10+', 'Bloomsbury'],
    'LB004': ['El Principito', 'Antoine de Saint-Exupéry', 'Fábula', '7+', 'Reynal & Hitchcock'],
    'LB005': ['It', 'Stephen King', 'Terror', '18+', 'Viking Press'],
}

inventario = {
    'LB001': [12990, 3],
    'LB002': [10990, 0],
    'LB003': [14990, 10],
    'LB004': [8990, 5],
    'LB005': [13990, 2],
}


def buscar_por_genero(genero):
    hay_libro = False
    for codigo,datos in libros.items():
        if datos[2].lower() == genero.lower():
            print(f"{datos[0]} {codigo}")
            hay_libro = True
    if not hay_libro:
        print("No hay libros de ese genero.")
    print(f"Actualemnente {datos[0]}({codigo}) - tiene un stock de: {inventario[codigo][1]}")    


        













while True:
    print("\n***Menú Principal***")
    print("1. buscar libros por su género")
    print("2.Salir")
    try:
        opcion = input("Ingrese opcion")
        if opcion == '1':
            genero = input("Ingrese el genero que desea buscar: ").lower()
            buscar_por_genero(genero)
        elif opcion == '2':
            print("Haz dejado el programa.")
            break
        else:
            print("Ingresa un numero en el rango de 1-2.")
    except ValueError:
        print("Ingresa un caracter valido para el menú.")