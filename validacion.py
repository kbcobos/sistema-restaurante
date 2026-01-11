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