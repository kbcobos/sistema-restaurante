import json
import os
from datetime import datetime

ARCHIVO_MENU = 'menu.json'
ARCHIVO_PEDIDOS = 'pedidos.json'
ARCHIVO_USUARIOS = 'usuarios.json'
ARCHIVO_ADMINS = 'admins.json'

CARPETA_TICKETS = 'tickets'
CARPETA_REPORTES = 'reportes'

NOMBRE_RESTAURANTE = "PIZZERIA ESPACIAL"

def inicializar_archivos():
    try:
        if not os.path.exists(CARPETA_TICKETS):
            os.makedirs(CARPETA_TICKETS)
        
        if not os.path.exists(CARPETA_REPORTES):
            os.makedirs(CARPETA_REPORTES)
        
        if not os.path.exists(ARCHIVO_MENU):
            menu_inicial = [
                {
                    'id': 'PROD001',
                    'nombre': 'Pizza Margarita',
                    'categoria': 'Principal',
                    'precio': 22000.00,
                    'descripcion': 'Salsa de tomate, mozzarella, albahaca',
                    'disponible': True
                },
                {
                    'id': 'PROD002',
                    'nombre': 'Pizza Pepperoni',
                    'categoria': 'Principal',
                    'precio': 24000.00,
                    'descripcion': 'Salsa de tomate, mozzarella, pepperoni',
                    'disponible': True
                },
                {
                    'id': 'PROD003',
                    'nombre': 'Pizza Cuatro Quesos',
                    'categoria': 'Principal',
                    'precio': 25000.00,
                    'descripcion': 'Mozzarella, parmesano, gorgonzola, provolone',
                    'disponible': True
                },
                {
                    'id': 'PROD004',
                    'nombre': 'Ensalada Cesar',
                    'categoria': 'Entrada',
                    'precio': 16000.50,
                    'descripcion': 'Lechuga, crutones, parmesano, aderezo cesar',
                    'disponible': True
                },
                {
                    'id': 'PROD005',
                    'nombre': 'Pan de Ajo',
                    'categoria': 'Entrada',
                    'precio': 4000.00,
                    'descripcion': 'Pan con mantequilla de ajo y hierbas',
                    'disponible': True
                },
                {
                    'id': 'PROD006',
                    'nombre': 'Tiramisu',
                    'categoria': 'Postre',
                    'precio': 5000.50,
                    'descripcion': 'Postre italiano con cafe y mascarpone',
                    'disponible': True
                },
                {
                    'id': 'PROD007',
                    'nombre': 'Helado de Vainilla',
                    'categoria': 'Postre',
                    'precio': 3000.50,
                    'descripcion': 'Tres bolas de helado',
                    'disponible': True
                },
                {
                    'id': 'PROD008',
                    'nombre': 'Coca Cola',
                    'categoria': 'Bebida',
                    'precio': 2500.50,
                    'descripcion': 'Bebida gaseosa 500ml',
                    'disponible': True
                },
                {
                    'id': 'PROD009',
                    'nombre': 'Agua Mineral',
                    'categoria': 'Bebida',
                    'precio': 1500.50,
                    'descripcion': 'Agua sin gas 500ml',
                    'disponible': True
                },
                {
                    'id': 'PROD010',
                    'nombre': 'Limonada',
                    'categoria': 'Bebida',
                    'precio': 3000.00,
                    'descripcion': 'Limonada natural 500ml',
                    'disponible': True
                }
            ]
            
            with open(ARCHIVO_MENU, 'w', encoding='utf-8') as archivo:
                json.dump(menu_inicial, archivo, indent=4, ensure_ascii=False)
        
        if not os.path.exists(ARCHIVO_PEDIDOS):
            with open(ARCHIVO_PEDIDOS, 'w', encoding='utf-8') as archivo:
                json.dump([], archivo, indent=4, ensure_ascii=False)
        
        if not os.path.exists(ARCHIVO_USUARIOS):
            with open(ARCHIVO_USUARIOS, 'w', encoding='utf-8') as archivo:
                json.dump({}, archivo, indent=4, ensure_ascii=False)
        
        if not os.path.exists(ARCHIVO_ADMINS):
            admins_inicial = {
                "admin": {
                    "Contraseña": "admin123",
                    "Mail": "admin@pizzeriaespacial.com",
                    "Nombre": "Admin",
                    "Apellido": "Sistema"
                }
            }
            with open(ARCHIVO_ADMINS, 'w', encoding='utf-8') as archivo:
                json.dump(admins_inicial, archivo, indent=4, ensure_ascii=False)
        
        return True
    
    except Exception as e:
        print(f"Error al inicializar archivos: {e}")
        return False

