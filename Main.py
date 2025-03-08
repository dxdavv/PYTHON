# Primer intento de aprender python

# Para imprimir muy facil
print ("Grande ang")

# Aqui vamos a crear una lista
Planetas = ["mercurio", "venus", "tierra", "marte" ]

# Ahora vamos a imprimir la lista
print (Planetas)

# Aqui probamos varios cosas sobre las listas
# 1. lista[i]: Devuelve el elemento que está en la posición i de la lista.
print (Planetas[2])

# 2. lista.pop(i): Devuelve el elemento en la posición i de una lista y luego lo borra.
Planetas.pop(1)
print (Planetas)

# 3. lista.append(elemento): Añade elemento al final de la lista.
Planetas.append("Jupiter")
print (Planetas)
Planetas.append("Urano")
print (Planetas)

# 4. lista.insert(i, elemento): Inserta elemento en la posición i.
Planetas.insert(4, "Saturno")
print (Planetas)

# 5. lista.extend(lista2): Fusiona lista con lista2.
planetas2 = ["Neptuno", "Pluton"]
Planetas.extend(planetas2)
print (Planetas)

# 6. lista.remove(elemento): Elimina la primera vez que aparece elemento.
planetas2.append("Pluton")
print (planetas2)

planetas2.remove("Pluton")
print (planetas2)

# Diccionario en python
Diccionario = {'Planeta 1' : 'Mercurio', 'Planeta 2' : 'Venus'}
print (Diccionario)