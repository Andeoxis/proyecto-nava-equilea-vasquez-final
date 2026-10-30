# --- LISTAS DE USUARIOS Y ADMINS ---
admins = ['admin']
contraseñas_admin = ['1234']

usuarios = ['usuario']
contraseñas_usuario = ['1234']

# --- LISTAS DEL MENÚ DE PLATOS Y PRECIOS ---
platos_menu = ['Fricase', 'Charque', 'Pique Macho', 'Churrasco', 'Silpancho','lawa de luspichi', 'Falsoconejo', 'Sopa de chairo', 'Planchita', 'Caldo de kawi']
precios_menu = [30, 50, 80, 60, 75, 50, 45, 56, 85, 100]

# --- LISTAS DEL CARRITO DEL USUARIO ---
carrito_nombres = []
carrito_precios = []
carrito_cantidades = []

# --- HISTORIAL DE PEDIDOS REGISTRADOS ---
historial_pedidos = []


def login():
    usuario = input('Ingrese su usuario: ').strip().lower()
    contraseña = input('Ingrese su contraseña: ').strip()

    # Verificar Administrador
    for i in range(len(admins)):
        if usuario == admins[i] and contraseña == contraseñas_admin[i]:
            print('\n--- ACCESO CONCEDIDO ---')
            print('Bienvenido Administrador')
            return 'administrador'

    # Verificar Usuario
    for i in range(len(usuarios)):
        if usuario == usuarios[i] and contraseña == contraseñas_usuario[i]:
            print('\n--- ACCESO CONCEDIDO ---')
            print('Bienvenido Usuario:', usuario)
            return 'usuario'

    print('Contraseña o usuario incorrecto')
    return 'incorrecto'


# ==============================================================================
# 1. GESTIONAR PERSONAL
# ==============================================================================

