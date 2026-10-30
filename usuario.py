from funciones import comprar_comida, ver_carrito_y_confirmar, cerrar_sesion

def menu_usuario():
    while True:
        print("\n--- MENU DE USUARIO ---")
        print("1. Comprar comida")
        print("2. Ver carrito y confirmar pedido")
        print("3. Cerrar sesion")

        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            comprar_comida()
        elif opcion == '2':
            ver_carrito_y_confirmar()
        elif opcion == '3':
            cerrar_sesion()
            break
        else:
            print('Opción invalida, intente nuevamente.')