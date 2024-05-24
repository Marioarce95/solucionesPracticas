def calcular_costo_mano_obra(ancho, alto, precio_por_m2):
  """
  Calcula el costo de mano de obra para pintar una pared rectangular.

  Args:
    ancho: El ancho de la pared en metros.
    alto: El alto de la pared en metros.
    precio_por_m2: El precio por metro cuadrado de mano de obra.

  Returns:
    El costo total de mano de obra.
  """
  if ancho <= 0 or alto <= 0 or precio_por_m2 <= 0:
    raise ValueError("Los valores deben ser números positivos.")

  superficie = ancho * alto
  costo_total = superficie * precio_por_m2
  return costo_total

# Ingreso de los datos
ancho = float(input("Ingrese el ancho de la pared en metros: "))
alto = float(input("Ingrese el alto de la pared en metros: "))
precio_por_m2 = float(input("Ingrese el precio por metro cuadrado de mano de obra: "))

# Cálculo del costo de mano de obra
try:
  costo_mano_obra = calcular_costo_mano_obra(ancho, alto, precio_por_m2)
except ValueError as e:
  print(f"Error: {e}")
else:
  print(f"El costo total de mano de obra es de ${costo_mano_obra:.2f}")
