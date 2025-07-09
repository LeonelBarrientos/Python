peliculas = {
    'P001': ['Inception', 'Ciencia Ficción', 2010, 'Christopher Nolan'],
    'P002': ['Parasite', 'Drama', 2019, 'Bong Joon-ho'],
    'P003': ['Toy Story', 'Animación', 1995, 'John Lasseter'],
    'P004': ['Interstellar', 'Ciencia Ficción', 2014, 'Christopher Nolan'],
    'P005': ['The Godfather', 'Crimen', 1972, 'Francis Ford Coppola']
}



def mostrar_por_director(director):
    hay_pelicula = False
    for codigo,datos in peliculas.items():
        if datos[3].lower()== director.lower():
            print(f"{datos[0]} ({codigo})")
            hay_pelicula = True
    if not hay_pelicula:
        print("No se encontraron películas de ese director.")

def agregar_pelicula():
        codigo = input("Ingrese un codigo: ").upper().strip()
        if codigo in peliculas:
            print("El codigo ya existe")
            return
        titulo = input("Ingrese titulo de la pelicula: ").strip()
        genero = input("Ingrese genero de la pelicula: ").strip()
        try:
            anio = int(input("Ingrese el anio de estreno de la pelicula: "))
        except ValueError:
            print("¡Debes ingresar un numero entero!")
            return
        director_pelicula = input("Ingrese el director: ").strip()
        peliculas[codigo] = [titulo,genero,anio,director_pelicula]
        print("¡Pelicula agregada exitosamente!")

        
while True:
    print("\n***Menú Principal***")
    print("1.Mostrar peliculas por director")
    print("2. Agregar pelicula")
    print("0. Salir")
    try:
        opcion = int(input("Ingrese una opción: "))
        
        if opcion == 1:
            director = input("Ingrese un director: ")
            mostrar_por_director(director)
        elif opcion == 2:
            agregar_pelicula()
        elif opcion == 0:
            print("Haz dejado el programa.")
            break

    except ValueError:
        print("Ingrese una opción valida.")
