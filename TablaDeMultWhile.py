def generar_tabla_multiplicar(numero):
  """
  Genera la tabla de multiplicar de un número entero.

  Args:
    numero: El número entero para el que se genera la tabla.

  Returns:
    None
  """
  if not isinstance(numero, int) or numero < 1 or numero > 10:
    raise ValueError("El número debe ser un entero entre 1 y 10.")

  multiplicador = 1
  while multiplicador <= 10:
    producto = numero * multiplicador
    print(f"{numero}x{multiplicador}={producto}")
    multiplicador += 1

# Ingreso del número
try:
  numero = int(input("Ingrese un número entero entre 1 y 10: "))
except ValueError as e:
  print(f"Error: {e}")
else:
  generar_tabla_multiplicar(numero)
