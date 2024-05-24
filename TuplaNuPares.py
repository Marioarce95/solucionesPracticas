# Ingresar el valor de n
n = int(input("Ingrese el valor de n: "))

# Crear una tupla con los primeros n números pares
pares = tuple(range(2, n * 2 + 1, 2))

# Mostrar la tupla de números pares
print("\nTupla de números pares:")
for numero in pares:
  print(numero)