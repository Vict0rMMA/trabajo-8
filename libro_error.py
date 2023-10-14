from tiendalibros.modelo.libro import Libro


class LibroError(Exception):
    pass
    def __init__(self, libro: Libro):
        self.libro = libro

class LibroAgotadoError(LibroError):
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        super().__init__()

    def __str__(self):
        return f"El libro con título '{self.titulo}' y ISBN '{self.isbn}' está agotado."

class ExistenciasInsuficientesError(LibroError):
    def __init__(self, mensaje, cantidad_a_comprar):
        super().__init__(mensaje)
        self.cantidad_a_comprar = cantidad_a_comprar

class ExistenciasInsuficientesError(LibroError):
    def __init__(self, titulo, isbn, cantidad_a_comprar, existencias):
        self.titulo = titulo
        self.isbn = isbn
        self.cantidad_a_comprar = cantidad_a_comprar
        self.existencias = existencias
        mensaje = (
            f"El libro con título '{self.titulo}' y ISBN '{self.isbn}' "
            f"no tiene suficientes existencias para realizar la compra: "
            f"cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.existencias}"
        )
        super().__init__(mensaje)

    def __str__(self):
        return self.args[0]