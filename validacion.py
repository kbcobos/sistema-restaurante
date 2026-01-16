import os
import json

ruta_usuarios = os.path.join(os.path.dirname(__file__), "usuarios.json")
ruta_menu = os.path.join(os.path.dirname(__file__), "menu.json")
ruta_pedidos = os.path.join(os.path.dirname(__file__), "pedidos.json")
ruta_admins = os.path.join(os.path.dirname(__file__), "admins.json")

def validar_mail(mail):

    dominios = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "gmail.com.ar", "hotmail.com.ar"]

    if not mail or "@" not in mail:
        return False
    
    partes_mail = mail.split("@")

    if len(partes_mail) != 2:
        return False
    
    nombre, dominio = partes_mail

    if not nombre or dominio not in dominios:
        return False
    
    return True
    
def validar_contrasena(contrasena):

    caracteres_minimos = 5
    if not contrasena or len(contrasena) < caracteres_minimos:
        return False
    return True

def validar_solo_letras(texto):
    if not texto or not texto.strip():
        return False
    
    texto_limpio = texto.strip()
    tiene_letra = False

    for caracter in texto_limpio:
        if caracter.isdigit():
            return False
        if caracter.isalpha():
            tiene_letra = True
        elif caracter.isspace() or caracter in ['-', "'", 'á', 'é', 'í', 'ó', 'ú', 'ñ']:
            continue
        else:
            return False
        
    return tiene_letra

def validar_datos_no_nulos(datos):
    for dato in datos:
        if dato is None:
            return False
        
        if isinstance(dato, str):
            dato_sin_espacios = dato.strip()
            if dato_sin_espacios == "":
                return False
    
    return True

def validar_numero_positivo(valor):
    try:
        numero = float(valor.strip())
        if numero <= 0:
            return None
        return numero
    except (ValueError, AttributeError):
        return None
    
def validar_mesa(mesa):
    try:
        numero_mesa = int(mesa)
        if numero_mesa <= 0:
            return None
        return numero_mesa
    except (ValueError, TypeError):
        return None
    
def validar_usuario_y_contrasena(usuario, contrasena):
    try:
        usuario = usuario.strip().lower() if usuario else ""
        contrasena = contrasena.strip() if contrasena else ""

        if not usuario or not contrasena:
            return None
        
        with open(ruta_usuarios, "r", enconding="utf-8") as archivo:
            usuarios = json.load(archivo)

        usuairo_encontrado = None
        for usuario_key in usuarios.keys():
            if usuario_key.lower() == usuario:
                usuairo_encontrado = usuario_key
                break

        if usuairo_encontrado is None:
            return None
        
        contrasena_guardada = usuarios[usuairo_encontrado].get("contraseña")

        if contrasena_guardada == contrasena:
            return usuarios[usuairo_encontrado]
        
        return None
    
    except FileExistsError:
        return None
    except Exception as e:
        print(f"ERROR: {e}")
        return None
    
def validar_admin_y_contrasena(usuario, contrasena):
    try:
        usuario = usuario.strip().lower() if usuario else ""
        contrasena = contrasena.strip() if contrasena else ""

        if not usuario or not contrasena:
            return None
        
        with open(ruta_admins, "r", encoding="utf-8") as archivo:
            admins = json.load(archivo)

        usuario_encontrado = None
        for usuario_key in admins.keys():
            if usuario_key.lower() == usuario:
                usuario_encontrado = usuario_key
                break
        
        if usuario_encontrado is None:
            return None
        
        contrasena_guardada = admins[usuario_encontrado].get("Contraseña")

        if contrasena_guardada == contrasena:
            return admins[usuario_encontrado]
        
        return None
    
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"ERROR: {e}")
        return None

def validar_producto_existente(producto_id, menu_dict=None):
    try:
        if menu_dict is not None:
            menu = menu_dict
        else:
            with open(ruta_menu, "r", encoding="utf-8") as archivo:
                menu = json.load(archivo)
        
        for item in menu:
            if item.get("id") == producto_id:
                return True
        
        return False
    
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False
    
def validar_pedido_existente(pedido_id, pedidos_dict=None):
    try:
        if pedidos_dict is not None:
            pedidos = pedidos_dict
        else:
            with open(ruta_pedidos, "r", encoding="utf-8") as archivo:
                pedidos = json.load(archivo)

            for pedido in pedidos:
                if pedido.get("id") == pedido_id:
                    return True
            
            return False
        
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False
    
def validar_usuario_registrado(usuario):
    try:
        usuario_normalizado = usuario.strip().lower() if usuario else ""

        with open(ruta_usuarios, "r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)

        for usuario_key in usuarios.keys():
            if usuario_key.lower() == usuario_normalizado:
                return True
        
        return False
    
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False
    
def confirmar_accion(accion):
    print(f"Confirma que desea {accion}? (S/N): ", end="")
    respuesta = input().strip().upper()

    while respuesta not in ("S", "N"):
        print("Respuesta invalida. Ingrese 'S' para Si o 'N' para No.")
        print("Confirma? (S/N): ", end="")
        respuesta = input().strip().upper()
    
    return respuesta == "S"

def validar_categoria(categoria):

    categorias_validas = ["entrada", "principal", "postre", "bebida"]

    if not categoria:
        return False
    
    return categoria.strip().lower() in categorias_validas

def validar_estado_pedido(estado):

    estados_validos = ["pendiente", "en preparación", "listo", "entregado", "cancelado"]

    if not estado:
        return False
    
    return estado.strip().lower() in estados_validos

def manejar_entrada_invalida(entrada):
    print(f"ERROR: Entrada invalida: '{entrada}'. Por favor, intentelo nuevamente")

def verificar_usuario_registrado(usuario):
    return validar_usuario_registrado(usuario)

def validar_nombre_producto(nombre):
    if not nombre or not nombre.strio():
        return False
    
    nombre_limpio = nombre.strip()

    if len(nombre_limpio) < 2:
        return False
    
    caracteres_validos = sum(1 for c in nombre_limpio if c.isalnum())

    if caracteres_validos == 0:
        return False
    
    return True

def validar_precio(precio):
    try:
        precio_float = float(precio)
        if precio_float < 0:
            return None
        return precio_float
    except (ValueError, TypeError):
        return None
    
def validar_cantidad(cantidad):
    try:
        cantidad_int = int(cantidad)
        if cantidad_int <= 0:
            return None
        return cantidad_int
    except (ValueError, TypeError):
        return None