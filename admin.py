import json
import os

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
        return False
    
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return False

def login_admin_menu():
    cargar_datos()

    while True:
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
                continue

            print("Funcionalidad pendiente de implementar completamente")

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
                    bandera = False
                else:
                    print("\n Credenciales incorrectas")
                    print("Opciones:")
                    print("1. Reintentar")
                    print("-1. Volver")
                    opcion_error = input("Seleccione: ").strip()
                    if opcion_error == "-1":
                        bandera = False