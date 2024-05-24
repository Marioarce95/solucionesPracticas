def convertir_pesos_a_dolares(pesos):
  """
  Convierte una cantidad de pesos argentinos a dólares estadounidenses.

  Args:
    pesos: La cantidad de pesos argentinos a convertir.

  Returns:
    La cantidad equivalente en dólares estadounidenses.
  """
  tipo_de_cambio = 0.0011  # Tasa de cambio actual (1 ARS = 0.0011 USD)
  dolares = pesos * tipo_de_cambio
  return dolares

# Ingreso del monto en pesos argentinos
pesos_argentinos = float(input("Ingrese la cantidad de pesos argentinos: "))

# Conversión a dólares estadounidenses
dolares_estadounidenses = convertir_pesos_a_dolares(pesos_argentinos)

# Impresión del resultado
print(f"{pesos_argentinos} pesos argentinos equivalen a {dolares_estadounidenses:.2f} dólares estadounidenses.")
