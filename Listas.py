# Crea una lista con 5 números y muestra el mayor.

# Agrega un elemento al final de una lista.

# Elimina el primer número par de una lista.

# Invierte una lista sin usar [::-1].

lista = [1,2,3,4,5]
print(lista)
mayor = max(lista)
print(f"el numero mayor es: {mayor}")
elemento_final = input("ingrese el elemento a agregar")
lista.append(elemento_final)
print(lista)
for numero in lista:
    if numero % 2==0:
        lista.remove(numero)
        break
print(lista)
lista.reverse()
print(lista)


