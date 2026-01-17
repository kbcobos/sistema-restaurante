import json
import os
from datetime import datetime
from utilidades import limpiar_pantalla, pausar, mostrar_tabla_productos
import validacion

admins = {}
menu_productos = []
pedidos = []

def cargar_datos():
    global admins, menu_productos, pedidos
    try:
        ruta_admins = os.path.join(os.path.dirname(__file__), "admins.json")
        try:
            with open(ruta_admins, "r", encoding="utf-8") as f:
                admins = json.load(f)
        except FileNotFoundError:
            admins = {}

        ruta_menu = os.path.join(os.path.dirname(__file__), "menu.json")
        try:
            with open(ruta_menu, "r", encoding="utf-8") as f:
                menu_productos = json.load(f)
        except FileNotFoundError:
            menu_productos = []
        
        ruta_pedidos = os.path.join(os.path.dirname(__file__), "pedidos.json")
        try:
            with open(ruta_pedidos, "r", encoding="utf-8") as f:
                pedidos = json.load(f)
        except FileNotFoundError:
            pedidos = []
        
        print("Datos cargados correctamente")
        return True
    
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return False

def guardar_datos():
    try:
        ruta_admins = os.path.join(os.path.dirname(__file__), "admins.json")
        with open(ruta_admins, "w", encoding="utf-8") as f:
            json.dump(admins, f, indent=4, ensure_ascii=False)

            ruta_admins = os.path.join(os.path.dirname(__file__), "menu.json")
            with open(ruta_menu, "w", encoding="utf-8") as f:
                json.dump(menu_productos, f, indent=4, ensure_ascii=False)

            ruta_pedidos = os.path.join(os.path.dirname(__file__), "pedidos.json")
            with open(ruta_pedidos, "w", encoding="utf-8") as f:
                json.dump(pedidos, f, indent=4, ensure_ascii=False)
            
            print("Datos guardados correctamente")
            return True
        
    except Exception as e:
        print(f"Error al guardar datos: {e}")
        return False
    
def registrar_admin(usuario, contrasena, mail, nombre, apellido):
    from validacion import validar_mail, validar_contrasena, validar_solo_letras, validar_datos_no_nulos

    datos = [usuario, contrasena, mail, nombre, apellido]
    if not validar_datos_no_nulos(datos):
        print("ERROR: Todos los campos son obligatorios")
        return False
    
    if not validar_mail(mail):
        print("ERROR: El mail debe tener un dominio valido")
        return False
    
    if not validar_contrasena(contrasena):
        print("ERROR: La contraseña debe tener al menos 5 caracteres")
        return False
    
    if not validar_solo_letras(nombre) or not validar_solo_letras(apellido):
        print("ERROR: Nombre y apellido solo pueden contener letras")
        return False
    
    usuario = usuario.strip().lower()

    if usuario in admins:
        print(f"ERROR: El administrador '{usuario}' ya existe.")
        return False
    
    try:
        admins[usuario] = {
            "Contraseña": contrasena.strip(),
            "Mail": mail.strip().lower(),
            "Nombre": nombre.strip(),
            "Apellido": apellido.strip()
        }

        ruta = os.path.join(os.path.dirname(__file__), "admins.join")
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(admins, f, indent=4, ensure_ascii=False)

        print(f"¡Bienvenido {usuario}! Administrador registrado correctamente")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False
    
def login_admin(usuario, contrasena):
    from validacion import validar_admin_y_contrasena

    resultado = validar_admin_y_contrasena(usuario, contrasena)

    if resultado is None:
        print("Usuario o contraseña incorrectos")
        return False
    
    print(f"¡Bienvenido {resultado['Nombre']}!")
    return True

def menu_gestion_menu():
    while True:
        limpiar_pantalla()
        print("=" * 60)
        print("GESTION DE MENU")
        print("=" * 60)
        print("\n1. Ver menú completo")
        print("2. Agregar producto")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("0. Volver")
        print("-" * 60)

        opcion = input("\n Seleccione una opción: ").strip()

        if opcion == "1":
            ver_menu_admin()

        elif opcion == "2":
            agregar_producto()
        
        elif opcion == "3":
            modificar_producto()

        elif opcion == "4":
            eliminar_producto()
            break

        else:
            print("Opcion invalida")
            pausar()
    
def ver_menu_admin():
    limpiar_pantalla()
    print("=" * 60)
    print("MENU COMPLETO (ADMIN)")
    print("=" * 60)

    if not menu_productos:
        print("\n No hay productos en el menú.")
        pausar()
        return
    
    print(f"\n{'#':<4} {'ID':<8} {'Producto':<20} {'Categoria':<12} {'Precio':<10} {'Disponible'}")
    print("-" * 60)

    for i, producto in enumerate(menu_productos, 1):
        disponible = "SI" if producto.get('disponible', True) else "NOT OK"
        print(f"{i:<4} {producto['id']:<8} {producto['nombre']:<20} {producto['categoria']:<12} ${producto['precio']:<9.2f} {disponible}")

        print("-" * 60)
        print(f"Total de productos: {len(menu_productos)}")

        pausar()

