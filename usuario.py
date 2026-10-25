from funciones import platos, platos_especiales, cerrar_sesion, ver_pedido

def menu_usuario():

    while True:
        try:

            print("\n--- MENU DE USUARIO ---")
            print("1. Platos")
            print("2. Platos especiales")
            print("3. Ver carrito y confirmar pedido")
            print("4. Cerrar sesión")

            opcion = int(input("Seleccione una opción: "))

            match opcion:
                case 1:
                    platos()
                case 2:
                    platos_especiales()
                case 3:
                    ver_pedido()
                case 4:
                    cerrar_sesion()
                    break
                case _:
                    raise ValueError
                
        except ValueError:
            print('Dato erroneo, intente nuevamente')
