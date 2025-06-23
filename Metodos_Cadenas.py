
cadena1 = "Hola,me,lamo,Leonel"
cadena2 = "Bienvenido"

#convierte a mayusculas
mayusc = cadena1.upper()

#convierte a minuscula
minusc = cadena1.lower()

#primera letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()

#Buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("a")

#Buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepcion
busqueda_index = cadena1.index("o")

#Si es numerico devolvemos True, sino devolvemos False
es_numerico = cadena1.isnumeric()

#Si es alfanumerico (De la letra A-Z SIN ESPACIOS) devolvemos True, sino False
es_alfanumerico = cadena1.isalpha()

#Contamos las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("L")

#Contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#Verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("Hola")

#Verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("Leonel")

#Reemplaza un pedazo de la cadena dada, por otra dada
#Si el valor 1, se encuentra en la cadena original, reemplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace(","," ")
cadena_nueva2 = cadena1.replace("Hola","Que sucede")

#Separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")
print(cadena_separada)
#Como te los separa como si fuera una lista le puedes pedir que te imprima solo la cadena que este en x lugar
print(cadena_separada[3])






