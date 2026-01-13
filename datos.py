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
                    'desprecion': 'Salsa de tomate, mozzarrella, albahaca',
                    'disponible': True
                },
                {
                    'id': 'PROD002',
                    'nombre': 'Pizza Pepperoni',
                    'categoria': 'Principal',
                    'precio': 24000.00,
                    'desprecion': 'Salsa de tomate, mozzarrella, pepperoni',
                    'disponible': True
                },
                {
                    'id': 'PROD003',
                    'nombre': 'Pizza Cuatro Quesos',
                    'categoria': 'Principal',
                    'precio': 25000.00,
                    'desprecion': 'Mozzarella, parmesano, gorgonzola, provolone',
                    'disponible': True
                },
                {
                    'id': 'PROD004',
                    'nombre': 'Ensalada Cesar',
                    'categoria': 'Entrada',
                    'precio': 16000.50,
                    'desprecion': 'Lechuga, crutones, parmesano, aderezo cesar',
                    'disponible': True
                },
                {
                    'id': 'PROD005',
                    'nombre': 'Pan de Ajo',
                    'categoria': 'Entrada',
                    'precio': 4000.00,
                    'desprecion': 'Pan con mantequilla de ajo y hierbas',
                    'disponible': True
                },
                {
                    'id': 'PROD006',
                    'nombre': 'Tiramisu',
                    'categoria': 'Postre',
                    'precio': 5000.50,
                    'desprecion': 'Postre italiano con cafe y mascarpone',
                    'disponible': True
                },
                {
                    'id': 'PROD007',
                    'nombre': 'Helado de Vainilla',
                    'categoria': 'Postre',
                    'precio': 3000.50,
                    'desprecion': 'Tres bolas de helado',
                    'disponible': True
                },
                {
                    'id': 'PROD008',
                    'nombre': 'Coca Cola',
                    'categoria': 'Bebida',
                    'precio': 2500.50,
                    'desprecion': 'Bebida gaseosa 500ml',
                    'disponible': True
                },
                {
                    'id': 'PROD009',
                    'nombre': 'Agua Mineral',
                    'categoria': 'Bebida',
                    'precio': 1500.50,
                    'desprecion': 'Agua sin gas 500ml',
                    'disponible': True
                },
                {
                    'id': 'PROD010',
                    'nombre': 'Limonada',
                    'categoria': 'Bebida',
                    'precio': 3000.00,
                    'desprecion': 'Limonada natural 500ml',
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
            with open(ARCHIVO_ADMINS, 'w', encoding="utf-8") as archivo:
                json.dump(admins_inicial, archivo, indent=4, ensure_ascii=False)
        
        return True
    
    except Exception as e:
        print(f"Error al inicializara archivos: {e}")
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
