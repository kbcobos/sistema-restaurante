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
        print(f"El administrador '{usuario}' ya existe")
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

        elif opcion == "0":
            break

        else:
            print("Opcion invalida")
                