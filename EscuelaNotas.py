def calcular_promedio_y_rendimiento(notas):
  """
  Calcula el promedio de notas y determina el rendimiento del curso.

  Args:
    notas: La lista de notas de los alumnos.

  Returns:
    El promedio de notas y el rendimiento del curso ("elevado", "aceptable" o "bajo").
  """
  if not notas:
    return None, None

  promedio = sum(notas) / len(notas)

  if promedio > 8:
    rendimiento = "elevado"
  elif promedio >= 6:
    rendimiento = "aceptable"
  else:
    rendimiento = "bajo"

  return promedio, rendimiento

# Ingreso de las notas
notas = []
cantidad_alumnos = int(input("Ingrese la cantidad de alumnos que rindieron el examen: "))
for i in range(cantidad_alumnos):
  nota = float(input(f"Ingrese la nota del alumno {i + 1}: "))
  notas.append(nota)

# Cálculo del promedio y rendimiento
promedio, rendimiento = calcular_promedio_y_rendimiento(notas)

# Impresión del resultado
if promedio is None or rendimiento is None:
  print("Error: No se ingresaron notas.")
else:
  print(f"El promedio de notas es: {promedio:.2f}")
  print(f"El rendimiento del curso es: {rendimiento}")
