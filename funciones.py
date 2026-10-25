usuarios = ['admin', 'usuario']
contraseñas = ['1234', '1234']
carrito = {}


def login():
    usuario = input('Ingrese su usuario: ').strip().lower()
    contraseña = input('Ingrese su contraseña: ').strip()

    for i in range(len(usuarios)):
        if usuario == usuarios[i] and contraseña == contraseñas[i]:

            if usuario == 'admin':
                print('--- Acceso concedido ---\n')
                print('Bienvenido administrador')
                return 'administrador'

            else:
                print('--- Acceso concedido ---')
                print('Bienvenido usuario')
                return 'usuario'

    print('Contraseña o usuario incorrecto')
    return 'incorrecto'


# -------------------- FUNCIONES DE ADMINISTRADOR --------------------


def registrar_usuario():
    nuevo_usuario = input('\nIngrese el usuario: ').strip().lower()

    if nuevo_usuario in usuarios:
        print('El usuario ya existe')
        return

    nueva_contraseña = input('Ingrese la contraseña de cuatro dígitos: ').strip()

    if len(nueva_contraseña) != 4 or not nueva_contraseña.isdigit():
        print('La contraseña debe tener cuatro dígitos')
        return

    usuarios.append(nuevo_usuario)
    contraseñas.append(nueva_contraseña)

    print('Nuevo usuario registrado exitosamente...')


def mostrar_usuarios():
    print('\n--- USUARIOS REGISTRADOS ---')

    for i in range(len(usuarios)):
        print('Usuario:', usuarios[i])
        print('Contraseña:', contraseñas[i])


def buscar_usuario():
    buscar_u = input('\nIngrese el nombre de usuario: ').strip().lower()

    if buscar_u in usuarios:
        posicion = usuarios.index(buscar_u)

        print('Usuario encontrado')
        print('Usuario:', usuarios[posicion])
        print('Contraseña:', contraseñas[posicion])

    else:
        print('Usuario no encontrado...')

def modificar_usuario():
    buscar_u = input('\nIngrese el usuario que desea modificar: ').strip().lower()

    if buscar_u in usuarios:
        posicion = usuarios.index(buscar_u)

        nuevo_usuario = input('Ingrese el nuevo usuario: ').strip().lower()
        nueva_contraseña = input('Ingrese la nueva contraseña de cuatro dígitos: ').strip()

        usuarios[posicion] = nuevo_usuario
        contraseñas[posicion] = nueva_contraseña

        print('Usuario modificado correctamente...')

    else:
        print('Usuario no encontrado...')


def eliminar_usuario():
    buscar_u = input('\nIngrese el usuario que desea eliminar: ').strip().lower()

    if buscar_u in usuarios:
        posicion = usuarios.index(buscar_u)

        usuarios.pop(posicion)
        contraseñas.pop(posicion)

        print('Usuario eliminado correctamente...')

    else:
        print('Usuario no encontrado...')


def cerrar_sesion():
    print('\nSesión cerrada')


# -------------------- FUNCIONES DE USUARIO --------------------


def platos():
    print('\n--- PLATOS ---')
    print('1. Fricase (28 Bs)')
    print('2. Charque (30 Bs)')
    print('3. Pique (40 Bs)')
    print('4. Churrasco (90 Bs)')
    
    seleccion = input('\nIngrese el numero o nombre del plato que desea (o "salir"): ').lower().strip()
    
    if seleccion == 'salir':
        return

    if seleccion == '1' or seleccion == 'fricase':
        nombre = 'Fricase'
        precio = 28
    elif seleccion == '2' or seleccion == 'charque':
        nombre = 'Charque'
        precio = 30
    elif seleccion == '3' or seleccion == 'pique':
        nombre = 'Pique'
        precio = 40
    elif seleccion == '4' or seleccion == 'churrasco':
        nombre = 'Churrasco'
        precio = 90
    else:
        print('Plato no reconocido')
        return
        
    try:
        cantidad = int(input(f'¿Cuántos platos de {nombre} desea pedir?: '))
        if cantidad > 0:
            if nombre in carrito:
                carrito[nombre]['cantidad'] += cantidad
            else:
                carrito[nombre] = {'precio': precio, 'cantidad': cantidad}
            print(f'Se agregaron {cantidad} {nombre} al pedido')
        else:
            print('Debe pedir al menos 1')
    except ValueError:
        print('Error: Ingrese un número válido para la cantidad')



    
def platos_especiales():
    print('\n--- PLATOS ESPECIALES ---')
    print('1. Mariscos (110 Bs)')
    print('2. Cangrejo (150 Bs)')
    print('3. Calamar (130 Bs)')
    print('4. Pulpo (200 Bs)')



def ver_pedido():
    if not carrito:
        print('\nSu carrito está vacío actualmente')
        return

    print('\n--- SU PEDIDO ACTUAL ---')
    total = 0
    lista_platos = list(carrito.keys()) 

    for i, nombre in enumerate(lista_platos, 1):
        datos = carrito[nombre]
        subtotal = datos['cantidad'] * datos['precio']
        total += subtotal
        print(f'{i}. {nombre} (Cantidad: {datos['cantidad']}) - {subtotal} Bs')

    print(f'\nTOTAL A PAGAR: {total} Bs')
    
    print('\nOpciones:')
    print('1. Confirmar pedido')
    print('2. Eliminar un plato del carrito')
    print('3. Volver al menú')
    
    opcion = input('Seleccione una opción: ')
    
    if opcion == '1':
        print('\nPedido confirmado gracias por su compra')
        print('Gracias por su compra')
        carrito.clear()
        
    elif opcion == '2':
        borrar = input('Ingrese el numero o nombre exacto del plato a eliminar: ').capitalize().strip()
        plato_a_borrar = None
        
        if borrar.isdigit() and 1 <= int(borrar) <= len(lista_platos):
            plato_a_borrar = lista_platos[int(borrar) - 1]
        elif borrar in carrito:
            plato_a_borrar = borrar
            
        if plato_a_borrar:
            try:
                cant_quitar = int(input(f'Tiene {carrito[plato_a_borrar]['cantidad']} de {plato_a_borrar} ¿Cuántos desea quitar?: '))
                if cant_quitar >= carrito[plato_a_borrar]['cantidad']:
                    del carrito[plato_a_borrar]
                    print(f' Se eliminó {plato_a_borrar} por completo')
                elif cant_quitar > 0:
                    carrito[plato_a_borrar]['cantidad'] -= cant_quitar
                    print(f' Cantidad reducida. Ahora tiene {carrito[plato_a_borrar]['cantidad']}')
            except ValueError:
                print('Error: Ingrese un número válido')
        else:
            print('Ese plato no se encontró en su pedido')

    print(carrito)
