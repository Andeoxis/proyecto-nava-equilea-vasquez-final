from funciones import login
from administrador import menu_administrador
from usuario import menu_usuario

def main():

    print("--- BIENVENIDO/A AL SISTEMA ---")

    tipo_usuario = login()

    if tipo_usuario == "administrador":
        menu_administrador()

    elif tipo_usuario == "usuario":
        menu_usuario()

    else:
        print("Error... Acceso denegado...")


main()
