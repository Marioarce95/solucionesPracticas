Proceso CalcularPuntosAcumulados
    Definir partidos_ganados, partidos_empatados, partidos_perdidos Como Entero
    Definir puntos_ganados, puntos_empatados, puntos_perdidos, puntos_totales Como Entero
	
    // Ingreso de los datos
    Escribir "Ingrese la cantidad de partidos ganados: "
    Leer partidos_ganados
    Escribir "Ingrese la cantidad de partidos empatados: "
    Leer partidos_empatados
    Escribir "Ingrese la cantidad de partidos perdidos: "
    Leer partidos_perdidos
	
    // Cálculo de los puntos acumulados
    Si partidos_ganados < 0 O partidos_empatados < 0 O partidos_perdidos < 0 Entonces
        Escribir "Error: Los valores deben ser números no negativos."
    Sino
        puntos_ganados <- partidos_ganados * 3
        puntos_empatados <- partidos_empatados * 1
        puntos_perdidos <- partidos_perdidos * 0
		
        puntos_totales <- puntos_ganados + puntos_empatados + puntos_perdidos
        Escribir "El equipo ha acumulado ", puntos_totales, " puntos."
    FinSi
FinProceso
