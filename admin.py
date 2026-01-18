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

        print("Datos cargados correctamente.")
        return True
    
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return False

def guardar_datos():
    try:
        ruta_admins = os.path.join(os.path.dirname(__file__), "admins.json")
        with open(ruta_admins, "w", encoding="utf-8") as f:
            json.dump(admins, f, indent=4, ensure_ascii=False)

        ruta_menu = os.path.join(os.path.dirname(__file__), "menu.json")
        with open(ruta_menu, "w", encoding="utf-8") as f:
            json.dump(menu_productos, f, indent=4, ensure_ascii=False)
        
        ruta_pedidos = os.path.join(os.path.dirname(__file__), "pedidos.json")
        with open(ruta_pedidos, "w", encoding="utf-8") as f:
            json.dump(pedidos, f, indent=4, ensure_ascii=False)
        
        print("Datos guardados correctamente.")
        return True
    
    except Exception as e:
        print(f"Error al guardar datos: {e}")
        return False

def registrar_admin(usuario, contrasena, mail, nombre, apellido):
    from validacion import validar_mail, validar_contrasena, validar_solo_letras, validar_datos_no_nulos
    datos = [usuario, contrasena, mail, nombre, apellido]
    if not validar_datos_no_nulos(datos):
        print("ERROR: Todos los campos son obligatorios.")
        return False
    
    if not validar_mail(mail):
        print("ERROR: El mail debe tener un dominio valido.")
        return False
    
    if not validar_contrasena(contrasena):
        print("ERROR: La contrasena debe tener al menos 5 caracteres.")
        return False
    
    if not validar_solo_letras(nombre) or not validar_solo_letras(apellido):
        print("ERROR: Nombre y apellido solo pueden contener letras.")
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
        
        ruta = os.path.join(os.path.dirname(__file__), "admins.json")
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(admins, f, indent=4, ensure_ascii=False)
        
        print(f"Bienvenido {usuario}! Administrador registrado correctamente.")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False

def login_admin(usuario, contrasena):
    from validacion import validar_admin_y_contrasena
    
    resultado = validar_admin_y_contrasena(usuario, contrasena)
    
    if resultado is None:
        print("ERROR: Usuario o contrasena incorrectos.")
        return False
    
    print(f"Bienvenido {resultado['Nombre']}!")
    return True

def menu_gestion_menu():
    while True:
        limpiar_pantalla()
        print("=" * 60)
        print("GESTION DE MENU")
        print("=" * 60)
        print("\n1. Ver menu completo")
        print("2. Agregar producto")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("0. Volver")
        print("-" * 60)
        
        opcion = input("\nSeleccione una opcion: ").strip()
        
        if opcion == "1":
            ver_menu_admin()
        
        elif opcion == "2":
            agregar_producto()
        
        elif opcion == "3":
            modificar_producto()
        
        elif opcion == "4":
            eliminar_producto()
        
        elif opcion == "0":
            break
        
        else:
            print("ERROR: Opcion invalida.")
            pausar()

def ver_menu_admin():
    limpiar_pantalla()
    print("=" * 60)
    print("MENU COMPLETO (ADMIN)")
    print("=" * 60)
    
    if not menu_productos:
        print("\nNo hay productos en el menu.")
        pausar()
        return
    
    print(f"\n{'#':<4} {'ID':<8} {'Producto':<20} {'Categoria':<12} {'Precio':<10} {'Disponible'}")
    print("-" * 60)
    
    for i, producto in enumerate(menu_productos, 1):
        disponible = "SI" if producto.get('disponible', True) else "NO"
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
    
    descripcion = input("Descripcion (opcional, Enter para omitir): ").strip()
    
    try:
        nuevo_id = f"PROD{len(menu_productos) + 1:03d}"
        
        nuevo_producto = {
            'id': nuevo_id,
            'nombre': nombre,
            'categoria': categoria,
            'precio': precio,
            'descripcion': descripcion,
            'disponible': True
        }
        
        menu_productos.append(nuevo_producto)
        guardar_datos()
        
        print(f"\nProducto '{nombre}' agregado exitosamente.")
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
        opcion = input("\nNumero de producto (0 para cancelar): ").strip()
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
    
    print("Categorias: Entrada, Principal, Postre, Bebida")
    nueva_categoria = input(f"Categoria [{producto['categoria']}]: ").strip()
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
            print("Operacion cancelada.")
            pausar()
            return
        
        try:
            indice = int(opcion) - 1
            if 0 <= indice < len(menu_productos):
                producto = menu_productos[indice]
                
                if validacion.confirmar_accion(f"eliminar '{producto['nombre']}'"):
                    menu_productos.pop(indice)
                    guardar_datos()
                    print(f"\nProducto '{producto['nombre']}' eliminado.")
                else:
                    print("\nEliminacion cancelada.")
                
                bandera = False
            else:
                print("ERROR: Numero invalido.")
        except ValueError:
            print("ERROR: Debe ingresar un numero.")
    
    pausar()

