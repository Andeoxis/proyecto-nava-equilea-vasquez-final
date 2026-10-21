from funciones import ver_informacion
from funciones import consultar_datos
from funciones import realizar_operacion
from funciones import cerrar_sesion


def menu_usuario():

    while True:

        print("\n--- MENU USUARIO ---")
        print("1. Ver información")
        print("2. Consultar datos")
        print("3. Realizar una operación")
        print("4. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_informacion()

        elif opcion == "2":
            consultar_datos()

        elif opcion == "3":
            realizar_operacion()

        elif opcion == "4":
            cerrar_sesion()
            break

        else:
            print("ERROR... Opción inválida...")