def cargar_menu():
    try:
        with open(ARCHIVO_MENU, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("ERROR: Error al leer el archivo de menú")
        return []
    except Exception as e:
        print(f"Error al cargar menú: {e}")
        return []

def guardar_menu(menu):
    try:
        with open(ARCHIVO_MENU, 'w', encoding='utf-8') as archivo:
            json.dump(menu, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar menú: {e}")
        return False

def cargar_pedidos():
    try:
        with open(ARCHIVO_PEDIDOS, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("ERROR: Error al leer el archivo de pedidos")
        return []
    except Exception as e:
        print(f"Error al cargar pedidos: {e}")
        return []

def guardar_pedidos(pedidos):
    try:
        with open(ARCHIVO_PEDIDOS, 'w', encoding='utf-8') as archivo:
            json.dump(pedidos, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar pedidos: {e}")
        return False

def guardar_pedido(pedido):
    try:
        pedidos = cargar_pedidos()
        pedidos.append(pedido)
        return guardar_pedidos(pedidos)
    except Exception as e:
        print(f"Error al guardar pedido: {e}")
        return False

def cargar_usuarios():
    try:
        with open(ARCHIVO_USUARIOS, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("ERROR: Error al leer el archivo de usuarios")
        return {}
    except Exception as e:
        print(f"Error al cargar usuarios: {e}")
        return {}

def guardar_usuarios(usuarios):
    try:
        with open(ARCHIVO_USUARIOS, 'w', encoding='utf-8') as archivo:
            json.dump(usuarios, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar usuarios: {e}")
        return False

def cargar_admins():
    try:
        with open(ARCHIVO_ADMINS, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("ERROR: Error al leer el archivo de administradores")
        return {}
    except Exception as e:
        print(f"Error al cargar administradores: {e}")
        return {}

def guardar_admins(admins):
    try:
        with open(ARCHIVO_ADMINS, 'w', encoding='utf-8') as archivo:
            json.dump(admins, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar administradores: {e}")
        return False

def generar_ticket_txt(pedido):
    try:
        nombre_archivo = f"{CARPETA_TICKETS}/ticket_{pedido['id']}.txt"
        
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write("=" * 60 + "\n")
            archivo.write(f"     RESTAURANTE {NOMBRE_RESTAURANTE}\n")
            archivo.write("=" * 60 + "\n\n")
            
            archivo.write(f"TICKET DE PEDIDO\n")
            archivo.write(f"Numero: {pedido['id']}\n")
            archivo.write(f"Fecha: {pedido['fecha']}\n")
            archivo.write("-" * 60 + "\n\n")
            
            archivo.write(f"Cliente: {pedido['nombre']}\n")
            archivo.write(f"Mesa: {pedido['mesa']}\n")
            archivo.write(f"Estado: {pedido['estado']}\n")
            archivo.write("-" * 60 + "\n\n")
            
            archivo.write("DETALLE DEL PEDIDO\n")
            archivo.write("-" * 60 + "\n")
            archivo.write(f"{'Producto':<30} {'Cant':<6} {'Precio':<10} {'Subtotal'}\n")
            archivo.write("-" * 60 + "\n")
            
            for item in pedido['productos']:
                archivo.write(f"{item['nombre']:<30} {item['cantidad']:<6} ${item['precio']:<9.2f} ${item['subtotal']:.2f}\n")
            
            archivo.write("-" * 60 + "\n")
            archivo.write(f"{'TOTAL:':<46} ${pedido['total']:.2f}\n")
            archivo.write("=" * 60 + "\n\n")
            
            archivo.write("Gracias por su compra!\n")
            archivo.write("Esperamos verlo pronto nuevamente.\n")
            archivo.write("=" * 60 + "\n")
        
        return True
    
    except Exception as e:
        print(f"Error al generar ticket: {e}")
        return False

def exportar_reporte_txt():
    try:
        pedidos = cargar_pedidos()
        menu = cargar_menu()
        
        fecha_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_archivo = f"{CARPETA_REPORTES}/reporte_ventas_{fecha_actual}.txt"
        
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write("=" * 80 + "\n")
            archivo.write(f"REPORTE DE VENTAS - RESTAURANTE {NOMBRE_RESTAURANTE}\n")
            archivo.write("=" * 80 + "\n\n")
            
            archivo.write(f"Fecha de generacion: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            archivo.write("-" * 80 + "\n\n")
            
            archivo.write("MENU ACTUAL\n")
            archivo.write("-" * 80 + "\n")
            archivo.write(f"Total de productos: {len(menu)}\n\n")
            
            categorias = {}
            for producto in menu:
                cat = producto.get('categoria', 'Sin categoría')
                if cat not in categorias:
                    categorias[cat] = []
                categorias[cat].append(producto)
            
            for categoria, productos in categorias.items():
                archivo.write(f"\n{categoria.upper()}\n")
                for producto in productos:
                    disponible = "SI" if producto.get('disponible', True) else "NO"
                    archivo.write(f"  - {producto['nombre']} - ${producto['precio']:.2f} Disponible: {disponible}\n")
            
            archivo.write("\n" + "=" * 80 + "\n\n")
            
            archivo.write("HISTORIAL DE PEDIDOS\n")
            archivo.write("-" * 80 + "\n")
            archivo.write(f"Total de pedidos: {len(pedidos)}\n\n")
            
            if pedidos:
                total_ventas = sum(p['total'] for p in pedidos)
                promedio_venta = total_ventas / len(pedidos)
                
                archivo.write(f"RESUMEN FINANCIERO\n")
                archivo.write(f"  Total de ventas: ${total_ventas:.2f}\n")
                archivo.write(f"  Promedio por pedido: ${promedio_venta:.2f}\n\n")
                
                archivo.write(f"PEDIDOS POR ESTADO\n")
                estados = {}
                for pedido in pedidos:
                    estado = pedido['estado']
                    estados[estado] = estados.get(estado, 0) + 1
                
                for estado, cantidad in estados.items():
                    archivo.write(f"  {estado}: {cantidad} pedidos\n")
                
                archivo.write("\n")
                
                archivo.write(f"PRODUCTOS MAS VENDIDOS\n")
                productos_vendidos = {}
                ingresos_por_producto = {}
                
                for pedido in pedidos:
                    for item in pedido['productos']:
                        nombre = item['nombre']
                        cantidad = item['cantidad']
                        subtotal = item['subtotal']
                        
                        if nombre in productos_vendidos:
                            productos_vendidos[nombre] += cantidad
                            ingresos_por_producto[nombre] += subtotal
                        else:
                            productos_vendidos[nombre] = cantidad
                            ingresos_por_producto[nombre] = subtotal
                
                top_productos = sorted(productos_vendidos.items(), key=lambda x: x[1], reverse=True)[:10]
                
                for i, (producto, cantidad) in enumerate(top_productos, 1):
                    ingreso = ingresos_por_producto[producto]
                    archivo.write(f"  {i}. {producto} - {cantidad} unidades (${ingreso:.2f})\n")
                
                archivo.write("\n" + "-" * 80 + "\n\n")
                
                archivo.write(f"DETALLE DE TODOS LOS PEDIDOS\n")
                archivo.write("-" * 80 + "\n\n")
                
                for i, pedido in enumerate(pedidos, 1):
                    archivo.write(f"Pedido #{i} - ID: {pedido['id']}\n")
                    archivo.write(f"  Cliente: {pedido['nombre']} | Mesa: {pedido['mesa']}\n")
                    archivo.write(f"  Fecha: {pedido['fecha']}\n")
                    archivo.write(f"  Estado: {pedido['estado']}\n")
                    archivo.write(f"  Total: ${pedido['total']:.2f}\n")
                    archivo.write(f"  Productos:\n")
                    for item in pedido['productos']:
                        archivo.write(f"    - {item['nombre']} x{item['cantidad']} (${item['subtotal']:.2f})\n")
                    archivo.write("\n")
            
            archivo.write("=" * 80 + "\n")
            archivo.write("Fin del reporte\n")
            archivo.write("=" * 80 + "\n")
        
        nombre_fijo = f"{CARPETA_REPORTES}/reporte_ventas.txt"
        with open(nombre_archivo, 'r', encoding='utf-8') as origen:
            with open(nombre_fijo, 'w', encoding='utf-8') as destino:
                destino.write(origen.read())
        
        return True
    
    except Exception as e:
        print(f"Error al exportar reporte: {e}")
        return False