def menu_gestion_pedidos():
    while True:
        limpiar_pantalla()
        print("=" * 60)
        print("GESTION DE PEDIDOS")
        print("=" * 60)
        print("\n1. Ver todos los pedidos")
        print("2. Ver pedidos por estado")
        print("3. Cambiar estado de pedido")
        print("4. Ver estadisticas")
        print("0. Volver")
        print("-" * 60)
        
        opcion = input("\nSeleccione una opcion: ").strip()
        
        if opcion == "1":
            ver_todos_pedidos()
        
        elif opcion == "2":
            ver_pedidos_por_estado()
        
        elif opcion == "3":
            cambiar_estado_pedido()
        
        elif opcion == "4":
            ver_estadisticas()
        
        elif opcion == "0":
            break
        
        else:
            print("ERROR: Opcion invalida.")
            pausar()

def ver_todos_pedidos():
    limpiar_pantalla()
    print("=" * 60)
    print("TODOS LOS PEDIDOS")
    print("=" * 60)
    
    if not pedidos:
        print("\nNo hay pedidos registrados.")
        pausar()
        return
    
    print(f"\n{'#':<4} {'ID':<16} {'Usuario':<20} {'Mesa':<6} {'Total':<10} {'Estado':<15} {'Fecha'}")
    print("-" * 90)
    
    for i, pedido in enumerate(pedidos, 1):
        print(f"{i:<4} {pedido['id']:<16} {pedido['usuario']:<20} {pedido['mesa']:<6} ${pedido['total']:<9.2f} {pedido['estado']:<15} {pedido['fecha']}")
    
    print("-" * 90)
    print(f"Total de pedidos: {len(pedidos)}")
    
    pausar()

def ver_pedidos_por_estado():
    limpiar_pantalla()
    print("=" * 60)
    print("FILTRAR POR ESTADO")
    print("=" * 60)
    
    print("\n1. Pendiente")
    print("2. En preparacion")
    print("3. Listo")
    print("4. Entregado")
    print("5. Cancelado")
    
    opcion = input("\nSeleccione estado: ").strip()
    
    estados = {
        '1': 'Pendiente',
        '2': 'En preparacion',
        '3': 'Listo',
        '4': 'Entregado',
        '5': 'Cancelado'
    }
    
    estado_filtro = estados.get(opcion)
    
    if not estado_filtro:
        print("ERROR: Opcion invalida.")
        pausar()
        return
    
    pedidos_filtrados = [p for p in pedidos if p['estado'].lower() == estado_filtro.lower()]
    
    if not pedidos_filtrados:
        print(f"\nNo hay pedidos con estado '{estado_filtro}'.")
    else:
        print(f"\n{'#':<4} {'ID':<16} {'Usuario':<20} {'Mesa':<6} {'Total':<10} {'Fecha'}")
        print("-" * 70)
        
        for i, pedido in enumerate(pedidos_filtrados, 1):
            print(f"{i:<4} {pedido['id']:<16} {pedido['usuario']:<20} {pedido['mesa']:<6} ${pedido['total']:<9.2f} {pedido['fecha']}")
        
        print("-" * 70)
        print(f"Total: {len(pedidos_filtrados)} pedido(s)")
    
    pausar()