def gestionar_personal():
    while True:
        print("\n--- GESTIONAR PERSONAL ---")
        print("1. Gestionar Administradores")
        print("2. Gestionar Usuarios")
        print("3. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            menu_crud_personal("Administrador", admins, contraseñas_admin)
        elif opcion == '2':
            menu_crud_personal("Usuario", usuarios, contraseñas_usuario)
        elif opcion == '3':
            break
        else:
            print("Opcion incorrecta, intente de nuevo.")


def menu_crud_personal(tipo, lista_nombres, lista_passwords):
    while True:
        print("\n--- GESTIONAR", tipo.upper(), "---")
        print("1. Registrar")
        print("2. Mostrar")
        print("3. Buscar")
        print("4. Modificar")
        print("5. Eliminar")
        print("6. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            nuevo = input('Ingrese el usuario: ').strip().lower()
            if nuevo in lista_nombres:
                print('El usuario ya existe.')
            else:
                passw = input('Ingrese la contraseña de 4 digitos: ').strip()
                if len(passw) == 4 and passw.isdigit():
                    lista_nombres.append(nuevo)
                    lista_passwords.append(passw)
                    print('Registrado exitosamente.')
                else:
                    print('La contraseña debe tener 4 digitos.')

        elif opcion == '2':
            print('\n--- LISTA REGISTRADA ---')
            for i in range(len(lista_nombres)):
                print('Usuario:', lista_nombres[i], '| Contraseña:', lista_passwords[i])

        elif opcion == '3':
            buscar = input('Ingrese el usuario a buscar: ').strip().lower()
            if buscar in lista_nombres:
                pos = lista_nombres.index(buscar)
                print('Encontrado -> Usuario:', lista_nombres[pos], '| Contraseña:', lista_passwords[pos])
            else:
                print('Usuario no encontrado.')

        elif opcion == '4':
            mod = input('Ingrese el usuario a modificar: ').strip().lower()
            if mod in lista_nombres:
                pos = lista_nombres.index(mod)
                nuevo_nom = input('Ingrese el nuevo usuario: ').strip().lower()
                nueva_pas = input('Ingrese la nueva contraseña de 4 dígitos: ').strip()
                if len(nueva_pas) == 4 and nueva_pas.isdigit():
                    lista_nombres[pos] = nuevo_nom
                    lista_passwords[pos] = nueva_pas
                    print('Modificado con éxito.')
                else:
                    print('La contraseña debe ser de 4 dígitos.')
            else:
                print('Usuario no encontrado.')

        elif opcion == '5':
            elim = input('Ingrese el usuario a eliminar: ').strip().lower()
            if elim in lista_nombres:
                pos = lista_nombres.index(elim)
                lista_nombres.pop(pos)
                lista_passwords.pop(pos)
                print('Eliminado correctamente.')
            else:
                print('Usuario no encontrado.')

        elif opcion == '6':
            break
        else:
            print("Opción no valida.")


# ==============================================================================
# 2. GESTIONAR MENÚ DE PLATOS
# ==============================================================================

def gestionar_menu():
    while True:
        print("\n--- GESTIONAR MENU DE PLATOS ---")
        print("1. Registrar plato")
        print("2. Mostrar platos")
        print("3. Buscar plato")
        print("4. Modificar plato")
        print("5. Eliminar plato")
        print("6. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            nuevo_p = input('Ingrese el plato: ').strip().capitalize()
            if nuevo_p in platos_menu:
                print('Ese plato ya existe.')
            else:
                try:
                    precio = int(input('Ingrese el precio en Bs: '))
                    platos_menu.append(nuevo_p)
                    precios_menu.append(precio)
                    print('Plato guardado exitosamente.')
                except ValueError:
                    print('Dato de precio invalido.')

        elif opcion == '2':
            mostrar_carta_platos()

        elif opcion == '3':
            buscar = input('Ingrese el plato a buscar: ').strip().capitalize()
            if buscar in platos_menu:
                pos = platos_menu.index(buscar)
                print('Plato:', platos_menu[pos], '| Precio:', precios_menu[pos], 'Bs')
            else:
                print('Plato no encontrado.')

        elif opcion == '4':
            mod = input('Ingrese el plato a modificar: ').strip().capitalize()
            if mod in platos_menu:
                pos = platos_menu.index(mod)
                nuevo_n = input('Ingrese el nuevo nombre: ').strip().capitalize()
                try:
                    nuevo_pr = int(input('Ingrese el nuevo precio: '))
                    platos_menu[pos] = nuevo_n
                    precios_menu[pos] = nuevo_pr
                    print('Plato actualizado.')
                except ValueError:
                    print('Precio no valido.')
            else:
                print('Plato no encontrado.')

        elif opcion == '5':
            elim = input('Ingrese el plato a eliminar: ').strip().capitalize()
            if elim in platos_menu:
                pos = platos_menu.index(elim)
                platos_menu.pop(pos)
                precios_menu.pop(pos)
                print('Plato eliminado.')
            else:
                print('Plato no encontrado.')

        elif opcion == '6':
            break
        else:
            print("Opción invalida.")


# ==============================================================================
# 3. GESTIONAR PEDIDOS
# ==============================================================================

def gestionar_pedidos():
    print("\n--- HISTORIAL DE PEDIDOS REALIZADOS ---")
    if len(historial_pedidos) == 0:
        print("No hay pedidos realizados todavía.")
    else:
        for i in range(len(historial_pedidos)):
            print(i + 1, ".", historial_pedidos[i])


# ==============================================================================
# 4. GESTIONAR COSTOS DE PLATOS
# ==============================================================================

def gestionar_costos():
    print("\n--- GESTIONAR COSTO DE PLATOS ---")
    mostrar_carta_platos()
    mod = input('\nIngrese el nombre del plato a cambiar costo: ').strip().capitalize()

    if mod in platos_menu:
        pos = platos_menu.index(mod)
        try:
            nuevo_precio = int(input('Ingrese el nuevo precio: '))
            precios_menu[pos] = nuevo_precio
            print('Precio actualizado correctamente.')
        except ValueError:
            print('Dato no valido.')
    else:
        print('Plato no encontrado.')


# 5. MENÚ DE USUARIO / COMPRAR COMIDA

def mostrar_carta_platos():
    print("\n--- PLATOS DISPONIBLES ---")
    for i in range(len(platos_menu)):
        print(i + 1, ".", platos_menu[i], "-", precios_menu[i], "Bs")


def comprar_comida():
    while True:
        mostrar_carta_platos()
        print(len(platos_menu) + 1, ". Volver")

        opc = input("\nSeleccione el numero del plato a pedir: ")

        if opc.isdigit():
            num = int(opc)
            if 1 <= num <= len(platos_menu):
                pos = num - 1
                plato = platos_menu[pos]
                precio = precios_menu[pos]

                try:
                    cant = int(input('¿Cuántos desea pedir?: '))
                    if cant > 0:
                        if plato in carrito_nombres:
                            idx = carrito_nombres.index(plato)
                            carrito_cantidades[idx] += cant
                        else:
                            carrito_nombres.append(plato)
                            carrito_precios.append(precio)
                            carrito_cantidades.append(cant)
                        print('Plato agregado al carrito.')
                    else:
                        print('Debe ingresar un numero positivo.')
                except ValueError:
                    print('Cantidad inválida.')
            elif num == len(platos_menu) + 1:
                break
            else:
                print('Numero fuera de rango.')
        else:
            print('Debe ingresar un numero.')


def ver_carrito_y_confirmar():
    if len(carrito_nombres) == 0:
        print('\nSu carrito esta vacío.')
        return

    print('\n--- CARRITO DE COMPRAS ---')
    total = 0
    resumen = ""

    for i in range(len(carrito_nombres)):
        subtotal = carrito_cantidades[i] * carrito_precios[i]
        total += subtotal
        item = carrito_nombres[i] + " x" + str(carrito_cantidades[i]) + " (" + str(subtotal) + " Bs)"
        print(i + 1, ".", item)
        resumen = resumen + item + " | "

    print("\nTOTAL A PAGAR:", total, "Bs")

    print("\n1. Confirmar y pagar")
    print("2. Cancelar pedido")
    print("3. Volver")

    opc = input("Seleccione una opcion: ")

    if opc == '1':
        pedido_final = "Pedido: " + resumen + " Total: " + str(total) + " Bs"
        historial_pedidos.append(pedido_final)
        print("\n¡Pedido confirmado gracias por su compra!")
        carrito_nombres.clear()
        carrito_precios.clear()
        carrito_cantidades.clear()

    elif opc == '2':
        carrito_nombres.clear()
        carrito_precios.clear()
        carrito_cantidades.clear()
        print("Carrito vaciado.")


def cerrar_sesion():
    print('\nSesion cerrada.')