def calcular_total_a_pagar(cantidad_litros, es_jubilado):
  """
  Calcula el total a pagar por la leche considerando descuentos y promoción.

  Args:
    cantidad_litros: La cantidad de litros de leche comprados.
    es_jubilado: Indica si el cliente es jubilado (True) o no (False).

  Returns:
    El total a pagar por el cliente.
  """
  if cantidad_litros <= 0:
    raise ValueError("La cantidad de litros debe ser un número positivo.")

  precio_unitario = 1000

  # Cálculo del descuento por cantidad
  descuento_cantidad = 0
  if cantidad_litros > 12 and cantidad_litros <= 24:
    descuento_cantidad = 0.1
  elif cantidad_litros > 24:
    descuento_cantidad = 0.15

  # Cálculo del descuento por jubilado
  descuento_jubilado = 0
  if es_jubilado:
    descuento_jubilado = 0.1

  # Cálculo del precio antes de descuentos
  precio_antes_descuentos = cantidad_litros * precio_unitario

  # Aplicación de descuentos
  precio_con_descuento_cantidad = precio_antes_descuentos * (1 - descuento_cantidad)
  precio_con_descuentos = precio_con_descuento_cantidad * (1 - descuento_jubilado)

  # Cálculo del total a pagar
  total_a_pagar = precio_con_descuentos

  return total_a_pagar

# Ingreso de los datos
cantidad_litros = int(input("Ingrese la cantidad de litros de leche: "))
es_jubilado = input("¿El cliente es jubilado? (Sí/No): ").lower() == "sí"

# Cálculo del total a pagar
try:
  total_a_pagar = calcular_total_a_pagar(cantidad_litros, es_jubilado)
except ValueError as e:
  print(f"Error: {e}")
else:
  print(f"El total a pagar es de ${total_a_pagar:.2f}")
