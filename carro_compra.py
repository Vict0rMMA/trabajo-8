
from item_compra import ItemCompra

class CarroCompras:
    def __init__(self):
        self.items = []

    def agregar_item(self, libro, cantidad):
        item = ItemCompra(libro, cantidad)
        self.items.append(item)
        return item

    def quitar_item(self, isbn):
        self.items = [item for item in self.items if item.libro.isbn != isbn]

    def calcular_total(self) -> float:
        total = 0
        for item in self.items:
            total += item.calcular_subtotal()
        return total




    
    
    
    
    
    
    # Defina metodo inicializador __init__(self)

    # Defina el metodo agregar_item

    # Defina el metodo calcular_total

    # Defina el metodo quitar_item
