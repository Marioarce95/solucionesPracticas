Proceso calcular_promedio_y_rendimiento
    Definir cantidad_alumnos, nota, suma_notas, promedio Como Real
    Definir rendimiento Como Caracter
	
    // Ingreso de las notas y cálculo del promedio
    suma_notas <- 0
    Escribir "Ingrese la cantidad de alumnos que rindieron el examen: "
    Leer cantidad_alumnos
    Para i <- 1 Hasta cantidad_alumnos Hacer
        Escribir "Ingrese la nota del alumno ", i, ": "
        Leer nota
        suma_notas <- suma_notas + nota
    FinPara
    promedio <- suma_notas / cantidad_alumnos
	
    // Determinación del rendimiento del curso
	Si promedio > 8 Entonces
		rendimiento <- "elevado"
	Sino Si promedio >= 6 Entonces
			rendimiento <- "aceptable"
		Sino
			rendimiento <- "bajo"
		FinSi
	FinSi
		
		// Impresión del resultado
		Escribir "El promedio de notas es: ", promedio
		Escribir "El rendimiento del curso es: ", rendimiento
FinProceso
