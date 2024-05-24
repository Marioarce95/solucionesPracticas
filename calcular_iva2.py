def calcular_precio_final(precio_producto, porcentaje_iva):
    precio_final = precio_producto * (1 + porcentaje_iva / 100)
    return precio_final

def main():
    precio_str = input("Ingrese el precio del producto: $")
    precio_str = precio_str.replace(',', '.')
    precio_producto = float(precio_str)
    
    # Solicitar al usuario el porcentaje del IVA
    porcentaje_iva = float(input("Ingrese el porcentaje del IVA: "))
    
    # Llamar a la función para calcular el precio final
    precio_final = calcular_precio_final(precio_producto, porcentaje_iva)
    
    print("El precio final del producto es: ${:.2f}".format(precio_final))

main()
