def mostrar_menu():
    print("\nAgenda Telefónica")
    print("1. Agregar una persona")
    print("2. Modificar una persona")
    print("3. Eliminar una persona")
    print("4. Mostrar toda la agenda")
    print("5. Salir")

def agregar_persona(agenda):
    dni = input("Ingrese el DNI: ")
    if dni in agenda:
        print("Esta persona ya existe en la agenda.")
    else:
        apellido = input("Ingrese el apellido: ")
        nombre = input("Ingrese el nombre: ")
        email = input("Ingrese el email: ")
        telefono = input("Ingrese el número de teléfono: ")
        agenda[dni] = {
            'apellido': apellido,
            'nombre': nombre,
            'email': email,
            'telefono': telefono
        }
        print("Persona agregada exitosamente.")

def modificar_persona(agenda):
    dni = input("Ingrese el DNI de la persona que desea modificar: ")
    if dni in agenda:
        print("Deje en blanco si no desea modificar el campo.")
        apellido = input(f"Apellido actual ({agenda[dni]['apellido']}): ") or agenda[dni]['apellido']
        nombre = input(f"Nombre actual ({agenda[dni]['nombre']}): ") or agenda[dni]['nombre']
        email = input(f"Email actual ({agenda[dni]['email']}): ") or agenda[dni]['email']
        telefono = input(f"Teléfono actual ({agenda[dni]['telefono']}): ") or agenda[dni]['telefono']
        agenda[dni] = {
            'apellido': apellido,
            'nombre': nombre,
            'email': email,
            'telefono': telefono
        }
        print("Persona modificada exitosamente.")
    else:
        print("Persona no encontrada.")

def eliminar_persona(agenda):
    dni = input("Ingrese el DNI de la persona que desea eliminar: ")
    if dni in agenda:
        del agenda[dni]
        print("Persona eliminada exitosamente.")
    else:
        print("Persona no encontrada.")

def mostrar_agenda(agenda):
    if agenda:
        print("\nAgenda Telefónica:")
        for dni, datos in agenda.items():
            print(f"DNI: {dni}")
            print(f"Apellido: {datos['apellido']}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Email: {datos['email']}")
            print(f"Teléfono: {datos['telefono']}")
            print("-" * 20)
    else:
        print("La agenda está vacía.")

def main():
    agenda = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_persona(agenda)
        elif opcion == '2':
            modificar_persona(agenda)
        elif opcion == '3':
            eliminar_persona(agenda)
        elif opcion == '4':
            mostrar_agenda(agenda)
        elif opcion == '5':
            print("Saliendo de la agenda. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()