def agregar_producto():
    limpiar_pantalla()
    print("=" * 60)
    print("AGREGAR PRODUCTO")
    print("=" * 60)

    bandera = True
    nombre = None
    while bandera:
        nombre_input = input("\nNombre del producto (-1 para cancelar): ").strip()
        if nombre_input == "-1":
            print("Operacion cancelada.")
            pausar()
            return
        
        if not validacion.validar_nombre_producto(nombre_input):
            print("ERROR: El nombre debe tener al menos 2 caracteres.")
            continue

        nombre = nombre_input
        bandera = False

    print("\nCategorias disponibles: Entrada, Principal, Postre, Bebida")
    bandera = True
    categoria = None
    while bandera:
        categoria_input = input("Categoria (-1 para cancelar): ").strip()
        if categoria_input == "-1":
            print("Operacion cancelada.")
            pausar()
            return
        
        if not validacion.validar_categoria(categoria_input):
            print("ERROR: Categoria invalida.")
            continue

        categoria = categoria_input.title()
        bandera = False

    bandera = True
    precio = None
    while bandera:
        precio_input = input("Precio ($) (-1 para cancelar): ").strip()
        if precio_input == "-1":
            print("Operacion cancelada.")
            pausar()
            return
        
        precio = validacion.validar_precio(precio_input)
        if precio is None:
            print("ERROR: El precio debe ser un numero positivo.")
            continue

        bandera = False
    
    descripcion = input("Descripcion (opcion, Enter para omitir): ").strip()

    try:
        nuevo_id = f"PROD{len(menu_productos) + 1:03d}"

        numero_producto = {
            'id': nuevo_id,
            'nombre': nombre,
            'precio': precio,
            'descripcion': descripcion,
            'disponible': True
        }

        menu_productos.append(nuevo_producto)
        guardar_datos()

        print("f\nProducto '{nombre}' agregado exitosamente.")
        print(f"ID asignado: {nuevo_id}")
    
    except Exception as e:
        print(f"Error: {e}")

    pausar()

def modificar_producto():
    limpiar_pantalla()
    print("=" * 60)
    print("MODIFICAR PRODUCTO")
    print("=" * 60)

    if not menu_productos:
        print("\nNo hay productos para modificar.")
        pausar()
        return
    
    mostrar_tabla_productos(menu_productos, mostrar_indices=True)

    bandera = True
    indice = None
    while bandera:
        opcion = input("\nNombre de producto (0 para cancelar): ").strip()
        if opcion == "0" or opcion == "-1":
            print("Operacion cancelada.")
            pausar()
            return
        
        try:
            idx = int(opcion) - 1
            if 0 <= idx < len(menu_productos):
                indice = idx
                bandera = False
            else:
                print("ERROR: Numero invalido.")
        except ValueError:
            print("ERROR: Debe ingresar un numero.")

    producto = menu_productos[indice]

    print(f"\nEditando: {producto['nombre']}")
    print("(Presione Enter para mantener el valor actual)")

    nuevo_nombre = input(f"Nombre [{producto['nombre']}]: ").strip()
    if nuevo_nombre and validacion.validar_nombre_producto(nuevo_nombre):
        producto['nombre'] = nuevo_nombre

    print("Categoria: Entrada, Principal, Postre, Bebida")
    nueva_categoria = input(f"Categoria[{producto['categoria']}]: ").strip()
    if nueva_categoria and validacion.validar_categoria(nueva_categoria):
        producto['categoria'] = nueva_categoria.title()

    nuevo_precio_input = input(f"Precio [${producto['precio']:.2f}]: ").strip()
    if nuevo_precio_input:
        nuevo_precio = validacion.validar_precio(nuevo_precio_input)
        if nuevo_precio is not None:
            producto['precio'] = nuevo_precio

    disponible_input = input(f"Disponible (s/n) [{'s' if producto.get('disponible', True) else 'n'}]: ").strip().lower()
    if disponible_input in ['s', 'n']:
        producto['disponible'] = (disponible_input == 's')

    if validacion.confirmar_accion("guardar los cambios"):
        guardar_datos()
        print("\nProducto actualizado exitosamente.")
    else:
        print("\nCambios descartados.")

    pausar()

def eliminar_producto():
    limpiar_pantalla()
    print("=" * 60)
    print("ELIMINAR PRODUCTO")
    print("=" * 60)

    if not menu_productos:
        print("\nNo hay productos para eliminar.")
        pausar()
        return
    
    mostrar_tabla_productos(menu_productos, mostrar_indices=True)

    bandera = True
    while bandera:
        opcion = input("\nNumero de producto (0 para cancelar): ").strip()
        if opcion == "0" or opcion == "-1":
            print("Operación cancelada.")
            pausar()
            return

def login_admin_menu():
    cargar_datos()

    while True:
        limpiar_pantalla()
        print("=" * 60)
        print("ACCESO ADMINISTRADOR")
        print("=" * 60)
        print("\n1. Registrar administrador")
        print("2. Iniciar sesion")
        print("0. Volver al menu principal")
        print("-" * 60)

        opcion = input("\n Seleccione una opcion: ").strip()

        if opcion == "1":
            print("\n REGISTRO DE ADMINISTRADOR")
            print("-" * 60)

            clave = input("Clave de registro (-1 para cancelar): ").strip()
            if clave == "-1":
                continue

            if clave != "admin123":
                print("Clave incorrecta")
                pausar()
                continue

            print("Funcionalidad pendiente de implementar completamente")
            pausar()

        elif opcion == "2":
            print("\n INICIO DE SESION")
            print("-" * 60)

            bandera = True
            while bandera:
                usuario = input("Usuario (-1 para cancelar): ").strip().lower()
                if usuario == "-1":
                    bandera = False
                    continue

                contrasena = input("Contraseña: ").strip()

                if login_admin_menu(usuario, contrasena):
                    pausar()
                    bandera = False
                else:
                    print("\n Credenciales incorrectas")
                    print("Opciones:")
                    print("1. Reintentar")
                    print("-1. Volver")
                    opcion_error = input("Seleccione: ").strip()
                    if opcion_error == "-1":
                        bandera = False

        elif opcion == "0":
            break

        else:
            print("Opcion invalida")
            pausar()
