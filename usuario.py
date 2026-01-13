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
    except FileExistsError:
        usuarios = {}
        return True
    except Exception as e:
        print("Error al cargar usuarios: {e}")
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
    datos = [nombre, mail, contrasena]
    if not validar_datos_no_nulos(datos):
        print("ERROR: Todos los campos son obligatorios")
        return False
    
    if not validar_solo_letras(nombre):
        print("ERROR: El nombre solo puede contener letras")
        return False
    
    if not validar_mail(mail):
        print("ERROR: El mail debe tener un dominio valido")
        return False
    
    if not validar_contrasena(contrasena):
        print("ERROR: La contraseña debe tener al menos 5 caracteres")
        return False
    
    mail = mail.strip().lower()

    if mail in usuarios:
        print(f"El usuario {mail} ya existe")
        return False
    
    try:
        usuarios[mail] = {
            "nombre": nombre.strip(),
            "mail": mail,
            "contraseña": contrasena.strip(),
            "pedidos": []
        }

        guardar_usuarios()
        print(f"¡Bienvenido {nombre}! Usuario registrado correctamente")
        return True
    
    except Exception as e:
        print(f"Error al registrar: {e}")
        return False

def login_usuario():
    from validacion import validar_usuario_y_contrasena

    resultado = validar_usuario_y_contrasena(usuario, contrasena)

    if resultado is None:
        print("Usuario o contraseña incorrectos.")
        return False
    
    print(f"¡Bienvenido {resultado['nombre']}!")
    return True

def menu_usuario(usuario_actual):
    cargar_usuarios()

    while True:
        limpiar_pantalla()
        print("=" * 60)
        print(f"BIENVENIDO: {usuarios.get(usuario_actual, {}).get('nombre', usuario_actual)}")
        print("=" * 60)
        print("\n MENÚ DE OPCIONES")
        print("-" * 60)
        print("1. Ver menú completo")
        print("2. Hacer pedido")
        print("3. Ver mis pedidos")
        print("0. Cerrar sesión")
        print("-" * 60)

        opcion = input("\n Seleccione una opción: ").strip()

        if opcion == "1":
            ver_menu_completo()
        
        elif opcion == "2":
            hacer_pedido(usuario_actual)

        elif opcion == "3":
            ver_mis_pedidos(usuario_actual)

        elif opcion == "0":
            print("\n ¡Hasta luego!")
            pausar()
            break

        else:
            print("Opción invalida.")
            pausar()

def login_usuario_menu():
    cargar_usuarios()

    while True:
        limpiar_pantalla()
        print("=" * 60)
        print("ACCESO USUARIO")
        print("=" * 60)
        print("\n1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("0. Volver al menú principal")
        print("-" * 60)

        opcion = input("\n Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n REGISTRO DE USUARIO")
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
                mail_input = input("Emil (-1 para cancelar): ").strip().lower()
                if mail_input == "-1":
                    break

                if not validacion.validar_mail(mail_input):
                    print("ERROR: El mail debe tener un dominio valido.")
                    continue

                if mail_input in usuarios:
                    print("ERROR: El mail ya está registrado.")
                    continue

                mail = mail_input
                bandera = False

            if mail is None:
                continue

            bandera = True
            contrasena = None
            while bandera:
                contrasena_input = input("Contraseña (-1 para cancelar): ").strip()
                if contrasena_input == "-1":
                    break

                if not validacion.validar_contrasena(contrasena_input):
                    print("ERROR: La contraseña debe tener al menos 5 caracteres.")
                    continue

                contrasena = contrasena_input
                bandera = False

            if contrasena is None:
                continue

            if registrar_usuario(nombre, mail, contrasena):
                pausar()
        
        elif opcion == "2":
            print("\n INICIO DE SESIÓN")
            print("-" * 60)

            bandera = True
            while bandera:
                usuario = input("Email (-1 para cancelar): ").strip().lower()
                if usuario == "-1":
                    bandera = False
                    continue

                contrasena = input("Contraseña: ").strip()

                if login_usuario(usuario, contrasena):
                    pausar()
                    menu_usuario(usuario)
                    bandera = False
                else:
                    print("\n Credenciales incorrectos.")
                    print("Opciones:")
                    print("1. Reintentar")
                    print("-1. Volver")
                    opcion_error = input("Seleccione: ").strip()
                    if opcion_error == "-1":
                        bandera = False
        
        elif opcion == "0":
            break

        else:
            print("Opción inválida.")
            pausar()