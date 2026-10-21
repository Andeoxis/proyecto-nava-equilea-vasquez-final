from funciones import ver_informacion
from funciones import consultar_datos
from funciones import realizar_operacion
from funciones import cerrar_sesion


def menu_usuario():

    while True:
        try:

            print("\n--- MENU USUARIO ---")
            print("1. Ver información")
            print("2. Consultar datos")
            print("3. Realizar una operación")
            print("4. Cerrar sesión")

            opcion = input("Seleccione una opción: ")

            match opcion:
                case 1:
                    ver_informacion()
                case 2:
                    consultar_datos()
                case 3:
                    realizar_operacion()
                case 4:
                    cerrar_sesion()
                case _:
                    raise ValueError
                
        except ValueError:
            print('Dato erroneo, intente nuevamente')
