usuarios = ["admin", "usuario"]
contraseñas = ["1234", "1234"]


def login():
    usuario = input("Ingrese su usuario: ").strip().lower()
    contraseña = input("Ingrese la contraseña de cuatro dígitos: ").strip()

    for i in range(len(usuarios)):
        if usuario == usuarios[i] and contraseña == contraseñas[i]:

            if usuario == "admin":
                print("--- Acceso concedido ---\n")
                print("Bienvenido administrador")
                return "administrador"

            else:
                print("--- Acceso concedido ---")
                print("Bienvenido como usuario")
                return "usuario"

    print("Contraseña o usuario incorrecto")
    return "incorrecto"


def registrar_usuario():
    nuevo_usuario = input("\nIngrese el usuario: ").strip().lower()

    if nuevo_usuario in usuarios:
        print("El usuario ya existe")
        return

    nueva_contraseña = input(
        "Ingrese la contraseña de cuatro dígitos: "
    ).strip()

    if len(nueva_contraseña) != 4 or not nueva_contraseña.isdigit():
        print("La contraseña debe tener cuatro dígitos")
        return

    usuarios.append(nuevo_usuario)
    contraseñas.append(nueva_contraseña)

    print("Nuevo usuario registrado exitosamente...")


def mostrar_usuarios():
    print("\n--- USUARIOS REGISTRADOS ---")

    for i in range(len(usuarios)):
        print("Usuario:", usuarios[i])
        print("Contraseña:", contraseñas[i])


def buscar_usuario():
    buscar_u = input("\nIngrese el nombre de usuario: ").strip().lower()

    if buscar_u in usuarios:
        posicion = usuarios.index(buscar_u)

        print("Usuario encontrado")
        print("Usuario:", usuarios[posicion])
        print("Contraseña:", contraseñas[posicion])

    else:
        print("Usuario no encontrado...")
def modificar_usuario():
    buscar_u = input("\nIngrese el usuario que desea modificar: ").strip().lower()

    if buscar_u in usuarios:
        posicion = usuarios.index(buscar_u)

        nuevo_usuario = input("Ingrese el nuevo usuario: ").strip().lower()
        nueva_contraseña = input(
            "Ingrese la nueva contraseña de cuatro dígitos: "
        ).strip()

        usuarios[posicion] = nuevo_usuario
        contraseñas[posicion] = nueva_contraseña

        print("Usuario modificado correctamente...")

    else:
        print("Usuario no encontrado...")


def eliminar_usuario():
    buscar_u = input("\nIngrese el usuario que desea eliminar: ").strip().lower()

    if buscar_u in usuarios:
        posicion = usuarios.index(buscar_u)

        usuarios.pop(posicion)
        contraseñas.pop(posicion)

        print("Usuario eliminado correctamente...")

    else:
        print("Usuario no encontrado...")


def cerrar_sesion():
    print("\nSesión cerrada")
    exit()


def ver_informacion():
    print("\n--- INFORMACIÓN DEL USUARIO ---")
    print("Usted ha iniciado sesión como usuario.")
def consultar_datos():
    print("\n--- CONSULTAR DATOS ---")
    print("Consulta realizada correctamente...")


def realizar_operacion():
    print("\n--- REALIZAR OPERACIÓN ---")
    print("Operación realizada correctamente...")