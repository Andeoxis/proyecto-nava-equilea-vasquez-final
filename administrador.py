from funciones import (
    gestionar_personal,
    gestionar_menu,
    gestionar_pedidos,
    gestionar_costos,
    comprar_comida,
    ver_carrito_y_confirmar,
    cerrar_sesion
)

def menu_administrador():
    while True:
        print("\n--- MENU ADMINISTRADOR ---")
        print("1. Gestionar Personal")
        print("2. Gestionar Menu")
        print("3. Gestionar Pedidos")
        print("4. Gestionar Costo de los Platos")
        print("5. Menú de Usuario")
        print("6. Cerrar sesion")

        opcion = input('Seleccione una opcion: ')

        if opcion == '1':
            gestionar_personal()
        elif opcion == '2':
            gestionar_menu()
        elif opcion == '3':
            gestionar_pedidos()
        elif opcion == '4':
            gestionar_costos()
        elif opcion == '5':
            menu_usuario_desde_admin()
        elif opcion == '6':
            cerrar_sesion()
            break
        else:
            print('Opcion invalida, intente nuevamente.')


def menu_usuario_desde_admin():
    while True:
        print("\n--- MENÚ DE COMPRA (ADMIN) ---")
        print("1. Comprar comida")
        print("2. Ver carrito y confirmar pedido")
        print("3. Volver al menu de Admin")

        opc = input("Seleccione una opcion: ")

        if opc == '1':
            comprar_comida()
        elif opc == '2':
            ver_carrito_y_confirmar()
        elif opc == '3':
            break
        else:
            print("Opcion no valida.")
