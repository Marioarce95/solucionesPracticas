Proceso Principal
    Definir pesos_argentinos, dolares_estadounidenses Como Real
	
    // Ingreso del monto en pesos argentinos
    Escribir "Ingrese la cantidad de pesos argentinos: "
    Leer pesos_argentinos
	
    // Conversión a dólares estadounidenses
    convertir_pesos_a_dolares(pesos_argentinos, dolares_estadounidenses)
	
    // Impresión del resultado
    Escribir pesos_argentinos, " pesos argentinos equivalen a ", dolares_estadounidenses, " dólares estadounidenses."
FinProceso

 Funcion convertir_pesos_a_dolares (pesos, dolares)
    Definir tipo_de_cambio Como Real
	
    // Tasa de cambio actual (1 ARS = 0.0011 USD)
    tipo_de_cambio <- 0.0011
	
    // Cálculo de la cantidad en dólares
    dolares <- pesos * tipo_de_cambio
FinSubProceso
