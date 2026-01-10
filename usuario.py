import json
import os

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