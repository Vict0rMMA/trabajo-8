from tienda_libros import TiendaLibros
from ui_consola_interfaz import UIConsola

if __name__ == "__main__":
    tienda = TiendaLibros()
    ui = UIConsola(tienda)

    while True:
        print("\nOpciones:")
        print("1. Agregar libro al carrito de compras")
        print("2. Retirar libro del carrito de compras")
        print("3. Agregar libro al catálogo")
        print("4. Calcular total del carrito")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ui.agregar_libro_a_carrito_de_compras()
        elif opcion == "2":
            ui.retirar_libro_de_carrito_de_compras()
        elif opcion == "3":
            ui.adicionar_un_libro_a_catalogo()
        elif opcion == "4":
           
            pass
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
