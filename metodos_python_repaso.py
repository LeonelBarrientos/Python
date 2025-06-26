
# Métodos y funciones comunes en Python - Explicaciones y ejemplos

# 1. .items()
# Para diccionarios: devuelve lista de tuplas (clave, valor)
dic = {"nombre": "Ana", "edad": 30}
for clave, valor in dic.items():
    print(clave, valor)

# 2. enumerate()
# Para listas: devuelve índice y valor al recorrer
nombres = ["Luis", "Ana"]
for i, nombre in enumerate(nombres):
    print(i, nombre)

# 3. .clear()
# Borra todos los elementos de una lista o diccionario
lista = [1, 2, 3]
lista.clear()
print(lista)  # []

# 4. sum()
# Suma todos los valores numéricos de una lista
notas = [5, 6, 7]
print(sum(notas))  # 18

# 5. None
# Representa un valor vacío o sin definir
x = None
if x is None:
    print("Sin valor")

# 6. is not None
# Verifica si una variable sí tiene valor
if x is not None:
    print("Tiene valor")

# 7. .split()
# Divide un string en partes según separador
fecha = "12-06-2024"
print(fecha.split("-"))  # ['12', '06', '2024']

# 8. .zfill()
# Rellena con ceros a la izquierda
mes = "3"
print(mes.zfill(2))  # "03"

# 9. .pop()
# Elimina y devuelve el último valor de la lista (o por índice)
nombres = ["Ana", "Luis", "Pedro"]
ultimo = nombres.pop()
print(ultimo)  # "Pedro"

# 10. .keys()
# Devuelve solo las claves de un diccionario
persona = {"nombre": "Ana", "edad": 30}
print(persona.keys())  # dict_keys(['nombre', 'edad'])

# 11. .get()
# Busca una clave y evita error si no existe
print(persona.get("apellido", "No definido"))  # "No definido"

# 12. .insert()
# Inserta valor en posición específica en lista
numeros = [1, 2, 4]
numeros.insert(2, 3)
print(numeros)  # [1, 2, 3, 4]

# 13. .remove()
# Elimina la primera aparición del valor
colores = ["rojo", "verde", "rojo"]
colores.remove("rojo")
print(colores)  # ['verde', 'rojo']

# 14. .sort()
# Ordena una lista de menor a mayor
numeros = [3, 1, 2]
numeros.sort()
print(numeros)  # [1, 2, 3]
