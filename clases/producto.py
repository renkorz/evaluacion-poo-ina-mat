class Product():
    def __init__(self, id_product, name, price, stock):
        self.id_product = id_product
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, amount):
        self.stock += amount

    def __str__(self):
        return f"Producto: {self.name}, Precio: {self.price}, Stock: {self.stock}"