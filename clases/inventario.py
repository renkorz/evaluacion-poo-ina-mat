class Inventory():
    def __init__(self):
        self.productos = {}

    def add_product(self, product):
        self.product[product.id_product] = product

    def __str__(self):
        return f"Inventario con {len(self.product)} productos."