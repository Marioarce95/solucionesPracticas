def main():
    precio_str = input("Ingrese el precio del producto: $")
    # Reemplazamos la coma por un punto para asegurarnos de que sea un número válido
    precio_str = precio_str.replace(',', '.')
    precio_producto = float(precio_str)
    precio_final = precio_producto * 1.21  # Se aplica directamente el 21% de IVA
    print("El precio final del producto es: ${:.2f}".format(precio_final))
    
# {:.2f} es una cadena de formato especial que le dice a Python cómo formatear un número de punto flotante.
# El : indica que se va a especificar un formato.
# .2 indica que queremos que el número tenga dos decimales después del punto decimal.
# f indica que el número es un número de punto flotante.
# Cuando llamamos .format(precio_final), el valor de precio_final se formatea según las especificaciones de 
# la cadena de formato {:.2f} y se inserta en ese lugar dentro de la cadena.

# Llamamos a la función main() directamente
main()

"""
Inicio
Función principal main():
    Solicitar al usuario que ingrese el precio del producto
    Leer el precio ingresado como una cadena de texto
    Reemplazar cualquier coma en la cadena por un punto
    Convertir la cadena modificada a un número de punto flotante
    Calcular el precio final multiplicando el precio del producto por 1.21
    Mostrar el precio final del producto con dos decimales
Fin de la función principal

Llamar a la función principal main()
Fin

"""