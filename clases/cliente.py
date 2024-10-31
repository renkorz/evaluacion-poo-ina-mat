class Client():
    def __init__(self, id_client, name, contact):
        self.id_client = id_client
        self.name = name
        self.contact = contact

    def __str__(self):
        return f"Cliente: {self.name}, Contacto: {self.contact}"