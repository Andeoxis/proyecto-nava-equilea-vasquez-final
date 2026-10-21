from funciones import registrar_usuario
from funciones import mostrar_usuarios
from funciones import buscar_usuario
from funciones import modificar_usuario
from funciones import eliminar_usuario
from funciones import cerrar_sesion


def menu_administrador():

    while True:

        print("\n--- MENU ADMINISTRADOR ---")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Buscar usuario")
        print("4. Modificar usuario")
        print("5. Eliminar usuario")
        print("6. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()

        elif opcion == "2":
            mostrar_usuarios()

        elif opcion == "3":
            buscar_usuario()

        elif opcion == "4":
            modificar_usuario()

        elif opcion == "5":
            eliminar_usuario()

        elif opcion == "6":
            cerrar_sesion()
            break

        else:
            print("ERROR... Opción inválida...")
