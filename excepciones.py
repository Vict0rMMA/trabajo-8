class LibroError(Exception):
    pass

class LibroExistenteError(LibroError):
    def __init__(self, titulo, isbn):
        super().__init__()
        self.titulo = titulo
        self.isbn = isbn

    def __str__(self):
        return f"El libro con título {self.titulo} y ISBN {self.isbn} ya existe en el catálogo."

class LibroAgotadoError(LibroError):
    def __init__(self, titulo, isbn):
        super().__init()
        self.titulo = titulo
        self.isbn = isbn

    def __str__(self):
        return f"El libro con título {self.titulo} y ISBN {self.isbn} está agotado."

class ExistenciasInsuficientesError(LibroError):
    def __init__(self, titulo, isbn, cantidad_a_comprar, existencias):
        super().__init()
        self.titulo = titulo
        self.isbn = isbn
        self.cantidad_a_comprar = cantidad_a_comprar
        self.existencias = existencias

    def __str__(self):
        return f"El libro con título {self.titulo} y ISBN {self.isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.existencias}."