def cambiar_estado_pedido():
    limpiar_pantalla()
    print("=" * 60)
    print("CAMBIAR ESTADO DE PEDIDO")
    print("=" * 60)
    
    pedidos_activos = [p for p in pedidos if p['estado'] != 'Entregado']
    
    if not pedidos_activos:
        print("\nTodos los pedidos han sido entregados.")
        pausar()
        return
    
    print(f"\n{'#':<4} {'ID':<16} {'Usuario':<20} {'Estado':<15}")
    print("-" * 60)
    
    for i, pedido in enumerate(pedidos_activos, 1):
        print(f"{i:<4} {pedido['id']:<16} {pedido['usuario']:<20} {pedido['estado']:<15}")
    
    bandera = True
    while bandera:
        opcion = input("\nNumero de pedido (0 para cancelar): ").strip()
        if opcion == "0" or opcion == "-1":
            print("Operacion cancelada.")
            pausar()
            return
        
        try:
            indice = int(opcion) - 1
            if 0 <= indice < len(pedidos_activos):
                pedido_seleccionado = pedidos_activos[indice]
                
                print(f"\nPedido: {pedido_seleccionado['id']}")
                print(f"Estado actual: {pedido_seleccionado['estado']}")
                print("\nNuevo estado:")
                print("1. Pendiente")
                print("2. En preparacion")
                print("3. Listo")
                print("4. Entregado")
                
                nuevo_estado_num = input("\nSeleccione: ").strip()
                
                estados = {
                    '1': 'Pendiente',
                    '2': 'En preparacion',
                    '3': 'Listo',
                    '4': 'Entregado'
                }
                
                nuevo_estado = estados.get(nuevo_estado_num)
                
                if nuevo_estado and validacion.confirmar_accion(f"cambiar estado a '{nuevo_estado}'"):
                    for p in pedidos:
                        if p['id'] == pedido_seleccionado['id']:
                            p['estado'] = nuevo_estado
                            break
                    
                    guardar_datos()
                    print(f"\nEstado actualizado a: {nuevo_estado}")
                else:
                    print("\nOperacion cancelada.")
                
                bandera = False
            else:
                print("ERROR: Numero invalido.")
        except ValueError:
            print("ERROR: Debe ingresar un numero.")
    
    pausar()

def ver_estadisticas():
    limpiar_pantalla()
    print("=" * 60)
    print("ESTADISTICAS DE VENTAS")
    print("=" * 60)
    
    if not pedidos:
        print("\nNo hay datos para estadisticas.")
        pausar()
        return
    
    total_pedidos = len(pedidos)
    total_ventas = sum(p['total'] for p in pedidos)
    promedio = total_ventas / total_pedidos if total_pedidos > 0 else 0
    
    estados = {}
    for pedido in pedidos:
        estado = pedido['estado']
        estados[estado] = estados.get(estado, 0) + 1
    
    productos_vendidos = {}
    for pedido in pedidos:
        for item in pedido['productos']:
            nombre = item['nombre']
            cantidad = item['cantidad']
            if nombre in productos_vendidos:
                productos_vendidos[nombre] += cantidad
            else:
                productos_vendidos[nombre] = cantidad
    
    print(f"\nRESUMEN GENERAL")
    print("-" * 60)
    print(f"Total de pedidos: {total_pedidos}")
    print(f"Total de ventas: ${total_ventas:.2f}")
    print(f"Promedio por pedido: ${promedio:.2f}")
    
    print(f"\nPEDIDOS POR ESTADO")
    print("-" * 60)
    for estado, cantidad in estados.items():
        print(f"{estado:<20} {cantidad} pedidos")
    
    if productos_vendidos:
        print(f"\nTOP 5 PRODUCTOS MAS VENDIDOS")
        print("-" * 60)
        top = sorted(productos_vendidos.items(), key=lambda x: x[1], reverse=True)[:5]
        for i, (producto, cantidad) in enumerate(top, 1):
            print(f"{i}. {producto:<30} {cantidad} unidades")
    
    pausar()

