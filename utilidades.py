import os
import platform

def limpiar_pantalla():
    try:
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
    except Exception:
        print("\n" * 50)

def pausar():
    try:
        input("\n Presione Enter para continuar...")
    except KeyboardInterrupt:
        print("\n")

def mostrar_tabla_productos(productos, mostrar_indices=False):
    if not productos:
        print("No hay productos para mostrar")
        return
    
    if mostrar_indices:
        print(f"{'#':<4} {'ID':<8} {'Producto':<25} {'Categoria':<15} {'Precio'}")
        print("-" * 60)
        for i, producto in enumerate(productos, 1):
            print(f"{i:<4} {producto['id']:<8} {producto['nombre']:<25} {producto['categoria']:<15} ${producto['precio']:.2f}")
    else:
        print(f"{'ID':<8} {'Producto':<25} {'Categoria':<15} {'Precio'}")
        print("-" * 60)
        for producto in productos:
            print(f"{producto['id']:<8} {producto['nombre']:<25} {producto['categoria']:<15} ${producto['precio']:.2f}")

def validar_numero_positivo(mensaje, tipo=int):
    while True:
        try:
            valor = tipo(input(mensaje).strip())
            if valor > 0:
                return valor
            else:
                print("El valor debe ser mayor a 0")
        except ValueError:
            print(f"Debe ingresar un numero valido")
        except KeyboardInterrupt:
            print("\n")
            return None
        
def confirmar_accion(mensaje="¿Está seguro?"):
    try:
        respuesta = input(f"{mensaje} (s/n): ").strip().lower()
        return respuesta == 's' or respuesta == 'si' or respuesta == 'sí'
    except KeyboardInterrupt:
        print("\n")
        return False
    
def formatear_precio(precio):
    try:
        return f"${float(precio):.2f}"
    except (ValueError, TypeError):
        return "$0.00"
    
def calcular_total_carrito(carrito):
    try:
        return sum(item.get('subtotal', 0) for item in carrito)
    except Exception:
        return 0.0

def obtener_fecha_hora_actual():
    from datetime import datetime
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def validar_opcion_menu(opcion, opciones_validas):
    return opcion in opciones_validas

def mostrar_mensaje_error(mensaje):
    print(f"\n ERROR: {mensaje}")

def mostrar_mensaje_exito(mensaje):
    print(f"\n EXITO: {mensaje}")

def mostrar_mensaje_adventencia(mensaje):
    print(f"\n ADVENTENCIA: {mensaje}")

def mostrar_mensaje_info(mensaje):
    print(f"\n INFO: {mensaje}")

def centrar_texto(texto, ancho=60, caracter=' '):
    return texto.center(ancho, caracter)

def crear_separador(caracter='=', longitud=60):
    return caracter * longitud

def truncar_texto(texto, longitud_maxima):
    if len(texto) <= longitud_maxima:
        return texto
    return texto[:longitud_maxima - 3] + "..."

def validar_string_no_vacio(mensaje):
    try:
        while True:
            valor = input(mensaje).strip()
            if valor:
                return valor
            print("Este campo no puede estar vacio")
    except KeyboardInterrupt:
        print("\n")
        return None
    
def mostrar_barra_progreso(actual, total, longitud=40):
    try:
        porcentaje = int((actual / total) * 100)
        lleno = int((longitud * actual)/total)
        barra = '#' * lleno + '-' * (longitud - lleno)
        print(f'\r|{barra}| {porcentaje}%', end='')

        if actual >= total:
            print()
    except Exception:
        pass

def es_numero(valor):
    try:
        float(valor)
        return True
    except (ValueError, TypeError):
        return False