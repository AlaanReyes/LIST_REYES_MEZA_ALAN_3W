print("Welcome to Project 1!")  # BIENVENIDA AL PROGRAMADOR 
print(" ")  # ESPACIO

print("REYES MEZA ALAN EDUARDO : PRACTICAS TUPLAS   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

# Primera lista
thislist = ["apple", "banana", "cherry"]
print("Lista original:", thislist)

# Número de elementos en la lista
print("Número de elementos en la lista:", len(thislist))

# Separar con un espacio
print(" ")

# Definición de varias listas
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]

# Muestra los miembros de cada lista
print("List1:", list1)
print("List2:", list2)
print("List3:", list3)
print("List4:", list4)
print(" ")

# Muestra el miembro 1 (comenzando en 0)
print("El segundo elemento de list1 es:", thislist[1])

# Muestra el último miembro de la lista
print("El último elemento de list1 es:", thislist[-1])

# Muestra los elementos del índice 2 al 5 (exclusivo)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("Elementos del índice 2 al 5:", thislist[2:5])

# Agregando miembros
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print("Lista después de agregar 'orange':", thislist)

# Agregando en la segunda posición
thislist.insert(1, "kiwi")
print("Lista después de insertar 'kiwi' en la segunda posición:", thislist)

# Quitando 'banana' de la lista
thislist.remove("banana")
print("Lista después de quitar 'banana':", thislist)

# Quitando una de las dos 'bananas' de la lista
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print("Lista después de quitar una 'banana':", thislist)

# Borrando el segundo miembro
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print("Lista después de borrar el segundo miembro:", thislist)

# Borrando el último miembro
thislist.pop()
print("Lista después de borrar el último miembro:", thislist)

# Borrando el primer miembro
del thislist[0]
print("Lista después de borrar el primer miembro:", thislist)

# Agregando en la segunda posición un miembro
thislist = ["banana", "cherry"]
thislist.insert(1, "orange")
print("Lista después de insertar 'orange' en la segunda posición:", thislist)

# Agregando elementos tropicales a la lista
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print("Lista después de extender con elementos tropicales:", thislist)

# Agregando tuplas a la lista
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print("Lista después de agregar elementos de la tupla:", thislist)

# Ejemplo adicional: Copiar una lista
copied_list = thislist.copy()
print("Copia de la lista original:", copied_list)

# Ordenando la lista
thislist.sort()
print("Lista después de ordenarla:", thislist)

# Invirtiendo la lista
thislist.reverse()
print("Lista después de invertirla:", thislist)

# Contar la cantidad de veces que aparece un elemento
count_banana = thislist.count("banana")
print("Cantidad de veces que 'banana' aparece en la lista:", count_banana)

# Limpiando la lista
thislist.clear()
print("Lista después de limpiarla:", thislist)

