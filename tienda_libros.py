


from carro_compra import CarroCompras
from libro import Libro

class LibroError(Exception):
    pass

class LibroExistenteError(LibroError):
    def __init__(self, titulo: str, isbn: str):
        super().__init(f"El libro con título {titulo} y ISBN {isbn} ya existe en el catálogo")

class LibroAgotadoError(LibroError):
    def __init__(self, titulo: str, isbn: str):
        super().__init(f"El libro con título {titulo} y ISBN {isbn} está agotado")

class ExistenciasInsuficientesError(LibroError):
    def __init__(self, titulo: str, isbn: str, cantidad_a_comprar: int, existencias: int):
        super().__init(
            f"El libro con título {titulo} y ISBN {isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {cantidad_a_comprar}, existencias: {existencias}"
        )

class TiendaLibros:
    def __init__(self):
        self.catalogo = {}
        self.carrito = CarroCompras()

    def adicionar_libro_a_catalogo(self, isbn: str, titulo: str, precio: float, existencias: int) -> Libro:
        if not isbn.isalnum():
            raise ValueError("El ISBN debe ser un valor alfanumérico")

        if isbn in self.catalogo:
            raise LibroExistenteError(titulo, isbn)

        if existencias < 0:
            raise ValueError("El número de existencias debe ser un valor positivo")

        libro = Libro(isbn, titulo, precio, existencias)
        self.catalogo[isbn] = libro
        return libro

    def agregar_libro_a_carrito(self, libro: Libro, cantidad: int) -> None:
        if not isinstance(libro, Libro):
            raise TypeError("El libro debe ser una instancia de la clase Libro")

        if cantidad < 0:
            raise ValueError("La cantidad debe ser un valor positivo")

        if libro.existencias <= 0:
            raise LibroAgotadoError(libro.titulo, libro.isbn)

        if cantidad > libro.existencias:
            raise ExistenciasInsuficientesError(libro.titulo, libro.isbn, cantidad, libro.existencias)

        self.carrito.agregar_item(libro, cantidad)

    def retirar_item_de_carrito(self, isbn: str) -> None:
        self.carrito.quitar_item(isbn)











    # Defina metodo inicializador __init__

    # Defina metodo adicionar_libro_a_catalogo

    # Defina metodo agregar_libro_a_carrito

    # Defina metodo retirar_item_de_carrito
