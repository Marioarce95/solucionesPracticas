import random

def generar_lista_aleatoria(cantidad):
  """
  Genera una lista de números aleatorios sin repeticiones y ordenados.

  Args:
    cantidad: La cantidad de números a generar.

  Returns:
    Una lista de números aleatorios sin repeticiones y ordenados.
  """
  if cantidad <= 0:
    raise ValueError("La cantidad debe ser un número positivo.")

  numeros_aleatorios = []
  while len(numeros_aleatorios) < cantidad:
    numero_aleatorio = random.randint(0, 9)
    if numero_aleatorio not in numeros_aleatorios:
      numeros_aleatorios.append(numero_aleatorio)

  numeros_aleatorios.sort()
  return numeros_aleatorios

# Generar la lista de 5 números aleatorios
cantidad = 5
lista_aleatoria = generar_lista_aleatoria(cantidad)

# Imprimir la lista
print(lista_aleatoria)
