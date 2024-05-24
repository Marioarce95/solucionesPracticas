def calcular_puntos_acumulados(partidos_ganados, partidos_empatados, partidos_perdidos):
  """
  Calcula la cantidad de puntos acumulados por un equipo de fútbol.

  Args:
    partidos_ganados: La cantidad de partidos ganados.
    partidos_empatados: La cantidad de partidos empatados.
    partidos_perdidos: La cantidad de partidos perdidos.

  Returns:
    La cantidad total de puntos acumulados.
  """
  if partidos_ganados < 0 or partidos_empatados < 0 or partidos_perdidos < 0:
    raise ValueError("Los valores deben ser números no negativos.")

  puntos_ganados = partidos_ganados * 3
  puntos_empatados = partidos_empatados * 1
  puntos_perdidos = partidos_perdidos * 0

  puntos_totales = puntos_ganados + puntos_empatados + puntos_perdidos
  return puntos_totales

# Ingreso de los datos
partidos_ganados = int(input("Ingrese la cantidad de partidos ganados: "))
partidos_empatados = int(input("Ingrese la cantidad de partidos empatados: "))
partidos_perdidos = int(input("Ingrese la cantidad de partidos perdidos: "))

# Cálculo de los puntos acumulados
try:
  puntos_acumulados = calcular_puntos_acumulados(partidos_ganados, partidos_empatados, partidos_perdidos)
except ValueError as e:
  print(f"Error: {e}")
else:
  print(f"El equipo ha acumulado {puntos_acumulados} puntos.")
