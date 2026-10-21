from funciones import registrar_usuario, mostrar_usuarios, buscar_usuario, modificar_usuario, eliminar_usuario, cerrar_sesion

def menu_administrador():
    while True:
        try:

            print("\n--- MENU ADMINISTRADOR ---")
            print("1. Registrar usuario")
            print("2. Mostrar usuarios")
            print("3. Buscar usuario")
            print("4. Modificar usuario")
            print("5. Eliminar usuario")
            print("6. Cerrar sesión")

            opcion = int(input('Seleccione una opcion: '))

            match opcion:
                case 1:
                    registrar_usuario()
                case 2:
                    mostrar_usuarios()
                case 3:
                    buscar_usuario()
                case 4:
                    modificar_usuario()
                case 5:
                    eliminar_usuario()
                case 6:
                    cerrar_sesion()
                case _:
                    raise ValueError
        except ValueError:
            print('Dato erroneo, intente nuevamente')
            print()
