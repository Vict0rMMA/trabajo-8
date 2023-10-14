from tiendalibros.modelo.libro_error import LibroError

class LibroError(Exception):
    pass

class LibroExistenteError(LibroError):
    def __init__(self, mensaje="El libro ya existe en el catálogo."):
        super().__init__(mensaje)


class LibroExistenteError(LibroError):
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        super().__init__()

    def __str__(self):
        return f"El libro con título '{self.titulo}' y ISBN: '{self.isbn}' ya existe en el catálogo."
    
    # Defina metodo inicializador

    # Defina metodo especial
