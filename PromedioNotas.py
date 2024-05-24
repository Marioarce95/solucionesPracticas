def calcular_promedio(notas):
  """
  Calcula el promedio de una lista de notas.

  Args:
    notas: La lista de notas a promediar.

  Returns:
    El promedio de las notas.
  """
  if not notas:
    return None

  promedio = sum(notas) / len(notas)
  return promedio

# Ingreso de las notas
notas = []
for i in range(5):
  nota = float(input(f"Ingrese la nota de la materia {i + 1}: "))
  notas.append(nota)

# Cálculo del promedio
promedio = calcular_promedio(notas)

# Impresión del resultado
if promedio is None:
  print("No se ingresaron notas.")
else:
  print(f"El promedio de las notas es: {promedio:.2f}")
