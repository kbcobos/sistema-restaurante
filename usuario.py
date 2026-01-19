import json
import os
from datetime import datetime
from utilidades import limpiar_pantalla, pausar, mostrar_tabla_productos
import validacion

usuarios = {}

def cargar_usuarios():
    global usuarios
    try:
        ruta = os.path.join(os.path.dirname(__file__), "usuarios.json")
        with open(ruta, "r", encoding="utf-8") as f:
            usuarios = json.load(f)
        return True
    except FileNotFoundError:
        usuarios = {}
        return True
    except Exception as e:
        print(f"Error al cargar usuarios: {e}")
        return False

def guardar_usuarios():
    try:
        ruta = os.path.join(os.path.dirname(__file__), "usuarios.json")
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(usuarios, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar usuarios: {e}")
        return False

def registrar_usuario(nombre, mail, contrasena):
    from validacion import validar_mail, validar_contrasena, validar_solo_letras, validar_datos_no_nulos
    
    datos = [nombre, mail, contrasena]
    if not validar_datos_no_nulos(datos):
        print("ERROR: Todos los campos son obligatorios.")
        return False
    
    if not validar_solo_letras(nombre):
        print("ERROR: El nombre solo puede contener letras.")
        return False
    
    if not validar_mail(mail):
        print("ERROR: El mail debe tener un dominio valido.")
        return False
    
    if not validar_contrasena(contrasena):
        print("ERROR: La contrasena debe tener al menos 5 caracteres.")
        return False
    
    mail = mail.strip().lower()
    
    if mail in usuarios:
        print(f"ERROR: El usuario {mail} ya existe.")
        return False
    
    try:
        usuarios[mail] = {
            "nombre": nombre.strip(),
            "mail": mail,
            "contraseña": contrasena.strip(),
            "pedidos": []
        }
        
        guardar_usuarios()
        print(f"Bienvenido {nombre}! Usuario registrado correctamente.")
        return True
    
    except Exception as e:
        print(f"Error al registrar: {e}")
        return False

def login_usuario(usuario, contrasena):
    from validacion import validar_usuario_y_contrasena
    
    resultado = validar_usuario_y_contrasena(usuario, contrasena)
    
    if resultado is None:
        print("ERROR: Usuario o contrasena incorrectos.")
        return False
    
    print(f"Bienvenido {resultado['nombre']}!")
    return True

def ver_menu_completo():
    limpiar_pantalla()
    print("=" * 60)
    print("MENU DEL RESTAURANTE")
    print("=" * 60)
    
    try:
        ruta = os.path.join(os.path.dirname(__file__), "menu.json")
        with open(ruta, "r", encoding="utf-8") as f:
            menu = json.load(f)
        
        if not menu:
            print("\nNo hay productos disponibles.")
            pausar()
            return
        
        categorias = {}
        for producto in menu:
            categoria = producto.get('categoria', 'Sin categoria').title()
            if categoria not in categorias:
                categorias[categoria] = []
            categorias[categoria].append(producto)
        
        for categoria, productos in sorted(categorias.items()):
            print(f"\n{categoria.upper()}")
            print("-" * 60)
            mostrar_tabla_productos(productos)
        
    except FileNotFoundError:
        print("\nNo se pudo cargar el menu.")
    except Exception as e:
        print(f"\nError: {e}")
    
    pausar()

def hacer_pedido(usuario_actual):
    limpiar_pantalla()
    print("=" * 60)
    print("HACER PEDIDO")
    print("=" * 60)
    
    print("\nInformacion del pedido")
    bandera = True
    mesa = None
    while bandera:
        mesa_input = input("Numero de mesa (-1 para cancelar): ").strip()
        if mesa_input == "-1":
            print("Pedido cancelado.")
            pausar()
            return
        
        mesa = validacion.validar_mesa(mesa_input)
        if mesa is None:
            print("ERROR: El numero de mesa debe ser un entero positivo.")
            continue
        bandera = False
    
    try:
        ruta = os.path.join(os.path.dirname(__file__), "menu.json")
        with open(ruta, "r", encoding="utf-8") as f:
            menu = json.load(f)
    except Exception as e:
        print(f"Error al cargar menu: {e}")
        pausar()
        return
    
    if not menu:
        print("No hay productos disponibles.")
        pausar()
        return
    
    carrito = []
    
    while True:
        limpiar_pantalla()
        print("=" * 60)
        print(f"PEDIDO - Mesa {mesa}")
        print("=" * 60)
        print("\nMENU DISPONIBLE")
        mostrar_tabla_productos(menu, mostrar_indices=True)
        
        print("\n" + "=" * 60)
        print("Opciones:")
        print("  [Numero] - Agregar producto al carrito")
        print("  [V] - Ver carrito actual")
        print("  [C] - Confirmar pedido")
        print("  [X] - Cancelar pedido")
        print("=" * 60)
        
        opcion = input("\nSeleccione opcion: ").strip().upper()
        
        if opcion == "X":
            if validacion.confirmar_accion("cancelar el pedido"):
                print("Pedido cancelado.")
                pausar()
                return
        
        elif opcion == "V":
            if not carrito:
                print("\nTu carrito esta vacio.")
            else:
                print(f"\n{'Cant':<6} {'Producto':<25} {'Precio':<10} {'Subtotal'}")
                print("-" * 60)
                total = 0
                for item in carrito:
                    subtotal = item['precio'] * item['cantidad']
                    print(f"{item['cantidad']:<6} {item['nombre']:<25} ${item['precio']:<9.2f} ${subtotal:.2f}")
                    total += subtotal
                print("-" * 60)
                print(f"{'TOTAL:':<42} ${total:.2f}")
            pausar()
        
        elif opcion == "C":
            if not carrito:
                print("ERROR: El carrito esta vacio.")
                pausar()
                continue
            
            total = sum(item['precio'] * item['cantidad'] for item in carrito)
            print(f"\nTotal a pagar: ${total:.2f}")
            
            if validacion.confirmar_accion("confirmar el pedido"):
                pedido_id = datetime.now().strftime("%Y%m%d%H%M%S")
                pedido = {
                    'id': pedido_id,
                    'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'usuario': usuario_actual,
                    'mesa': mesa,
                    'productos': carrito.copy(),
                    'total': total,
                    'estado': 'Pendiente'
                }
                
                try:
                    ruta_pedidos = os.path.join(os.path.dirname(__file__), "pedidos.json")
                    try:
                        with open(ruta_pedidos, "r", encoding="utf-8") as f:
                            pedidos = json.load(f)
                    except FileNotFoundError:
                        pedidos = []
                    
                    pedidos.append(pedido)
                    
                    with open(ruta_pedidos, "w", encoding="utf-8") as f:
                        json.dump(pedidos, f, indent=4, ensure_ascii=False)
                    
                    if usuario_actual in usuarios:
                        usuarios[usuario_actual]['pedidos'].append(pedido_id)
                        guardar_usuarios()
                    
                    from datos import generar_ticket_txt
                    generar_ticket_txt(pedido)
                    
                    print(f"\nPedido realizado exitosamente!")
                    print(f"Numero de pedido: {pedido_id}")
                    print(f"Total: ${total:.2f}")
                    print("Ticket generado en la carpeta 'tickets/'")
                    pausar()
                    return
                
                except Exception as e:
                    print(f"Error al guardar pedido: {e}")
                    pausar()
                    return
        
        else:
            try:
                indice = int(opcion) - 1
                if 0 <= indice < len(menu):
                    producto = menu[indice]
                    
                    bandera = True
                    cantidad = None
                    while bandera:
                        cantidad_input = input(f"Cantidad de '{producto['nombre']}' (-1 para cancelar): ").strip()
                        if cantidad_input == "-1":
                            break
                        
                        cantidad = validacion.validar_cantidad(cantidad_input)
                        if cantidad is None:
                            print("ERROR: La cantidad debe ser un entero positivo.")
                            continue
                        bandera = False
                    
                    if cantidad is None:
                        continue
                    
                    encontrado = False
                    for item in carrito:
                        if item['id'] == producto['id']:
                            item['cantidad'] += cantidad
                            encontrado = True
                            break
                    
                    if not encontrado:
                        carrito.append({
                            'id': producto['id'],
                            'nombre': producto['nombre'],
                            'precio': producto['precio'],
                            'cantidad': cantidad
                        })
                    
                    subtotal = producto['precio'] * cantidad
                    print(f"\n{cantidad}x {producto['nombre']} agregado (${subtotal:.2f})")
                    pausar()
                else:
                    print("ERROR: Numero de producto invalido.")
                    pausar()
            
            except ValueError:
                print("ERROR: Opcion invalida.")
                pausar()

def ver_mis_pedidos(usuario_actual):
    limpiar_pantalla()
    print("=" * 60)
    print("MIS PEDIDOS")
    print("=" * 60)
    
    try:
        ruta = os.path.join(os.path.dirname(__file__), "pedidos.json")
        with open(ruta, "r", encoding="utf-8") as f:
            todos_pedidos = json.load(f)
        
        mis_pedidos = [p for p in todos_pedidos if p['usuario'] == usuario_actual]
        
        if not mis_pedidos:
            print("\nNo tienes pedidos registrados.")
        else:
            for pedido in mis_pedidos:
                print(f"\nPedido #{pedido['id']}")
                print(f"Fecha: {pedido['fecha']}")
                print(f"Mesa: {pedido['mesa']}")
                print(f"Estado: {pedido['estado']}")
                print(f"Total: ${pedido['total']:.2f}")
                print("   Productos:")
                for prod in pedido['productos']:
                    print(f"   - {prod['cantidad']}x {prod['nombre']} (${prod['precio']:.2f})")
                print("-" * 60)
            
            print(f"\nTotal de pedidos: {len(mis_pedidos)}")
    
    except FileNotFoundError:
        print("\nNo hay pedidos registrados.")
    except Exception as e:
        print(f"\nError: {e}")
    
    pausar()

def menu_usuario(usuario_actual):
    cargar_usuarios()
    
    while True:
        limpiar_pantalla()
        print("=" * 60)
        print(f"BIENVENIDO: {usuarios.get(usuario_actual, {}).get('nombre', usuario_actual)}")
        print("=" * 60)
        print("\nMENU DE OPCIONES")
        print("-" * 60)
        print("1. Ver menu completo")
        print("2. Hacer pedido")
        print("3. Ver mis pedidos")
        print("0. Cerrar sesion")
        print("-" * 60)
        
        opcion = input("\nSeleccione una opcion: ").strip()
        
        if opcion == "1":
            ver_menu_completo()
        
        elif opcion == "2":
            hacer_pedido(usuario_actual)
        
        elif opcion == "3":
            ver_mis_pedidos(usuario_actual)
        
        elif opcion == "0":
            print("\nHasta luego!")
            pausar()
            break
        
        else:
            print("ERROR: Opcion invalida.")
            pausar()

def login_usuario_menu():
    cargar_usuarios()
    
    while True:
        limpiar_pantalla()
        print("=" * 60)
        print("    ACCESO USUARIO")
        print("=" * 60)
        print("\n1. Registrar nuevo usuario")
        print("2. Iniciar sesion")
        print("0. Volver al menu principal")
        print("-" * 60)
        
        opcion = input("\nSeleccione una opcion: ").strip()
        
        if opcion == "1":
            print("\nREGISTRO DE USUARIO")
            print("-" * 60)
            
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
            mail = None
            while bandera:
                mail_input = input("Email (-1 para cancelar): ").strip().lower()
                if mail_input == "-1":
                    break
                
                if not validacion.validar_mail(mail_input):
                    print("ERROR: El mail debe tener un dominio valido.")
                    continue
                
                if mail_input in usuarios:
                    print("ERROR: El mail ya esta registrado.")
                    continue
                
                mail = mail_input
                bandera = False
            
            if mail is None:
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
            
            if registrar_usuario(nombre, mail, contrasena):
                pausar()
        
        elif opcion == "2":
            print("\nINICIO DE SESION")
            print("-" * 60)
            
            bandera = True
            while bandera:
                usuario = input("Email (-1 para cancelar): ").strip().lower()
                if usuario == "-1":
                    bandera = False
                    continue
                
                contrasena = input("Contrasena: ").strip()
                
                if login_usuario(usuario, contrasena):
                    pausar()
                    menu_usuario(usuario)
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