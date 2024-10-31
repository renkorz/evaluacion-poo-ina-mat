class Supplier():
    def __init__(self, id_supplier, name, products_supplied):
        self.id_supplier = id_supplier
        self.name = name
        self.products_supplied = products_supplied

    def __str__(self):
        return f"Proveedor: {self.name}, Productos: {', '.join(self.products_supplied)}"