def menu_administrador():
    cargar_datos()
    while True:
        limpiar_pantalla()
        print("=" * 60)
        print("    PANEL ADMINISTRADOR")
        print("=" * 60)
        print("\n1. Gestion de Menu")
        print("2. Gestion de Pedidos")
        print("3. Guardar datos")
        print("0. Cerrar sesion")
        print("-" * 60)
        
        opcion = input("\nSeleccione una opcion: ").strip()
        
        if opcion == "1":
            menu_gestion_menu()
        
        elif opcion == "2":
            menu_gestion_pedidos()
        
        elif opcion == "3":
            guardar_datos()
            pausar()
        
        elif opcion == "0":
            print("\nSesion cerrada.")
            pausar()
            return

        else:
            print("ERROR: Opcion invalida.")
            pausar()

def login_admin_menu():
    cargar_datos()

    while True:
        limpiar_pantalla()
        print("=" * 60)
        print("    ACCESO ADMINISTRADOR")
        print("=" * 60)
        print("\n1. Registrar administrador")
        print("2. Iniciar sesion")
        print("0. Volver al menu principal")
        print("-" * 60)
        
        opcion = input("\nSeleccione una opcion: ").strip()
        
        if opcion == "1":
            print("\nREGISTRO DE ADMINISTRADOR")
            print("-" * 60)
            
            clave = input("Clave de registro (-1 para cancelar): ").strip()
            if clave == "-1":
                continue
            
            if clave != "admin2025":
                print("ERROR: Clave incorrecta.")
                pausar()
                continue
            
            bandera = True
            usuario = None
            while bandera:
                usuario_input = input("Usuario (-1 para cancelar): ").strip().lower()
                if usuario_input == "-1":
                    break
                
                if not usuario_input:
                    print("ERROR: El usuario no puede estar vacio.")
                    continue
                
                if usuario_input in admins:
                    print("ERROR: El usuario ya existe.")
                    continue
                
                usuario = usuario_input
                bandera = False
            
            if usuario is None:
                continue
            
            bandera = True
            contrasena = None
            while bandera:
                contrasena_input = input("Contrasena (-1 para cancelar): ").strip()
                if contrasena_input == "-1":
                    break
                
                if not validacion.validar_contrasena(contrasena_input):
                    print("ERROR: La contrasena debe tener al menos 5 caracteres.")
                    continue
                
                contrasena = contrasena_input
                bandera = False
            
            if contrasena is None:
                continue
            
            bandera = True
            mail = None
            while bandera:
                mail_input = input("Mail (-1 para cancelar): ").strip().lower()
                if mail_input == "-1":
                    break
                
                if not validacion.validar_mail(mail_input):
                    print("ERROR: El mail debe tener un dominio valido.")
                    continue
                
                mail = mail_input
                bandera = False
            
            if mail is None:
                continue
            
            bandera = True
            nombre = None
            while bandera:
                nombre_input = input("Nombre (-1 para cancelar): ").strip()
                if nombre_input == "-1":
                    break
                
                if not validacion.validar_solo_letras(nombre_input):
                    print("ERROR: El nombre solo puede contener letras.")
                    continue
                
                nombre = nombre_input
                bandera = False
            
            if nombre is None:
                continue
            
            bandera = True
            apellido = None
            while bandera:
                apellido_input = input("Apellido (-1 para cancelar): ").strip()
                if apellido_input == "-1":
                    break
                
                if not validacion.validar_solo_letras(apellido_input):
                    print("ERROR: El apellido solo puede contener letras.")
                    continue
                
                apellido = apellido_input
                bandera = False
            
            if apellido is None:
                continue
            
            if registrar_admin(usuario, contrasena, mail, nombre, apellido):
                pausar()
        
        elif opcion == "2":
            print("\nINICIO DE SESION")
            print("-" * 60)
            
            bandera = True
            while bandera:
                usuario = input("Usuario (-1 para cancelar): ").strip().lower()
                if usuario == "-1":
                    bandera = False
                    continue
                
                contrasena = input("Contrasena: ").strip()
                
                if login_admin(usuario, contrasena):
                    pausar()
                    menu_administrador()
                    bandera = False
                else:
                    print("\nCredenciales incorrectas.")
                    print("Opciones:")
                    print("1. Reintentar")
                    print("-1. Volver")
                    opcion_error = input("Seleccione: ").strip()
                    if opcion_error == "-1":
                        bandera = False
        
        elif opcion == "0":
            break
        
        else:
            print("ERROR: Opcion invalida.")
            pausar()
