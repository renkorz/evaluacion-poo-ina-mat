class Facture():
    def __init__(self, id_facture, client, product, total):
        self.id_facture = id_facture
        self.client = client
        self.product = product
        self.total = total

    def __str__(self):
        return f"Factura {self.id_facture} para {self.client.name}, total: {self.total}"