from tienda_libros import TiendaLibros, LibroExistenteError

class UIConsola:
    def __init__(self, tienda):
        self.tienda = tienda

    def agregar_libro_a_carrito_de_compras(self):
        try:
            isbn = input("Ingrese el ISBN del libro: ")
            cantidad = int(input("Ingrese la cantidad: "))
            libro = self.tienda.catalogo.get(isbn)
            if libro:
                self.tienda.agregar_libro_a_carrito(libro, cantidad)
                print("Libro agregado al carrito.")
            else:
                print(f"El libro con ISBN {isbn} no existe en el catálogo.")
        except ValueError:
            print("Error: Ingrese una cantidad válida.")

    def retirar_libro_de_carrito_de_compras(self):
        isbn = input("Ingrese el ISBN del libro a retirar del carrito: ")
        self.tienda.retirar_item_de_carrito(isbn)
        print("Libro retirado del carrito con éxito.")

    def adicionar_un_libro_a_catalogo(self):
        try:
            isbn = input("ISBN del libro: ")
            titulo = input("Título del libro: ")
            precio = float(input("Precio del libro: "))
            existencias = int(input("Existencias del libro: "))
            libro = self.tienda.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
            print(f"Libro '{titulo}' agregado al catálogo con éxito.")
        except ValueError:
            print("Error: Ingrese un precio y existencias válidos.")
        except LibroExistenteError as e:
            print(e)


