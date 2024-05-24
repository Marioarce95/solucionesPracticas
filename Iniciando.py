nombres = []

# Ingresar 10 nombres
while len(nombres) < 10:
  nombre = input("Ingrese un nombre: ")
  if nombre not in nombres:
    nombres.append(nombre)
  else:
    print(f"El nombre '{nombre}' ya está en la lista.")

# Mostrar la lista de nombres
print("\nNombres ingresados:")
for nombre in nombres:
  print(nombre)


# Eliminar la tercera persona
del nombres[2]

# Eliminar la última persona
nombres.pop()

# Ordenar la lista
nombres.sort()

# Mostrar la lista ordenada
print("\nNombres después de eliminar y ordenar:")
for nombre in nombres:
  print(nombre)

persona = {
  "nombre": "Mario",
  "apellido": "Arce",
  "dni": 32456789,
  "email": "marioarce952@example.com",
  "fecha_nacimiento": "1995-10-6"
}

# Imprimir los datos de la persona
print("\nDatos de la persona:")
for clave, valor in persona.items():
  print(f"{clave}: {valor}")


