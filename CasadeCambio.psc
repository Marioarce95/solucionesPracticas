Proceso Principal
    Definir pesos_argentinos, dolares_estadounidenses Como Real
	
    // Ingreso del monto en pesos argentinos
    Escribir "Ingrese la cantidad de pesos argentinos: "
    Leer pesos_argentinos
	
    // Conversi�n a d�lares estadounidenses
    dolares_estadounidenses <- pesos_argentinos * 0.0011
	
    // Impresi�n del resultado
    Escribir pesos_argentinos, " pesos argentinos equivalen a ", dolares_estadounidenses, " d�lares estadounidenses."
FinProceso
