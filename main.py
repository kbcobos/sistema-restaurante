def mostrar_banner():
    print("=" * 70)
    print(" " * 20 + "RESTAURANTE PIZZA ESPACIAL" + 20 * " ")
    print("=" * 70)
    print(" " * 22 + "Sistema de Gestion de Pedidos")
    print("=" * 70)

def main():
    while True:
        mostrar_banner()
        print("\n MENU PRINCIPAL")
        print("-" * 70)
        print("1. Acceder como Cliente")
        print("2. Acceder como Administrador")
        print("0. Salir")
        print("-" * 70)

        opcion = input("\n Seleccione una opcion: ").strip()

        if opcion == "1":
            try:
                login_usuario_menu()
            except KeyboardInterrupt:
                print("\n Operacion interrumpida por el usuario")
            except Exception as e:
                print(f"\n Error inesperado: {e}")
        
        elif opcion == "2":
            try:
                login_admin_menu()
            except KeyboardInterrupt:
                print("\n Operacion interrumpida por el usuario")
            except Exception as e:
                print(f"\n Error inesperado: {e}")
        
        elif opcion == "0":
            print("\n" + "=" * 70)
            print("¡Gracias por usar nuestro sistema!")
            print("=" * 70 + "\n")
            break

        else:
            print("Opcion invalida. Por favor, seleccione 1, 2 o 0")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n ¡Hasta luego!")
    except Exception as e:
        print(f"\n Error critico: {e}")
        print("Por favor, contacte al administrador del sistema")
            